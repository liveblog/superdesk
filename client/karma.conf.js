'use strict';

module.exports = require('superdesk-core/karma.conf.js');

<<<<<<< HEAD
        preprocessors: {
            '**/*.html': ['ng-html2js'],
            '**/superdesk/**/*.js': ['coverage'],
            '**/superdesk-*/**/*.js': ['coverage']
        },

        // list of files / patterns to load in the browser
        files: [
            'app/scripts/bower_components/jquery/dist/jquery.js',
            'app/scripts/bower_components/angular/angular.js',
            'app/scripts/bower_components/angular-route/angular-route.js',
            'app/scripts/bower_components/angular-mocks/angular-mocks.js',
            'app/scripts/bower_components/angular-resource/angular-resource.js',
            'app/scripts/bower_components/angular-gettext/dist/angular-gettext.js',
            'app/scripts/bower_components/angular-bootstrap/ui-bootstrap-tpls.js',
            'app/scripts/bower_components/ng-file-upload/angular-file-upload.js',

            'app/scripts/bower_components/gridster/dist/jquery.gridster.with-extras.js',
            'app/scripts/bower_components/medium-editor/dist/js/medium-editor.js',
            'app/scripts/bower_components/ment.io/dist/mentio.js',
            'app/scripts/bower_components/rangy/rangy-core.js',
            'app/scripts/bower_components/rangy/rangy-selectionsaverestore.js',

            'app/scripts/bower_components/momentjs/moment.js',
            'app/scripts/bower_components/moment-timezone/builds/moment-timezone-with-data-2010-2020.js',
            'app/scripts/bower_components/langmap/language-mapping-list.js',
            'app/scripts/bower_components/angular-moment/angular-moment.js',
            'app/scripts/bower_components/d3/d3.js',
            'app/scripts/bower_components/jcrop/js/jquery.Jcrop.js',

            'app/scripts/superdesk/mocks.js',
            'app/scripts/superdesk-*/**/*.html',
            'app/scripts/superdesk/**/*.html',
            'test-main.js'
        ],

        // list of files to exclude
        exclude: [
            'app/scripts/bower_components/**/*[sS]pec.js',
            'app/main.js'
        ],

        ngHtml2JsPreprocessor: {
            stripPrefix: 'app/',
            moduleName: 'superdesk.templates-cache'
        },

        junitReporter: {
            outputFile: 'test-results.xml'
        },

        // test results reporter to use
        reporters: ['dots'],

        // web server port
        port: 8080,

        // cli runner port
        runnerPort: 9100,

        // enable / disable watching file and executing tests whenever any file changes
        autoWatch: true,

        // Start these browsers, currently available:
        browsers: ['Chrome'],

        // Continuous Integration mode
        singleRun: false
    });
};
=======
>>>>>>> mainupstream-master
