# Run Local Testnet

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

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

In this tutorial, we assume the operating system is **Ubuntu 22.04**. Other Linux distributions should also work, but the instructions or commands may vary. **4 cores** and **8GB RAM** is the minimal requirement to build the project including the core blockchain.

{% hint style="warning" %}
The Apple M-Series chips do not support the deployment of a local testnet at this time. If you are using a machine with these chips, you will have to deploy to the [Phala PoC6 Testnet](https://phat.phala.network/).
{% endhint %}

## Deployment Options

There are 2 ways to deploy a local testnet.

1. [devPHAse](https://github.com/l00k/devphase) or [Swanky Phala](https://github.com/Phala-Network/swanky-plugin-phala) CLI Tools
2. Build from Source (Most time-consuming)

## Environment Setup

Make sure to go through the environment setup before continuing.

Next, install the following on your system:

* [GCC](https://gcc.gnu.org/)
* [Protobuf](https://github.com/protocolbuffers/protobuf) compiler
* [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config)
* [OpenSSL](https://www.openssl.org/) development package

{% tabs %}
{% tab title="apt" %}
```bash
sudo apt install -y build-essential pkg-config libssl-dev protobuf-compiler
```
{% endtab %}

{% tab title="dnf" %}
```bash
sudo dnf install -y gcc protobuf-compiler pkg-config openssl-devel openssl1.1
```
{% endtab %}
{% endtabs %}

## Deploy via devPHAse

In this section, you will deploy your local testnet using the DevPHAse CLI Tool. First, you will need to create a new workspace folder on your system and execute the following:

{% hint style="warning" %}
When using `npm`, you will see conflicting/duplicated packages. `yarn` will not have these errors. Until this problem is solved, it is best to use `yarn`.
{% endhint %}

{% hint style="danger" %}
Currently, `npm` and `npx` commands do not work and will report an error `invalid format for V0 (detected) contract metadata`. Opt to use `yarn` until the problem is resolved.
{% endhint %}

### 1) Install devPHAse and required libs

{% tabs %}
{% tab title="yarn" %}
```bash
yarn init
yarn add -D typescript ts-node
yarn add -D @devphase/cli
yarn add -D @devphase/service
```
{% endtab %}

{% tab title="npm" %}
```bash
npm init
npm install -D typescript ts-node
npm install -D @devphase/cli
npm install -D @devphase/service
```
{% endtab %}
{% endtabs %}

### 2) Init project

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase init
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase init
```
{% endtab %}
{% endtabs %}

Your directory will be initiated with all required files and template Flipper contract.

```
- .devphase/        # devPHAse cache directory
- contracts/        # here you store your contracts
    - flipper/          # template Flipper contract
        - Cargo.toml        # rust project file
        - lib.rs            # contract source
- scripts/          # scripts which you can all with devPHAse environment
    - deploy.ts         # sample deployment script
    - get-logs.ts       # sample demonstrating how to get contract logs
- tests/            # here you store e2e tests for contracts
    - flipper/          # flipper related test suite
        - flipper.test.ts   # flipper tests example
```

### 3) Prepare environment

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase check
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase check
```
{% endtab %}
{% endtabs %}

This command will ensure the proper stack (node, pruntime, pherry) is ready to run. Download stack from official repository. Verify dependencies.

#### Output:

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase check
[StackBinaryDownloader] Creating stack directory
  ✔ Checking configuration file
  ✔ Check dependencies
  ✔ Checking Phala stack binaries
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase check
[StackBinaryDownloader] Creating stack directory
  ✔ Checking configuration file
  ✔ Check dependencies
  ✔ Checking Phala stack binaries
```
{% endtab %}
{% endtabs %}

You will see a new directory called `stacks/` has been created

```
- stacks/                 # here all prepared stacks will be stored
  - nightly-2024-03-07/     # bases on your configuration it will latest available stack or any specific you choose
      - phala-node            # node binary
      - pherry                # pherry binary
      - pruntime              # pruntime binary
      - *.so.*                # multiple requried libs
      - *.contract            # system contracts
```

Now you are ready to go.

### 4) Compile contract

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase contract compile -c flipper
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase contract compile -c flipper
```
{% endtab %}
{% endtabs %}

#### Output:

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase contract compile -c flipper
[MultiContractExecutor] Criteria: flipper
[MultiContractExecutor] Matched contracts:
[MultiContractExecutor] flipper
[MultiContractExecutor]
  ❯ flipper
  ✔ flipper
Done in 32.49s.
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase contract compile -c flipper
[MultiContractExecutor] Criteria: flipper
[MultiContractExecutor] Matched contracts:
[MultiContractExecutor] flipper
[MultiContractExecutor]
  ❯ flipper
  ✔ flipper
```
{% endtab %}
{% endtabs %}

This command will:

* install contract dependencies
* compile contract (only flipper in this case) and save output to ./contracts/flipper/target
* copy contract artificats
* generate typescript bindings which you can use in scripts and tests

New files:

```
- artifacts/            # here devPHAse will store compiled contract artifacts
  - flipper/              # specific contract
    - flipper.contract
    - flipper.json
    - flipper.wasm
- typings/              # here devPHAse will store ts bindings
  - Flipper.ts
```

### 5) Run tests

{% hint style="danger" %}
Currently, `npm` and `npx` commands do not work and will report an error `invalid format for V0 (detected) contract metadata`. Opt to use `yarn` until the problem is resolved.
{% endhint %}

{% tabs %}
{% tab title="yarn w/o logger" %}
```bash
yarn devphase contract test -t flipper
```
{% endtab %}

{% tab title="yarn w/ logger" %}
```bash
yarn devphase contract test -t flipper -m 3
```
{% endtab %}

{% tab title="npx w/o logger " %}
```bash
npx devphase contract test -t flipper
```
{% endtab %}

{% tab title="npx w/ logger" %}
```basic
yarn devphase contract test -t flipper -m 3
```
{% endtab %}
{% endtabs %}

devPHAse in default config will:

* check stack dependencies
* start local stack
* configure local environment (with minimal required deps)
* execute tests
* save logs into files

#### Output:

{% tabs %}
{% tab title="yarn w/o logger" %}
```bash
yarn devphase contract test -t flipper
[StackBinaryDownloader] Preparing Phala stack release nightly-2024-03-13
  ✔ Checking releases directory
  ✔ Checking target release binaries
 
 
[Test] Global setup start
[Test] Preparing dev stack
[StackManager] Starting stack nightly-2024-03-13
  ✔ Start node component
  ✔ Start pRuntime component
  ✔ Start pherry component
[Test] Init API
[Test] Setup environment
[StackSetupService] Starting stack setup with default version
  ✔ Fetch worker info
  ✔ Load system contracts
  ↓ Register worker [skipped]
  ✔ Register gatekeeper
  ✔ Upload Pink system code
  ✔ Verify cluster
  ✔ Create cluster
  ✔ Wait for cluster to be ready
  ✔ Add worker endpoint
  ✔ Create system contract API
[Test] Global setup done
[Test] Starting tests
  Flipper
    default constructor
      ✔ Should be created with proper intial value
      ✔ Should be able to flip value (2572ms)
    new constructor
      ✔ Should be created with proper intial value
 
[Test] Global teardown start
[Test] Internal clean up
[Test] Stopping stack
[Test] Global teardown done
 
  3 passing (27s)
 
[StackManager] pherry exited
[StackManager] pruntime exited
[StackManager] node exited
Done in 33.00s.
```
{% endtab %}

{% tab title="yarn w/ logger" %}
```bash
yarn devphase contract test -t flipper -m 3
[StackBinaryDownloader] Preparing Phala stack release nightly-2024-03-13
  ✔ Checking releases directory
  ✔ Checking target release binaries
 
 
[Test] Global setup start
[Test] Preparing dev stack
[StackManager] Starting stack nightly-2024-03-13
  ✔ Start node component
  ✔ Start pRuntime component
  ✔ Start pherry component
[Test] Init API
[Test] Setup environment
[StackSetupService] Starting stack setup with default version
  ✔ Fetch worker info
  ✔ Load system contracts
  ↓ Register worker [skipped]
  ✔ Register gatekeeper
  ✔ Upload Pink system code
  ✔ Verify cluster
  ✔ Create cluster
  ✔ Wait for cluster to be ready
  ✔ Add worker endpoint
  ✔ Create system contract API
  ✔ Deploy tokenomic driver
  ✔ Deploy SideVM driver
  ✔ Calculate logger server contract ID
  ✔ Prepare chain for logger server
  ✔ Deploy logger server
[Test] Global setup done
[Test] Starting tests
  Flipper
    default constructor
      ✔ Should be created with proper intial value
Logs from pink server:
#366	TX	info		Resource uploaded to cluster, by 8eaf04151687736326c9fea17e25fc5287613693c912909cb226aa4794f26a48 (5FHneW46...), type=InkCode, hash=0xcbf8151426f6ce308a875a1c5cc6e2a4f4c0bca3be4371a15b0d25bcca336f55
#376	EST	info		instantiated
#392	TX	info		instantiated
      ✔ Should be able to flip value (2636ms)
Logs from pink server:
#402	EST	info		instantiated
#422	TX	info		instantiated
    new constructor
      ✔ Should be created with proper intial value
Logs from pink server:
#456	EST	info		instantiated
#473	TX	info		instantiated
 
[Test] Global teardown start
[Test] Internal clean up
[Test] Stopping stack
[Test] Global teardown done
 
  3 passing (54s)
 
[StackManager] pherry exited
[StackManager] pruntime exited
[StackManager] node exited
Done in 59.67s.
```
{% endtab %}
{% endtabs %}

New directories created for logs.

```
- logs/             # here devPHAse will store execution logs
  - 2024-03-07T16:09:43.421Z/     # single execution
    - node.log
    - pherry.log
    - pruntime.log
    - pink_logger.log               # if stack setup with logger here all logs will be stored
```

Running tests this way is nice but only if it is single execution. If you are developing new feature it may be required to continuously test it. In this case default procedure is time-consuming, because setting up stack takes \~40s.

Nothing blocks you from using the same running node for multiple tests.

### 6) Long-running local environment

This command will start and keep running all stack components. However, network is not configured yet to accept contracts.

{% hint style="danger" %}
Currently, `npm` and `npx` commands do not work and will report an error `invalid format for V0 (detected) contract metadata`. Opt to use `yarn` until the problem is resolved.
{% endhint %}

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase stack run --save-logs
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase stack run --save-logs
```
{% endtab %}
{% endtabs %}

### 7) Configure network

Now let's configure the network to enable your local environment to deploy a Phat Contract and collect logs.

{% hint style="danger" %}
Currently, `npm` and `npx` commands do not work and will report an error `invalid format for V0 (detected) contract metadata`. Opt to use `yarn` until the problem is resolved.
{% endhint %}

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase stack setup -m 3
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase stack setup -m 3
```
{% endtab %}
{% endtabs %}

#### Output:

```bash
yarn devphase stack setup -m 3
[StackSetupService] Starting stack setup with default version
  ✔ Fetch worker info
  ✔ Load system contracts
  ↓ Register worker [skipped]
  ✔ Register gatekeeper
  ✔ Upload Pink system code
  ✔ Verify cluster
  ✔ Create cluster
  ✔ Wait for cluster to be ready
  ✔ Add worker endpoint
  ✔ Create system contract API
  ✔ Deploy tokenomic driver
  ✔ Deploy SideVM driver
  ✔ Calculate logger server contract ID
  ✔ Prepare chain for logger server
  ✔ Deploy logger server
[StackSetup] Stack is ready
[StackSetup] Cluster Id
[StackSetup] 0x0000000000000000000000000000000000000000000000000000000000000001
Done in 38.52s.
```

Now all required network components should be ready for Phat Contract deployment.

### 8) Run tests using long-running local environment

`-e` flag will make devPHAse to execute test without setting up temporary stack but using existing one.

{% hint style="danger" %}
Currently, `npm` and `npx` commands do not work and will report an error `invalid format for V0 (detected) contract metadata`. Opt to use `yarn` until the problem is resolved.
{% endhint %}

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase contract test -t flipper -e
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase contract test -t flipper -e
```
{% endtab %}
{% endtabs %}

#### Output:

```bash
yarn devphase contract test -t flipper -e
[Test] Global setup start
[Test] Init API
[Test] Setup environment
[StackSetupService] Starting stack setup with default version
  ✔ Fetch worker info
  ✔ Load system contracts
  ↓ Register worker [skipped]
  ↓ Register gatekeeper [skipped]
  ↓ Upload Pink system code [skipped]
  ✔ Verify cluster
  ↓ Create cluster [skipped]
  ✔ Wait for cluster to be ready
  ↓ Add worker endpoint [skipped]
  ✔ Create system contract API
[Test] Global setup done
[Test] Starting tests
  Flipper
    default constructor
      ✔ Should be created with proper intial value
Logs from pink server:
#996	TX	info		Resource uploaded to cluster, by 8eaf04151687736326c9fea17e25fc5287613693c912909cb226aa4794f26a48 (5FHneW46...), type=InkCode, hash=0xcbf8151426f6ce308a875a1c5cc6e2a4f4c0bca3be4371a15b0d25bcca336f55
#999	EST	info		instantiated
#1007	TX	info		instantiated
      ✔ Should be able to flip value (2390ms)
Logs from pink server:
#1009	EST	info		instantiated
#1021	TX	info		instantiated
    new constructor
      ✔ Should be created with proper intial value
Logs from pink server:
#1036	EST	info		instantiated
#1044	TX	info		instantiated
 
[Test] Global teardown start
[Test] Internal clean up
[Test] Global teardown done
 
  3 passing (18s)
 
Done in 24.33s.
```

### 9) Running Scripts

DevPHAse will run script on specified environment. If environment provides a PinkLogger - logs will be saved locally.

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase script scripts/deploy.ts
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase script scripts/deploy.ts
```
{% endtab %}
{% endtabs %}

#### Output:

```bash
yarn devphase script scripts/deploy.ts
[Script] Executing /home/hashwarlock/Templates/YarnTest/scripts/deploy.ts
Contract ID: 0x8e132d6bdebe37824b31df98669063d52d25d7eb0c40358c7f0e47876bc8a879
{ Ok: false }
{
  Finalized: '0xda06fe993f51260a4bd726d721ae34ec7d1b939cb9a425a0dd4fd9c24831d023'
}
{ Ok: true }
Done in 9.62s.
```

**Get logs locally**

Using the contract ID from the previous script `0x8e132d6bdebe37824b31df98669063d52d25d7eb0c40358c7f0e47876bc8a879` modify contractIds variable in `scripts/get-logs.ts` then execute the script to get logs.

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase script scripts/get-logs.ts
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase script scripts/get-logs.ts
```
{% endtab %}
{% endtabs %}

#### Output:

```bash
yarn devphase script scripts/get-logs.ts
[Script] Executing /home/hashwarlock/Templates/YarnTest/scripts/get-logs.ts
0x8e132d6bdebe37824b31df98669063d52d25d7eb0c40358c7f0e47876bc8a879
[
  {
    sequence: 50,
    type: 'Log',
    blockNumber: 1714,
    contract: '0x8e132d6bdebe37824b31df98669063d52d25d7eb0c40358c7f0e47876bc8a879',
    entry: '0x8e132d6bdebe37824b31df98669063d52d25d7eb0c40358c7f0e47876bc8a879',
    execMode: 'transaction',
    timestamp: 2024-03-14T05:40:24.365Z,
    level: 3,
    message: 'instantiated'
  },
  {
    sequence: 55,
    type: 'MessageOutput',
    blockNumber: 1723,
    origin: '0xd43593c715fdd31c61141abd04a99fd6822c8558854ccde39a5684e7a56da27d',
    contract: '0x8e132d6bdebe37824b31df98669063d52d25d7eb0c40358c7f0e47876bc8a879',
    nonce: '0xacac9d33a106f1051887b243f82755276d8443c070fb4c9987018674cbbe478b',
    output: {
      gasConsumed: { refTime: 440059308, proofSize: 67027 },
      gasRequired: { refTime: 65728937984, proofSize: 10485760 },
      storageDeposit: { charge: 0 },
      debugMessage: '',
      result: { ok: { flags: [], data: '0x00' } }
    }
  }
]
```

### 10) Run devPHAse on PoC6 Testnet or Phala Mainnet

You can specify to run commands on any network - including PoC6 Testnet or Phala Mainnet. Check commands help for further details.

#### Deploy contract command

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase help contract deploy
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase help contract deploy
```
{% endtab %}
{% endtabs %}

#### Output:

```bash
Deploy contract
 
USAGE
  $ devphase contract deploy [ARGS] -c <value> -o <value> [-t InkCode|SidevmCode|IndeterministicInkCode] [-n
    <value>] [-l <value>] [-a <value>]
 
ARGUMENTS
  ARGS  Constructor arguments
 
FLAGS
  -a, --account=<value>   [default: alice] Account used to deploy (managed account key)
  -c, --contract=<value>  (required) Contract name
  -l, --cluster=<value>   Target cluster Id
  -n, --network=<value>   [default: local] Target network to deploy (local default)
  -o, --ctor=<value>      (required) Contract constructor to call (name)
  -t, --type=<option>     [default: InkCode]
                          <options: InkCode|SidevmCode|IndeterministicInkCode>
 
Done in 0.99s.
```

#### Call contract command

{% tabs %}
{% tab title="yarn" %}
```bash
yarn devphase help contract call
```
{% endtab %}

{% tab title="npx" %}
```bash
npx devphase help contract call
```
{% endtab %}
{% endtabs %}

#### Output:

```bash
Call contract
 
USAGE
  $ devphase contract call [ARGS] -c <value> -i <value> -m <value> [-t InkCode|SidevmCode|IndeterministicInkCode]
    [-a query|tx] [-n <value>] [-l <value>] [-a <value>]
 
ARGUMENTS
  ARGS  Call arguments
 
FLAGS
  -a, --accessor=<option>  [default: query] Method type: transaction or query
                           <options: query|tx>
  -a, --account=<value>    [default: alice] Account used to call (managed account key)
  -c, --contract=<value>   (required) Contract name
  -i, --id=<value>         (required) Contract ID
  -l, --cluster=<value>    Target cluster Id
  -m, --method=<value>     (required) Contract method to call (name)
  -n, --network=<value>    [default: local] Target network to deploy (local default)
  -t, --type=<option>      [default: InkCode]
                           <options: InkCode|SidevmCode|IndeterministicInkCode>
 
Done in 1.00s
```

## Build from source <a href="#build-from-source" id="build-from-source"></a>

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

After all, you testnet is ready. You can continue with the [Connect the polkadot app to the local testnet](../../developers/advanced-topics/broken-reference/) section.

## Connect the Phat UI to the local testnet <a href="#connect-the-phat-ui-to-the-local-testnet" id="connect-the-phat-ui-to-the-local-testnet"></a>

We have a client-side application at [https://phat.phala.network/](https://phat.phala.network/), you can follow the instructions from [Phat Contract Console](../../.gitbook/assets/awesome%20phat%20contracts%20\(2\)/) to connect the application to the local testnet.

<figure><img src="../../.gitbook/assets/phat-ui-to-testnet.png" alt=""><figcaption></figcaption></figure>

As the above figure shows, we first click the green dot at the upper-right cornor to set the `RPC Endpoint` to `ws://localhost:19944`, or `ws://localhost:9944` if you start the chain via the devPHAse approach, and change the PRuntime field accordingly.

Don’t forget to claim some `Test-PHA`s, they’re required to deploy Phat Contracts and send transactions.

## Connect the polkadot app to the local testnet <a href="#connect-the-polkadot-app-to-the-local-testnet" id="connect-the-polkadot-app-to-the-local-testnet"></a>

Open up [https://polkadot.js.org/apps](https://polkadot.js.org/apps/#/explorer), click the upper-left corner to call forth the endpoint setup menu:

<figure><img src="../../.gitbook/assets/phat-ui-to-polkadot-app.png" alt=""><figcaption></figcaption></figure>

Set the field `custom endpoint` to `ws://localhost:9944` and then click the `switch` button to connect to it.

Congratulations! Now you have a fully qualified local development environment!
