# Migrating from v0

## Overview <a href="#overview" id="overview"></a>

This article explains the steps to migrate data from Runtime Bridge v0 to v2.

Before doing the migration, please set environment variables referring to the Deployment Guide.

## Migrate Data Provider(fetch) data <a href="#migrate-data-providerfetch-data" id="migrate-data-providerfetch-data"></a>

| Required env var        | Comments                             | Default value     |
| ----------------------- | ------------------------------------ | ----------------- |
| OLD\_DATA\_PATH         | Path to the old data folder          | /var/data\_old/   |
| NEW\_DATA\_PATH         | Path to the new data folder          | /var/data/        |
| PHALA\_CHAIN\_ENDPOINT  | WebSocket endpoint to Phala.         | N/A               |
| PHALA\_PEER\_ID\_PREFIX | Path to libp2p identity store folder | /var/data/keys/id |

1. Run `docker-compose down` and make sure there is no other Runtime Bridge instance running.
2. Pull latest images from `phalanetwork/prb:next`.
3. Change to mount point of the current data folder to `/var/data_old/` and set the new mount point of the new data folder to `/var/data`, for example:

```
volumes: &default-volume-config
    - /opt/deploy/data:/var/data_old
    - /opt/deploy/data_1:/var/data
```

1. Run `docker-compose run --entrypoint "yarn migrate_data_provider" data_provider`, and wait for the migration progress. This script will copy raw block data to a new clean database. Make sure that there is sufficient disk capacity.
2. Check the Deployment Guide to make everything okay then run `docker-compose up` to start the data provider, the data provider will re-process the block data.

## Migrate lifecycle manager <a href="#migrate-lifecycle-manager" id="migrate-lifecycle-manager"></a>

| Required env var        | Comments                             | Default value      |
| ----------------------- | ------------------------------------ | ------------------ |
| OLD\_DATA\_PATH         | Path to the old data folder          | /var/data\_old/    |
| PHALA\_LOCAL\_DB\_PATH  | Path to the new database             | /var/data/local.db |
| PHALA\_PEER\_ID\_PREFIX | Path to libp2p identity store folder | /var/data/keys/id  |

1. Run `docker-compose down` and make sure there is no other Runtime Bridge instance running.
2. Pull latest images from `phalanetwork/prb:next`.
3. Change to mount point of the current data folder to `/var/data_old/` and set the new mount point of the new data folder to `/var/data`, refer to above for example.
4. Run `docker-compose run --entrypoint "yarn migrate_lifecycle" lifecycle`, and wait for the migration progress. This script will generate an RSA keypair as the identity of its libp2p peer, it will be also used as the encryption key of saved Polkadot account.
5. Check the Deployment Guide to configure data providers and make everything okay then run `docker-compose up` to start the lifecycle manager.

## Clean up unused data <a href="#clean-up-unused-data" id="clean-up-unused-data"></a>

After making sure the new Runtime Bridge v2 setup running, delete the old data folder to free up disk space.
