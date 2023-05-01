# Runtime Bridge 2.2 Release Note

> If you are for a step-by-step guide, please refer to the [upgrading guide from the community.](migrating-from-v2.0-and-v2.1-to-v2.2.md)e

## Overview <a href="#overview" id="overview"></a>

Runtime Bridge 2 uses P2P technologies to improve the mining experience. It allows multiple lifecycle instances to share data providers to reduce storage pressure and support data provider redundancy to ensure overall stability.

Deployment guide: https://github.com/Phala-Network/runtime-bridge/wiki/Deployment-Guide-for-Runtime-Bridge-2 Migrate from v0: https://github.com/Phala-Network/runtime-bridge/wiki/Migrate-from-v0-to-v2

To use with docker: `docker pull phalanetwork/prb:next` To use monitor with docker: `docker pull phalanetwork/prb-monitor:next`

Version 2.2.0 increases worker synchronization speed hugely and introduces TCP keep-alive to improve overall stability.

## Important Message <a href="#important-message" id="important-message"></a>

> `pRuntime` on workers must be upgraded to version 0.2.4(`phalanetwork/phala-pruntime:22051201`) or greater to work with Runtime Bridge v2.2.0.

## Data Provider <a href="#data-provider" id="data-provider"></a>

* Re-running the [data provider database migration](migrating-from-v0.md#migrate-data-providerfetch-data) script is required since data needs to be recomputed to work with the improved syncing mechanism.

## Lifecycle <a href="#lifecycle" id="lifecycle"></a>

* Add `WORKER_KEEPALIVE_ENABLED=true` to environment to enable the TCP keepalive feature, this improves the performance on the scenario with huge amount of workers. **Warning: workers will be failed if running an old version of `pRuntime`.**
* Add `USE_BUILT_IN_TRADER=true` to environment to enable the built-in trader, `trader` and `arena` will be up with the lifecycle manager when the option is enabled, and the external trader will not be needed anymore. This option will be enabled by default in next major version.
* Align the process with `pherry` when synching block data to workers.

## Known issues <a href="#known-issues" id="known-issues"></a>

* Data Provider: Synching from the P2P network is not implemented yet.
* Trade: Will deprecate `bee-queue` in future releases.
