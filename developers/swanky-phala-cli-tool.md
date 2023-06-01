# Swanky Phala CLI Tool

> **Note:** Feedback and contributions are welcome. Please add issues for any features or bugs found. Join our [discord](https://discord.gg/phala) and jump in our `#dev` channel to speak with our devs.

## Swanky Suite

[Swanky Suite](https://docs.astar.network/docs/wasm/sc-dev/swanky/) aims to be an "all-in-one" tool for Wasm smart contract developers. It is modeled on existing tools like `cargo contract CLI` and `polkadot.js`. The `swanky-cli` tool is built with the `oclif` (Open CLI Framework [repo](https://oclif.io/docs/introduction)).

Building with `oclif` allows for the `swanky-cli` to be extended through the [plugin-plugin](https://github.com/oclif/plugin-plugins) feature. Now the `swanky-phala-plugin` plugin can be added to the `swanky-cli` (note: must install `swanky-cli`first) with the command `swanky plugins:link [PATH_TO_REPO]`. Specific installation instructions and examples will be displayed later, so do not worry about getting this set up now.

## DevPHAse

[DevPHAse](https://github.com/l00k/devphase) is a developer tool built and maintained by Phala community member 100k. DevPhase is a command line utility that enables a developer building Phat Contracts to:

* Install binaries for phala-node, pherry and pruntime.
* Install local testnet configuration files to allow for Phat Contracts to be deployed into a cluster with a systems contract to enable SideVM for logging.
* Create testnet accounts.
* Start the local testnet.
* Configure the local testnet by:
  * Registering Workers and their endpoints
  * Register Gatekeeper
  * Upload systems contract code
  * Deploy a Cluster with the `su` account (Default: Alice)
  * Deploy driver contract code
    * Phat Contract Tokenomics
    * SideVm Deployer
  * Authorize Logger SideVM Contract
  * Upload SideVM Logger to cluster and Deploy SideVM Logger
* Compile Phat contracts into a `.wasm`, `metadata.json` and `.contract` file(combines the `.wasm` and `metadata.json` file into one `.contract` file).
* Upload and Instantiate a compiled Phat Contract to a cluster on the local testnet.
* Call (queries and transactions) instantiated Phat Contracts directly.
* Check local dev environment setup.

## Getting Started

### Installation

> _Currently `swanky phala` will only support Ubuntu Linux. Other Linux operating systems are support, but this requires downloading and compiling `phala-node`, `pherry` and `pruntime` binaries locally. Then copy the binaries to the `stacks/` folder._

#### Install Swanky CLI

Follow the instructions from Astar Network wiki [here](https://docs.astar.network/docs/wasm/sc-dev/swanky#installing).

#### Install Swanky Phala Plugin

**npm**

```bash
npm install -g @phala/swanky-phala-plugin
```

or

```bash
npx @phala/swanky-phala-plugin
```

**locally**

Clone the `swanky-phala-plugin` GitHub repository.

```bash
git clone git@github.com:Phala-Network/swanky-plugin-phala.git
cd swanky-plugin-phala
yarn install
yarn build
```

#### Add `swanky-phala-plugin` to `swanky` CLI

Use `plugins:install` for **npm**

```bash
swanky plugins:install @phala/swanky-phala-plugin
```

or **GitHub URL**

```bash
swanky plugins:install https://github.com/Phala-Network/swanky-plugin-phala.git
```

If installed and built **locally** then use `plugins:link` to link `swanky` to the local path to `swanky-phala-plugin`

```bash
swanky plugins:link [PATH_TO_REPO]
```

example:

```bash
swanky plugins:link ~/Projects/swanky-phala-plugin

@astar-network/swanky-cli: linking plugin @phala/swanky-plugin-phala... done
```

#### Commands

Now there should be a `swanky phala` CLI available. Execute the `swanky phala --help` command to check available commands.

```bash
swanky phala --help
Swanky plugin to setup Phala developer environment for Phat Contracts.

USAGE
  $ swanky phala COMMAND

TOPICS
  phala account   Create or list accounts.
  phala contract  Create, compile, deploy, test or call Phat Contracts.
  phala node      Download binaries to start local testnet and configure for Phat Contract development.

COMMANDS
  phala check  Not Available
  phala init   Generate a new Phat Contract environment
```

#### Initialize a Project

Easily get started with a new Phat Contract project by executing `swanky phala init [PROJECT_NAME]`

```bash
swanky phala init test-swanky-phala
```

This will initiate a round of questions to get your Phat Contract template configured. First question will ask:

```bash
? Which contract language should we use? (Use arrow keys)
❯ pink
```

At this moment, `pink` is the only contract language option at this time. `pink` is the Phala `ink` library to support rust-based [ink! language](https://paritytech.github.io/ink/) in Phala’s `pRuntime` workers.

Next you’ll be asked the what contract template to use (`blank`, `http_client`, or `phat_hello` more to come!).

```bash
? Which contract template should we use? (Use arrow keys)
  blank 
❯ http_client 
  phat_hello
```

Now that you have a Phat Contract language and template picked, you will be asked to create a name for the PC. (_**default is the template name**_)

```bash
? What should we name your contract? (http_client)
```

After you select a name, you’ll be asked for your `git` username (default is `git config --get user.name`) and email.

```bash
? What is your name? (HashWarlock)
? What is your email?
```

An expected final output will display when the template files and project directory is created.

```bash
? Which contract language should we use? pink
? Which contract template should we use? phat_hello
? What should we name your contract? phat_hello
? What is your name? hashwarlock
? What is your email? 
✔ Checking dependencies OK
Initializing
✔ Copying template files OK
✔ Processing templates OK
✔ Initializing git OK
✔ Installing dependencies OK
⠋ Copying devphase config files[Initializer] Creating directories
[Initializer] Creating files
[Initializer] devphase.config.ts
[Initializer] accounts.json
[Initializer] scripts
[Initializer] Creating sample contract
[ContractManager] Contract created in:
[ContractManager] /home/hashwarlock/Projects/Phala/Swanky/demo/swanky-plugin-phala/test-swanky-phala/contracts/flipper
✔ Copying devphase config files OK
⠋ Installing phala node, pruntime and pherry binaries[StackBinaryDownloader] Preparing Phala stack release
[StackBinaryDownloader] Creating stack directory
  ✔ Checking releases directory
  ✔ Checking target release binaries
✔ Installing phala node, pruntime and pherry binaries OK
😎 Phat Contract project successfully initialised! 😎
```

Execute `ls` to list the new project directory called `test-swanky-phala` in the current working directory.

```bash
ls
total 0
drwxr-xr-x   3 hashwarlock  staff    96B Jan 19 20:45 .
drwxr-xr-x   5 hashwarlock  staff   160B Jan 19 18:37 ..
drwxr-xr-x  15 hashwarlock  staff   480B Jan 19 20:46 test-swanky-phala
```

`cd` into `test-swanky-phala` and execute `ls`.

```bash
cd test-swanky-phala
└─[$]> ls
total 152
drwxr-xr-x. 1 hashwarlock hashwarlock    254 Apr  4 16:27 .
drwxr-xr-x. 1 hashwarlock hashwarlock    468 Apr  4 16:27 ..
-rw-r--r--. 1 hashwarlock hashwarlock    143 Apr  4 16:27 accounts.json
drwxr-xr-x. 1 hashwarlock hashwarlock     34 Apr  4 16:27 contracts
drwxr-xr-x. 1 hashwarlock hashwarlock     26 Apr  4 16:27 .devphase
-rw-r--r--. 1 hashwarlock hashwarlock   4582 Apr  4 16:27 devphase.config.json
drwxr-xr-x. 1 hashwarlock hashwarlock     98 Apr  4 16:26 .git
-rw-r--r--. 1 hashwarlock hashwarlock   3595 Apr  4 16:26 .gitignore
drwxr-xr-x. 1 hashwarlock hashwarlock   6116 Apr  4 16:27 node_modules
-rw-r--r--. 1 hashwarlock hashwarlock    255 Apr  4 16:26 package.json
drwxr-xr-x. 1 hashwarlock hashwarlock     18 Apr  4 16:27 scripts
drwxr-xr-x. 1 hashwarlock hashwarlock     36 Apr  4 16:27 stacks
drwxr-xr-x. 1 hashwarlock hashwarlock     20 Apr  4 16:26 tests
-rw-r--r--. 1 hashwarlock hashwarlock    520 Apr  4 16:26 tsconfig.json
-rw-r--r--. 1 hashwarlock hashwarlock 130190 Apr  4 16:27 yarn.lock
```

Here is an example of how the directory structure looks like:

```bash
└─[$]> cd stacks
└─[$]> cd nightly-2023-04-04 
└─[$]> ls
total 116256
drwxr-xr-x. 1 hashwarlock hashwarlock      272 Apr  4 16:27 .
drwxr-xr-x. 1 hashwarlock hashwarlock       36 Apr  4 16:27 ..
-rw-r--r--. 1 hashwarlock hashwarlock  6411768 Apr  4 16:27 libpink.so.1.0
-rw-r--r--. 1 hashwarlock hashwarlock    59475 Apr  4 16:27 log_server.contract
-rw-r--r--. 1 hashwarlock hashwarlock  2278251 Apr  4 16:27 log_server.sidevm.wasm
-rwxr-xr-x. 1 hashwarlock hashwarlock 68365760 Apr  4 16:27 phala-node
-rwxr-xr-x. 1 hashwarlock hashwarlock 14814056 Apr  4 16:27 pherry
-rwxr-xr-x. 1 hashwarlock hashwarlock 26937712 Apr  4 16:27 pruntime
-rw-r--r--. 1 hashwarlock hashwarlock    41568 Apr  4 16:27 sidevm_deployer.contract
-rw-r--r--. 1 hashwarlock hashwarlock    79326 Apr  4 16:27 system.contract
-rw-r--r--. 1 hashwarlock hashwarlock    39543 Apr  4 16:27 tokenomic.contract
```

#### Start a Phala Local Testnet

`swanky phala node start` will check if the following exists in the current directory or up:

* `devphase.config.json`
* `stack/`
  * `phala-node`
  * `pruntime`
  * `pherry`

Once verified file are downloaded and there is not an instance running currently, the local testnet will start.

```bash
swanky phala node start
Starting local tesnet stack
[StackBinaryDownloader] Preparing Phala stack release
  ✔ Checking releases directory
  ✔ Checking target release binaries
[StackManager] Starting stack
  ✔ Start node component
  ✔ Start pRuntime component
  ✔ Start pherry component
```

#### Configure the Running Local Testnet for Phat Contract Deployment

A Phala local testnet needs the following for Phat Contracts to be deployed and instantiated to a cluster:

* Register the Workers and setup their endpoints;
* Register the Gatekeepers;
* Create Cluster 0x0 with`Alice`as the owner and the System contract above;
* Register two Drivers to the System contract
  * the log server printing all the Phat contracts' log;
  * the SideVM deployer controlling which contracts can start the SideVM;

This is accomplished by executing `swanky phala node setup`.

```bash
swanky phala node setup
Setting up Phala local testnet stack
⠋ Setting up local testnet stack[StackSetupService] Starting stack setup with default version
  ✔ Fetch worker info
  ✔ Load system contracts
  ↓ Register worker [skipped]
  ↓ Register gatekeeper [skipped]
  ↓ Upload Pink system code [skipped]
  ✔ Verify cluster
  ↓ Create cluster [skipped]
  ✔ Wait for cluster to be ready
  ✔ Create system contract API
  ✔ Deploy tokenomic driver
  ✔ Deploy SideVM driver
  ✔ Calculate logger server contract ID
  ✔ Prepare chain for logger server
  ✔ Deploy logger server
Stack is ready
Cluster Id
0x0000000000000000000000000000000000000000000000000000000000000000
✔ Setting up local testnet stack OK
✔ Cleanup OK
😎 Phala local testnet configured successfully! 😎
```

#### Compile Your Contract

We have accomplished the following:

* Created a project directory with a configured template Phat Contract.
* Downloaded Phala binaries, drivers, system contracts and sideVM programs.
* Started and set up a local testnet to start deploying Phat Contracts to a worker node in the deployed `0x0` cluster.

Let’s begin the process of deploying the Phat Contract, but first the PC must be compiled to get the `contract.wasm`, `metadata.json` and `contract.contract` files that will be used to upload and instantiate the PC to the local testnet cluster.

> **Note:** Follow these [installation steps](https://wiki.phala.network/en-us/build/stateless/setup/) before continuing to ensure you can compile your Phat Contract.

We can compile the PC with `swanky phala contract compile -c [CONTRACT_NAME]` and will look like the follow:

```bash
swanky phala contract compile -c phat_hello
Compile contract(s)
⠋ Compiling Phat Contract phat_hello[MultiContractExecutor] Criteria: phat_hello
[MultiContractExecutor] Matched contracts:
[MultiContractExecutor] phat_hello
[MultiContractExecutor] 
  ❯ phat_hello
  ✔ phat_hello
✔ Compiling Phat Contract phat_hello OK
😎 Phat Contract compiled successfully! 😎
```

#### Generate Types for Contract

If you have compiled your contract already, the types will be auto-generated at the end of a successful compilation. In the case that the types were not generated for the contract, execute the `swanky phala contract typegen [CONTRACT_NAME]`.

An example of the output will create `typings/` folder with a TypeScript file of the contract's generated types.

```bash
└─[$]> swanky phala contract typegen phat_hello
Create type bindings for contracts
⠋ Creating type bindings for Phat Contract phat_hello[TypeBinder] Generating type bindings for: phat_hello
✔ Creating type bindings for Phat Contract phat_hello OK
😎 Phat Contract types generated successfully! 😎
```

#### Validate Your Compiled WASM Contract

Sometimes there are difficult to find errors that lie within a succesfully compiled wasm blob. The command `swanky phala contract validate -c [CONTRACT_NAME]` will do a preliminary check to verify if the compiled contract is valid for deployment.

```
└─[$]> swanky phala contract validate -c phat_hello
Validating compiled WASM of phat_hello contract...
[ERROR] Invalid contract: validation of new code failed: sign extension operations support is not enabled (at offset 0x1a36b)
└─[$]> swanky phala contract validate -c flipper
Validating compiled WASM of flipper contract...
flipper.wasm validated successfully!
😎 Phat Contract validated successfully! 😎
```

#### Deploy and Instantiate Contract

```bash
USAGE
  $ phala phala contract deploy [CONTRACTNAME] [CONTRACTCONSTRUCTOR] [CTORARGS] [-t <value>] [-n <value>] [-l <value>] [-a
    <value>]

ARGUMENTS
  CONTRACTNAME         Contract name
  CONTRACTCONSTRUCTOR  Contract constructor
  CTORARGS             Contract constructor arguments

FLAGS
  -a, --account=<value>       [default: alice] Account used to deploy (alice default)
  -l, --clusterId=<value>     [default: 0x0000000000000000000000000000000000000000000000000000000000000000] Target
                              cluster id
  -n, --network=<value>       [default: local] Target network to deploy (local default)
  -t, --contractType=<value>  [default: InkCode] Contract type (InkCode default)

DESCRIPTION
  Deploy contract

EXAMPLES
  $ phala phala contract deploy [CONTRACT_NAME] [CONSTRUCTOR] -t [CONTRACT_TYPE] -n [NETWORK] -l [CLUSTER_ID] -a [ACCOUNT] [ctorArgs...]
```

Let's deploy the `phat_hello` contract to the local testnet in cluster `0x0000000000000000000000000000000000000000000000000000000000000000`. Note if there is no account defined then `alice` will deploy the Phat Contract by default.

```bash
└─[$]> swanky phala contract deploy -c phat_hello -o new -l 0x0000000000000000000000000000000000000000000000000000000000000000
Deploy contract
⠧ Deploying contract phat_helloContract deployed
Contract Id: 0x2e11166f9a623f7536434b5f4456b2311d3bb06717dd91a376380a61b8f9b0a8
Cluster Id:  0x0000000000000000000000000000000000000000000000000000000000000000
✔ Deploying contract phat_hello OK
😎 Phat Contract deployed successfully! 😎
```

#### Interact with Deployed Contract

```bash
└─[$]> swanky phala contract call --help
Call a Phat Contract

USAGE
  $ phala phala contract call -c <value> -i <value> -m <value> [-t InkCode|SidevmCode] [-r query|tx] [-n <value>] [-l
    <value>] [-a <value>] [-p <value>]

FLAGS
  -a, --account=<value>    [default: alice] Account used to call (managed account key)
  -c, --contract=<value>   (required) Contract name
  -i, --id=<value>         (required) Contract ID
  -l, --cluster=<value>    Target cluster Id
  -m, --method=<value>     (required) Contract method to call (name)
  -n, --network=<value>    [default: local] Target network to deploy (local default)
  -p, --params=<value>...  [default: ] Arguments supplied to the message
  -r, --request=<option>   [default: query] Request type: transaction or query
                           <options: query|tx>
  -t, --type=<option>      [default: InkCode]
                           <options: InkCode|SidevmCode>

DESCRIPTION
  Call a Phat Contract

EXAMPLES
  $ phala phala contract call -c [CONTRACT_NAME] -t [CONTRACT_TYPE] -i [CONTRACT_ID] -r [REQUEST_TYPE] -m [METHOD] -t [NETWORK] -l [CLUSTER_ID] -a [ACCOUNT] -p [..ARGS]

```

Now we can interact with our deployed contract by taking the `Contract Id: 0x2e11166f9a623f7536434b5f4456b2311d3bb06717dd91a376380a61b8f9b0a8` returned from deploying `phat_hello` successfully. There is a function called `get_eth_balance` that takes a hex string of the account address. This is how the composed call would look like.

> **Note:** ETH address has to be converted to the Hex representation `0x307844306645333136423966303141336235666436373930463838433244353337333946383042343634` of the account opposed to using the Account ID `0xD0fE316B9f01A3b5fd6790F88C2D53739F80B464`. This can be retrieved through the `@polkadot/util` method `stringToHex(0xD0fE316B9f01A3b5fd6790F88C2D53739F80B464)`. Check the phat\_hello.test.ts for the example.

```bash
└─[$]> swanky phala contract call -c phat_hello -l 0x0000000000000000000000000000000000000000000000000000000000000000 -i 0x2e11166f9a623f7536434b5f4456b2311d3bb06717dd91a376380a61b8f9b0a8 -m getEthBalance -p 0x307844306645333136423966303141336235666436373930463838433244353337333946383042343634
Executing call to Phat Contract
Call result:
{
  output: { ok: { ok: '20950198739626844' } },
  debugMessage: '',
  result: {
    ok: { flags: [], data: '0x0000443230393530313938373339363236383434' }
  },
  gasConsumed: { refTime: 1342177279, proofSize: 0 },
  gasRequired: { refTime: 65766686719, proofSize: 0 },
  storageDeposit: { charge: 2047 }
}
```

#### Create a New Contract

To add a new contract there is the `swanky phala contract new [CONTRACT_NAME]` command. This can be done at the root of your new project folder and would look like the following.

```bash
└─[$]> swanky phala contract new new_contract
Creating new Phat Contract
? Which contract language should we use? pink
? Which contract template should we use? flipper
? What should we name your contract? new_contract
? What is your name? hashwarlock
? What is your email? 
✔ Checking dependencies OK
Initializing
✔ Copying template files OK
✔ Processing templates OK
😎 Successfully created new Phat Contract! 😎
└─[$]> ls contracts
total 0
drwxr-xr-x. 1 hashwarlock hashwarlock  58 Apr  4 17:16 .
drwxr-xr-x. 1 hashwarlock hashwarlock 362 Apr  4 17:16 ..
drwxr-xr-x. 1 hashwarlock hashwarlock  26 Apr  4 17:16 new_contract
drwxr-xr-x. 1 hashwarlock hashwarlock  58 Apr  4 16:45 phat_hello
```

#### Create/List Accounts

There is a basic dev account generation that can be protected by a configured password if desired. By default, the list of accounts can be seen with `swanky phala account list`.

```bash
└─[$]> swanky phala account list
✔ Stored dev accounts:
 Alias   Address                                          Protected 
 ─────── ──────────────────────────────────────────────── ───────── 
 alice   45R2pfjQUW2s9PQRHU48HQKLKHVMaDja7N3wpBtmF28UYDs2 false     
 bob     43qsYbZGLn2xzNuurY6BY4QNDSUU7gLEcXuckpm6B3DEmEx9 false     
 charlie 43tXcmhJfmvbczKaPKgWXirf3a9r6zD63KAxHq4CTSPm4DRf false     
 dave    41iFgxEGsnyGv5Abdo6Uq6n6BjoLS3p1UMKv9GvwMVuY5er7 false     
 eve     45ppQG9QcAkUdh2AP25CxDAnBAK1EACefQA2rMtbApzu6UXa false     
 ferdie  41GUHy9gmjhst2edhhoWCZcf6rqCheD5XMGTUF53CWJTePuc false  
```

Creating a new account is simple and can be done with `swanky phala account create -a [ALIAS]`.

```bash
└─[$]> swanky phala account create -a hash
? Account passphrase (leave empty if to save as plain text)
Account created

 Alias Address                                          Islocked 
 ───── ──────────────────────────────────────────────── ──────── 
 hash  41b5ANRroHu44tKDoF3rtJnHFtdQnyTt72uXhad1vhja2oNQ          
😎 Account created successfully! 😎
└─[$]> swanky phala account list
✔ Stored dev accounts:
 Alias   Address                                          Protected 
 ─────── ──────────────────────────────────────────────── ───────── 
 alice   45R2pfjQUW2s9PQRHU48HQKLKHVMaDja7N3wpBtmF28UYDs2 false     
 bob     43qsYbZGLn2xzNuurY6BY4QNDSUU7gLEcXuckpm6B3DEmEx9 false     
 charlie 43tXcmhJfmvbczKaPKgWXirf3a9r6zD63KAxHq4CTSPm4DRf false     
 dave    41iFgxEGsnyGv5Abdo6Uq6n6BjoLS3p1UMKv9GvwMVuY5er7 false     
 eve     45ppQG9QcAkUdh2AP25CxDAnBAK1EACefQA2rMtbApzu6UXa false     
 ferdie  41GUHy9gmjhst2edhhoWCZcf6rqCheD5XMGTUF53CWJTePuc false     
 hash    41b5ANRroHu44tKDoF3rtJnHFtdQnyTt72uXhad1vhja2oNQ false 
```
