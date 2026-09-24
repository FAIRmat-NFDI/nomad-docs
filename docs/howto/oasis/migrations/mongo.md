# MongoDB Migration (v5.0.6 to v8.x)

Starting with NOMAD Oasis template **v1.4.2**, the MongoDB image was upgraded from version `5.0.6` to version `8.x` (`docker.io/mongo:8.0`).

MongoDB requires sequential upgrades through major versions (`5.0` → `6.0` → `7.0` → `8.0`), updating the `featureCompatibilityVersion` at each step. You cannot directly mount a MongoDB 5.x data directory into a MongoDB 8.x container.

---

## Prerequisites

- Python >= 3.8 installed on the Docker host machine.
- Sufficient disk space for database backups.
- Ensure your existing NOMAD Oasis MongoDB container is running and healthy before starting.

---

## Migration Steps

### 1. Back up your existing MongoDB data

Before running any migration, create and verify a backup of your MongoDB database.

If you are using the `nomad-distro-template`, run the included helper backup script:

```bash
bash scripts/backup-mongo.sh
```

Confirm that the backup dump was created in `.volumes/mongo`:

```bash
ls -lh .volumes/mongo
cat .volumes/mongo/backup.log
```

!!! important
    Always ensure your MongoDB backup files exist and are verified before proceeding with the upgrade.

### 2. Run the Sequential Upgrade Script

FAIRmat provides an automated helper script that upgrades MongoDB through intermediate versions (5 → 6 → 7 → 8) and sets the appropriate `featureCompatibilityVersion` at each stage:

```bash
curl -O https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/snippets/188/raw/main/upgrade_mongo.py
python3 upgrade_mongo.py -c nomad_oasis_mongo -f docker-compose.yaml --from-version 5.0.6
```

### 3. Verify the Upgrade

1. Check that the MongoDB container is running version 8.x:
   ```bash
   docker compose exec mongo mongosh --eval 'db.version()'
   ```
2. Verify that the feature compatibility version is set to 8.0:
   ```bash
   docker compose exec mongo mongosh --eval 'db.adminCommand({getParameter: 1, featureCompatibilityVersion: 1})'
   ```
3. Check the NOMAD Oasis logs to ensure services connect successfully:
   ```bash
   docker compose logs -f app worker
   ```
