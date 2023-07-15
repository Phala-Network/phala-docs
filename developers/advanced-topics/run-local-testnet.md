# Run Local Testnet

## Overview <a href="#overview" id="overview"></a>

In this tutorial, we’re going to set up a development environment. We are going to deploy a full stack of the core blockchain and connect the Web UI to the blockchain. By the end of the tutorial, you will be able to:

* Send confidential Commands and Queries
* Get a ready-to-hack version of Phala Network for building your confidential DApps

A full Phala Network stack has three components, with an optional Javascript SDK. The core components are available at [Phala-Network/phala-blockchain](https://github.com/Phala-Network/phala-blockchain):

* `phala-node`: The Substrate blockchain node
* `pRuntime`: The TEE runtime. Contracts run in `pRuntime`
* `pherry`: The Substrate-TEE bridge relayer. Connects the blockchain and `pRuntime`

<figure><img src="../../.gitbook/assets/simple_architecture.png" alt=""><figcaption><p>(Phala architecture overview)</p></figcaption></figure>

The Javascript SDK is at [Phala-Network/js-sdk](https://github.com/Phala-Network/js-sdk). The Web UI based on our SDK needs to connect to both the blockchain and the `pRuntime` to send Commands and Queries.

## Setting up <a href="#setting-up" id="setting-up"></a>

In this tutorial, we assume the operating system is _Ubuntu 22.04_. Other Linux distributions should also work, but the instructions or commands may vary. 4 cores and 8GB RAM is the minimal requirement to build the project including the core blockchain.

### Build from source <a href="#build-from-source" id="build-from-source"></a>

The Phala-Network/phala-blockchain repository always contains [the latest build instructions](https://github.com/Phala-Network/phala-blockchain#native-build), at the time of writing (December 26, 2022), we use the following commands to set up development environment:

```
# First clone the repository
git clone https://github.com/Phala-Network/phala-blockchain.git
# Change to the repository directory
cd phala-blockchain
# Install system dependencies:
sudo apt install -y build-essential pkg-config libssl-dev protobuf-compiler
# Install Rust
curl https://sh.rustup.rs -sSf | sh
# Install dependencies for Substrate development
git submodule update --init
sh ./scripts/init.sh
# Installl LLVM 14
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
./llvm.sh 14
```

Then run the following command to build the Phala blockchain:

```
cargo build --release
```

It takes approximately 20 minutes to complete the building process on a laptop equipped with an AMD Ryzen 7 4700U processor with 8 cores, 8 threads, and 32GB of RAM.

### Start the local testnet <a href="#start-the-local-testnet" id="start-the-local-testnet"></a>

We have a dedicate set of scripts to get the blockchain to run, checkout out [this page](https://github.com/Phala-Network/phala-blockchain/tree/master/scripts/run) for full details. For simplicity we can start as simple as follows:

We might want to clean up runtime data to have to clean starting environment, from the root of the `phala-blockchain` project, run this to clean things up:

```
./scripts/run/clear-pruntime.sh
```

Then go ahead and run these 3 commands in 3 separate terminals:

```
./scripts/run/node.sh
./scripts/run/pruntime.sh
./scripts/run/pherry.sh
```

Now you have a full node at [ws://localhost:19944](ws://localhost:19944/), and the pruntime is at [http://localhost:18000](http://localhost:18000/).

After you start the node and the pruntime, you need set up Phat Contract environment once. This can be done with our [phala-blockchain-setup repo](https://github.com/shelvenzhou/phala-blockchain-setup):

```
git clone https://github.com/shelvenzhou/phala-blockchain-setup.git
cd phala-blockchain-setup
yarn

ENDPOINT=ws://localhost:19944 \
WORKERS=http://localhost:18000 \
GKS=http://localhost:18000 \
yarn setup:drivers
```

After all, you testnet is ready. You can continue with the [Connect the polkadot app to the local testnet](broken-reference) section.

### Alternatively, use devPHAse <a href="#alternatively-use-devphase" id="alternatively-use-devphase"></a>

Our community has [an excellent tool](https://github.com/l00k/devphase) to automate the setup process, developed by [100k](https://github.com/l00k), it is like the Phala version of [Hardhat](https://hardhat.org/) or [Truffle](https://trufflesuite.com/).

Run the following commands to create a devPHAse project:

```
# create a new project, or skip it if you already have one
yarn init
# Add devPHAse to the project
yarn add -D devphase
yarn add -D typescript ts-node
# Init project
yarn devphase init
```

Then start the local testnet with:

```
yarn devphase stack run
```

Open a separate terminal, run the following command to setup the local testnet:

```
yarn devphase stack:setup
```

By default you get the Phala blockchain node at ws://localhost:9944 and the pruntime at http://localhost:8000, you can change the configuration at `devphase.config.ts`, for more details check out [the devPHAse repository](https://github.com/l00k/devphase#configuration)

## Connect the Phat UI to the local testnet <a href="#connect-the-phat-ui-to-the-local-testnet" id="connect-the-phat-ui-to-the-local-testnet"></a>

We have a client-side application at [https://phat.phala.network/](https://phat.phala.network/), you can follow the instructions from [Phat Contract Console](<../../.gitbook/assets/awesome phat contracts (2)>) to connect the application to the local testnet.

<figure><img src="../../.gitbook/assets/phat-ui-to-testnet.png" alt=""><figcaption></figcaption></figure>

As the above figure shows, we first click the green dot at the upper-right cornor to set the `RPC Endpoint` to `ws://localhost:19944`, or `ws://localhost:9944` if you start the chain via the devPHAse approach, and change the PRuntime field accordingly.

Don’t forget to claim some `Test-PHA`s, they’re required to deploy Phat Contracts and send transactions.

## Connect the polkadot app to the local testnet <a href="#connect-the-polkadot-app-to-the-local-testnet" id="connect-the-polkadot-app-to-the-local-testnet"></a>

Open up [https://polkadot.js.org/apps](https://polkadot.js.org/apps/#/explorer), click the upper-left corner to call forth the endpoint setup menu:

<figure><img src="../../.gitbook/assets/phat-ui-to-polkadot-app.png" alt=""><figcaption></figcaption></figure>

Set the field `custom endpoint` to `ws://localhost:9944` and then click the `switch` button to connect to it.

Congratulations! Now you have a fully qualified local development environment!
