# Superdesk

Superdesk is an open source end-to-end news creation, production, curation,
distribution and publishing platform developed and maintained by Sourcefabric
with the sole purpose of making the best possible software for journalism. It
is scaleable to suit news organizations of any size.

### Installation

Use [docker-compose](http://docs.docker.com/compose/ "") and the config from the `docker` folder or build docker images manually from `Dockerfile`s from `client` and `server` folders accordingly.

##### install system-wide dependencies

```sh
$ sudo apt-get install python2.7 python-virtualenv git
```
and install [the newest docker](https://docs.docker.com/installation/).
and make sure you can run [docker without sudo](http://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo).


##### install docker compose and run app

```sh
$ git clone https://github.com/liveblog/superdesk.git
$ cd superdesk
$ git clone https://github.com/superdesk/superdesk-content-api.git
$ ./scripts/docker-local-demo.sh
```

Open in a browser `http://localhost:80` after the server will be ready.

If you can't log in then you probably need to run `./scripts/docker-local-create-user.sh`.

If you're going to assign some hostname to the instance, you should also set it in the config file  [common.yml](./docker/common.yml) instead of `127.0.0.1`.

For manual installation just follow the steps described in both [client](./client/Dockerfile) and [server](./server/Dockerfile) Dockerfiles.
