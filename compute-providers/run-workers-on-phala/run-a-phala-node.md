# Run a Phala Node

## Setup Environment

* Hardware
  * CPU: 4 Cores is recommended
  * Memory: 8GB is recommended
  * Storage: 500GB is minimum for now (07/07/2022), this requirement needs to be re-evaluated each six months.
* Software
  * Ubuntu 20.04 (Recommended) or other popular server Linux distro
  * [Docker-CE](https://docs.docker.com/engine/install/ubuntu/)
  * Bandwidth：the stabler, the better

## Run a node

We provide [prebuilt Docker image](https://hub.docker.com/repository/registry-1.docker.io/phalanetwork/phala-node/tags). We recommend use the latest version, the old version may incompatible with current chain.

```bash
docker run -dti --name phala -p 9933:9933 -p 9944:9944 -e NODE_NAME=phala-node -e NODE_ROLE=ARCHIVE -e PARACHAIN_EXTRA_ARGS='--state-cache-size 0 --unsafe-ws-external --unsafe-rpc-external' -v /data/khala:/root/data phalanetwork/phala-node
```

> More detail about start configuration can learn from [https://github.com/Phala-Network/khala-docker/blob/main/dockerfile.d/start\_node.sh](https://github.com/Phala-Network/khala-docker/blob/main/dockerfile.d/start\_node.sh)
