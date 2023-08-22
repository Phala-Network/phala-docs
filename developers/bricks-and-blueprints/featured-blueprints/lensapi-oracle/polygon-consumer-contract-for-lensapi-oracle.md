---
description: >-
  Next step in requesting data from your deployed LensAPI Oracle. Deploy a
  Polygon Consumer Smart Contract.
---

# Polygon Consumer Contract for LensAPI Oracle

## Overview

This project represents a basic Polygon Consumer Contract that is compatible with a deployed LensAPI Oracle via [Phat Bricks UI](https://bricks.phala.network). This tutorial assumes the developer is familiar with executing commands in a terminal.

## Prerequisites

* Active deployed LensAPI Oracle Blueprint via [Phat Bricks](https://bricks.phala.network)
  * Follow steps to deploy [here](./)
* Address of the "[Oracle Endpoint](https://docs.phala.network/developers/bricks-and-blueprints/featured-blueprints/lensapi-oracle#step-3-connect-your-smart-contract-to-the-oracle)" in deployed LensAPI Oracle
* [Hardhat](https://hardhat.org)
* For Polygon Mainnet deployments:
  * Polygonscan API Key that can be generated on [polygonscan](https://polygonscan.com)
* RPC Endpoint for Polygon Mainnet & Mumbai Testnet
  * [Alchemy](https://alchemy.com) - This repo example uses Alchemy's API Key.
  * [Infura](https://infura.io)
  * Personal RPC Node

## Getting Started

### Start Your Own Consumer Contract Template

{% tabs %}
{% tab title="Git" %}
Clone the repo.

```sh
git clone git@github.com:Phala-Network/lensapi-oracle-consumer-contract.git
```
{% endtab %}

{% tab title="GitHub UI" %}
Go to the GitHub [repo](https://github.com/Phala-Network/lensapi-oracle-consumer-contract/tree/main) and click the "**Use this template**" button.

<figure><img src="../../../../.gitbook/assets/github-use-this-template.png" alt=""><figcaption><p>Click "Use this template"</p></figcaption></figure>
{% endtab %}
{% endtabs %}

> **Note** The rest of the tutorial will assume you have cloned your git repo locally and are using a terminal or IDE.

First you will need to run `cp .env.local .env` to copy over the local environment variables.

#### Environment Variables:

* `MUMBAI_RPC_URL` - JSON-RPC URL with an API key for RPC endpoints on Polygon Mumbai Testnet (e.g. [Alchemy](https://alchemy.com) `https://polygon-mumbai.g.alchemy.com/v2/<api-key>`, [Infura](https://infura.io) `https://polygon.infura.io/v3/<api-key>`).
* `POLYGON_RPC_URL` - JSON-RPC URL with an API key for RPC endpoints on Polygon Mainnet (e.g. [Alchemy](https://alchemy.com) `https://polygon.g.alchemy.com/v2/<api-key>`, [Infura](https://infura.io) `https://polygon.infura.io/v3/<api-key>`).
* `DEPLOYER_PRIVATE_KEY` - Secret key for the deployer account that will deploy the Consumer Contract on either Polygon Mainnet or Polygon Mumbai Testnet.
* `POLYGONSCAN_API_KEY` - Polygonscan API Key that can be generated at [polygonscan](https://polygonscan.com).
* `MUMBAI_LENSAPI_ORACLE_ENDPOINT` - LensAPI Oracle Endpoint Address that can be found in the dashboard of the deployed LensAPI Oracle Blueprint at [Phala PoC5 Testnet](https://bricks-poc5.phala.network) for Polygon Mumbai Testnet.
* `POLYGON_LENSAPI_ORACLE_ENDPOINT` - LensAPI Oracle Endpoint Address that can be found in the dashboard of the deployed LensAPI Oracle Blueprint at [Phala Mainnet](https://bricks.phala.network) for Polygon Mainnet.

### Deployment

Now that you have the prerequisites to deploy a Polygon Consumer Contract on Polygon, lets begin with some initials tasks.

#### Install Dependencies & Compile Contracts

```shell
# install dependencies
$ yarn

# compile contracts
$ yarn compile
```

#### Deploy to Polygon Mumbai Testnet

With the contracts successfully compiled, now we can begin deploying first to Polygon Mumbai Testnet. If you have not gotten `MATIC` for Mumbai Testnet then get `MATIC` from a [faucet](https://mumbaifaucet.com/). Ensure to save the address after deploying the Consumer Contract because this address will be use in the "[Configure Client](./#step-4-configure-the-client-address)" section of Phat Bricks UI. The deployed address will also be set to the environment variable `MUMBAI_CONSUMER_CONTRACT_ADDRESS`.

```shell
# deploy contracts to testnet mumbai
$ yarn test-deploy
# Deployed { consumer: '0x93891cb936B62806300aC687e12d112813b483C1' }

# Check our example deployment in <https://mumbai.polygonscan.com/address/0x93891cb936B62806300aC687e12d112813b483C1>
```

**Verify Contract on Polygon Mumbai Testnet**

Ensure to update the `mumbai.arguments.ts` file with the constructor arguments used to instantiate the Consumer Contract. If you add additional parameters to the constructor function then make sure to update the `mumbai.arguments.ts` file.

> **Note**: Your contract address will be different than `0x93891cb936B62806300aC687e12d112813b483C1` when verifying your contract. Make sure to get your actual contract address from the console log output after executing `yarn test-deploy`.

```shell
$ yarn test-verify 0x93891cb936B62806300aC687e12d112813b483C1
Nothing to compile
No need to generate any newer typings.
Successfully submitted source code for contract
contracts/TestLensApiConsumerContract.sol.sol.sol:TestLensApiConsumerContract.sol at 0x93891cb936B62806300aC687e12d112813b483C1
for verification on the block explorer. Waiting for verification result...

Successfully verified contract TestLensApiConsumerContract.sol on Etherscan.
https://mumbai.polygonscan.com/address/0x93891cb936B62806300aC687e12d112813b483C1#code
Done in 8.88s.
```

**Interact with Consumer Contract on Polygon Mumbai**

Test Consumer Contract on Mumbai with a few tests to check for malformed requests failures, successful requests, and set the attestor.

```shell
# set the attestor to the Oracle Endpoint in Phat Bricks UI
$ yarn test-set-attestor
Setting attestor...
🚨NOTE🚨
Make sure to go to your Phat Bricks 🧱 UI dashboard (https://bricks-poc5.phala.network)
- Go to 'Configure Client' section where a text box reads 'Add Consumer Smart Contract'
- Set value to 0x93891cb936B62806300aC687e12d112813b483C1
Done
✨  Done in 1.56s.
# execute push-malformed-request
$ yarn test-push-malformed-request
Pushing a malformed request...
Done
# execute push-request
$ yarn test-push-request
Pushing a request...
Done
```

#### Deploy to Polygon Mainnet

Ensure to save the address after deploying the Consumer Contract because this address will be used in the "[`Configure Client`](./#step-4-configure-the-client-address)" section of Phat Bricks UI. The deployed address will also be set to the environment variable `POLYGON_CONSUMER_CONTRACT_ADDRESS`.

> **Note**: Your contract address will be different than `0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4` when verifying your contract. Make sure to get your actual contract address from the console log output after executing `yarn main-deploy`.

```shell
# deploy contracts to polygon mainnet
$ yarn main-deploy
Deploying...
Deployed { consumer: '0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4' }
Configuring...
Done

# Check our example deployment in <https://polygonscan.com/address/0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4>
```

**Verify Contract on Polygon Mainnet**

Ensure to update the `polygon.arguments.ts` file with the constructor arguments used to instantiate the Consumer Contract. If you add additional parameters to the constructor function then make sure to update the `polygon.arguments.ts` file.

```shell
$ yarn main-verify 0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
Nothing to compile
No need to generate any newer typings.
Successfully submitted source code for contract
contracts/TestLensApiConsumerContract.sol.sol:TestLensApiConsumerContract.sol.sol at 0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
for verification on the block explorer. Waiting for verification result...

Successfully verified contract TestLensApiConsumerContract.sol on Etherscan.
https://polygonscan.com/address/0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4#code
Done in 8.88s.
```

**Interact with Consumer Contract on Polygon Mainnet**

Execute Scripts to Consumer Contract on Polygon Mainnet. The Consumer Contract on Polygon Mainnet with a few actions to mimic a malformed request, successful requests, and set the attestor.

```shell
# set the attestor to the Oracle Endpoint in Phat Bricks UI
$ yarn main-set-attestor
Setting attestor...
🚨NOTE🚨
Make sure to set the Consumer Contract Address in your Phat Bricks 🧱 UI dashboard (https://bricks-poc5.phala.network)
- Go to 'Configure Client' section where a text box reads 'Add Consumer Smart Contract'
- Set value to 0xbb0d733BDBe151dae3cEf8D7D63cBF74cCbf04C4
Done
✨  Done in 1.56s.
# execute push-malformed-request
$ yarn main-push-malformed-request
Pushing a malformed request...
Done
# execute push-request
$ yarn main-push-request
Pushing a request...
Done
```

### Closing

Once you have stored, the deployed address of the Consumer Contract and set the value in the "Configure Client" section of the deployed LensAPI Oracle, you will now have a basic boilerplate example of how to connect your Polygon dApp to a LensAPI Oracle Blueprint. Execute a new requests and check if your configuration is correct like below:&#x20;

<figure><img src="../../../../.gitbook/assets/polygonscan-ex.png" alt=""><figcaption></figcaption></figure>
