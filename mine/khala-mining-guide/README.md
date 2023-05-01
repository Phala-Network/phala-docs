# Khala Mining Guide

Khala Network is Phala’s canary network on Kusama Parachain featuring decentralized mining. We provide an overview to setup the mining environment, followed by a detailed explanation of each step.

We highly recommend workers to first read about Phala’s [tokenomics](../../general/phala-network/pay-for-cloud-service.md) and [staking mechanism](staking-mechanism.md) to understand the calculation of incomings and how the mining proceeds.

## Introduction <a href="#introduction" id="introduction"></a>

Workers provide computing power to the Phala Network. Anyone with the appropriate hardware can participate.

> More information about hardware requirements: 👉 [here](hardware-requirements.md)

This section provides some theory about the mining concepts of Phala and additional background information.

> To get directly started, feel free to check the quick start guide: 👉 [here](quick-start.md)

## Worker Registration <a href="#worker-registration" id="worker-registration"></a>

Registration is required before a worker or gatekeeper can join the network. After that, any parties with secure-enclave-supported devices can serve as workers. To register as a validated worker in the blockchain, Secure Enclave runners need to run `pRuntime` and let it send a signed attestation report to gatekeepers.

`pRuntime` requests a Remote Attestation with a hash of the `WorkerInfo` committed in the attestation report. `WorkerInfo` includes the public key of `IdentityKey` and `EcdhKey` and other data collected from the enclave. By verifying the report, gatekeepers can know the hardware information of workers and ensure that they are running unmodified `pRuntime`.

## Remote Attestation <a href="#remote-attestation" id="remote-attestation"></a>

The attestation report is relayed to the blockchain by `register_worker()` call. The blockchain has the trusted certificates to validate the attestation report. It validates:

1. The signature of the report is correct;
2. The embedded hash in the report matches the hash of the submitted `WorkerInfo`;

`register_worker()` is called by workers, and a worker can only be assigned contracts when it has certain amounts of staking PHA tokens. On the blockchain there is a `WorkerState` map from the worker to the `WorkerInfo` entry. Gatekeepers will update the `WorkerState` map after they receive and verify the submitted `WorkerInfo`.

## Offline Worker Detection <a href="#offline-worker-detection" id="offline-worker-detection"></a>

The `pRuntime` of a worker is regularly required to answer the online challenge as a heartbeat event on chain. The blockchain detects the liveness of workers by monitoring the interval of their heartbeat events. A worker is punished with the penalty of his staking tokens if it goes offline during a contract execution.

## Community

If you have any questions, you can always reach out to the Phala community for help:

## Khala Components <a href="#khala-components" id="khala-components"></a>

Khala requires the following components:

* Khala RPC Endpoint: `wss://khala.api.onfinality.io/public-ws`
* Khala Console: [Mining Console](https://app.phala.network/mining/)
