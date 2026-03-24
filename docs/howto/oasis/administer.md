# How to perform admin tasks

## Backups

To backup your Oasis at least the file data and mongodb data needs to be saved. You determined the path to your file data (your uploads) during the installation. By
default all data is stored in a directory called `.volumes` that is created in the
current working directory of your installation/docker-compose. This directory can be backed up like any other file backup (e.g. rsync).

To backup the mongodb, please refer to the official [mongodb documentation](https://docs.mongodb.com/manual/core/backups/){:target="_blank" rel="noopener"}. We suggest a simple mongodump export that is backed up alongside your files. The default configuration mounts `.volumes/mongo` into the mongodb container (as `/backup`) for this purpose. You can use this to export the NOMAD mongo database. Combine this with rsync on the `.volumes` directory and everything should be set. To create a new mongodump run:

```sh
docker exec nomad_oasis_mongo mongodump -d nomad_oasis_v1 -o /backup
```

The elasticsearch contents can be reproduced with the information in the files and the mongodb.

To create a new Oasis with the backup data, create the `.volumes` directory from your backup. Start the new Oasis. Use mongorestore:

```sh
docker exec nomad_oasis_mongo mongorestore /backup
```

Now you still have to recreate the elasticsearch index:

```sh
docker exec nomad_oasis_app python -m nomad.cli admin uploads index
```

## Managing data with the CLI

The NOMAD command line interface (CLI) provides a few useful administrative functions. To use the NOMAD CLI, open a shell into the app container and run it from there:

```sh
docker exec -ti nomad_oasis_app bash
```

For example you can ls or remove uploads:

```sh
nomad admin uploads ls
nomad admin uploads rm -- <upload_id> <upload_id>
```

You can also reset the processing (of "stuck") uploads and reprocess:

```sh
nomad admin uploads reset -- <upload_id>
nomad admin uploads process -- <upload_id>
```

You can also use the CLI to wipe the whole installation:

```sh
nomad admin reset --i-am-really-sure
```

### Upload commands

The `nomad admin uploads` group of CLI commands allow you to inspect and modify
all or some uploads in your installation. Sub-commands include `ls`, `rm`,
`chown`, `process` (see below), `index` (see below).

The command group takes many different parameters to target specific subsets of uploads.
Here are a few examples:

- `--unpublished`
- `--published`
- `--outdated` Select published uploads with older NOMAD versions than the current
- `--processing-failure` Uploads with processing failures.

For a complete list refer to the [CLI reference documentation](../../reference/cli.md#nomad-admin-uploads).

Alternatively, you can use a list of upload ids at the end of the command, e.g.:

```sh
```sh
nomad admin uploads ls -- <id1> <id2>
```

If you have a list of ids (e.g. in a file), you could use `xargs`:

```sh
cat file_with_ids.txt | xargs nomad admin uploads ls --
```

### Re-processing

Processing includes the conversion of raw files into NOMAD entries. Files are parsed,
normalizers are called, the processing results are stored, and the search index
is updated. In certain scenarios (failed processing, [migration](update.md#migration-steps),
changed plugins) might require that admins process certain uploads again.

```sh
nomad admin uploads process
```

### Re-Indexing

Each NOMAD entry is represented in NOMAD's search index. Only if an entry is in this
index, you can find it via the search interface. Some changes between NOMAD versions
(see also our [update guide](update.md#migration-steps)), might require that
you re-index all uploads.

```sh
nomad admin uploads index
```
