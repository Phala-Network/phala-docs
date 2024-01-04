---
description: >-
  Next step in requesting data from your deployed LensAPI Oracle. Deploy a
  Polygon Consumer Smart Contract.
---

# 🧑🚀 Polygon Consumer Contract for LensAPI Oracle

## Overview

This project represents a basic Polygon Consumer Contract that is compatible with a deployed LensAPI Oracle via [Phat Contract 2.0 UI](https://bricks.phala.network). This tutorial assumes the developer is familiar with executing commands in a terminal.

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

## Prerequisites

* Active deployed LensAPI Oracle Blueprint via [Phat Bricks](https://bricks.phala.network)
  * Follow steps to deploy [here](broken-reference)
* Address of the "[Oracle Endpoint](https://docs.phala.network/developers/bricks-and-blueprints/featured-blueprints/lensapi-oracle#step-3-connect-your-smart-contract-to-the-oracle)" in deployed LensAPI Oracle
* [Hardhat](https://hardhat.org)
* For Polygon Mainnet deployments:
  * Polygonscan API Key that can be generated on [polygonscan](https://polygonscan.com)
* RPC Endpoint for Polygon Mainnet & Mumbai Testnet
  * [Alchemy](https://alchemy.com) - This repo example uses Alchemy's API Key.
  * [Infura](https://infura.io)
  * Personal RPC Node
* Test Tokens at [Phala Faucet](https://bit.ly/3Tomopi)

### Environment Variables: <a href="#user-content-environment-variables" id="user-content-environment-variables"></a>

Check out the environment variables here in [.env.local](https://github.com/Phala-Network/lensapi-oracle-consumer-contract/blob/refactor/.env.local) file.

## Getting Started <a href="#user-content-getting-started" id="user-content-getting-started"></a>

> Note: If you cloned this repo or created a template, skip to [Create a Phala Profile](https://github.com/Phala-Network/lensapi-oracle-consumer-contract/blob/refactor/LENSAPI\_ORACLE.md#create-a-bricks-profile)

First you will need to install the `@phala/fn` CLI tool using your node package manager (`npm`) or use node package execute (`npx`). In this tutorial we use `npx`.

Now create your first template with the CLI tool command:

```sh
npx @phala/fn init example
```

We currently have only one template. Just press enter to see something similar to the example below:

```sh
npx @phala/fn init example
# ? Please select one of the templates for your "example" project: lensapi-oracle-consumer-contract. Polygon Consumer Contract for LensAPI Oracle
# Downloading the template: https://github.com/Phala-Network/lensapi-oracle-consumer-contract... ✔
# The project is created in ~/Projects/Phala/example
```

`cd` into the newly created template and `ls` the directory which will look similar to below.

```sh
cd example
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

### Create a Bricks Profile <a href="#user-content-create-a-bricks-profile" id="user-content-create-a-bricks-profile"></a>

This step requires you to have a Polkadot account. You can get an account from one of the following:

* [Polkadot.js Wallet Extension](https://polkadot.js.org/extension/)
* [Talisman Wallet](https://www.talisman.xyz/)
* [SubWallet](https://www.subwallet.app/) (**Support for iOS/Android**)

First, create your Bricks Profile account on the [Phala PoC6 Testnet](https://bricks-poc5.phala.network/) or [Phala Mainnet](https://bricks.phala.network/). Here is a quick 1 minute [YouTube video](https://youtu.be/z1MR48NYtYc) on setting up from scratch.

Here is what your Bricks Profile account overview should look like:&#x20;

<figure><img src="https://github.com/Phala-Network/lensapi-oracle-consumer-contract/raw/refactor/assets/BricksProfileCheck.png" alt=""><figcaption></figcaption></figure>

After creating your Bricks Profile, set your `.env` variable `POLKADOT_WALLET_SURI` to the mnemonic phrase from generating the new Polkadot Account.

Here is a screenshot of how to set `POLKADOT_WALLET_SURI`:&#x20;

<figure><img src="https://github.com/Phala-Network/lensapi-oracle-consumer-contract/raw/refactor/assets/PolkadotAccountSuri.png" alt=""><figcaption></figcaption></figure>

\
Testing Locally
---------------

### Test Default Function Locally <a href="#user-content-test-default-function-locally" id="user-content-test-default-function-locally"></a>

With a template created and a basic default function example ready to test, let’s step through the process of preparing your repo to execute the test locally.

First step is to install the package dependencies with the following command:

```
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

Now that the package dependencies are installed, lets build the default function which is located in `./src/index.ts`.

<details>

<summary>View file <code>./src/index.ts</code></summary>

```typescript
// *** YOU ARE LIMITED TO THE FOLLOWING IMPORTS TO BUILD YOUR PHAT CONTRACT     ***
// *** ADDING ANY IMPORTS WILL RESULT IN ERRORS & UPLOADING YOUR CODE TO PHALA  ***
// *** NETWORK WILL FAIL. IF YOU WANT TO KNOW MORE, JOIN OUR DISCORD TO SPEAK   ***
// *** WITH THE PHALA TEAM AT https://discord.gg/5HfmWQNX THANK YOU             ***
// *** FOR DOCS ON HOW TO CUSTOMIZE YOUR PC 2.0 https://bit.ly/customize-pc-2-0 ***
import "@phala/pink-env";
import {decodeAbiParameters, encodeAbiParameters, parseAbiParameters} from "viem";

type HexString = `0x${string}`;
const encodeReplyAbiParams = 'uint respType, uint id, uint256 data';
const decodeRequestAbiParams = 'uint id, string reqData';

function encodeReply(abiParams: string, reply: any): HexString {
  return encodeAbiParameters(parseAbiParameters(abiParams),
      reply
  );
}

function decodeRequest(abiParams: string, request: HexString): any {
  return decodeAbiParameters(parseAbiParameters(abiParams),
      request
  );
}

// Defined in OracleConsumerContract.sol
const TYPE_RESPONSE = 0;
const TYPE_ERROR = 2;

enum Error {
  BadRequestString = "BadRequestString",
  FailedToFetchData = "FailedToFetchData",
  FailedToDecode = "FailedToDecode",
  MalformedRequest = "MalformedRequest",
}

function errorToCode(error: Error): number {
  switch (error) {
    case Error.BadRequestString:
      return 1;
    case Error.FailedToFetchData:
      return 2;
    case Error.FailedToDecode:
      return 3;
    case Error.MalformedRequest:
      return 4;
    default:
      return 0;
  }
}

function stringToHex(str: string): string {
  var hex = "";
  for (var i = 0; i < str.length; i++) {
    hex += str.charCodeAt(i).toString(16);
  }
  return "0x" + hex;
}

function fetchApiStats(apiUrl: string, requestStr: string): any {
  let headers = {
    "Content-Type": "application/json",
    "User-Agent": "phat-contract",
  };
  let query = JSON.stringify({
    query: `
      query Profile {
        profile(request: { forProfileId: "${requestStr}" }) {
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
    `,
  });
  let body = stringToHex(query);
  //
  // In Phat Contract runtime, we not support async/await, you need use `pink.batchHttpRequest` to
  // send http request. The Phat Contract will return an array of response.
  //
  let response = pink.batchHttpRequest(
    [
      {
        url: apiUrl,
        method: "POST",
        headers,
        body,
        returnTextBody: true,
      },
    ],
    10000 // Param for timeout in milliseconds. Your Phat Contract script has a timeout of 10 seconds
  )[0]; // Notice the [0]. This is important bc the `pink.batchHttpRequest` function expects an array of up to 5 HTTP requests.
  if (response.statusCode !== 200) {
    console.log(
      `Fail to read Lens api with status code: ${response.statusCode}, error: ${
        response.error || response.body
      }}`
    );
    throw Error.FailedToFetchData;
  }
  let respBody = response.body;
  if (typeof respBody !== "string") {
    throw Error.FailedToDecode;
  }
  return JSON.parse(respBody);
}

//
// Here is what you need to implemented for Phat Contract, you can customize your logic with
// JavaScript here.
//
// The Phat Contract will be called with two parameters:
//
// - request: The raw payload from the contract call `request` (check the `request` function in TestLensApiConsumerConract.sol).
//            In this example, it's a tuple of two elements: [requestId, profileId]
// - secrets: The custom secrets you set with the `config_core` function of the Action Offchain Rollup Phat Contract. In
//            this example, it just a simple text of the lens api url prefix. For more information on secrets, checkout the SECRETS.md file.
//
// Your returns value MUST be a hex string, and it will send to your contract directly. Check the `_onMessageReceived` function in
// OracleConsumerContract.sol for more details. We suggest a tuple of three elements: [successOrNotFlag, requestId, data] as
// the return value.
//
export default function main(request: HexString, secrets: string): HexString {
  console.log(`handle req: ${request}`);
  // Uncomment to debug the `secrets` passed in from the Phat Contract UI configuration.
  // console.log(`secrets: ${secrets}`);
  let requestId, encodedReqStr;
  try {
    [requestId, encodedReqStr] = decodeRequest(decodeRequestAbiParams, request);
    console.log(`[${requestId}]: ${encodedReqStr}`);
  } catch (error) {
    console.info("Malformed request received");
    return encodeReply(encodeReplyAbiParams, [BigInt(TYPE_ERROR), 0n, BigInt(errorToCode(error as Error))]);
  }
  console.log(`Request received for profile ${encodedReqStr}`);
  try {
    const respData = fetchApiStats(secrets, encodedReqStr);
    let stats = respData.data.profile.stats.posts;
    console.log("response:", [TYPE_RESPONSE, requestId, stats]);
    return encodeReply(encodeReplyAbiParams, [TYPE_RESPONSE, requestId, stats]);
  } catch (error) {
    if (error === Error.FailedToFetchData) {
      throw error;
    } else {
      // otherwise tell client we cannot process it
      console.log("error:", [TYPE_ERROR, requestId, error]);
      return encodeReply(encodeReplyAbiParams, [TYPE_ERROR, requestId, errorToCode(error as Error)]);
    }
  }
}

```

</details>

Build the default function with this command:

```sh
npx @phala/fn build
```

You will see output similar to the example below. and a file in `./dist/index.js` will be generated.

```sh
npx @phala/fn build
# Creating an optimized build... done
# Compiled successfully.
#
#   17.66 KB  dist/index.js
# ✨  Done in 3.48s.
```

With our default function built, we can run some initial tests. First test will be simple.

```sh
npx @phala/fn run dist/index.js
```

It was expected for it to fail like this:

```sh
npx @phala/fn run dist/index.js
# handle req: undefined
# Malformed request received
# {"output":"0x000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"}
# ✨  Done in 0.96s.
```

Notice that the test fails and reports that a `Malformed request received` was emitted and the request was `undefined`. This is expected as you will need to define the parameters by adding a `-a abi.encode(requestId, profileId) https://api-v2-mumbai-live.lens.dev` to your command.

To simulate the expected result locally, run the Phala Oracle function now with this command:

```sh
npx @phala/fn run dist/index.js -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000 https://api-v2-mumbai-live.lens.dev
```

> **What are the ingredients for the `npx @phala/fn run` command?**
>
> Our Phat Contract script, now fully constructed, is ready for a trial run. This simulation mirrors the live script's operation when deployed on the Phala Network.
>
> The command's first parameter is a HexString, representing a tuple of types `[uint, bytes]`. This serves as the entry function. The second parameter is a `string`, embodying the configurable secrets fed into the main function.
>
> The `Coders.decode` function deciphers these parameters, yielding the decoded `requestId` and `encodedReqStr`. These decoded elements then become the raw material for the rest of the custom logic within the script.
>
> ```solidity
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
npx @phala/fn run dist/index.js -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000 https://api-v2-mumbai-live.lens.dev/

> lensapi-oracle-consumer-contract@0.0.1 run-function
> phat-fn run dist/index.js -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000 https://api-v2-mumbai-live.lens.dev/

handle req: 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000
[1]: 0x01
Request received for profile 0x01
response: 0,1,14
{"output":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000e"}
```

We have now successfully tested the default function and ran a test to verify the function returns a response as expected.

### Testing Default Function with Local Hardhat Node <a href="#user-content-testing-default-function-with-local-hardhat-node" id="user-content-testing-default-function-with-local-hardhat-node"></a>

Previously we showed how to test the default function locally without a running node, but we can also run two other tests.

1. Run the default mocha e2e tests.
2. Run local hardhat node and watch the requests that are pushed and see how the function transforms the data.

### **Run the default mocha e2e tests**

Lets’s start with the first test case.

> Note: You will need to ensure you configure your local vars `POLYGON_RPC_URL` and `MUMBAI_RPC_URL` `.env` file. You can do this with `cp .env.local .env` then edit the `.env` with your information.

<details>

<summary>Expected error if <code>.env</code> not configured.</summary>

```sh
npm run localhost-test
# Error HH8: There's one or more errors in your config file:

#  * Invalid value undefined for HardhatConfig.networks.polygon.url - Expected a value of type string.
#  * Invalid value undefined for HardhatConfig.networks.mumbai.url - Expected a value of type string.
  
# To learn more about Hardhat's configuration, please go to https://hardhat.org/config/

# For more info go to https://hardhat.org/HH8 or run Hardhat with --show-stack-traces
# error Command failed with exit code 1.
```

</details>

```sh
npm run localhost-test
```

You will now see that all test cases have passed.

```sh
npm run localhost-test
# Compiled 14 Solidity files successfully
#
#  TestLensApiConsumerContract
#    ✔ Push and receive message (1664ms)
#
#  1 passing (2s)
#
# ✨  Done in 3.29s.
```

This is how the e2e mocha test will look like. You can customize this file at `./test/TestLensApiConsumerContract.ts`.

<details>

<summary>View file <code>TestLensApiConsumerContract.ts</code></summary>

```typescript
import { expect } from "chai";
import { type Contract, type Event } from "ethers";
import { ethers } from "hardhat";
import { execSync } from "child_process";

async function waitForResponse(consumer: Contract, event: Event) {
  const [, data] = event.args!;
  // Run Phat Function
  const result = execSync(`phat-fn run --json dist/index.js -a ${data} https://api-mumbai.lens.dev/`).toString();
  const json = JSON.parse(result);
  const action = ethers.utils.hexlify(ethers.utils.concat([
    new Uint8Array([0]),
    json.output,
  ]));
  // Make a response
  const tx = await consumer.rollupU256CondEq(
    // cond
    [],
    [],
    // updates
    [],
    [],
    // actions
    [action],
  );
  const receipt = await tx.wait();
  return receipt.events;
}

describe("TestLensApiConsumerContract", function () {
  it("Push and receive message", async function () {
    // Deploy the contract
    const [deployer] = await ethers.getSigners();
    const TestLensApiConsumerContract = await ethers.getContractFactory("TestLensApiConsumerContract");
    const consumer = await TestLensApiConsumerContract.deploy(deployer.address);

    // Make a request
    const profileId = "0x01";
    const tx = await consumer.request(profileId);
    const receipt = await tx.wait();
    const reqEvents = receipt.events;
    expect(reqEvents![0]).to.have.property("event", "MessageQueued");

    // Wait for Phat Function response
    const respEvents = await waitForResponse(consumer, reqEvents![0])

    // Check response data
    expect(respEvents[0]).to.have.property("event", "ResponseReceived");
    const [reqId, input, value] = respEvents[0].args;
    expect(ethers.BigNumber.isBigNumber(reqId)).to.be.true;
    expect(input).to.equal(profileId);
    expect(ethers.BigNumber.isBigNumber(value)).to.be.true;
  });
});
```

</details>

**Run local hardhat node and watch the requests that are pushed and see how the function transforms the data**

First we will start a local hardhat node.

```
npm run localhost-node
```

<details>

<summary>Example output</summary>

```sh
npm run localhost-node
# Started HTTP and WebSocket JSON-RPC server at http://127.0.0.1:8545/

# Accounts
# ========

# WARNING: These accounts, and their private keys, are publicly known.
# Any funds sent to them on Mainnet or any other live network WILL BE LOST.
```

</details>

With our hardhat node running locally, we can now deploy the `LensApiConsumerContract.sol` contract to the local hardhat network.

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
npx @phala/fn watch 0x0165878A594ca255338adfa4d48449f69242Eb8F artifacts/contracts/TestLensApiConsumerContract.sol/TestLensApiConsumerContract.json dist/index.js -a https://api-mumbai.lens.dev/
```

```sh
npx @phala/fn watch 0x0165878A594ca255338adfa4d48449f69242Eb8F artifacts/contracts/TestLensApiConsumerContract.sol/TestLensApiConsumerContract.json dist/index.js -a https://api-v2-mumbai-live.lens.dev/
# $ phat-fn watch 0x0165878A594ca255338adfa4d48449f69242Eb8F artifacts/contracts/TestLensApiConsumerContract.sol/TestLensApiConsumerContract.json dist/index.js -a https://api-v2-mumbai-live.lens.dev/
# Listening for TestLensApiConsumerContract MessageQueued events...
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
#  value: BigNumber { value: "3361" }
# }
# ✨  Done in 4.99s.
```

If we look back at the listener tab, we will see output has been appended.

```sh
Listening for TestLensApiConsumerContract MessageQueued events...
Received event [MessageQueued]: {
  tail: 0n,
  data: '0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000'
}
handle req: 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000
Request received for profile 0x01
response: 0,1,14
JS Execution output: 0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000c9
```

## Deployment

Now that you have the prerequisites to deploy a Polygon Consumer Contract on Polygon, lets begin with some initials tasks.

### Install Dependencies & Compile Contracts

```shell
# install dependencies
$ npm install

# compile contracts
$ npm run compile
```

### &#x20;Deploy to Polygon Mumbai Testnet <a href="#user-content-deploy-to-polygon-mumbai-testnet" id="user-content-deploy-to-polygon-mumbai-testnet"></a>

With the contracts successfully compiled, now we can begin deploying first to Polygon Mumbai Testnet. If you have not gotten `MATIC` for Mumbai Testnet then get `MATIC` from a [faucet](https://mumbaifaucet.com/). Ensure to save the address after deploying the Consumer Contract because this address will be use in the "[Configure Client](https://docs.phala.network/developers/bricks-and-blueprints/featured-blueprints/lensapi-oracle#step-4-configure-the-client-address)" section of Phat Bricks UI. The deployed address will also be set to the environment variable [`MUMBAI_CONSUMER_CONTRACT_ADDRESS`](https://github.com/Phala-Network/lensapi-oracle-consumer-contract/blob/refactor/.env.local).

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

Ensure to update the [`mumbai.arguments.ts`](https://github.com/Phala-Network/lensapi-oracle-consumer-contract/blob/refactor/mumbai.arguments.ts) file with the constructor arguments used to instantiate the Consumer Contract. If you add additional parameters to the constructor function then make sure to update the `mumbai.arguments.ts` file.

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
# contracts/TestLensApiConsumerContract.sol:TestLensApiConsumerContract at 0x090E8fDC571d65459569BC87992C1026121DB955
# for verification on the block explorer. Waiting for verification result...
#
# Successfully verified contract TestLensApiConsumerContract on Etherscan.
# https://mumbai.polygonscan.com/address/0x090E8fDC571d65459569BC87992C1026121DB955#code
# ✨  Done in 5.91s.
```

### Deploy Phat Contract to PoC6 Testnet <a href="#user-content-deploy-phat-contract-to-poc5-testnet" id="user-content-deploy-phat-contract-to-poc5-testnet"></a>

For customizing your Phat Contract, checkout Phat Contract custom configurations in [JS\_API\_DOC.md](https://github.com/Phala-Network/lensapi-oracle-consumer-contract/blob/refactor/src/JS\_API\_DOC.md) to learn more before deploying to PoC6 testnet.

Now that are Phat Contract has built successfully, let's deploy to Phala PoC6 Testnet with the following command:

```sh
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn upload --coreSettings=https://api-v2-mumbai-live.lens.dev/
# If polkadot-account.json is in the root of project
npx @phala/fn upload --coreSettings=https://api-v2-mumbai-live.lens.dev/ -a ./polkadot-account.json
```

Here is the expected output:

> Note: your contract IDs will vary and not be the same as the IDs below.

```sh
npx @phala/fn upload --coreSettings=https://api-v2-mumbai-live.lens.dev/ -a ./polkadot-account.json
# ? Please enter your client RPC URL https://polygon-mumbai.g.alchemy.com/v2/JLjOfWJycWFOA0kK_SJ4jLGjtXkMN1wc
# ? Please enter your consumer address 0xA4Be456Fd0d41968a52b34Cdb8Ba875F2281134a
# ? Please Enter hahaha account password [hidden]
# Creating an optimized build... done
# Compiled successfully.
#
#  17.64 KB  dist/index.js
# Connecting to the endpoint: wss://poc6.phala.network/ws... ⡿
# (node:25497) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
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

Go to the [PoC6 Testnet Bricks UI](https://bricks-poc5.phala.network/) Dashboard and you can see your newly deployed Phat Contract.&#x20;

<figure><img src="https://github.com/Phala-Network/lensapi-oracle-consumer-contract/raw/refactor/assets/Function-added.png" alt=""><figcaption></figcaption></figure>

### **Interact with Consumer Contract on Polygon Mumbai**

Test Consumer Contract on Mumbai with a few tests to check for malformed requests failures, successful requests, and set the attestor.

**Please make sure your have set your attestor address in .env file `MUMBAI_PHALA_ORACLE_ATTESTOR`**

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

```sh
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn update
# If polkadot-account.json is in the root of project
npx @phala/fn update -a ./polkadot-account.json
```

```sh
npx @phala/fn update -a ./polkadot-account.json
# ? Please Enter hahaha account password [hidden]
# Creating an optimized build... done
# Compiled successfully.
#
#   17.64 KB  dist/index.js
# Connecting to the endpoint: wss://poc6.phala.network/ws... ⡿
# (node:25392) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
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
# contracts/TestLensApiConsumerContract.sol.sol:TestLensApiConsumerContract.sol.sol at 0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
# for verification on the block explorer. Waiting for verification result...
#
# Successfully verified contract TestLensApiConsumerContract.sol on Etherscan.
# https://polygonscan.com/address/0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4#code
# Done in 8.88s.
```

### Deploy Phat Contract to Phala Mainnet <a href="#user-content-deploy-phat-contract-to-phala-mainnet" id="user-content-deploy-phat-contract-to-phala-mainnet"></a>

For customizing your Phat Contract, Phat Contract custom configurations can be found here in [JS\_API\_DOC.md](https://github.com/Phala-Network/lensapi-oracle-consumer-contract/blob/main/src/JS\_API\_DOC.md) to learn more before deploying to Phala Mainnet.

Now that are Phat Contract has built successfully, let's deploy to Phala Mainnet with the following command:

```sh
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn upload --mode=production --coreSettings=https://api-v2.lens.dev/
# If polkadot-account.json is in the root of project
npx @phala/fn upload --mode=production --coreSettings=https://api-v2.lens.dev/ -a ./polkadot-account.json
```

Here is the expected output:

> Note: your contract IDs will vary and not be the same as the IDs below.

```sh
npx @phala/fn upload --mode=production --coreSettings=https://api-v2.lens.dev/ -a ./polkadot-account.json
# ? Please enter your client RPC URL https://polygon.g.alchemy.com/v2/JLjOfWJycWFOA0kK_SJ4jLGjtXkMN1wc
# ? Please enter your consumer address 0xA4Be456Fd0d41968a52b34Cdb8Ba875F2281134a
# ? Please Enter hahaha account password [hidden]
# Creating an optimized build... done
# Compiled successfully.
#
#  17.64 KB  dist/index.js
# Connecting to the endpoint: wss://api.phala.network/ws... ⡿
# (node:25497) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
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

Sometimes you may have had a bug in your script or you want to test things out on the fly without deploying a whole new Phat Contract. We now allow you to update your Phat Contract easily in the command-line. Now let's update the Phat Contract with the following command:

```sh
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn update --mode=production
# If polkadot-account.json is in the root of project
npx @phala/fn update --mode=production -a ./polkadot-account.json
```

```sh
npx @phala/fn update --mode=production -a ./polkadot-account.json
# ? Please Enter hahaha account password [hidden]
# Creating an optimized build... done
# Compiled successfully.
#
#   17.64 KB  dist/index.js
# Connecting to the endpoint: wss://api.phala.network/ws... ⡿
# (node:25392) ExperimentalWarning: buffer.Blob is an experimental feature. This feature could change at any time
# Connecting to the endpoint: wss://api.phala.network/ws... done
# Querying your Brick Profile contract ID... done
# Your Brick Profile contract ID: 0x4071788a8ce6fbab0cacea0cb1aa52853b5537db7955643e5010c22913c2b1dd
# Checking your workflow settings... done
# Updating... done
# The Phat Function for workflow 1 has been updated.
# ✨  Done in 10.82s.
```

## Closing

Once you have stored, the deployed address of the Consumer Contract and set the value in the "Configure Client" section of the deployed LensAPI Oracle, you will now have a basic boilerplate example of how to connect your Polygon dApp to a LensAPI Oracle Blueprint. Execute a new requests and check if your configuration is correct like below:

<figure><img src="../../../.gitbook/assets/polygonscan-ex.png" alt=""><figcaption></figcaption></figure>
