# Running Directly in Linux

Running `prb` directly in a Linux shell is not recommended since using Docker is more convenient in both development and production.

## Requirements <a href="#requirements" id="requirements"></a>

* git
* Redis 5 or newer
* Node.js 14 (Latest LTS)
* pnpm

## Set up dependencies and generate Protobuf interfaces <a href="#set-up-dependencies-and-generate-protobuf-interfaces" id="set-up-dependencies-and-generate-protobuf-interfaces"></a>

```
git submodule init
git submodule update
pnpm install
pnpm proto:build # use `pnpm proto:darwin:build` in macOS
pnpm proto:build_prpc # use `pnpm proto:darwin:build_prpc` in macOS
```

## Start Services <a href="#start-services" id="start-services"></a>

To start any of the services, run `pnpm start_module`, all parameters are read from the environment variables of current shell.

```
PHALA_MODULE=fetch # module to start
NODE_ENV=development
PHALA_DB_HOST=io # hostname/ip to io service
PHALA_DB_PORT_BASE=9000
PHALA_LOGGER_LEVEL=debug
PHALA_PARENT_CHAIN_ENDPOINT=ws://127.0.0.0:9945 # parent chain substrate websocket endpoint
PHALA_CHAIN_ENDPOINT=ws://127.0.0.0:9945 # parachain substrate websocket endpoint
PHALA_REDIS_ENDPOINT=redis://127.0.0.1:6379 # redis endpoint for mq and rpc

# for `io`
PHALA_DB_PREFIX=/var/data # path to data directory
PHALA_DB_TYPE=rocksdb # rocksdb or leveldb
```
