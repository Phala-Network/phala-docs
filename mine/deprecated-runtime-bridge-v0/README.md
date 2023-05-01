# (Deprecated) Runtime Bridge v0

## Abount Runtime Bridge

In the solo mining scenario, [pherry](https://github.com/Phala-Network/phala-blockchain/tree/master/standalone/pherry) plays the part of fetching blocks from the network and send them to the TEE runtime. It works gracefully but enconters some productivity and performance issues in the pool mining scenario. Thus, Phala [Runtime Bridge](https://github.com/Phala-Network/runtime-bridge) a.k.a. `prb` is introduced to take advantage of the mining pool machanism introduced in Tokenomic v0.9 and reduces the complexity of using standalone pherry.

The `prb` is designed to be deployed in a Cloud Native environments but also runs via traditional Linux shell, it provides a RPC interface to manage workers' lifecycle through Redis. It is intended to replace pherry (previous `phost`) in both solo and pool mining scenarios.

## Requirements <a href="#requirements" id="requirements"></a>

For that `prb` uses Node.js since only the JavaScript client of Substrate is officially well maintained, it creates serval processes when running because of Node.js' single-thread model. In this case, a CPU with at least 8 cores and strong single-core performance is recommended.

Both RocksDB and LevelDB are available for the `prb` to use as the storage backend, it requires sufficient random I/O performance to support the large number of concurrent workers. Thus, a PCI-E 4.0 x4 SSD with big cache would be preferred. FYI, the space usage for each block in average:

* 50 KiB using LevelDB,
* 40 KiB using RocksDB.

While `prb` sends extrinsics to synchronize between the TEE workers and the blockchain, it does require a full-featured node running in the local network environment for both Phala(`parachain`) and the Parent Chain.

## Services <a href="#services" id="services"></a>

The `prb` provides the following services:

* `io`: a simple server to provide internal RocksDB/LevelDB I/O ability. while RocksDB/LevelDB is thread-safe, it can only keep one instance running at the same time.
* `fetch`: it fetches block data the blockchains then processes them for synchronization.
* `trade`: it makes transactions(extrinsics) to the blockchain.
* `lifecycle`: it handles the lifecycle and status of the workers, synchronize message queues and block data between the TEE and the blockchain.

### Redis, RPC and the monitor <a href="#redis-rpc-and-the-monitor" id="redis-rpc-and-the-monitor"></a>

Redis is used to maintain the internal message queue and to communicate between components. since Redis allows unauthorized access by default, **DO NOT EXPOSE IT TO THE INTERNET DIRECTLY**.

The `prb` uses Protobuf to define the RPC interface, [here is the definitions](https://github.com/Phala-Network/runtime-bridge-proto/blob/main/message.proto).

The [monitor](https://github.com/Phala-Network/runtime-bridge-monitor) is a simple web server that provides a simple web interface to manage the workers. It’s also an example of the RPC usage.

### Linux kernel tuning <a href="#linux-kernel-tuning" id="linux-kernel-tuning"></a>

It’s unnecessary to do the tuning during development and testing.

When there are more than \~300 workers in the setup, the machine running the lifecycle component should be tuned to be able to maintain huge amount of TCP connections, [an example](https://github.com/Phala-Network/runtime-bridge/tree/master/system/bridge) is provided for referring, be ware that we can not provides support of the Linux kernel and your actual environment.
