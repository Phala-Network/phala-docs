# ⚔ Connect Phat Contract to EVM Consumer Contract

## Overview <a href="#user-content-overview" id="user-content-overview"></a>

This project represents a basic EVM Consumer Contract that is compatible with a deployed Oracle written in TypeScript on Phala Network.

> **Note**: For simplicity, we will utilize Polygon Mumbai and Polygon Mainnet for the following examples.

## Prerequisites <a href="#user-content-prerequisites" id="user-content-prerequisites"></a>

* Active Phala Profile with version `>= 1.0.1` via [Phat Contract 2.0 UI](https://bit.ly/3LHccmR)
* [Hardhat](https://bit.ly/469uyW5)
* For EVM Mainnet deployments:
  * Ex: Polygonscan API Key that can be generated on [polygonscan](https://bit.ly/3rBkypp)
* RPC Endpoint for EVM Chain Mainnet & EVM Chain Testnet
  * [Alchemy](https://bit.ly/46uObaH) - This repo example uses Alchemy's API Key.
  * [Infura](https://bit.ly/3PXXCtN)
  * Personal RPC Node (Ex. [ProjectPi](https://bit.ly/3RGf7QS))
* Polkadot Account for Phala PoC6 Testnet and Mainnet deployment
* Node >= 18.x

### Environment Variables: <a href="#user-content-environment-variables" id="user-content-environment-variables"></a>

Check out the environment variables here in [.env.local](https://bit.ly/3ZAA814) file.

## Getting Started <a href="#user-content-getting-started" id="user-content-getting-started"></a>

> 🚨 **Note** 🚨:&#x20;
>
> If you cloned this repo or created a template, skip to [Create a Phala Profile](connect-phat-contract-to-evm-consumer-contract.md#user-content-create-a-phala-profile).

First you will need to install the `@phala/fn` CLI tool using your node package manager (`npm`) or use node package execute (`npx`). In this tutorial we use `npx`.

Now create your first template with the CLI tool command:

```sh
npx @phala/fn@latest init userJourney
```

Select one of the template and press enter to see something similar to the example below:

```sh
npx @phala/fn@latest init userJourney
# @phala/fn@0.2.8
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

```sh
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
# -rw-r--r--   1 hashwarlock  staff   290K Sep  6 15:32 package-lock.json
```

## Create a Phala Profile <a href="#user-content-create-a-phala-profile" id="user-content-create-a-phala-profile"></a>

This step requires you to have a Polkadot account. You can get an account from one of the following:

* [Polkadot.js Wallet Extension](https://bit.ly/3RMUjqy)
* [Talisman Wallet](https://bit.ly/3ZzAPYD)
* [SubWallet](https://bit.ly/3tjS8R7) (**Support for iOS/Android**)

First, create your Phala Profile account on the [Phala PoC6 Testnet](https://bit.ly/3LHccmR) or [Phala Mainnet](https://bit.ly/3LHccmR). Here is a quick 1 minute [YouTube video](https://bit.ly/46clfo4) on setting up from scratch. Here is what your Phala Profile account overview should look like:&#x20;

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/BricksProfileCheck.png" alt=""><figcaption></figcaption></figure>

**Option 1: Export Polkadot account as json file**

Go to your browser and click on the polkadot.js extension. Select your account and click "Export Account".  Next, you will be prompted for your password before saving the file to your project directory. **Note** this is what will be set to `POLKADOT_WALLET_ACCOUNT_PASSPHRASE`.  Make sure to save the file as `polkadot-account.json` in the root of your project directory.&#x20;

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/ExportTypePass.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/SaveAccount.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/ExportAccount.png" alt=""><figcaption></figcaption></figure>

**Option 2: Set mnemonic phrase to `POLKADOT_WALLET_SURI`**

After creating your Phala Profile, set your `.env` variable `POLKADOT_WALLET_SURI` to the mnemonic phrase from generating the new Polkadot Account.

Here is a screenshot of how to set `POLKADOT_WALLET_SURI`:&#x20;

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/PolkadotAccountSuri.png" alt=""><figcaption></figcaption></figure>

## Testing Locally <a href="#user-content-testing-locally" id="user-content-testing-locally"></a>

#### Test Default Phat Contract Locally <a href="#user-content-test-default-phat-contract-locally" id="user-content-test-default-phat-contract-locally"></a>

With a template created and a basic default Phat Contract example ready to test, let’s step through the process of preparing your repo to execute the test locally.

First step is to install the package dependencies with the following command:

```sh
npm install
```

Everything should go smoothly and produce similar output below:

```
npm install
# [1/4] 🔍  Resolving packages...
# [2/4] 🚚  Fetching packages...
# [3/4] 🔗  Linking dependencies...
# warning " > @typechain/ethers-v5@10.1.0" has unmet peer dependency "@ethersproject/bytes@^5.0.0".
# [4/4] 🔨  Building fresh packages...
# ✨  Done in 4.95s.
```

Now that the package dependencies are installed, lets build the default Phat Contract which is located in [`./src/index.ts`](https://bit.ly/3PBnP02).

For those want to understand what the contents of `./src/index.ts` mean, go to the `PHAT_CONTRACT_INFO.md` file to read more. If you are already familiar with the concepts then you can proceed to with the deployment process.

Build the default Phat Contract with this command:

```bash
npx @phala/fn build
```

You will see output similar to the example below. and a file in `./dist/index.js` will be generated.

```bash
npx @phala/fn build
# ✓ Compiled successfully.
#   17.66 KB  dist/index.js
```

With our default Phat Contract built, we can run some initial tests. First test will be simple.

```bash
npx @phala/fn run dist/index.js
```

It was expected for it to fail like this:

```bash
npx @phala/fn run dist/index.js
# handle req: undefined
# Malformed request received
# {"output":"0x000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"}
# ✨  Done in 0.96s.
```

Notice that the test fails and reports that a `Malformed request received` was emitted and the request was `undefined`. This is expected as you will need to define the parameters by adding a `-a abi.encode(requestId, profileId) https://api-v2-mumbai-live.lens.dev` to your command.

To simulate the expected result locally, run the Phala Oracle function now with this command:

```bash
npx @phala/fn run dist/index.js -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000 https://api-v2-mumbai-live.lens.dev
```

> **What are the ingredients for the `npx @phala/fn run` command?**
>
> Our Phat Contract script, now fully constructed, is ready for a trial run. This simulation mirrors the live script's operation when deployed on the Phala Network.
>
> The command's first parameter is a HexString, representing a tuple of types `[uintCoder, bytesCoder]`. This serves as the entry function. The second parameter is a `string`, embodying the configurable secrets fed into the main function.
>
> The `Coders.decode` function deciphers these parameters, yielding the decoded `requestId` and `encodedReqStr`. These decoded elements then become the raw material for the rest of the custom logic within the script.
>
> ```typescript
> export default function main(request: HexString, settings: string): HexString {
>   console.log(`handle req: ${request}`);
>   let requestId, encodedReqStr;
>   try {
>     [requestId, encodedReqStr] = decodeRequest(decodeRequestAbiParams, request);
>   } catch (error) {
>     console.info("Malformed request received");
>   }
> // ...
> } 
> ```

<details>

<summary>How the query looks under the hood</summary>

* HTTP Endpoint: [https://api-v2-mumbai-live.lens.dev](https://api-mumbai.lens.dev/)
* Profile ID: `0x01`
* Expected Graphql Query:

```graphql
query Profile {
    profile(request: { forProfileId: "0x01" }) {
      stats {
          followers
          following
          comments
          countOpenActions
          posts
          quotes
          mirrors
          publications
          reacted
          reactions
      }
    }
}
```

* Expected Output:

```graphql
{
  "data": {
    "profile": {
      "stats": {
        "followers": 2,
        "following": 0,
        "comments": 0,
        "countOpenActions": 1,
        "posts": 14,
        "quotes": 0,
        "mirrors": 0,
        "publications": 14,
        "reacted": 0,
        "reactions": 0
    }
  }
}
```

</details>

You will see:

```bash
npx @phala/fn run dist/index.js -a 0x00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000040000000
00000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000 https://api-mumbai.lens.dev
# handle req: 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000
# Request received for profile 0x01
# response: 0,1,201
# {"output":"0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000c9"}
# ✨  Done in 1.42s.
```

We have now successfully tested the default Phat Contract and ran a test to verify the function returns a response as expected.

### Testing Default Phat Contract with Local Hardhat Node <a href="#user-content-testing-default-phat-contract-with-local-hardhat-node" id="user-content-testing-default-phat-contract-with-local-hardhat-node"></a>

Previously we showed how to test the default Phat Contract locally without a running node, but we can also run two other tests.

1. Run the default mocha e2e tests.
2. Run local hardhat node and watch the requests that are pushed and see how the Phat Contract transforms the data.

**Run the default mocha e2e tests**

Lets’s start with the first test case.

> Note: You will need to ensure you configure your local vars `POLYGON_RPC_URL` and `MUMBAI_RPC_URL` `.env` file. You can do this with `cp .env.local .env` then edit the `.env` with your information.

```sh
npm run localhost-test
```

You will now see that all test cases have passed.

```sh
npm run localhost-test
# Compiled 14 Solidity files successfully
#
#  OracleConsumerContract.sol
#    ✔ Push and receive message (1664ms)
#
#  1 passing (2s)
#
# ✨  Done in 3.29s.
```

This is how the e2e mocha test will look like. You can customize this file at `OracleConsumerContract.ts`.

**Run local hardhat node and watch the requests that are pushed and see how the Phat Contract transforms the data**

First we will start a local hardhat node.

```sh
npm run localhost-node
```

With our hardhat node running locally, we can now deploy the `OracleConsumerContract.sol` contract to the local hardhat network.

```sh
npm run localhost-deploy 
```

```sh
npm run localhost-deploy
# Deploying...
# Deployed { consumer: '0x0165878A594ca255338adfa4d48449f69242Eb8F' }
# ✨  Done in 0.94s.
```

Make sure to copy the deployed contract address when you deploy your own contract locally. Note you contract address will be different than `0x0165878A594ca255338adfa4d48449f69242Eb8F`. We will now start watching the hardhat node deployed contract for any new requests.

```sh
npx @phala/fn watch 0x0165878A594ca255338adfa4d48449f69242Eb8F artifacts/contracts/OracleConsumerContract.sol/OracleConsumerContract.json dist/index.js -a https://api-mumbai.lens.dev/
```

```sh
npx @phala/fn watch 0x0165878A594ca255338adfa4d48449f69242Eb8F artifacts/contracts/OracleConsumerContract.sol/OracleConsumerContract.json dist/index.js -a https://api-mumbai.lens.dev/
# Listening for OracleConsumerContract.sol MessageQueued events...
```

Let’s now make a new request and see what happens with the listener’s output. In separate tab, you will push a request with the following.

```sh
LOCALHOST_CONSUMER_CONTRACT_ADDRESS=0x0165878A594ca255338adfa4d48449f69242Eb8F npm run localhost-push-request
```

```sh
LOCALHOST_CONSUMER_CONTRACT_ADDRESS=0x0165878A594ca255338adfa4d48449f69242Eb8F npm run localhost-push-request
# Pushing a request...
# Received event [ResponseReceived]: {
#  reqId: BigNumber { value: "1" },
#  input: '0x01',
#  value: BigNumber { value: "1597" }
# }
# ✨  Done in 4.99s.
```

If we look back at the listener tab, we will see output has been appended.

```sh
Listening for OracleConsumerContract MessageQueued events...
Received event [MessageQueued]: {
  tail: 0n,
  data: '0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000'
}
handle req: 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000
Request received for profile 0x01
response: 201
JS Execution output: 0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000c9
```

## Deployment <a href="#user-content-deployment" id="user-content-deployment"></a>

Now that you have the prerequisites to deploy a Polygon Consumer Contract on Polygon, lets begin with some initials tasks.

### Install Dependencies & Compile Contracts <a href="#user-content-install-dependencies--compile-contracts" id="user-content-install-dependencies--compile-contracts"></a>

```sh
# install dependencies
$ npm install

# compile contracts
$ npm run compile
```

### Deploy to Polygon Mumbai Testnet <a href="#user-content-deploy-to-polygon-mumbai-testnet" id="user-content-deploy-to-polygon-mumbai-testnet"></a>

With the contracts successfully compiled, now we can begin deploying first to Polygon Mumbai Testnet. If you have not gotten `MATIC` for Mumbai Testnet then get `MATIC` from a [faucet](https://bit.ly/3ZyFoT3). Ensure to save the address after deploying the Consumer Contract because this address will be use in the "Configure Client" section of Phat Bricks UI. The deployed address will also be set to the environment variable `MUMBAI_CONSUMER_CONTRACT_ADDRESS`.

```sh
npm run test-deploy
```

```sh
# deploy contracts to testnet mumbai
npm run test-deploy
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

### **(Optional) Verify Contract on Polygon Mumbai Testnet**

Ensure to update the `mumbai.arguments.ts` file with the constructor arguments used to instantiate the Consumer Contract. If you add additional parameters to the constructor function then make sure to update the `mumbai.arguments.ts` file.

> **Note**: Your contract address will be different than `0x090E8fDC571d65459569BC87992C1026121DB955` when verifying your contract. Make sure to get your actual contract address from the console log output after executing `npm run test-deploy`.

```sh
npm run test-verify -- <MUMBAI_CONSUMER_CONTRACT_ADDRESS>
```

```sh
npm run test-verify -- 0x090E8fDC571d65459569BC87992C1026121DB955
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

### Deploy Phat Contract to PoC6 Testnet <a href="#user-content-deploy-phat-contract-to-poc5-testnet" id="user-content-deploy-phat-contract-to-poc5-testnet"></a>

For customizing your Phat Contract, checkout Phat Contract custom configurations in [customizing-your-phat-contract.md](customizing-your-phat-contract.md "mention") to learn more before deploying to PoC6 testnet.

Now that are Phat Contract has built successfully, let's deploy to Phala PoC6 Testnet with the following command:

```shell
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn upload --coreSettings=https://api-v2-mumbai-live.lens.dev/
# If polkadot-account.json is in the root of project
npx @phala/fn upload -a ./polkadot-account.json --coreSettings=https://api-v2-mumbai-live.lens.dev/
```

Here is the expected output:

> Note: your contract IDs will vary and not be the same as the IDs below.

```shell
npx @phala/fn upload -a ./polkadot-account.json --coreSettings=https://api-v2-mumbai-live.lens.dev/
# ? Please enter your client RPC URL https://polygon-mumbai.g.alchemy.com/v2/JLjOfWJycWFOA0kK_SJ4jLGjtXkMN1wc
# ? Please enter your consumer address 0xA4Be456Fd0d41968a52b34Cdb8Ba875F2281134a
# ? Please Enter hahaha account password [hidden]
# Creating an optimized build... done
# Compiled successfully.
#
#  17.64 KB  dist/index.js
# Connecting to the endpoint: wss://poc6.phala.network/ws... done
# Querying your Brick Profile contract ID... done
# Your Brick Profile contract ID: 0x4071788a8ce6fbab0cacea0cb1aa52853b5537db7955643e5010c22913c2b1dd
# Instantiating the ActionOffchainRollup contract... done
# The ActionOffchainRollup contract has been instantiated: 0x9c777c16b0a185caa895835b8f3b9e8d67be9f5e30197f71b4d32d2b8fde4b3b
# Setting up the actions... done
# 🎉 Your workflow has been added, you can check it out here: https://bricks-poc6.phala.network/workflows/0x4071788a8ce6fbab0cacea0cb1aa52853b5537db7955643e5010c22913c2b1dd/3
# Your Attestor address: 0x2b5fe2920cce2f522d69613adaa9378ba43b687d
# Your WORKFLOW_ID: 3
# ✨  Done in 73.22s.
```

Go to the [PoC6 Testnet Bricks UI](https://bit.ly/3ZzwWCY) Dashboard and you can see your newly deployed Phat Contract.&#x20;

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/Function-added.png" alt=""><figcaption></figcaption></figure>

### **Interact with Consumer Contract on Polygon Mumbai**

Test Consumer Contract on Mumbai with a few tests to check for malformed requests failures, successful requests, and set the attestor.

```sh
npm run test-set-attestor
```

```sh
npm run test-set-attestor
# $ hardhat run --network mumbai ./scripts/mumbai/set-attestor.ts
# Setting attestor...
# 🚨NOTE🚨
# Make sure to set the Consumer Contract Address in your Phat Bricks 🧱 UI dashboard (https://bricks-poc6.phala.network)
# - Go to 'Configure Client' section where a text box reads 'Add Consumer Smart Contract'
# - Set value to 0x090E8fDC571d65459569BC87992C1026121DB955
# Done
# ✨  Done in 2.69s.
```

Test pushing a malform request.

```sh
npm run test-push-malformed-request
```

```sh
npm run test-push-malformed-request
# $ hardhat run --network mumbai ./scripts/mumbai/push-malformed-request.ts
# Pushing a malformed request...
# Done
# ✨  Done in 2.48s.
```

Test pushing a valid request.

```sh
npm run test-push-request
```

```sh
npm run test-push-request
# Pushing a request...
# Done
# ✨  Done in 2.97s.
```

### Update Phat Contract on Phala PoC6 Testnet <a href="#user-content-update-phat-contract-on-phala-poc5-testnet" id="user-content-update-phat-contract-on-phala-poc5-testnet"></a>

Sometimes you may have had a bug in your script or you want to test things out on the fly without deploying a whole new Phat Contract. We now allow you to update your Phat Contract easily in the commandline. Now let's update the Phat Contract with the following command:

```shell
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn update
# If polkadot-account.json is in the root of project
npx @phala/fn update -a ./polkadot-account.json
```

```shell
npx @phala/fn update -a ./polkadot-account.json
# ? Please Enter hahaha account password [hidden]
# Creating an optimized build... done
# Compiled successfully.
#
#   17.64 KB  dist/index.js
# Connecting to the endpoint: wss://poc6.phala.network/ws... done
# Querying your Brick Profile contract ID... done
# Your Brick Profile contract ID: 0x4071788a8ce6fbab0cacea0cb1aa52853b5537db7955643e5010c22913c2b1dd
# Checking your workflow settings... done
# Updating... done
# The Phat Function for workflow 1 has been updated.
# ✨  Done in 10.82s.
```

Congrats! You've now successfully updated your Phat Contract!

### Deploy to Polygon Mainnet <a href="#user-content-deploy-to-polygon-mainnet" id="user-content-deploy-to-polygon-mainnet"></a>

Ensure to save the address after deploying the Consumer Contract because this address will be used in the "[Configure Client](https://docs.phala.network/developers/bricks-and-blueprints/featured-blueprints/lensapi-oracle#step-4-configure-the-client-address)" section of Phat Bricks UI. The deployed address will also be set to the environment variable `POLYGON_CONSUMER_CONTRACT_ADDRESS`.

> **Note**: Your contract address will be different than `0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4` when verifying your contract. Make sure to get your actual contract address from the console log output after executing `npm run main-deploy`.

```sh
npm run main-deploy
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

### **(Optional) Verify Contract on Polygon Mainnet**

Ensure to update the `polygon.arguments.ts` file with the constructor arguments used to instantiate the Consumer Contract. If you add additional parameters to the constructor function then make sure to update the `polygon.arguments.ts` file.

```sh
npm run main-verify -- 0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
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

### Deploy Phat Contract to Phala Mainnet <a href="#user-content-deploy-phat-contract-to-phala-mainnet" id="user-content-deploy-phat-contract-to-phala-mainnet"></a>

For customizing your Phat Contract, Phat Contract custom configurations can be found here in [customizing-your-phat-contract.md](customizing-your-phat-contract.md "mention") to learn more before deploying to Phala Mainnet.

Now that are Phat Contract has built successfully, let's deploy to Phala Mainnet with the following command:

```shell
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn upload --mode=production --coreSettings=https://api-v2.lens.dev/
# If polkadot-account.json is in the root of project
npx @phala/fn upload --mode=production -a ./polkadot-account.json --coreSettings=https://api-v2.lens.dev/
```

Here is the expected output:

> Note: your contract IDs will vary and not be the same as the IDs below.

```shell
npx @phala/fn upload --mode=production -a ./polkadot-account.json --coreSettings=https://api-v2.lens.dev/
# ? Please enter your client RPC URL https://polygon.g.alchemy.com/v2/JLjOfWJycWFOA0kK_SJ4jLGjtXkMN1wc
# ? Please enter your consumer address 0xA4Be456Fd0d41968a52b34Cdb8Ba875F2281134a
# ? Please Enter hahaha account password [hidden]
# Creating an optimized build... done
# Compiled successfully.
#
#  17.64 KB  dist/index.js
# Connecting to the endpoint: wss://api.phala.network/ws... done
# Querying your Brick Profile contract ID... done
# Your Brick Profile contract ID: 0x4071788a8ce6fbab0cacea0cb1aa52853b5537db7955643e5010c22913c2b1dd
# Instantiating the ActionOffchainRollup contract... done
# The ActionOffchainRollup contract has been instantiated: 0x9c777c16b0a185caa895835b8f3b9e8d67be9f5e30197f71b4d32d2b8fde4b3b
# Setting up the actions... done
# 🎉 Your workflow has been added, you can check it out here: https://bricks-poc6.phala.network/workflows/0x4071788a8ce6fbab0cacea0cb1aa52853b5537db7955643e5010c22913c2b1dd/3
# Your Attestor address: 0x2b5fe2920cce2f522d69613adaa9378ba43b687d
# Your WORKFLOW_ID: 2
# ✨  Done in 73.22s.
```

### **Interact with Consumer Contract on Polygon Mainnet**

Execute Scripts to Consumer Contract on Polygon Mainnet. The Consumer Contract on Polygon Mainnet with a few actions to mimic a malformed request, successful requests, and set the attestor.

```sh
npm run main-set-attestor
# Setting attestor...
# 🚨NOTE🚨
# Make sure to set the Consumer Contract Address in your Phat Bricks 🧱 UI dashboard (https://bricks-poc6.phala.network)
# - Go to 'Configure Client' section where a text box reads 'Add Consumer Smart Contract'
# - Set value to 0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
# Done
# ✨  Done in 1.56s.
# execute push-malformed-request
npm run main-push-malformed-request
# Pushing a malformed request...
# Done
# execute push-request
npm run main-push-request
# Pushing a request...
# Done
```

### Update Phat Contract on Phala Mainnet <a href="#user-content-update-phat-contract-on-phala-mainnet" id="user-content-update-phat-contract-on-phala-mainnet"></a>

Sometimes you may have had a bug in your script or you want to test things out on the fly without deploying a whole new Phat Contract. We now allow you to update your Phat Contract easily in the command line. Now let's update the Phat Contract with the following command:

```shell
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn update --mode=production
# If polkadot-account.json is in the root of project
npx @phala/fn update --mode=production -a ./polkadot-account.json
```

```shell
npx @phala/fn update --mode=production -a ./polkadot-account.json
# ? Please Enter hahaha account password [hidden]
# Creating an optimized build... done
# Compiled successfully.
#
#   17.64 KB  dist/index.js
# Connecting to the endpoint: wss://api.phala.network/ws... done
# Querying your Brick Profile contract ID... done
# Your Brick Profile contract ID: 0x4071788a8ce6fbab0cacea0cb1aa52853b5537db7955643e5010c22913c2b1dd
# Checking your workflow settings... done
# Updating... done
# The Phat Function for workflow 1 has been updated.
# ✨  Done in 10.82s.
```

:tada: Congrats! You've now successfully updated your Phat Contract!

## Closing <a href="#user-content-closing" id="user-content-closing"></a>

Once you have stored, the deployed address of the Consumer Contract and set the value in the "Configure Client" section of the deployed Phala Oracle, you will now have a basic boilerplate example of how to connect your Polygon dApp to a LensAPI Oracle Blueprint. Execute a new requests and check if your configuration is correct like below:&#x20;

<figure><img src="https://github.com/Phala-Network/phat-contract-starter-kit/raw/main/assets/polygonscan-ex.png" alt=""><figcaption></figcaption></figure>
