---
description: >-
  Connect your subgraphs from The Graph to your on-chain dApps via Phat
  Contract.
---

# 🦋 Quick Start

## Overview

The Graph template enables you to connect to subgraph endpoints for data and utilize the data to calculate a trust score and send to a Web3 dApp on an EVM chain.

<figure><img src="../../../.gitbook/assets/The_Graph.png" alt=""><figcaption></figcaption></figure>

## Prerequisites <a href="#user-content-prerequisites" id="user-content-prerequisites"></a>

* Active Phala Profile with version `>= 1.0.1` via [Phat Contract 2.0 UI](https://bit.ly/3LHccmR)
* [Hardhat](https://bit.ly/469uyW5)
* API Key from [The Graph](https://bit.ly/subgraph-api-key)
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

<figure><img src="../../../.gitbook/assets/TheGraphFlow.jpg" alt=""><figcaption></figcaption></figure>

The diagram above displays the user journey of (1) Alice requesting a trust score for Eve from the EVM Consumer Contract. When (2) a new action request is added to the queue, (3) the Phala Network Phat Contract will pop the action off the queue and perform the off-chain work to compute a trust score.

First (4) the Phat Contract will create a `batchHttpRequest` to query 3 separate subgraph endpoints to determine if Eve has any ERC-721 NFTs, a NounsDAO NFT,  an ENS Domain, and if any accounts delegate votes to Eve on Snapshot. Once this data is returned then (5) the Phat Contract will compute a score based on some scoring criteria. You can view the code [here](https://github.com/Phala-Network/the-graph-phat-contract/blob/da510bbbefd7a4cca16bf04b090136cf0d5d7503/src/index.ts#L108). Lastly, (6) the trust score for Eve has been returned to the EVM Consumer Contract and Eve's score is set in the Consumer Contract's storage for anyone to query.

## Quick Start

Make sure you have created a Phat Contract Profile in the Phat Contract 2.0 UI and claimed some PoC6 Testnet Tokens. Instructions on creating a profile can be found [here](../create-a-phat-contract-profile.md). Also, make sure to get an [API Key from The Graph](get-an-api-key-for-the-graph.md) to avoid being rate limited by the default API Key provided by the Phala team.

To kickstart your journey with The Graph Starter Kit, you have 2 options:

1.  Create a template from the [`the-graph-starter-kit`](https://bit.ly/3PVlgHs) template repo. Click on the "**Use this template**" button in the top right corner of the webpage. Then skip the `npx @phala/fn@latest init example` step.&#x20;

    <figure><img src="https://github.com/Phala-Network/the-graph-phat-contract/raw/main/assets/TheGraphStarterKit.png" alt=""><figcaption></figcaption></figure>
2. Install the `@phala/fn` CLI tool. You can do this using your node package manager (`npm`) or use node package execute (`npx`). For the purpose of this tutorial, we will be using `npx`.

(Option 2) Once you have the CLI tool installed, you can create your first Phala Oracle template with the following command.

```
# Skip this step if chose option 1 or cloned this repo
npx @phala/fn@latest init example
```

🚨 Note 🚨

> When selecting your template, elect `the-graph-starter-kit`.

```
npx @phala/fn@latest init example
? Please select one of the templates for your "example" project: (Use arrow keys)
  phat-contract-starter-kit. The Phat Contract Starter Kit 
  lensapi-oracle-consumer-contract. Polygon Consumer Contract for LensAPI Oracle
❯ the-graph-starter-kit. The Graph Starter Kit 
```

🛑 **Not so fast!** What is it exactly that we are building? 🛑

> **What are we building?**
>
> The artifact we are compiling is a JavaScript file, serving as the Phat Contract Oracle's tailored logic. This script is designed to respond to requests initiated from the Consumer Contract. The diagram provided above offers a visual representation of this request-response interaction.
>
> **Why is it important?**
>
> In the context of the off-chain environment, on-chain Smart Contracts are inherently limited. Their functionality is confined to the information available to them within the on-chain ecosystem. This limitation underscores the critical need for a secure off-chain oracle, such as the Phat Contract. This oracle is capable of fetching and transforming data, thereby enhancing the intelligence and awareness of Smart Contracts about on-chain activities. This is a pivotal step towards bridging the gap between the on-chain and off-chain worlds, making Smart Contracts not just smart, but also informed.

After creating The Graph template repo, `cd` into the new project and install the package dependencies. You can do this with the following command:

```
npm install
```

Now, build the default Phat Contract script with this command:

```
npx @phala/fn build
```

To simulate the expected result locally, run the Phat Contract script now with this command:

```
npx @phala/fn run dist/index.js -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000de1683287529b9b4c3132af8aad210644b259cfd '{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
```

Finally, run the local end-to-end tests with this command. Here we will simulate locally the interaction between the Phat Contract and the Consumer Contract with hardhat.

```
npm run localhost-test 
```

🥳 **Congratulations!**

You have successfully completed the quick start. For the next steps, you will learn how to deploy The Graph Phat Contract to PoC6 Testnet & Phala Mainnet, and also deploy the EVM Consumer Contract on the target EVM chain. Then you will connect to the Phat Contract to the Consumer Contract for the EVM testnet chain to start testing the request-response model live.
