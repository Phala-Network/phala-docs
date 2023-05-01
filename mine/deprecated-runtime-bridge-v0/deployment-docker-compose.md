# Deployment: Docker Compose

Every release of `prb` is publish on [Docker Hub](https://hub.docker.com/r/phalanetwork/prb) once it gets on the Github release page, you can get the latest release by running:

```
docker pull phalanetwork/prb
```

The `prb` is designed to be simple, basic and easily integrated with RPC without modifying its code. With containers, managing `prb` services and integrating them is much easier. Here is an example of how to deploy `prb` with Docker Compose.

> **Note:** This expample explains the relationship between services only, you should design your setup regrading your own requirements.

## Requirements <a href="#requirements" id="requirements"></a>

* Ubuntu LTS 20.04
* Docker 20.10 or newer
* Docker Compose 1.29 or newer

> The version of docker in Ubuntu’s default APT source is too old，follow https://docs.docker.com/engine/install/ and https://docs.docker.com/compose/install/ to get latest Docker and Docker Compose.

> In production, use a prebuilt image instead of building from the master branch to prevent unexpected changes.

## Prepare the environment <a href="#prepare-the-environment" id="prepare-the-environment"></a>

1. Create a folder for the deployment environment, then create docker-compose.yml which is edited from [here](https://github.com/Phala-Network/runtime-bridge/blob/master/docker/testing/bridge/docker-compose.example.yml).
2. Run `docker-compose pull` to pull the latest images.
3. Deploy `pruntime` on worker machines.
4. Create mining pool on the blockchain.

## Base Services <a href="#base-services" id="base-services"></a>

Run `docker-compose up -d redis io` to start the base services.

In this example, data in Redis is not persisted, unexpected exit will break the whole environment, please do build a HA setup for Redis in production. Expose the Redis port to make the RPC work.

RocksDB/LevelDB will save data in `PHALA_DB_PREFIX` specified in environment variables. The `0` directory is used for the data of block data. The `1` directory is used for the data of saved pools and workers including credentials, do backup it!

## The `fetch` Service <a href="#the-fetch-service" id="the-fetch-service"></a>

Run `docker-compose up -d fetch` to start the `fetch` service.

It requires 3 CPU cores to:

1. Fetch headers with justification from the parent chain.
2. Fetch headers and storage changes from the parachain.
3. Encode them in formats that `pruntime` consumes by block.
4. Organize and merge data mentioned above for fast synchronization.

All these work are done asynchronously, you can see the processes can take a heavy load of CPU time. The `fetch` service can be stopped and started as many times as you want.

## The `trade` Service <a href="#the-trade-service" id="the-trade-service"></a>

Run `docker-compose up -d trade` to start the `trade` service.

It only needs 1 CPU core to sign and send extrinsics read from the message queue. It keeps keyring in memory, keep it safe.

Everytime you changed account information of pools, you need to restart the `trade` service to take effect.

## The `lifecycle` Service <a href="#the-lifecycle-service" id="the-lifecycle-service"></a>

Run `docker-compose up -d lifecycle` to start the `lifecycle` service. It controls the lifecycle of TEE workers. Use the [monitor](https://github.com/Phala-Network/runtime-bridge-monitor) to add, edit, remove, and check status for workers.

It should handle the corresponding worker lifecycles after making changes to workers(testing and debugging for now), roughly restarting it should also work.
