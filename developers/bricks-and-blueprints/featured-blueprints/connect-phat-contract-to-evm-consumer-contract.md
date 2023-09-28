# ⚔ Connect Phat Contract to EVM Consumer Contract

## [Overview](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#overview) <a href="#user-content-overview" id="user-content-overview"></a>

This project represents a basic EVM Consumer Contract that is compatible with a deployed Oracle written in TypeScript on Phala Network.

> **Note**: For simplicity, we will utilize Polygon Mumbai and Polygon Mainnet for the following examples.

## [Prerequisites](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#prerequisites) <a href="#user-content-prerequisites" id="user-content-prerequisites"></a>

* Active Phala Profile with version `>= 1.0.1` via [Phat Contract 2.0 UI](https://bricks.phala.network/)
* [Hardhat](https://hardhat.org/)
* For EVM Mainnet deployments:
  * Ex: Polygonscan API Key that can be generated on [polygonscan](https://polygonscan.com/)
* RPC Endpoint for EVM Chain Mainnet & EVM Chain Testnet
  * [Alchemy](https://alchemy.com/) - This repo example uses Alchemy's API Key.
  * [Infura](https://infura.io/)
  * Personal RPC Node (Ex. [ProjectPi](https://hub.projectpi.xyz/))
* Polkadot Account for Phala PoC5 Testnet and Mainnet deployment

### [Environment Variables:](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#environment-variables) <a href="#user-content-environment-variables" id="user-content-environment-variables"></a>

Check out the environment variables here in [.env.local](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/.env.local) file.

## [Getting Started](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#getting-started) <a href="#user-content-getting-started" id="user-content-getting-started"></a>

> 🚨 **Note** 🚨: If you cloned this repo or created a template, skip to [Create a Phala Profile](connect-phat-contract-to-evm-consumer-contract.md#user-content-create-a-phala-profile).

First you will need to install the [@phala/fn](https://www.npmjs.com/package/@phala/fn) CLI tool using your node package manager (`npm`) or use node package execute (`npx`). In this tutorial we use `npx`.

Now create your first template with the CLI tool command:

```
npx @phala/fn init userJourney
```

We currently have only one template. Just press enter to see something similar to the example below:

```
npx @phala/fn init example
# @phala/fn@0.1.5
# Ok to proceed? (y) y
# ? Please select one of the templates for your "userJourney" project: lensapi-oracle-consumer-contract. Polygon Consumer Contract for LensAPI Oracle
# Downloading the template: https://github.com/Phala-Network/lensapi-oracle-consumer-contract... ✔
# The project is created in /Users/hashwarlock/Projects/Phala/Temp/userJourney 🎉
# Now run:
#
#  cd userJourney
#  npm install
```

`cd` into the newly created template and `ls` the directory which will look similar to below.

```
cd userJourney
ls
# total 736
# drwxr-xr-x  18 hashwarlock  staff   576B Sep  6 15:32 .
# drwxr-xr-x  35 hashwarlock  staff   1.1K Sep  6 15:32 ..
# -rw-r--r--   1 hashwarlock  staff   2.1K Sep  6 15:32 .env.local
# -rw-r--r--   1 hashwarlock  staff   227B Sep  6 15:32 .gitignore
# -rw-r--r--   1 hashwarlock  staff    34K Sep  6 15:32 LICENSE
# -rw-r--r--   1 hashwarlock  staff   8.9K Sep  6 15:32 README.md
# drwxr-xr-x   5 hashwarlock  staff   160B Sep  6 15:32 abis
# drwxr-xr-x   4 hashwarlock  staff   128B Sep  6 15:32 assets
# drwxr-xr-x   5 hashwarlock  staff   160B Sep  6 15:32 contracts
# -rw-r--r--   1 hashwarlock  staff   1.3K Sep  6 15:32 hardhat.config.ts
# -rw-r--r--   1 hashwarlock  staff    95B Sep  6 15:32 mumbai.arguments.ts
# -rw-r--r--   1 hashwarlock  staff   2.6K Sep  6 15:32 package.json
# -rw-r--r--   1 hashwarlock  staff    96B Sep  6 15:32 polygon.arguments.ts
# drwxr-xr-x   5 hashwarlock  staff   160B Sep  6 15:32 scripts
# drwxr-xr-x   3 hashwarlock  staff    96B Sep  6 15:32 src
# drwxr-xr-x   3 hashwarlock  staff    96B Sep  6 15:32 test
# -rw-r--r--   1 hashwarlock  staff   201B Sep  6 15:32 tsconfig.json
# -rw-r--r--   1 hashwarlock  staff   290K Sep  6 15:32 yarn.lock
```

## [Create a Phala Profile](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#create-a-phala-profile) <a href="#user-content-create-a-phala-profile" id="user-content-create-a-phala-profile"></a>

This step requires you to have a Polkadot account. You can get an account from one of the following:

* [Polkadot.js Wallet Extension](https://polkadot.js.org/extension/)
* [Talisman Wallet](https://www.talisman.xyz/)
* [SubWallet](https://www.subwallet.app/) (**Support for iOS/Android**)

First, create your Bricks Profile account on the [Phala PoC5 Testnet](https://bricks-poc5.phala.network/) or [Phala Mainnet](https://bricks.phala.network/). Here is a quick 1 minute [YouTube video](https://youtu.be/z1MR48NYtYc) on setting up from scratch. Here is what your Phala Profile account overview should look like:&#x20;

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/BricksProfileCheck.png" alt=""><figcaption></figcaption></figure>

[**Option 1: Export Polkadot account as json file**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#option-1-export-polkadot-account-as-json-file)

Go to your browser and click on the polkadot.js extension. Select your account and click "Export Account".  Next, you will be prompted for your password before saving the file to your project directory. **Note** this is what will be set to [`POLKADOT_WALLET_PASSPHRASE`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/.env.local).  Make sure to save the file as `polkadot-account.json` in the root of your project directory.&#x20;

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/ExportTypePass.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/SaveAccount.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/ExportAccount.png" alt=""><figcaption></figcaption></figure>

[**Option 2: Set mnemonic phrase to** ](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#option-2-set-mnemonic-phrase-to-polkadot\_wallet\_suri)[**`POLKADOT_WALLET_SURI`**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/.env.local)

After creating your Phala Profile, set your `.env` variable [`POLKADOT_WALLET_SURI`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/.env.local) to the mnemonic phrase from generating the new Polkadot Account.

Here is a screenshot of how to set `POLKADOT_WALLET_SURI`:&#x20;

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/PolkadotAccountSuri.png" alt=""><figcaption></figcaption></figure>

## [Testing Locally](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#testing-locally) <a href="#user-content-testing-locally" id="user-content-testing-locally"></a>

#### [Test Default Phat Contract Locally](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#test-default-phat-contract-locally) <a href="#user-content-test-default-phat-contract-locally" id="user-content-test-default-phat-contract-locally"></a>

With a template created and a basic default Phat Contract example ready to test, let’s step through the process of preparing your repo to execute the test locally.

First step is to install the package dependencies with the following command:

```
yarn install
```

Everything should go smoothly and produce similar output below:

```
yarn install
# [1/4] 🔍  Resolving packages...
# [2/4] 🚚  Fetching packages...
# [3/4] 🔗  Linking dependencies...
# warning " > @typechain/ethers-v5@10.1.0" has unmet peer dependency "@ethersproject/bytes@^5.0.0".
# [4/4] 🔨  Building fresh packages...
# ✨  Done in 4.95s.
```

Now that the package dependencies are installed, lets build the default Phat Contract which is located in [`./src/index.ts`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/src/index.ts).

For those want to understand what the contents of `./src/index.ts` mean, go to the `PHAT_CONTRACT_INFO.md` file to read more. If you are already familiar with the concepts then you can proceed to with the deployment process.

Build the default Phat Contract with this command:

```
yarn build-function
```

You will see output similar to the example below. and a file in `./dist/index.js` will be generated.

```
yarn build-function
# Creating an optimized build... done
# Compiled successfully.
#
#   17.66 KB  dist/index.js
# ✨  Done in 3.48s.
```

With our default Phat Contract built, we can run some initial tests. First test will be simple.

```
yarn run-function
```

It was expected for it to fail like this:

```
yarn run-function
# handle req: undefined
# Malformed request received
# {"output":"0x000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"}
# ✨  Done in 0.96s.
```

Notice that the test fails and reports that a `Malformed request received` was emitted and the request was `undefined`. This is expected as you will need to define the parameters by adding a `-a abi.encode(requestId, profileId) https://api-mumbai.lens.dev` to your command.

Let’s try again.

> Note: You will need to use `abi.encode` the tuple of `(requestId, profileId)` to get the appropriate hexstring for the first argument.

```
yarn run-function -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000 https://api-mumbai.lens.dev
```

You will see:

```
yarn run-function -a 0x00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000040000000
00000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000 https://api-mumbai.lens.dev
# handle req: 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000
# Request received for profile 0x01
# response: 0,1,3346
# {"output":"0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000d12"}
# ✨  Done in 1.42s.
```

We have now successfully tested the default Phat Contract and ran a test to verify the function returns a response as expected.

### [Testing Default Phat Contract with Local Hardhat Node](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#testing-default-phat-contract-with-local-hardhat-node) <a href="#user-content-testing-default-phat-contract-with-local-hardhat-node" id="user-content-testing-default-phat-contract-with-local-hardhat-node"></a>

Previously we showed how to test the default Phat Contract locally without a running node, but we can also run two other tests.

1. Run the default mocha e2e tests.
2. Run local hardhat node and watch the requests that are pushed and see how the Phat Contract transforms the data.

**Run the default mocha e2e tests**

Lets’s start with the first test case.

> Note: You will need to ensure you configure your local vars `POLYGON_RPC_URL` and `MUMBAI_RPC_URL` `.env` file. You can do this with `cp .env.local .env` then edit the `.env` with your information.

```
yarn hardhat test
```

You will now see that all test cases have passed.

```
yarn hardhat test
# Compiled 14 Solidity files successfully
#
#  OracleConsumerContract.sol
#    ✔ Push and receive message (1664ms)
#
#  1 passing (2s)
#
# ✨  Done in 3.29s.
```

This is how the e2e mocha test will look like. You can customize this file at [`OracleConsumerContract.ts`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/contracts/OracleConsumerContract.sol).

**Run local hardhat node and watch the requests that are pushed and see how the Phat Contract transforms the data**

First we will start a local hardhat node.

```
yarn hardhat node
```

With our hardhat node running locally, we can now deploy the `OracleConsumerContract.sol` contract to the local hardhat network.

```
yarn localhost-deploy 
```

```
yarn localhost-deploy
# Deploying...
# Deployed { consumer: '0x0165878A594ca255338adfa4d48449f69242Eb8F' }
# ✨  Done in 0.94s.
```

Make sure to copy the deployed contract address when you deploy your own contract locally. Note you contract address will be different than `0x0165878A594ca255338adfa4d48449f69242Eb8F`. We will now start watching the hardhat node deployed contract for any new requests.

```
yarn localhost-watch 0x0165878A594ca255338adfa4d48449f69242Eb8F artifacts/contracts/OracleConsumerContract.sol/OracleConsumerContract.sol.json dist/index.js -a https://api-mumbai.lens.dev/
```

```
yarn localhost-watch 0x0165878A594ca255338adfa4d48449f69242Eb8F artifacts/contracts/OracleConsumerContract.sol.sol/OracleConsumerContract.sol.json dist/index.js -a https://api-mumbai.lens.dev/
# $ phat-fn watch 0x0165878A594ca255338adfa4d48449f69242Eb8F artifacts/contracts/OracleConsumerContract.sol/OracleConsumerContract.sol.json dist/index.js -a https://api-mumbai.lens.dev/
# Listening for OracleConsumerContract.sol MessageQueued events...
```

Let’s now make a new request and see what happens with the listener’s output. In separate tab, you will push a request with the following.

```
LOCALHOST_CONSUMER_CONTRACT_ADDRESS=0x0165878A594ca255338adfa4d48449f69242Eb8F yarn localhost-push-request
```

```
LOCALHOST_CONSUMER_CONTRACT_ADDRESS=0x0165878A594ca255338adfa4d48449f69242Eb8F yarn localhost-push-request
# Pushing a request...
# Received event [ResponseReceived]: {
#  reqId: BigNumber { value: "1" },
#  input: '0x01',
#  value: BigNumber { value: "1597" }
# }
# ✨  Done in 4.99s.
```

If we look back at the listener tab, we will see output has been appended.

```
Listening for OracleConsumerContract MessageQueued events...
Received event [MessageQueued]: {
  tail: 0n,
  data: '0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000'
}
handle req: 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000
Request received for profile 0x01
response: 0,1,1597
JS Execution output: 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000063d
```

## [Deployment](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#deployment) <a href="#user-content-deployment" id="user-content-deployment"></a>

Now that you have the prerequisites to deploy a Polygon Consumer Contract on Polygon, lets begin with some initials tasks.

#### [Install Dependencies & Compile Contracts](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#install-dependencies--compile-contracts) <a href="#user-content-install-dependencies--compile-contracts" id="user-content-install-dependencies--compile-contracts"></a>

```
# install dependencies
$ yarn

# compile contracts
$ yarn compile
```

### [Deploy to Polygon Mumbai Testnet](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#deploy-to-polygon-mumbai-testnet) <a href="#user-content-deploy-to-polygon-mumbai-testnet" id="user-content-deploy-to-polygon-mumbai-testnet"></a>

With the contracts successfully compiled, now we can begin deploying first to Polygon Mumbai Testnet. If you have not gotten `MATIC` for Mumbai Testnet then get `MATIC` from a [faucet](https://mumbaifaucet.com/). Ensure to save the address after deploying the Consumer Contract because this address will be use in the "[Configure Client](https://docs.phala.network/developers/bricks-and-blueprints/featured-blueprints/lensapi-oracle#step-4-configure-the-client-address)" section of Phat Bricks UI. The deployed address will also be set to the environment variable [`MUMBAI_CONSUMER_CONTRACT_ADDRESS`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/.env.local).

```
yarn test-deploy
```

```
# deploy contracts to testnet mumbai
yarn test-deploy
# Deploying...
#
# 🎉 Your Consumer Contract has been deployed, check it out here: https://mumbai.polygonscan.com/address/0x10FA409109E073C15b77A8352cB6A89C12CD1605
#
# You also need to set up the consumer contract address in your .env file:
#
# MUMBAI_CONSUMER_CONTRACT_ADDRESS=0x10FA409109E073C15b77A8352cB6A89C12CD1605
#
# Configuring...
# Done
# ✨  Done in 8.20s.
```

### [**Verify Contract on Polygon Mumbai Testnet**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#verify-contract-on-polygon-mumbai-testnet)

Ensure to update the [`mumbai.arguments.ts`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/mumbai.arguments.ts) file with the constructor arguments used to instantiate the Consumer Contract. If you add additional parameters to the constructor function then make sure to update the `mumbai.arguments.ts` file.

> **Note**: Your contract address will be different than `0x090E8fDC571d65459569BC87992C1026121DB955` when verifying your contract. Make sure to get your actual contract address from the console log output after executing `yarn test-deploy`.

```
yarn test-verify <MUMBAI_CONSUMER_CONTRACT_ADDRESS>
```

```
yarn test-verify 0x090E8fDC571d65459569BC87992C1026121DB955
# yarn run v1.22.18
# $ hardhat verify --network mumbai --constructor-args mumbai.arguments.ts 0x090E8fDC571d65459569BC87992C1026121DB955
# Nothing to compile
# No need to generate any newer typings.
# Successfully submitted source code for contract
# contracts/OracleConsumerContract.sol:OracleConsumerContract.sol at 0x090E8fDC571d65459569BC87992C1026121DB955
# for verification on the block explorer. Waiting for verification result...
#
# Successfully verified contract OracleConsumerContract.sol on Etherscan.
# https://mumbai.polygonscan.com/address/0x090E8fDC571d65459569BC87992C1026121DB955#code
# ✨  Done in 5.91s.
```

### [Deploy Phat Contract to PoC5 Testnet](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#deploy-phat-contract-to-poc5-testnet) <a href="#user-content-deploy-phat-contract-to-poc5-testnet" id="user-content-deploy-phat-contract-to-poc5-testnet"></a>

For customizing your Phat Contract, checkout Phat Contract custom configurations in [JS\_API\_DOC.md](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/src/JS\_API\_DOC.md) to learn more before deploying to PoC5 testnet.

First you will need to build your Phat Contract with this command:

```
yarn build-function
```

Here is the expected output:

```
yarn build-function
# yarn run v1.22.18
# $ phat-fn build src/index.ts
# Creating an optimized build... done
# Compiled successfully.
#
#   17.66 KB  dist/index.js
# ✨  Done in 3.71s.
```

Now that are Phat Contract has built successfully, let's deploy to Phala PoC5 Testnet with the following command:

```
yarn test-deploy-function
```

Here is the expected output:

> Note: your contract IDs will vary and not be the same as the IDs below.

```
yarn test-deploy-function
# yarn run v1.22.18
# $ hardhat run --network mumbai ./scripts/mumbai/deploy-function.ts
# We going to deploy your Phat Contract to Phala Network Testnet: wss://poc5.phala.network/ws
# (node:12200) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
# (Use `node --trace-warnings ...` to show where the warning was created)
# Your Brick Profile contract ID: 0xfd18dca07dc76811dd99b14ee6fe3b82e135ed06a2c311b741e6c9163892b32c
# The ActionOffchainRollup contract has been instantiated:  0x1161a649467fac4532b3ef85b70bf750380dea49c3efbb4ce8db66d0de47389a
#
# 🎉 Your workflow has been added, you can check it out here: https://bricks-poc5.phala.network//workflows/0xfd18dca07dc76811dd99b14ee6fe3b82e135ed06a2c311b741e6c9163892b32c/0
#
#   You also need set up the attestor to your .env file:
#
#   MUMBAI_PHALA_ORACLE_ATTESTOR=0x1f6911eaa71405eb043961c0ba4bb6ed7ecc5c8e
#
#   Then run:
#
#   yarn test-set-attestor
#
#   Then send the test request with follow up command:
#
#   yarn test-push-request
#
#   You can continue update the Phat Contract codes and update it with follow up commands:
#
#   yarn build-function
#   WORKFLOW_ID=0 yarn test-update-function
#
# ✨  Done in 36.35s.
```

Go to the [PoC5 Testnet Bricks UI](https://bricks-poc5.phala.network/) Dashboard and you can see your newly deployed Phat Contract. [![](https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/Function-added.png)](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/assets/Function-added.png)

### [**Interact with Consumer Contract on Polygon Mumbai**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#interact-with-consumer-contract-on-polygon-mumbai)

Test Consumer Contract on Mumbai with a few tests to check for malformed requests failures, successful requests, and set the attestor.

```
yarn test-set-attestor
```

```
yarn test-set-attestor
# yarn run v1.22.18
# $ hardhat run --network mumbai ./scripts/mumbai/set-attestor.ts
# Setting attestor...
# 🚨NOTE🚨
# Make sure to set the Consumer Contract Address in your Phat Bricks 🧱 UI dashboard (https://bricks-poc5.phala.network)
# - Go to 'Configure Client' section where a text box reads 'Add Consumer Smart Contract'
# - Set value to 0x090E8fDC571d65459569BC87992C1026121DB955
# Done
# ✨  Done in 2.69s.
```

Test pushing a malform request.

```
yarn test-push-malformed-request
```

```
yarn test-push-malformed-request
# yarn run v1.22.18
# $ hardhat run --network mumbai ./scripts/mumbai/push-malformed-request.ts
# Pushing a malformed request...
# Done
# ✨  Done in 2.48s.
```

Test pushing a valid request.

```
yarn test-push-request
```

```
yarn test-push-request
# Pushing a request...
# Done
# ✨  Done in 2.97s.
```

### [Update Phat Contract on Phala PoC5 Testnet](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#update-phat-contract-on-phala-poc5-testnet) <a href="#user-content-update-phat-contract-on-phala-poc5-testnet" id="user-content-update-phat-contract-on-phala-poc5-testnet"></a>

[**Option 1: If you exported your Polkadot account to root of project as `polkadot-account.json`**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#option-1-if-you-exported-your-polkadot-account-to-root-of-project-as-polkadot-accountjson)

With option 1 you are not required to rebuild the [`index.ts`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/src/index.ts) script since the `@phala/fn update` command will trigger the build for you.

> **Note**: Set `WORKFLOW_ID` to the ID of your deployed Phat Contract. You find this in the dashboard of deployed Phat Contracts.

```
WORKFLOW_ID=X npx @phala/fn update -a ./polkadot.json --workflowId=$WORKFLOW_ID
```

After the `index.ts` is built, you will be prompted for your password, before triggering the update to your deployed Phat Contract.

```
WORKFLOW_ID=0 npx @phala/fn update -a ./polkadot-account.json --workflowId=$WORKFLOW_ID
# Creating an optimized build... done
# Compiled successfully.
#
#  17.64 KB  dist/index.js
# Start updating...
#
# ? Enter hahaha account password [hidden]
# Connecting to the endpoint: wss://poc5.phala.network/ws... ⢿
# (node:20408) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
# Connecting to the endpoint: wss://poc5.phala.network/ws... done
# Querying your Brick Profile contract ID... done
# Your Brick Profile contract ID: 0x4071788a8ce6fbab0cacea0cb1aa52853b5537db7955643e5010c22913c2b1dd
# Checking your workflow settings... done
# Updating... done
# The Phat Function for workflow 1 has been updated.
# ✨  Done in 14.80s.
```

Congrats! You've now successfully updated your Phat Contract!

[**Option 2: Build Phat Contract script then update Phat Contract**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#option-2-build-phat-contract-script-then-update-phat-contract)

With option 2, we have to update the Phat Contract that we have deployed. Once we have updated the Phat Contract, we must build the Phat Contract again.

```
yarn build-function
```

```
yarn build-function
# yarn run v1.22.18
# $ phat-fn build src/index.ts
# Creating an optimized build... done
# Compiled successfully.
#
#  17.66 KB  dist/index.js
# ✨  Done in 3.48s.
```

> **Note**: Before we update the Phat Contract, make sure to take the `WORKFLOW_ID` from the deployment of the Phat Contract step and set it in your `.env` file.

Now let's update the Phat Contract with the following command:

```
yarn test-update-function
```

```
yarn test-update-function
# yarn run v1.22.18
# $ hardhat run --network mumbai ./scripts/mumbai/update-function.ts
# (node:12991) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
# (Use `node --trace-warnings ...` to show where the warning was created)
# Your Brick Profile contract ID: 0xfd18dca07dc76811dd99b14ee6fe3b82e135ed06a2c311b741e6c9163892b32c
# The Phat Contract for workflow 0 has been updated.
# ✨  Done in 5.07s.
```

### [Deploy to Polygon Mainnet](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#deploy-to-polygon-mainnet) <a href="#user-content-deploy-to-polygon-mainnet" id="user-content-deploy-to-polygon-mainnet"></a>

Ensure to save the address after deploying the Consumer Contract because this address will be used in the "[Configure Client](https://docs.phala.network/developers/bricks-and-blueprints/featured-blueprints/lensapi-oracle#step-4-configure-the-client-address)" section of Phat Bricks UI. The deployed address will also be set to the environment variable [`POLYGON_CONSUMER_CONTRACT_ADDRESS`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/.env.local).

> **Note**: Your contract address will be different than `0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4` when verifying your contract. Make sure to get your actual contract address from the console log output after executing `yarn main-deploy`.

```
yarn main-deploy
# Deploying...
#
# 🎉 Your Consumer Contract has been deployed, check it out here: https://polygonscan.com/address/0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
#
# You also need to set up the consumer contract address in your .env file:
#
# POLYGON_CONSUMER_CONTRACT_ADDRESS=0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
#
# Configuring...
# Done
# ✨  Done in 8.20s.
```

### [**Verify Contract on Polygon Mainnet**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#verify-contract-on-polygon-mainnet)

Ensure to update the [`polygon.arguments.ts`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/polygon.arguments.ts) file with the constructor arguments used to instantiate the Consumer Contract. If you add additional parameters to the constructor function then make sure to update the `polygon.arguments.ts` file.

```
yarn main-verify 0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
# Nothing to compile
# No need to generate any newer typings.
# Successfully submitted source code for contract
# contracts/OracleConsumerContract.sol.sol:OracleConsumerContract.sol.sol.sol at 0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
# for verification on the block explorer. Waiting for verification result...
#
# Successfully verified contract OracleConsumerContract.sol on Etherscan.
# https://polygonscan.com/address/0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4#code
# Done in 8.88s.
```

### [Deploy Phat Contract to Phala Mainnet](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#deploy-phat-contract-to-phala-mainnet) <a href="#user-content-deploy-phat-contract-to-phala-mainnet" id="user-content-deploy-phat-contract-to-phala-mainnet"></a>

For customizing your Phat Contract, Phat Contract custom configurations can be found here in [JS\_API\_DOC.md](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/src/JS\_API\_DOC.md) to learn more before deploying to Phala Mainnet.

First you will need to build your Phat Contract with this command:

```
yarn build-function
```

Here is the expected output:

```
yarn build-function
# yarn run v1.22.18
# $ phat-fn build src/index.ts
# Creating an optimized build... done
# Compiled successfully.
#
#   17.66 KB  dist/index.js
# ✨  Done in 3.71s.
```

Now that are Phat Contract has built successfully, let's deploy to Phala Mainnet with the following command:

```
yarn main-deploy-function
```

Here is the expected output:

> Note: your contract IDs will vary and not be the same as the IDs below.

```
yarn main-deploy-function
# yarn run v1.22.18
# $ hardhat run --network polygon ./scripts/polygon/deploy-function.ts
# We are going to deploy your Phat Contract to Phala Network Mainnet:: wss://api.phala.network/ws
# (node:12200) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
# (Use `node --trace-warnings ...` to show where the warning was created)
# Your Brick Profile contract ID: 0xfd18dca07dc76811dd99b14ee6fe3b82e135ed06a2c311b741e6c9163892b32c
# The ActionOffchainRollup contract has been instantiated:  0x1161a649467fac4532b3ef85b70bf750380dea49c3efbb4ce8db66d0de47389a
#
# 🎉 Your workflow has been added, you can check it out here: https://bricks.phala.network//workflows/0xfd18dca07dc76811dd99b14ee6fe3b82e135ed06a2c311b741e6c9163892b32c/0
#
#   You also need set up the attestor to your .env file:
#
#   POLYGON_PHALA_ORACLE_ATTESTOR=0x1f6911eaa71405eb043961c0ba4bb6ed7ecc5c8e
#
#   Then run:
#
#   yarn test-set-attestor
#
#   Then send the test request with follow up command:
#
#   yarn test-push-request
#
#   You can continue update the Phat Contract codes and update it with follow up commands:
#
#   yarn build-function
#   WORKFLOW_ID=0 yarn test-update-function
#
# ✨  Done in 36.35s.
```

### [**Interact with Consumer Contract on Polygon Mainnet**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#interact-with-consumer-contract-on-polygon-mainnet)

Execute Scripts to Consumer Contract on Polygon Mainnet. The Consumer Contract on Polygon Mainnet with a few actions to mimic a malformed request, successful requests, and set the attestor.

```
yarn main-set-attestor
# Setting attestor...
# 🚨NOTE🚨
# Make sure to set the Consumer Contract Address in your Phat Bricks 🧱 UI dashboard (https://bricks-poc5.phala.network)
# - Go to 'Configure Client' section where a text box reads 'Add Consumer Smart Contract'
# - Set value to 0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
# Done
# ✨  Done in 1.56s.
# execute push-malformed-request
yarn main-push-malformed-request
# Pushing a malformed request...
# Done
# execute push-request
yarn main-push-request
# Pushing a request...
# Done
```

### [Update Phat Contract on Phala Mainnet](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#update-phat-contract-on-phala-mainnet) <a href="#user-content-update-phat-contract-on-phala-mainnet" id="user-content-update-phat-contract-on-phala-mainnet"></a>

[**Option 1: If you exported your Polkadot account to root of project as `polkadot-account.json`**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#option-1-if-you-exported-your-polkadot-account-to-root-of-project-as-polkadot-accountjson-1)

With option 1 you are not required to rebuild the [`index.ts`](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/src/index.ts) script since the `@phala/fn update` command will trigger the build for you.

> **Note**: Set `WORKFLOW_ID` to the ID of your deployed Phat Contract. You find this in the dashboard of deployed Phat Contracts.

```
WORKFLOW_ID=X npx @phala/fn update --mode=production -a ./polkadot.json --workflowId=$WORKFLOW_ID
```

After the `index.ts` is built, you will be prompted for your password, before triggering the update to your deployed Phat Contract.

```
WORKFLOW_ID=0 npx @phala/fn update --mode=production -a ./polkadot-account.json  --workflowId=$WORKFLOW_ID
# Creating an optimized build... done
# Compiled successfully.
#
#  17.64 KB  dist/index.js
# Start updating...
#
# ? Enter hahaha account password [hidden]
# Connecting to the endpoint: wss://api.phala.network/ws... ⢿
# (node:20408) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
# Connecting to the endpoint: wss://api.phala.network/ws... done
# Querying your Brick Profile contract ID... done
# Your Brick Profile contract ID: 0x4071788a8ce6fbab0cacea0cb1aa52853b5537db7955643e5010c22913c2b1dd
# Checking your workflow settings... done
# Updating... done
# The Phat Function for workflow 1 has been updated.
# ✨  Done in 14.80s.
```

Congrats! You've now successfully updated your Phat Contract!

[**Option 2: Build Phat Contract script then update Phat Contract**](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#option-2-build-phat-contract-script-then-update-phat-contract-1)

With optin 2, update the function that we have deployed. Once we have updated the function, we must build the function again.

```
yarn build-function
```

```
yarn build-function
# yarn run v1.22.18
# $ phat-fn build src/index.ts
# Creating an optimized build... done
# Compiled successfully.
#
#  17.66 KB  dist/index.js
# ✨  Done in 3.48s.
```

> Note: Before we update the function, make sure to take the `WORKFLOW_ID` from the deployment of the Phat Contract function step and set it in your `.env` file.

Now let's update the function with the following command:

```
yarn main-update-function
```

```
yarn main-update-function
# yarn run v1.22.18
# $ hardhat run --network polygon ./scripts/polygon/update-function.ts
# (node:12991) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
# (Use `node --trace-warnings ...` to show where the warning was created)
# Your Brick Profile contract ID: 0xfd18dca07dc76811dd99b14ee6fe3b82e135ed06a2c311b741e6c9163892b32c
# The Phat Function for workflow 0 has been updated.
# ✨  Done in 5.07s.
```

## [Closing](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md#closing) <a href="#user-content-closing" id="user-content-closing"></a>

Once you have stored, the deployed address of the Consumer Contract and set the value in the "Configure Client" section of the deployed Phala Oracle, you will now have a basic boilerplate example of how to connect your Polygon dApp to a LensAPI Oracle Blueprint. Execute a new requests and check if your configuration is correct like below:&#x20;

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/polygonscan-ex.png" alt=""><figcaption></figcaption></figure>
