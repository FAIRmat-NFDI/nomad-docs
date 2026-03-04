# How to configure an Oasis

## Configuration files

The [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"}
provides all the neccessary configuration files. We strongly recommend to create your own distribution
project based on the template. This will allow you to version your configuration, build custom
images with plugins, and much more.

In this section, you can learn about settings that you might need to change. The most relevant config files are:

- `docker-compose.yaml`
- `configs/nomad.yaml`
- `configs/nginx.conf`

All docker containers are configured via docker-compose and the respective `docker-compose.yaml` file.
The other files are mounted into the docker containers.

### docker-compose.yaml

The most basic `docker-compose.yaml` to run an OASIS looks like this:

```yaml
--8<-- "docs/howto/oasis/ops/docker-compose/nomad-oasis/docker-compose.yaml"
```

Changes necessary:

- The group in the value of the hub's user parameter needs to match the docker group
  on the host. This should ensure that the user which runs the hub, has the rights to access the host's docker.
- On Windows or macOS computers you have to run the `app` and `worker` container without `user: '1000:1000'` and the `north` container with `user: root`.

A few things to notice:

- The app, worker, and north service use the NOMAD docker image. Here we use the `latest` tag, which
  gives you the latest *beta* version of NOMAD. You might want to change this to `stable`,
  a version tag (format is `vX.X.X`, you find all releases at [nomad-FAIR > tags](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/tags){:target="_blank" rel="noopener"}), or a specific [nomad-FAIR > branches](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/branches){:target="_blank" rel="noopener"}.
- All services use docker volumes for storage. This could be changed to host mounts.
- It mounts two configuration files that need to be provided (see below): `nomad.yaml`, `nginx.conf`.
- The only exposed port is `80` (proxy service). This could be changed to a desired port if necessary.
- The NOMAD images are pulled from our GitLab at MPCDF, the other services use images from a public registry (*dockerhub*).
- All containers will be named `nomad_oasis_*`. These names can be used later to reference the container with the `docker` cmd.
- The services are setup to restart `always`, you might want to change this to `no` while debugging errors to prevent indefinite restarts.
- Make sure that the `PWD` environment variable is set. NORTH needs to create bind mounts that require absolute paths and we need to pass the current working directory to the configuration from the PWD variable (see hub service in the `docker-compose.yaml`).
- The `north` service needs to run docker containers. We have to use the systems docker group as a group. You might need to replace `991` with your
  systems docker group id.

### nomad.yaml

NOMAD app and worker read a `nomad.yaml` for configuration.

```yaml
--8<-- "docs/howto/oasis/ops/docker-compose/nomad-oasis/configs/nomad.yaml"
```

You should change the following:

- Replace `localhost` with the hostname of your server. I user-management will redirect your
  users back to this host. Make sure this is the hostname, your users can use.
- Replace `deployment`, `deployment_url`, and `maintainer_email` with representative values.
  The `deployment_url` should be the url to the deployment's api (should end with `/api`).
- To enable the *log transfer* set `logtransfer.enable: true` ([data privacy notice above](#sharing-data-through-log-transfer-and-data-privacy-notice)).
- You can change `api_base_path` to run NOMAD under a different path prefix.
- You should generate your own `north.jupyterhub_crypt_key`. You can generate one
  with `openssl rand -hex 32`.
- On Windows or macOS, you have to add `hub_connect_ip: 'host.docker.internal'` to the `north` section.

A few things to notice:

- Under `mongo` and `elastic` you can configure database and index names. This might
  be useful, if you need to run multiple NOMADs with the same databases.
- All managed files are stored under `.volumes` of the current directory.

### nginx.conf

The GUI container serves as a proxy that forwards requests to the app container. The
proxy is an nginx server and needs a configuration similar to this:

```none
--8<-- "docs/howto/oasis/ops/docker-compose/nomad-oasis/configs/nginx.conf"
```

A few things to notice:

- It configures the base path (`nomad-oasis`). It needs to be changed, if you use a different base path.
- You can use the server for additional content if you like.
- `client_max_body_size` sets a limit to the possible upload size.

You can add an additional reverse proxy in front or modify the nginx in the docker-compose.yaml
to [support https](http://nginx.org/en/docs/http/configuring_https_servers.html){:target="_blank" rel="noopener"}.
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

The `-d` option runs container in the background as *daemons*. Later you can run all at once:

```sh
docker compose up -d
```

Running all services also contains NORTH. When you use a tool in NORTH for the first time,
your docker needs to pull the image that contains this tool. Be aware that this might take longer
than timeouts allow and starting a tool for the very first time might fail.

You can also use docker to stop and remove faulty containers that run as *daemons*:

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

Please refer to the [template README](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#adding-a-plugin){:target="_blank" rel="noopener"}
to learn how to add your own plugins.

## Configuring for performance

If you run the OASIS on a single computer, like described here (either with docker or bare
Linux), you might run into problems with processing large uploads. If the NOMAD worker
and app are run on the same computer, the app might become unresponsive, when the worker
consumes all system resources.

By default, the Temporal-based worker setup uses a single process per container. The default deployment template defines **4 replicas** of the worker container, allowing multiple uploads and tasks to be processed in parallel. Depending on your machine and workload, you may want to adjust how many replicas are running and how much CPU and memory they are allowed to use.

There are several ways to control resource usage and improve performance:

- Increase or decrease the number of worker **replicas** (recommended)
- Adjust CPU and memory limits in Docker
- (Optionally) Increase the number of worker **processes** on the Python side

---

### Increase the Number of Worker Replicas (Recommended)

The most robust way to scale worker performance is by changing the number of replicas for the worker container. This ensures that multiple worker instances can process tasks in parallel and that they are properly managed and restarted if one fails.

In your `docker-compose.yml`, you can modify the worker service like this:

```yml
services:
  worker:
    ...
    deploy:
      replicas: 4  # default value; adjust based on your system capacity
```

Each replica runs as an independent worker process. Docker will handle restarting and load balancing between them.

### Adjust the Number of Worker Processes (Advanced Option)

If necessary, you can also increase the number of processes within each worker container by modifying the worker command in your docker-compose.yml:

```yml
services:
  worker:
    ...
    command: python -m nomad.cli admin run action-internal-worker --workers 4
```

This will run multiple worker processes within a single container. However, this approach is less robust than scaling via replicas, as process-level management (e.g., restarting if one worker crashes) is handled less effectively inside a single container.

### Limiting the use of threads

You can also reduce the usable threads that Python packages based on OpenMP could use to
reduce the threads that might be spawned by a single worker process. Simply set the `OMP_NUM_THREADS`
environment variable in the worker container in your `docker-compose.yml`:

```yml
services:
    worker:
        ...
        environment:
            ...
            OMP_NUM_THREADS: 1
```

### Limit CPU with docker

You can add a `deploy.resources.limits` section to the worker service in the `docker-compose.yml`:

```yml
services:
    worker:
        ...
        deploy:
            resources:
                limits:
                    cpus: '0.50'
```

The number refers to the percentage use of a single CPU core.
See also the [docker-compose documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#resources){:target="_blank" rel="noopener"}.

## Restricting access to your Oasis

An Oasis works exactly the same way the official NOMAD works. It is open and everybody
can access published data. Everybody with an account can upload data. This might not be
what you want.

Currently there are three ways to restrict access to your Oasis. First, you do not
expose the Oasis to the public internet, e.g. you make it only available on an intra-net or
through a VPN.

Secondly, you can require authentication for all sensitive endpoints by enabling
the global `require_authentication` flag in your configuration:

```yaml
oasis:
    require_authentication: true
```

Lastly, we offer a simple white-list mechanism. As the Oasis administrator you provide a
list of accounts as part of your Oasis configuration. To use the Oasis, all users have to
be logged in and be on your white list of allowed users. To enable white-listing, you
can provide a list of NOMAD account email addresses in your `nomad.yaml` like this:

```yaml
oasis:
    allowed_users:
        - user1@gmail.com
        - user2@gmail.com
```

## User management

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

### Provide and connect your own user management

NOMAD uses [keycloak](https://www.keycloak.org/){:target="_blank" rel="noopener"} for its user management. NOMAD uses
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
--8<-- "docs/howto/oasis/ops/docker-compose/nomad-oasis-with-keycloak/docker-compose.yaml"
```

A few notes:

- You have to change the `KEYCLOAK_FRONTEND_URL` variable to match your host and set a path prefix.
- The environment variables on the keycloak service allow to use keycloak behind the nginx proxy with a path prefix, e.g. `keycloak`.
- By default, keycloak will use a simple H2 file database stored in the given volume. Keycloak offers many other options to connect SQL databases.
- We will use keycloak with our nginx proxy here, but you can also host-bind the port `8080` to access keycloak directly.
- We mount and use the downloaded `configs/nomad-realm.json` to configure a NOMAD compatible realm on the first startup of keycloak.

Second, we add a keycloak location to the nginx config:

```nginx
--8<-- "docs/howto/oasis/ops/docker-compose/nomad-oasis-with-keycloak/configs/nginx.conf"
```

A few notes:

- Again, we are using `keycloak` as a path prefix. We configure the headers to allow
  keycloak to pick up the rewritten url.

Third, we modify the keycloak configuration in the `nomad.yaml`:

```yaml
--8<-- "docs/howto/oasis/ops/docker-compose/nomad-oasis-with-keycloak/configs/nomad.yaml"
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

## Sharing data through log transfer and data privacy notice

NOMAD includes a *log transfer* functions. When enabled this it automatically collects
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

## Further steps

This is an incomplete list of potential things to customize your NOMAD experience.

- Learn [how to develop plugins](../plugins/plugins.md) that can be installed in an Oasis
- Write .yaml based [schemas](../manage/gui/yaml.md) and [ELNs](../manage/gui/elns.md)
- Learn how to use the [tabular parser](../manage/gui/tabular.md) to manage data from .xls or .csv
- Add specialized [NORTH tools](../manage/gui/north.md)
