---
description: >-
  If you don't have enough harddisk for a full node. Here is a deployment method
  to save your space:
---

# Archive node deployment

**Use the docker compose like this to deploy your Node and headers cache**

```docker
version: "3"
services:
  node:
    image: phalanetwork/phala-node-with-launcher:latest
    container_name: node
    hostname: node
    restart: always
    ports:
     - "9944:9944"
     - "9945:9945"
     - "30333:30333"
     - "30334:30334"
    environment:
     - NODE_NAME=NODE
     - NODE_ROLE=ARCHIVE
     - PARACHAIN_EXTRA_ARGS=--max-runtime-instances 32 --runtime-cache-size 8 --rpc-max-response-size 256
     - RELAYCHAIN_EXTRA_ARGS=--max-runtime-instances 32 --runtime-cache-size 8 --rpc-max-response-size 256 --blocks-pruning archive-canonical --state-pruning 50400
    volumes:
     - /var/phala/node-data:/root/data

  phala-headers-cache:
    image: phalanetwork/headers-cache:latest
    container_name: phala-headers-cache
    network_mode: host
    restart: always
    environment:
      - ROCKET_PORT=22111
      - ROCKET_ADDRESS=0.0.0.0
      - RUST_LOG=info
    command:
      - serve
      - --grab-headers
      - --node-uri=ws://{node-ip}:9945
      - --para-node-uri=ws://{node-ip}:9944
      - --interval=60
    volumes:
      - ./phala-headers-cache-public:/opt/headers-cache/data
```

It can be connected to both Prb3 or pherry, and then connected to pRuntime. But remember:

**You can't start syncing the headers cache with an existing archive node, they can only starting syncing from 0 together.**
