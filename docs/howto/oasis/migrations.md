# How to migrate a NOMAD Oasis

When updating a NOMAD Oasis across major releases, backend database and search engine services may require data migrations to ensure compatibility with new software versions. 

This section collects guides for major service migrations that have been introduced across NOMAD Oasis releases.

---

## Available Migration Guides

### [MongoDB Migration (v5.0.6 to v8.x)](migrations/mongo.md)

Starting with NOMAD Oasis template **v1.4.2**, the MongoDB image was upgraded from version `5.0.6` to version `8.x` (`docker.io/mongo:8.0`).

MongoDB requires sequential upgrades through major versions (`5.0` → `6.0` → `7.0` → `8.0`), updating the `featureCompatibilityVersion` at each step. FAIRmat provides an automated helper script to carry out this sequential upgrade safely.

- [Read the MongoDB Migration Guide](migrations/mongo.md)

---

### [Elasticsearch Migration (v7.17 to v9.5)](migrations/elastic.md)

Starting with **NOMAD 2.0**, NOMAD Oasis has migrated its search backend from **Elasticsearch 7** to **Elasticsearch 9** (default container version `9.5.0`).

Elasticsearch 9 cannot read index files created with Elasticsearch 7 due to major Lucene version changes. Two migration options are supported:

1. **Option 1: Reindex data from ES7 to ES9 (Running two containers)** — Migrates index data directly via Elasticsearch's `_reindex` API without reprocessing archive files.
2. **Option 2: Start from a fresh ES9 container and reindex uploads** — Starts with a clean ES9 container and rebuilds the search index from MongoDB and raw archives stored in `.volumes/fs`.

- [Read the Elasticsearch Migration Guide](migrations/elastic.md)

---

## General Migration Best Practices

Before performing any data or database migrations on your Oasis:

1. **Always back up your data**: Ensure you have an up-to-date dump of your MongoDB database (`scripts/backup-mongo.sh`) and that your uploaded file storage in `.volumes/fs` is securely backed up.
2. **Review release notes**: Check the [NOMAD distribution template releases](https://github.com/FAIRmat-NFDI/nomad-distro-template/releases) for any version-specific considerations or changes to configuration files (`docker-compose.yaml`, `nomad.yaml`, etc.).
3. **Verify container health**: After running a migration, always verify that your services start cleanly and report healthy status (`docker compose ps` and `docker compose logs`).
