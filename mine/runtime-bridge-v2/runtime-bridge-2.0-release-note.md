# Runtime Bridge 2.0 Release Note

## Overview <a href="#overview" id="overview"></a>

Runtime Bridge 2 uses P2P technologies to improve the mining experience. It allows multiple lifecycle instance share data providers to reduce storage pressure and support data provider redundancy to ensure overall stability.

* To use with docker: `docker pull phalanetwork/prb:next`
* To use monitor with docker: `docker pull phalanetwork/prb-monitor:next`

## Walkie <a href="#walkie" id="walkie"></a>

The internal communication protocol has been refactored with `libp2p`(The same protocol that Substrate uses), which provides component discovery ability to build a setup quickly.

Also, we’ve made it a separate package to make the API easier to use. Run `yarn add @phala/runtime-bridge-walkie` to add it to your Node.js app simply.

Source code: [https://github.com/Phala-Network/runtime-bridge-walkie](https://github.com/Phala-Network/runtime-bridge-walkie)

Detailed documents will be up with the stable release of Runtime Bridge 2.

## Data Provider <a href="#data-provider" id="data-provider"></a>

The old `fetch` component has been upgraded to `data_provider`. It does the same as the old `fetch` component but also serves as a blob server.

## Lifecycle <a href="#lifecycle" id="lifecycle"></a>

One lifecycle instance now runs multiple runners if it has too many workers due to the thread-safe model of Node.js.

Saved critical information is encrypted now. The raw `polkadotJson` can be no more exported.

## Monitor <a href="#monitor" id="monitor"></a>

The monitor can discover running components automatically thanks to `libp2p`.

## Updates from beta.0 <a href="#updates-from-beta0" id="updates-from-beta0"></a>

* Fix: OOM issues
* Fix: BlockNumberMismatch

## Known issues <a href="#known-issues" id="known-issues"></a>

* Data Provider: Synching from the P2P network is not implemented yet.
* Monitor: The functionalities to add/edit/delete workers/pools are not implemented yet.
* Trade: Will deprecate `bee-queue` in future releases.
