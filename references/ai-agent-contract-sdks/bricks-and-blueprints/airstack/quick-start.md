---
description: >-
  Request an account’s data from Airstack’s API to compute trust score and send
  to your Web3 dApp on-chain.
---

# 🛩️ Quick Start

## Overview

The Airstack template allows for users to request data from Airstack’s API to compute a trust/risk score and send to an on-chain consumer contract.

<figure><img src="../../../../.gitbook/assets/AirStack.png" alt=""><figcaption></figcaption></figure>

## Prerequisites <a href="#user-content-prerequisites" id="user-content-prerequisites"></a>

* Active Phala Profile with version `>= 1.0.1` via [Phat Contract 2.0 UI](https://bit.ly/3LHccmR)
* [Hardhat](https://bit.ly/469uyW5)
* API Key from [Airstack](https://bit.ly/airstack-api-key)
* For EVM Mainnet deployments:
  * Ex: Polygonscan API Key that can be generated on [polygonscan](https://bit.ly/3rBkypp)
* RPC Endpoint for EVM Chain Mainnet & EVM Chain Testnet
  * [Alchemy](https://bit.ly/46uObaH) - This repo example uses Alchemy's API Key.
  * [Infura](https://bit.ly/3PXXCtN)
  * Personal RPC Node (Ex. [ProjectPi](https://bit.ly/3RGf7QS))
* Polkadot Account for Phala PoC6 Testnet and Mainnet deployment
  * [Phala Faucet](https://bit.ly/3Tomopi)
* Node >= 18.x

## How it Works

<figure><img src="../../../../.gitbook/assets/AirstackUserJourney.png" alt=""><figcaption></figcaption></figure>

The diagram above displays the user journey of (1) Alice requesting a trust score for Eve from the EVM Consumer Contract. When (2) a new action request is added to the queue, (3) the Phala Network Phat Contract will pop the action off the queue and perform the off-chain work to compute a trust score.

First (4) the Phat Contract will create a `batchHttpRequest` to query the Airstack API endpoint to determine if Alice has interacted on-chain with Eve before through on-chain TXs, Web3 Social, or attended any IRL events by having the same POAPs. Once this data is returned then (5) the Phat Contract will compute a score based on some scoring criteria. You can view the code [here](https://github.com/Phala-Network/airstack-phat-contract/blob/2dc5aa54e1d0c313762fd4dfed79554d6eeddbf0/src/index.ts#L108). Lastly, (6) the trust score for Eve has been returned to the EVM Consumer Contract and Eve's score is set in the Consumer Contract's storage in a mapping of a mapping to show Alice's requested trust score for Eve.

## Quick Start

Make sure you have created a Phat Contract Profile in the Phat Contract 2.0 UI and claimed some PoC6 Testnet Tokens. Instructions on creating a profile can be found [here](broken-reference). Also, make sure to get an [API Key from Airstack](broken-reference) to avoid being rate limited by the default API Key provided by the Phala team.

To kickstart your journey with the Airstack Starter Kit, install the `@phala/fn` CLI tool.&#x20;

You can do this using your node package manager (`npm`) or use node package execute (`npx`). For the purpose of this tutorial, we will be using `npx`.

Once you have the CLI tool installed, you can create your first Phala Oracle template with the following command.

```
npx @phala/fn@latest init example
```

🚨 Note 🚨

> When selecting your template, elect `airstack-phat-contract`.

```bash
npx @phala/fn@latest init example
? Please select one of the templates for your "example" project: 
  phat-contract-starter-kit: Send data from any API to your smart contract with Javascript. 
  lensapi-oracle-consumer-contract: Send data from Lens API to your smart contract to empower your Web3 Social dApp. 
  vrf-oracle: TEE-guarded Verifiable Random Function template to bring randomness to your smart contract. 
❯ airstack-phat-contract: Request an account’s data from Airstack’s API to compute trust score and send to your Web3 dApp on-chain. 
  thegraph-phat-contract: Connect your subgraphs from The Graph to your on-chain dApps via Phat Contract.  
```

🛑 **Not so fast!** What is it exactly that we are building? 🛑

> **What are we building?**
>
> The artifact we are compiling is a JavaScript file, serving as the Phat Contract Oracle's tailored logic. This script is designed to respond to requests initiated from the Consumer Contract. The diagram provided above offers a visual representation of this request-response interaction.
>
> **Why is it important?**
>
> In the context of the off-chain environment, on-chain Smart Contracts are inherently limited. Their functionality is confined to the information available to them within the on-chain ecosystem. This limitation underscores the critical need for a secure off-chain oracle, such as the Phat Contract. This oracle is capable of fetching and transforming data, thereby enhancing the intelligence and awareness of Smart Contracts about on-chain activities. This is a pivotal step towards bridging the gap between the on-chain and off-chain worlds, making Smart Contracts not just smart, but also informed.

After creating the Airstack template repo, `cd` into the new project and install the package dependencies. You can do this with the following command:

```
npm install
```

Now, build the default Phat Contract script with this command:

```
npx @phala/fn build
```

To simulate the expected result locally, run the Phat Contract script now with the `npx @phala/fn run`command to test the expected output when passing an encoded hexstring and the `secrets` into the `main` function of the Phat Contract. This is helpful to test locally quick to understand the functionality of your compiled Phat Contract.

> Go to [https://playground.ethers.org](https://playground.ethers.org) to `decode` and `encode` the hexstring you want to pass into your Phat Contract `main` function.
>
> In this example, the hexstring  `0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000964256674e42d61f0ff84097e28f65311786ccb000000000000000000000000eaf55242a90bb3289db8184772b0b98562053559` represents types `uint id` and `address requester` and `address target`&#x20;
>
> Here is what you will enter in the playground:
>
> * `utils.defaultAbiCoder.decode(['uint id', 'address requester', 'address target'], '0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000964256674e42d61f0ff84097e28f65311786ccb000000000000000000000000eaf55242a90bb3289db8184772b0b98562053559')`
> * `[ BigNumber { value: "5" }, "0xeaf55242a90bb3289dB8184772b0B98562053559", "0x624Fef3390A244a834f19b3dBfddC28939530c17", id: BigNumber { value: "5" }, requester: "0xeaf55242a90bb3289dB8184772b0B98562053559", target: "0x624Fef3390A244a834f19b3dBfddC28939530c17" ]`
>
> You can easily validate this by encoding the types and data with the `utils.defaultAbiCoder.encode()` function like below.
>
> * `utils.defaultAbiCoder.encode(['uint id', 'address requester', 'address target'], [1, "0xeaf55242a90bb3289dB8184772b0B98562053559", "0x624Fef3390A244a834f19b3dBfddC28939530c17"])`
> * `"0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000964256674e42d61f0ff84097e28f65311786ccb000000000000000000000000eaf55242a90bb3289db8184772b0b98562053559"`

```
npx @phala/fn run dist/index.js -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000964256674e42d61f0ff84097e28f65311786ccb000000000000000000000000eaf55242a90bb3289db8184772b0b98562053559 '{"apiUrl": "https://api.airstack.xyz/gql", "apiKey": "3a41775a358a4cb99ca9a29c1f6fc486"}'
```

Finally, run the local end-to-end tests with this command. Here we will simulate locally the interaction between the Phat Contract and the Consumer Contract with hardhat.

```
npm run localhost-test 
```

🥳 **Congratulations!**

You have successfully completed the quick start. For the next steps, you will learn how to deploythe Airstack Phat Contract to PoC6 Testnet & Phala Mainnet, and also deploy the EVM Consumer Contract on the target EVM chain. Then you will connect to the Phat Contract to the Consumer Contract for the EVM testnet chain to start testing the request-response model live.
