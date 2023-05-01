# Migrating from v2.0 and v2.1 to v2.2

> This page is contributed by community members. For more information about the v2.2 update, please refer to the [release notes](runtime-bridge-2.2-release-note.md).

## Prerequisite <a href="#prerequisite" id="prerequisite"></a>

* Before you start, make sure you have enough storage. You should have max 40-45% in usage, but not more than 49% in usage!
* FYI: If you are running a HA active/standby setup, you can follow these steps … special indications for HA failover is provided.
* FYI: Please make sure your standby is in sync with keys/local.db with your master!
* FYI: You are recommended to upgrade to pruntime 1.2.4 FIRST, together with PRB 2.2 you will see improvement of syncing speeds.

## Steps <a href="#steps" id="steps"></a>

Start at your standby machine (or production machine if you have a single machine)

```
[email protected]:/opt/prb# df -h /
Filesystem                         Size  Used Avail Use% Mounted on
/dev/mapper/ubuntu--vg-ubuntu--lv  1.7T  756G  836G  48% /
```

Download new images

```
[email protected]:/opt/prb# cd /opt/prb
[email protected]:/opt/prb# docker-compose pull
```

Confirm you have the right images and using the right images in compose:

```
[email protected]:/opt/prb# docker image ls
REPOSITORY                 TAG        IMAGE ID       CREATED          SIZE
phalanetwork/prb           next       8f3e932046bc   16 minutes ago   1.75GB

[email protected]:/opt/prb# grep image docker-compose.yml
    image: redis:alpine
    image: phalanetwork/prb:next
    image: phalanetwork/prb:next
    image: phalanetwork/prb:next
    image: phalanetwork/prb:next
    image: phalanetwork/prb-monitor:next
```

Add the following items to docker-compose.yml, under the lifecycle section and the environment subsection

```
  - WORKER_KEEPALIVE_ENABLED=true
  - USE_BUILT_IN_TRADER=true
```

Add the following section back, you will likely have the first 3 lines, but the last line needs to be added at this stage:

```
x-defaults: &defaults
  volumes: &default-volume-config
    - /opt/prb/data:/var/data
    - /opt/prb/data_old:/var/data_old
```

Start the upgrade proces, please note you cannot cancel this and once started it might take several hours or days to complete. The speed depends on your hardware and configuration.

```
[email protected]:/opt/prb# docker-compose down
[email protected]:/opt/prb# mv data data_old
[email protected]:/opt/prb# docker-compose run --entrypoint "yarn migrate_data_provider" data_provider
```

Now noticed the upgrade of currentPara moving to the hieght of paraTarget, in my case this took about 30 minutes.

Now noticed the upgrade of currentParent moving to parentTarget, in my case this took about about 8 hours.

It would end back and the console with a message that is has completed. For monitoring purposes you are advices to remove the migration container with `docker rm`

```
[email protected]:/opt/prb# docker ps --all
CONTAINER ID   IMAGE                   COMMAND                  CREATED        STATUS                         PORTS     NAMES
f9a6788f649d   phalanetwork/prb:next   "yarn migrate_data_p…"   18 hours ago   Exited (0) About an hour ago             prb_data_provider_run_1c80b8f9f306

[email protected]:/opt/prb# docker rm prb_data_provider_run_1c80b8f9f306
prb_data_provider_run_1c80b8f9f306
```

If you are upgrading from version 2.0, no lifecycle migration is needed, if you upgrade from an earlier version, you also must upgrade LFM.

You can skip this step if you are running PRB:next (aka 2.0+):

```
[email protected]:/opt/prb#  docker-compose run --entrypoint "yarn migrate_lifecycle" lifecycle
```

If you do NOT have to migrate lifecycle, you will have to copy your old database and key back. Make sure you ONLY copy the files as described below!

```
[email protected]:/opt/prb# cp data_old/keys/id/LIFECYCLE data/keys/id/
[email protected]:/opt/prb# cp data_old/local.db data/
```

Alternatively (maybe even better) you should copy these files from your current active server.

Now comment the data\_old volume, as its no longer needed

```
x-defaults: &defaults
  volumes: &default-volume-config
    - /opt/prb/data:/var/data
#    - /opt/prb/data_old:/var/data_old
```

Now remove the trade and arena services from the docker-compose.yml, these services have been migrated into LFM and are now obsolete. You must remove these, else you cannot start your stack!

If you are running an HA setup, you are recommended to resync keys and data files from your current active node (assuming you are upgrading your standby node… if not, this is kinda mute)

Be very sure you rsync this in the RIGHT directory and you are advised to make backups before you start. Skip this if you run a single machine setup.

```
  rsync from active machine the local.db to your standby machine
  rsync from active machine the the LIFECYCLE file to your standby machine
```

WARNING: From this setup you can NOT make any changes to PRB until the failover is completed (!) and do NOT replace the DATAPROVIDER file (!)

Now start up data\_provider and let it sync up, this will take some type as its needs to process all the cache updates at its first run. You will know when its done syncing if the excessive scrolling stops.

```
[email protected]:/opt/prb#  docker-compose up -d data_provider
```

Once the machine is synced it is time to do a failover to your standby machine running this new PRB version:

```
# On active:
[email protected]:/opt/prb#  docker-compose down

#On Standby:
[email protected]:/opt/prb#  docker-compose up -d
```

Now the roles are switched. If all went well, your mining should continue where it has left off. If you see major issues, just turn the old active machine back online (after shutdown of the new PRB !)

If all went well I suggest you leave your old-active machine as-is for a few days, but you can restart data\_provider to make sure it’s kept in sync if you need to fail back to the machine. After this periode you are advised to upgrade it as well so your HA pair is in version sync again for the next upgrade. Make sure you copy keys to your old active as well. you should also keep the data\_old folder when you can, at least until you are satisfied the upgrade is successfulexxe.
