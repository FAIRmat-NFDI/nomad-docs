# Configure an Oasis

Originally, the NOMAD Central Repository is a service that runs at the Max-Planck's computing facility in Garching, Germany. However, the NOMAD software is Open-Source, and everybody can run it. Any service that uses NOMAD software independently is called a _NOMAD Oasis_. A _NOMAD Oasis_ does not need to be fully isolated. For example, you can publish uploads from your NOMAD Oasis to the central NOMAD installation.

!!! note

    **Register your Oasis**
    If you installed (or even just plan to install) a NOMAD Oasis, please
    [register your Oasis with FAIRmat](https://www.fairmat-nfdi.eu/fairmat/oasis_registration)
    and help us to assist you in the future.

## Creating a NOMAD distribution for your Oasis

The configuration for a NOMAD Oasis is defined in a NOMAD distribution project. We provide a [template](https://github.com/FAIRmat-NFDI/nomad-distro-template) for these distribution projects. A NOMAD distribution project contains all necessary config files and will allow you to version your configuration, install and configure plugins, build custom images automatically, and much more.

For a production installation, we recommend to create your own distribution project based on the template by pressing the "use this template" button on the top right of the [template's github page](https://github.com/FAIRmat-NFDI/nomad-distro-template). If you wish to instead try out the default setup locally, follow the instructions in "Try  NOMAD Oasis locally".

???+ "Try NOMAD Oasis locally"

	This is an example of how you would deploy a simple, single-machine NOMAD Oasis on your computer. This is meant only as an example and you should see our documentation on [Deploying an Oasis](./deploy.md) for more details on setting up a production deployment.

	1.  Make sure you have [docker](https://docs.docker.com/engine/install/) installed.
		Docker nowadays comes with `docker compose` built in. Prior, you needed to
		install the stand-alone [docker-compose](https://docs.docker.com/compose/install/).

	2.  Clone the `nomad-distro-template` repository or download the repository as a zip file.

		```sh
		git clone https://github.com/FAIRmat-NFDI/nomad-distro-template.git
		cd nomad-distro-template
		```

		or

		```sh
		curl-L -o nomad-distro-template.zip "https://github.com/FAIRmat-NFDI/nomad-distro-template/archive/main.zip"
		unzip nomad-distro-template.zip
		cd nomad-distro-template
		```

	3.  _On Linux only,_ recursively change the owner of the `.volumes` directory to the nomad user (1000)

		```sh
		sudo chown -R 1000 .volumes
		```

	4.  Pull the images specified in the `docker-compose.yaml`

		Note that the image needs to be public or you need to provide a PAT (see "Important" note above).

		```sh
		docker compose pull
		```

	5.  And run it with docker compose in detached (--detach or -d) mode

		```sh
		docker compose up -d
		```

	6.  Optionally you can now test that NOMAD is running with

		```
		curl localhost/nomad-oasis/alive
		```

	7.  Finally, open [http://localhost/nomad-oasis](http://localhost/nomad-oasis) in your browser to start using your new NOMAD Oasis.

	To run NORTH (the NOMAD Remote Tools Hub), the `hub` container needs to run docker and
	the container has to be run under the docker group. You need to replace the default group
	id `991` in the `docker-compose.yaml`'s `hub` section with your systems docker group id.
	Run `id` if you are a docker user, or `getent group | grep docker` to find your
	systems docker gid. The user id 1000 is used as the nomad user inside all containers.

## Configuring your installation

### Sharing data through log transfer and data privacy notice

NOMAD includes a _log transfer_ functions. When enabled this it automatically collects
and transfers non-personalized logging data to us. Currently, this functionality is experimental
and requires opt-in. However, in upcoming versions of NOMAD Oasis, we might change to out-out.

To enable this functionality add `logtransfer.enabled: true` to you `nomad.yaml`.

The service collects log-data and aggregated statistics, such as the number of users or the
number of uploaded datasets. In any case this data does not personally identify any users or
contains any uploaded data. All data is in an aggregated and anonymized form.

The data is solely used by the NOMAD developers and FAIRmat, including but not limited to:

- Analyzing and monitoring system performance to identify and resolve issues.
- Improving our NOMAD software based on usage patterns.
- Generating aggregated and anonymized reports.

We do not share any collected data with any third parties.

We may update this data privacy notice from time to time to reflect changes in our data practices.
We encourage you to review this notice periodically for any updates.

### Using the central user management

Our recommendation is to use the central user management provided by nomad-lab.eu. We
simplified its use and you can use it out-of-the-box. You can even run your system
from `localhost` (e.g. for initial testing). The central user management system is not
communicating with your OASIS directly. Therefore, you can run your OASIS without
exposing it to the public internet.

There are two requirements. First, your users must be able to reach the OASIS. If a user is
logging in, she/he is redirected to the central user management server and after login,
she/he is redirected back to the OASIS. These redirects are executed by your user's browser
and do not require direct communication.

Second, your OASIS must be able to request (via HTTP) the central user management and central NOMAD
installation. This is necessary for non JWT-based authentication methods and to
retrieve existing users for data-sharing features.

The central user management will make future synchronizing data between NOMAD installations easier
and generally recommend to use the central system.
But in principle, you can also run your own user management. See the section on
[your own user management](#provide-and-connect-your-own-user-management).

## Configuration files

The [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template)
provides all the neccessary configuration files. We strongly recommend to create your own distribution
project based on the template. This will allow you to version your configuration, build custom
images with plugins, and much more.

In this section, you can learn about settings that you might need to change. The config files are:

- `docker-compose.yaml`
- `configs/nomad.yaml`
- `configs/nginx.conf`

All docker containers are configured via docker-compose and the respective `docker-compose.yaml` file.
The other files are mounted into the docker containers.

### docker-compose.yaml

The most basic `docker-compose.yaml` to run an OASIS looks like this:

```yaml
--8<-- "ops/docker-compose/nomad-oasis/docker-compose.yaml"
```

Changes necessary:

- The group in the value of the hub's user parameter needs to match the docker group
  on the host. This should ensure that the user which runs the hub, has the rights to access the host's docker.
- On Windows or MacOS computers you have to run the `app` and `worker` container without `user: '1000:1000'` and the `north` container with `user: root`.

A few things to notice:

- The app, worker, and north service use the NOMAD docker image. Here we use the `latest` tag, which
  gives you the latest _beta_ version of NOMAD. You might want to change this to `stable`,
  a version tag (format is `vX.X.X`, you find all releases [here](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/tags){:target="\_blank"}), or a specific [branch tag](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/branches){:target="\_blank"}.
- All services use docker volumes for storage. This could be changed to host mounts.
- It mounts two configuration files that need to be provided (see below): `nomad.yaml`, `nginx.conf`.
- The only exposed port is `80` (proxy service). This could be changed to a desired port if necessary.
- The NOMAD images are pulled from our gitlab at MPCDF, the other services use images from a public registry (_dockerhub_).
- All containers will be named `nomad_oasis_*`. These names can be used later to reference the container with the `docker` cmd.
- The services are setup to restart `always`, you might want to change this to `no` while debugging errors to prevent indefinite restarts.
- Make sure that the `PWD` environment variable is set. NORTH needs to create bind mounts that require absolute paths and we need to pass the current working directory to the configuration from the PWD variable (see hub service in the `docker-compose.yaml`).
- The `north` service needs to run docker containers. We have to use the systems docker group as a group. You might need to replace `991` with your
  systems docker group id.

### nomad.yaml

NOMAD app and worker read a `nomad.yaml` for configuration.

```yaml
--8<-- "ops/docker-compose/nomad-oasis/configs/nomad.yaml"
```

You should change the following:

- Replace `localhost` with the hostname of your server. I user-management will redirect your
  users back to this host. Make sure this is the hostname, your users can use.
- Replace `deployment`, `deployment_url`, and `maintainer_email` with representative values.
  The `deployment_url` should be the url to the deployment's api (should end with `/api`).
- To enable the _log transfer_ set `logtransfer.enable: true` ([data privacy notice above](#sharing-data-through-log-transfer-and-data-privacy-notice)).
- You can change `api_base_path` to run NOMAD under a different path prefix.
- You should generate your own `north.jupyterhub_crypt_key`. You can generate one
  with `openssl rand -hex 32`.
- On Windows or MacOS, you have to add `hub_connect_ip: 'host.docker.internal'` to the `north` section.

A few things to notice:

- Under `mongo` and `elastic` you can configure database and index names. This might
  be useful, if you need to run multiple NOMADs with the same databases.
- All managed files are stored under `.volumes` of the current directory.

### nginx.conf

The GUI container serves as a proxy that forwards requests to the app container. The
proxy is an nginx server and needs a configuration similar to this:

```none
--8<-- "ops/docker-compose/nomad-oasis/configs/nginx.conf"
```

A few things to notice:

- It configures the base path (`nomad-oasis`). It needs to be changed, if you use a different base path.
- You can use the server for additional content if you like.
- `client_max_body_size` sets a limit to the possible upload size.

You can add an additional reverse proxy in front or modify the nginx in the docker-compose.yaml
to [support https](http://nginx.org/en/docs/http/configuring_https_servers.html){:target="\_blank"}.
If you operate the GUI container behind another proxy, keep in mind that your proxy should
not buffer requests/responses to allow streaming of large requests/responses for `api/v1/uploads` and `api/v1/.*/download`.
An nginx reverse proxy location on an additional reverse proxy, could have these directives
to ensure the correct http headers and allows the download and upload of large files:

```nginx
client_max_body_size 35g;
proxy_set_header Host $host;
proxy_pass_request_headers on;
proxy_buffering off;
proxy_request_buffering off;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_pass http://<your-oasis-host>/nomad-oasis;
```

## Plugins

[Plugins](../plugins/plugins.md) allow the customization of a NOMAD deployment in terms of
which search apps, normalizers, parsers and schema packages are available. In order for these
customization to be activated, they have to be configured and installed into an Oasis.
The basic template comes with a core set of plugins. If you want to configure
your own set of plugins, using the template and creating your own distro project
is mandatory.

Plugins are configured via the `pyproject.toml` file. Based on this file
the distro project CI pipeline creates the NOMAD docker image that is used by your installation.
Only plugins configured in the `pyproject.toml` files, will be installed into the docker
image and only those plugins installed in the used docker image are available in your
Oasis.

Please refer to the [template README](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#adding-a-plugin)
to learn how to add your own plugins.

## Starting and stopping NOMAD services

If you prepared the above files, simply use the usual `docker compose` commands to start everything.

To make sure you have the latest docker images for everything, run this first:

```sh
docker compose pull
```

In the beginning and to simplify debugging, it is recommended to start the services separately:

```sh
docker compose up -d mongo elastic rabbitmq
docker compose up app worker gui
```

The `-d` option runs container in the background as _daemons_. Later you can run all at once:

```sh
docker compose up -d
```

Running all services also contains NORTH. When you use a tool in NORTH for the first time,
your docker needs to pull the image that contains this tool. Be aware that this might take longer
than timeouts allow and starting a tool for the very first time might fail.

You can also use docker to stop and remove faulty containers that run as _daemons_:

```sh
docker stop nomad_oasis_app
docker rm nomad_oasis_app
```

You can wait for the start-up with curl using the apps `alive` "endpoint":

```sh
curl http://<your host>/nomad-oasis/alive
```

If everything works, the gui should be available under:

```none
http://<your host>/nomad-oasis/gui/
```

If you run into problems, use the dev-tools of your browser to check the javascript logs
or monitor the network traffic for HTTP 500/400/404/401 responses.

To see if at least the api works, check

```none
http://<your host>/nomad-oasis/alive
http://<your host>/nomad-oasis/api/info
```

To see logs or 'go into' a running container, you can access the individual containers
with their names and the usual docker commands:

```sh
docker logs nomad_oasis_app
```

```sh
docker exec -ti nomad_oasis_app /bin/bash
```

If you want to report problems with your OASIS. Please provide the logs for

- nomad_oasis_app
- nomad_oasis_worker
- nomad_oasis_gui

## Provide and connect your own user management

NOMAD uses [keycloak](https://www.keycloak.org/){:target="\_blank"} for its user management. NOMAD uses
keycloak in two ways. First, the user authentication uses the OpenID Connect/OAuth interfaces provided by keycloak.
Second, NOMAD uses the keycloak realm-management API to get a list of existing users.
Keycloak is highly customizable and numerous options to connect keycloak to existing
identity providers exist.

This tutorial assumes that you have some understanding of what keycloak is and
how it works.

The NOMAD Oasis installation with your own keyloak is very similar to the regular docker-compose
installation above. There are just a three changes.

- The `docker-compose.yaml` has an added keycloak service.
- The `nginx.conf` is also modified to add another location for keycloak.
- The `nomad.yaml` has modifications to tell nomad to use your and not the official NOMAD keycloak.

You can start with the regular installation above and manually adopt the config or
download the already updated configuration files: [nomad-oasis-with-keycloak.zip](../../assets/nomad-oasis-with-keycloak.zip).
The download also contains an additional `configs/nomad-realm.json` that allows you
to create an initial keycloak realm that is configured for NOMAD automatically.

First, the `docker-compose.yaml`:

```yaml
--8<-- "ops/docker-compose/nomad-oasis-with-keycloak/docker-compose.yaml"
```

A few notes:

- You have to change the `KEYCLOAK_FRONTEND_URL` variable to match your host and set a path prefix.
- The environment variables on the keycloak service allow to use keycloak behind the nginx proxy with a path prefix, e.g. `keycloak`.
- By default, keycloak will use a simple H2 file database stored in the given volume. Keycloak offers many other options to connect SQL databases.
- We will use keycloak with our nginx proxy here, but you can also host-bind the port `8080` to access keycloak directly.
- We mount and use the downloaded `configs/nomad-realm.json` to configure a NOMAD compatible realm on the first startup of keycloak.

Second, we add a keycloak location to the nginx config:

```nginx
--8<-- "ops/docker-compose/nomad-oasis-with-keycloak/configs/nginx.conf"
```

A few notes:

- Again, we are using `keycloak` as a path prefix. We configure the headers to allow
  keycloak to pick up the rewritten url.

Third, we modify the keycloak configuration in the `nomad.yaml`:

```yaml
--8<-- "ops/docker-compose/nomad-oasis-with-keycloak/configs/nomad.yaml"
```

You should change the following:

- There are two urls to configure for keycloak. The `server_url` is used by the nomad
  services to directly communicate with keycloak within the docker network. The `public_server_url`
  is used by the UI to perform the authentication flow. You need to replace `localhost`
  in `public_server_url` with `<yourhost>`.

A few notes:

- The particular `admin_user_id` is the Oasis admin user in the provided example realm
  configuration. See below.

If you open `http://<yourhost>/keycloak/auth` in a browser, you can access the admin
console. The default user and password are `admin` and `password`.

Keycloak uses `realms` to manage users and clients. A default NOMAD compatible realm
is imported by default. The realm comes with a test user and password `test` and `password`.

A few notes on the realm configuration:

- Realm and client settings are almost all default keycloak settings.
- You should change the password of the admin user in the nomad realm.
- The admin user in the nomad realm has the additional `view-users` client role for `realm-management`
  assigned. This is important, because NOMAD will use this user to retrieve the list of possible
  users for managing co-authors and reviewers on NOMAD uploads.
- The realm has one client `nomad_public`. This has a basic configuration. You might
  want to adapt this to your own policies. In particular you can alter the valid redirect URIs to
  your own host.
- We disabled the https requirement on the default realm for simplicity. You should change
  this for a production system.

## Further steps

This is an incomplete list of potential things to customize your NOMAD experience.

- Learn [how to develop plugins](../plugins/plugins.md) that can be installed in an Oasis
- Write .yaml based [schemas](../customization/basics.md) and [ELNs](../customization/elns.md)
- Learn how to use the [tabular parser](../customization/tabular.md) to manage data from .xls or .csv
- Add specialized [NORTH tools](../manage/north.md)
- [Restricting user access](admin.md#restricting-access-to-your-oasis)

## Troubleshooting

### Time offset between Oasis and the Authentication server

If during login you get an error like: `jwt.exceptions.ImmatureSignatureError: The token is not yet valid (iat)`, it most probably means that there is a time difference between the two machines: the one creating the JWT and the other that is validating it. This causes an error where the authentication server looking at the token thinks that it has not been issued yet.

To fix this problem, you should ensure that the time on the servers is synchronized. It is possible that a network port on one of the servers may be closed, preventing it from synchronizing the time. Note that the servers do not need to be on the same timezone, as internally everything is converted to UTC+0. To check the time on a server, you can on a linux-based machine use the [`timedatectl`](https://man7.org/linux/man-pages/man8/hwclock.8.html) command which will report both the harware clock and the system clock (see [here for the difference](https://developer.toradex.com/software/linux-resources/linux-features/real-time-clock-rtc-linux/#:~:text=Two%20clocks%20are%20important%20in,maintained%20by%20the%20operating%20system.)). For authentication, the system clocks on the two machines need to be set correctly, but you might also need to correct the hardware clock since it initially sets the system clock upon rebooting the machine.

### NOMAD in networks with restricted Internet access

Some network environments do not allow direct Internet connections, and require the use of an outbound proxy.
However, NOMAD needs to connect to the central user management or elasticsearch thus requires an active Internet
connection (at least on Windows) to work.
In these cases you need to configure docker to use your proxy.
See details via this link [https://docs.docker.com/network/proxy/](https://docs.docker.com/network/proxy/).
An example file `~/.docker/config.json` could look like this.

```json
{
  "proxies": {
    "default": {
      "httpProxy": "http://<proxy>:<port>",
      "httpsProxy": "http://<proxy>:<port>",
      "noProxy": "127.0.0.0/8,elastic,localhost"
    }
  }
}
```

Since not all used services respect proxy variables, one also has to change the docker compose config file `docker-compose.yaml` for elastic search to:

```yaml hl_lines="7 8"
elastic:
  restart: unless-stopped
  image: elasticsearch:7.17.24
  container_name: nomad_oasis_elastic
  environment:
    - ES_JAVA_OPTS=-Xms512m -Xmx512m
    - ES_JAVA_OPTS=-Djava.net.useSystemProxies=true
    - ES_JAVA_OPTS=-Dhttps.proxyHost=<proxy> -Dhttps.proxyPort=port -Dhttps.nonProxyHosts=localhost|127.0.0.1|elastic
    - discovery.type=single-node
  volumes:
    - elastic:/usr/share/elasticsearch/data
  healthcheck:
    test:
      - "CMD"
      - "curl"
      - "--fail"
      - "--silent"
      - "http://elastic:9200/_cat/health"
    interval: 10s
    timeout: 10s
    retries: 30
    start_period: 60s
```

Unfortunately there is no way yet to use the NORTH tools with the central user management, since the jupyterhub spawner does not respect proxy variables.
It has not been tested yet when using an authentication which does not require the proxy, e.g. a local keycloak server.

If you have issues please contact us on discord n the [oasis channel](https://discord.com/channels/1201445470485106719/1205480348050395136).

### NOMAD behind a firewall

It is also possible that your docker container is not able to talk to each other.
This could be due to restrictive settings on your server.
The firewall shall allow both inbound and outbound HTTP and HTTPS traffic.
The corresponding rules need to be added.
Furthermore, inbound traffic needs to be enabled for the port used on the `nginx` service.

In this case you should make sure this test runs through:
[https://docs.docker.com/network/network-tutorial-standalone/](https://docs.docker.com/network/network-tutorial-standalone/)

If not please contact your server provider for help.

### Elasticsearch and open files limit

Even when run in docker elasticsearch might require you to change your systems resource
limits as described in the elasticsearch documentation
[here](https://www.elastic.co/guide/en/elasticsearch/reference/current/setting-system-settings.html).

You can temporarely change the open files limit like this:

```sh
sudo ulimit -n 65535
```
