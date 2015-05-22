# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license
import logging
import superdesk

from superdesk.utc import utcnow
from superdesk.errors import SubscriberError, SuperdeskPublishError, PublishQueueError


logger = logging.getLogger(__name__)


class PublishService():
    """Base publish service class."""

    def _transmit(self, formatted_item, subscriber, destination):
        raise NotImplementedError()

    def transmit(self, queue_item, formatted_item, subscriber, destination, output_channel):
        if not subscriber.get('is_active'):
            raise SubscriberError.subscriber_inactive_error(Exception('Subscriber inactive'), subscriber)
        else:
            try:
                self._transmit(formatted_item, subscriber, destination) or []
                update_item_status(queue_item, 'success')
            except SuperdeskPublishError as error:
                update_item_status(queue_item, 'error', error)
                self.close_transmitter(output_channel, 'output_channels', error)
                self.close_transmitter(subscriber, 'subscribers', error)
                raise error

    def close_transmitter(self, transmitter, transmitter_type, error):
        """
        Checks if the transmitter has the error code set in the list of
        critical errors then closes the transmitter
        :param transmitter: Either an output channel or a subscriber
        :param transmitter_type: Name of the resource 'output_channels or subscribers
        :param error: The error thrown during transmission
        :return: None
        """
        if transmitter.get('critical_errors', {}).get(str(error.code)):
            update = {
                'is_active': False,
                'last_closed': {
                    'closed_at': utcnow(),
                    'message': '{} closed due to critical error: {}'.format(transmitter_type, error)
                }
            }

            transmitter_service = superdesk.get_resource_service(transmitter_type)
            transmitter_service.system_update(transmitter[superdesk.config.ID_FIELD], update, transmitter)


def update_item_status(queue_item, status, error=None):
    try:
        item_update = {'state': status}
        if status == 'in-progress':
            item_update['transmit_started_at'] = utcnow()
        elif status == 'success':
            item_update['completed_at'] = utcnow()
        elif status == 'error' and error:
            item_update['error_message'] = '{}:{}'.format(error, str(error.system_exception))

        superdesk.get_resource_service('publish_queue').patch(queue_item.get('_id'), item_update)
    except Exception as ex:
        raise PublishQueueError.item_update_error(ex)


def get_file_extension(formatted_item):
    try:
        format = formatted_item['format'].upper()
        if format == 'NITF':
            return 'ntf'
        if format == 'XML':
            return 'xml'
    except Exception as ex:
        raise PublishQueueError.item_update_error(ex)
