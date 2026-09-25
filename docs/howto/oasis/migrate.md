# How to migrate a NOMAD Oasis

From time to time, you will need to update your Oasis to a new NOMAD version. Usually this is straightforward: you update your Oasis distribution to the corresponding `nomad-distro-template` version. This ensures that you get compatible versions of the infrastructure components (such as databases) and that the Docker image built for your Oasis uses the right NOMAD version.

Sometimes, however, a new NOMAD version also requires migrating your existing data. Different NOMAD versions may represent data differently: the search index definition, database schema, file system layout, or internal file formats can change. For such changes, we may offer a transition period during which NOMAD supports both the old and the new representation. Eventually, though, the existing data must be migrated, either because the change is breaking, because the old representation is deprecated, or because the new representation enables new features.

It is important to understand that the NOMAD software and your data are independent of each other: switching to a new image does not change the data in your installation. Any required data migration is a separate step that you need to perform.

## General migration best practices

Before performing any data or database migration on your Oasis:

1. **Back up your data**: Make sure you have an up-to-date dump of your MongoDB database (e.g. using `scripts/backup-mongo.sh`) and that your uploaded files in `.volumes/fs` are securely backed up. See [Backups](administer.md#backups) for more details.
2. **Review the release notes**: Check the [NOMAD distribution template releases](https://github.com/FAIRmat-NFDI/nomad-distro-template/releases){:target="_blank" rel="noopener"} and the [NOMAD Python packages releases](https://github.com/FAIRmat-NFDI/nomad/releases){:target="_blank" rel="noopener"} for version-specific considerations and changes to configuration files (`docker-compose.yaml`, `nomad.yaml`, etc.).

After performing a migration, **verify container health**: check that all services start cleanly and report a healthy status using `docker compose ps` and `docker compose logs`.

## Migration guides for specific versions
The migration guides for specific NOMAD versions are found as subpages:

{{ nav_list(descriptions={
    "howto/oasis/migrate/v2.0.md": "Elasticsearch 7 → 9; the search index must be migrated or rebuilt.",
    "howto/oasis/migrate/v1.4.2.md": "MongoDB 5 → 8; step-by-step database upgrade.",
    "howto/oasis/migrate/v1.2.2.md": "JupyterHub database upgrade for NORTH.",
    "howto/oasis/migrate/v1.2.0.md": "Plugin mechanism and new archive format; re-processing recommended.",
    "howto/oasis/migrate/v0.8-to-v1.md": "Full data migration and reprocessing.",
}) }}
