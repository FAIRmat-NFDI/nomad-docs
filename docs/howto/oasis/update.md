# How to update Oasis versions

## Software versions

In order to update your Oasis to a newer software version, you usually should follow the <a href="https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#updating-the-distribution-from-the-template" target="_blank" rel="noopener">update guide in the distribution template</a>. This makes sure that you get both the most recent version of the configuration files, and the `nomad-lab` Python package.

You may also only update the `nomad-lab` Python package in your distribution by doing the following changes in the `pyproject.toml` file:

```toml
[project]
...
dependencies = ["nomad-lab[infrastructure]==<version-number>"]
...
dev = ["nomad-lab[infrastructure, dev]==<version-number>"]
...
```

## Data versions

Different version of NOMAD might represent data differently. For example, the
definition of the search index, database schema, file system layout, or internal file
formats might change.
For such changes, we might offer a migration period, where NOMAD supports two different
data representations at the same time.
However, eventually this requires some migration of the existing data. This might be necessary
for breaking changes (or because an old representation is deprecated) or advisable
because a new representation offers new features.
Therefore, it is important to understand that the used
NOMAD software and data are independent things. Using a new image, does not change the
data in your installation.

We will list respective changes and guides under [migration steps](#migration-steps) below.

## Using a new version

To use a different version of NOMAD, it can be as simple as swapping the tag in the
docker-compose services that use the nomad images (i.e. `app` and `worker`). Depending
on the version change, further steps might be necessary:

- for patch releases no further actions should be necessary
- for minor releases some additional actions might be required to unlock new features
- for major releases breaking changes are likely and further actions will be required

For changing the minor or major version, please check the [migration steps](#migration-steps) below.

## Migration steps

### to 1.2.2

We upgraded the JupyterHub version used for NORTH from 1.0.2 to 4.0.2. By default the
JupyterHub database is persisted in the `nomad_oasis_north` container. If you want to
keep the database (e.g. to not loose any open tools), you will have to upgrade the database.
Update the NOMAD docker image version and restart the Oasis like this:

```sh
docker compose down
docker compose pull
docker compose run north python -m jupyterhub upgrade-db
docker compose up -d
```

Alternatively, you can delete the `nomad_oasis_north` container and start with a fresh
database. Make sure that all north tools are stopped and removed.

```sh
docker compose down
docker rm nomad_oasis_north
docker compose pull
docker compose up -d
```

### to 1.2.0

- We introduced the plugin mechanism. There are now more options to control which schemas
  and parsers are available in your installation. By default all the existing and shipped
  schemas and parsers are enabled. See also [Configure > Plugins](configure.md#plugins).

- We changed the archive file format. [Re-processing](administer.md#re-processing) might yield better performance.

- Parsers are now using a different workflow model and the UI now includes a
  workflow card on the overview page of entries with workflows for the new model.
  [Re-processing](administer.md#re-processing) all data will enable this feature for old data. Any analysis build on
  the old workflow model, might not work for new data.

- We introduce the *log-transfer* service. This is currently an opt-in feature.

### from 0.8.x to 1.x

Between versions 0.10.x and 1.x we needed to change how archive and metadata data is stored
internally in files and databases. This means you cannot simply start a new version of
NOMAD on top of the old data. But there is a strategy to adapt the data. This should
work for data based on NOMAD >0.8.0 and <= 0.10.x.

The overall strategy is to create a new mongo database, copy all information, and then
reprocess all data for the new version.

First, shutdown the OASIS and remove all old containers.

```sh
docker compose stop
docker compose rm -f
```

Update your config files (`docker-compose.yaml`, `nomad.yaml`, `nginx.conf`) according
to the latest documentation (see above). Make sure to use index and database names that
are different. The default values contain a version number in those names, if you don't
overwrite those defaults, you should be safe.

Make sure you get the latest images and start the OASIS with the new version of NOMAD:

```sh
docker compose pull
docker compose up -d
```

If you go to the GUI of your OASIS, it should now show the new version and appear empty,
because we are using a different database and search index now.

To migrate the data, we created a command that you can run within your OASIS' NOMAD
application container. This command takes the old database name as an argument, it will copy
all data from the old mongodb to the current one. The default v8.x database name
was `nomad_fairdi`, but you might have changed this to `nomad_v0_8` as recommended by
our old Oasis documentation.

```sh
docker exec -ti nomad_oasis_app bash -c 'nomad admin upgrade migrate-mongo --src-db-name nomad_v0_8'
docker exec -ti nomad_oasis_app bash -c 'nomad admin uploads reprocess'
```

Now all your data should appear in your OASIS again. If you like, you can remove the
old index and database:

```sh
docker exec nomad_oasis_elastic bash -c 'curl -X DELETE http://elastic:9200/nomad_fairdi'
docker exec nomad_oasis_mongo bash -c 'mongo nomad_fairdi --eval "printjson(db.dropDatabase())"'
```
