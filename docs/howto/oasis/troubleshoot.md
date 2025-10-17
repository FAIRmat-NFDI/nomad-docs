# Troubleshoot your Oasis

## Time offset between Oasis and the Authentication server

If during login you get an error like: `jwt.exceptions.ImmatureSignatureError: The token is not yet valid (iat)`, it most probably means that there is a time difference between the two machines: the one creating the JWT and the other that is validating it. This causes an error where the authentication server looking at the token thinks that it has not been issued yet.

To fix this problem, you should ensure that the time on the servers is synchronized. It is possible that a network port on one of the servers may be closed, preventing it from synchronizing the time. Note that the servers do not need to be on the same timezone, as internally everything is converted to UTC+0. To check the time on a server, you can on a Linux-based machine use the [`timedatectl`](https://man7.org/linux/man-pages/man8/hwclock.8.html){:target="_blank" rel="noopener"} command which will report both the harware clock and the system clock (see [difference](https://developer.toradex.com/software/linux-resources/linux-features/real-time-clock-rtc-linux/#:~:text=Two%20clocks%20are%20important%20in,maintained%20by%20the%20operating%20system.){:target="_blank" rel="noopener"}). For authentication, the system clocks on the two machines need to be set correctly, but you might also need to correct the hardware clock since it initially sets the system clock upon rebooting the machine.

## NOMAD in networks with restricted Internet access

Some network environments do not allow direct Internet connections, and require the use of an outbound proxy.
However, NOMAD needs to connect to the central user management or elasticsearch thus requires an active Internet
connection (at least on Windows) to work.
In these cases you need to configure docker to use your proxy.
See details via this link [https://docs.docker.com/network/proxy/](https://docs.docker.com/network/proxy/){:target="_blank" rel="noopener"}.
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

If you have issues please contact us on discord n the [oasis channel](https://discord.com/channels/1201445470485106719/1205480348050395136){:target="_blank" rel="noopener"}.

## NOMAD behind a firewall

It is also possible that your docker container is not able to talk to each other.
This could be due to restrictive settings on your server.
The firewall shall allow both inbound and outbound HTTP and HTTPS traffic.
The corresponding rules need to be added.
Furthermore, inbound traffic needs to be enabled for the port used on the `nginx` service.

In this case you should make sure this test runs through:
[https://docs.docker.com/network/network-tutorial-standalone/](https://docs.docker.com/network/network-tutorial-standalone/){:target="_blank" rel="noopener"}

If not please contact your server provider for help.

## Elasticsearch and open files limit

Even when run in docker elasticsearch might require you to change your systems resource
limits as described in the elasticsearch documentation
[Elasticsearch documentation > setting-system-settings](https://www.elastic.co/guide/en/elasticsearch/reference/current/setting-system-settings.html){:target="_blank" rel="noopener"}.

You can temporarely change the open files limit like this:

```sh
sudo ulimit -n 65535
```
