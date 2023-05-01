# Closed Beta

Welcome to the Closed Beta test of Phat Contract!

> If you haven’t registered yet, fill in the [application form](https://docs.google.com/forms/u/0/d/1LUmSQ\_7B3Yh7tNCPAluBUAwhAN0HjZ3b9wragWI1Bbs) to get involved.

## What you will experience <a href="#what-you-will-experience" id="what-you-will-experience"></a>

You will be able to use trustless off-chain computation that doesn’t suffer from the limitations traditionally faced by Web3 computation.

* Phala Network brings decentralization, scale, and security, and manages the deployment of your compute off-chain.
* Phat Contract brings a quantum leap in capability, a serverless SDK you can write almost anything with.

For the first time, you can easily implement important Web3 services on a decentralized infrastructure, like

* Easily building decentralized Oracle;
* Allowing customers to sign in to your DApps with Web2 accounts through OAuth;
* Controlling your smart contracts even if they are on different chains;
* Reading and storing data to any storage services while remaining private;

and more for us to explore together.

## Table of contents <a href="#table-of-contents" id="table-of-contents"></a>

* [Getting Started](broken-reference) is prepared for everyone new to Phat Contract, even if you do not have any programming experience. It has no requirements on your operating system or environment. Follow our tutorial to:
  * Generate the test account
  * Try Phat Contract Console
  * Deploy the pre-compiled contract to our testnet
  * Invoke the contract, it will use its network access to read the Ethereum account balance for you
* [Build on Phat Contract](../build-on-phat-contract/build-stateless-backend.md) will lead you to config your environment and compile your first stateless DApp with Phat Contract. It covers all the basic information including:
  * Environment setup
  * Programming language basics
  * User interaction
  * Local unit test
* [Store Contract States](../store-contract-states.md) introduces the different storages you can utilize to store your contract states and data, including
  * Volatile local cache
  * Consistent on-chain storage
  * External storage services
* [Advanced Techniques](../advanced-topics/) includes advanced features like system contract and SideVM, which further extend the capabilities of Phat Contract.
* [Blockchain Infrastructure](broken-reference) contains the system design of the underlying infrastructure that supports Phat Contract. It helps to understand how your contract is deployed and why it’s safe.

## Other resources <a href="#other-resources" id="other-resources"></a>

* Code examples as your reference
  * [https://github.com/Phala-Network/awesome-phat-contracts](https://github.com/Phala-Network/awesome-phat-contracts)
  * [https://github.com/Phala-Network/phat-contract-examples](https://github.com/Phala-Network/phat-contract-examples)
* Developer toolings
  * Web console: [https://phat-cb.phala.network](https://phat-cb.phala.network/)
    * Built out a frontend where you can deploy and interact with your contract
  * Project manager
    * Quickly get a blank template and spin up a local cluster for testing with https://github.com/l00k/devphase
* Basic Libraries
  * Storage support: Wrapped Filecoin, Arweave, Storj, and Amazon S3 with an S3-standard API
    * [https://crates.io/crates/pink-s3](https://crates.io/crates/pink-s3)
  * Cross-chain transaction support: ETH and Substrate Tx’s & Queries
    * [https://crates.io/crates/pink-web3](https://crates.io/crates/pink-web3)
    * [https://github.com/Phala-Network/phat-offchain-rollup/tree/sub0-workshop/phat/crates/subrpc](https://github.com/Phala-Network/phat-offchain-rollup/tree/sub0-workshop/phat/crates/subrpc)
* Advanced Library
  * Stateful rollup: reliable cross-chain request processing
    * Allows you to monitor the requests from EVM contracts and Substrate-based chains and reliably send cross-chain transactions as replies
    * [https://github.com/Phala-Network/phat-offchain-rollup/tree/sub0-workshop](https://github.com/Phala-Network/phat-offchain-rollup/tree/sub0-workshop)
