# 🎫 Connect The Graph Phat Contract to EVM Consumer Contract

In the previous section we described how The Graph Starter Kit works. Let's revisit the diagram and description below.

## Overview

<figure><img src="../../../../.gitbook/assets/TheGraphFlow.jpg" alt=""><figcaption></figcaption></figure>

The diagram above displays the user journey of (1) Alice requesting a trust score for Eve from the EVM Consumer Contract. When (2) a new action request is added to the queue, (3) the Phala Network Phat Contract will pop the action off the queue and perform the off-chain work to compute a trust score.

First (4) the Phat Contract will create a `batchHttpRequest` to query 3 separate subgraph endpoints to determine if Eve has any ERC-721 NFTs, a NounsDAO NFT,  an ENS Domain, and if any accounts delegate votes to Eve on Snapshot. Once this data is returned then (5) the Phat Contract will compute a score based on some scoring criteria. You can view the code [here](https://bit.ly/pc-the-graph-repo). Lastly, (6) the trust score for Eve has been returned to the EVM Consumer Contract and Eve's score is set in the Consumer Contract's storage for anyone to query.

## Getting Started

If you have not setup The Graph code repo locally, go back to the [Quick Start](quick-start.md) section and follow the initial setup steps.

### Before Deployment

Before deploying, you will need to either export your Phala Account via polkadot.js extension or store your private key in the .env (optionally you can manually enter during deployment as well).

**Option 1: Export Polkadot account as json file**

Go to your browser and click on the polkadot.js extension. Select your account and click "Export Account". Next, you will be prompted for your password before saving the file to your project directory. **Note** this is what will be set to `POLKADOT_WALLET_ACCOUNT_PASSPHRASE`. Make sure to save the file as `polkadot-account.json` in the **root** of your project directory.

<figure><img src="../../../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

**Option 2: Set mnemonic phrase to `POLKADOT_WALLET_SURI`**

After creating your Phala Profile, set your `.env` variable `POLKADOT_WALLET_SURI` to the mnemonic phrase from generating the new Polkadot Account.

Here is a screenshot of how to set `POLKADOT_WALLET_SURI`:

<figure><img src="../../../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

## Deployments (Local, Testnet, Mainnet)

This guide will be separated into 3 tabs including:

* **Local**: Local Testnet Deployment
* **Testnet**: PoC6 Testnet & EVM Chain Testnet Deployment
* **Mainnet**: Phala Mainnet & EVM Chain Mainnet Deployment

> **Secrets (**[**What are Secrets**](../featured-blueprints/handling-secrets.md)**?):**
>
> * `apiUrl` - The endpoint base URL to the separate subgraph endpoints hosted on The Graph
> * `apiKey` - an API key created on The Graph
>
> ```
> {
>     "apiUrl": "https://gateway.thegraph.com/api/",
>     "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"
> }
> ```

{% tabs %}
{% tab title="Local" %}
In the previous [Quick Start](quick-start.md) section, we installed the dependencies and ran 2 separate tests locally, but these tests were not run against a live local testnet.&#x20;

This section will describe the process of:

* Start up a local hardhat node
* Deploy the EVM Consumer Contract to the local testnet
* Run the `@phala/fn watch` command to run a local instance of The Graph Phat Contract
* Simulate a sample request by executing `npm run localhost-push-request`
* See the The Graph Phat Contract reply with a result to the EVM Consumer Contract

### Testing Locally

First step is to install the package dependencies with the following command:

```bash
npm install
```

With all the dependencies installed, we are ready to build The Graph Phat Contract.

```bash
npx @phala/fn build
```

To simulate the expected result locally, run the Phat Contract script now with this command:

> Use `decode` and `encode` playground at [https://playground.ethers.org](https://playground.ethers.org).

```bash
npx @phala/fn run dist/index.js -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000de1683287529b9b4c3132af8aad210644b259cfd '{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
```

Here is the expected output of this call where the encoded call will request a trust score result for the address `hashwarlock.eth`. The result is `16`.

```bash
npx @phala/fn run dist/index.js -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000de1683287529b9b4c3132af8aad210644b259cfd '{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
handle req: 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000de1683287529b9b4c3132af8aad210644b259cfd
[1]: 0xdE1683287529B9B4C3132af8AaD210644B259CfD
Request received for profile 0xdE1683287529B9B4C3132af8AaD210644B259CfD
{"data":{"account":{"id":"0xde1683287529b9b4c3132af8aad210644b259cfd","ERC721tokens":[{"id":"0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85/0x1c1f4a45a4e02789c110c3771dac92f92a9498f8016c8a6fefcf4d117603d277","identifier":"12720044626168998947918556575205935844278720363082869735772187331921734521463","contract":{"id":"0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85"}},{"id":"0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85/0x8078323181367af7deac0d322698034faf460e340e8bcfde9469655682e637b5","identifier":"58108412688393927589019354909227047790661963669020827084996334376817871173557","contract":{"id":"0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85"}},{"id":"0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85/0x94286edc2c3c238c35cdeb1775c329c554fdd9df064c9ce86dad277d74a1667","identifier":"4188358787553715944519630366137388336862205236752970957509174576540310705767","contract":{"id":"0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85"}},{"id":"0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85/0xba4f236216fb3975855ea0572713af6335f992a110b7ea520a05f06440768b05","identifier":"84270014960222169810810437893688928763911475898905132261856796581223088950021","contract":{"id":"0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85"}}]}}}
ERC-721 NFTs owned on ETH Check... Result [4]
{"data":{"account":{"id":"0xde1683287529b9b4c3132af8aad210644b259cfd","ERC721tokens":[]}}}
Has a NounsDAO NFT Check... Result [4]
{"data":{"account":{"domains":[{"name":"warlox.eth"},{"name":"hashwarlock.eth"},{"name":"[4df3c10b7d9a8cfdbb386728d398389b2dfbcd0f66e4c1ee612a7c82f649ac0a].addr.reverse"}]}}}
Has ENS Domains Check... Result [16]
{"data":{"delegations":[]}}
Has Delegated Votes on Snapshot Check... Result [16]
response: 0,1,16
{"output":"0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000010"}
```

#### Deploy a Local Hardhat Node

Now that we have a simple understanding of the expected functionality of the Phat Contract, we can now take our tests to a local testnet. Here we will use Hardhat to deploy the EVM Consumer Contract then listen from new action requests and reply with built Phat Contract script.

First we will start a local hardhat node.

```sh
npm run localhost-node
```

With our hardhat node running locally, we can now deploy the `OracleConsumerContract.sol` contract to the local hardhat network.

```bash
npm run localhost-deploy
```

```bash
npm run localhost-deploy
> the-graph-phat-contract@1.0.0 localhost-deploy
> hardhat run --network localhost ./scripts/localhost/deploy.ts

Compiled 18 Solidity files successfully (evm target: london).
Deploying...
Deployed { consumer: '0x5FbDB2315678afecb367f032d93F642f64180aa3' }
```

Make sure to copy the deployed contract address when you deploy your own contract locally. Note you contract address will be different than `0x5FbDB2315678afecb367f032d93F642f64180aa3`. We will now start watching the hardhat node deployed contract for any new requests from The Graph Phat Contract.

```bash
npx @phala/fn watch 0x5FbDB2315678afecb367f032d93F642f64180aa3 artifacts/contracts/OracleConsumerContract.sol/OracleConsumerContract.json dist/index.js -a '{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
```

```bash
npx @phala/fn watch 0x5FbDB2315678afecb367f032d93F642f64180aa3 artifacts/contracts/OracleConsumerContract.sol/OracleConsumerContract.json dist/index.js -a '{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
Listening for OracleConsumerContract MessageQueued events...
```

Let’s now make a new request and see what happens with the listener’s output. In separate tab, you will push a request with the following.

> **Note**: The file can be edited [here](https://github.com/Phala-Network/the-graph-phat-contract/blob/b9ba89d26ac288500685410b98d2fe01bf426846/scripts/localhost/push-request.ts#L16) where you can change the `target` address.

```bash
LOCALHOST_CONSUMER_CONTRACT_ADDRESS=0x5FbDB2315678afecb367f032d93F642f64180aa3 npm run localhost-push-request
```

```bash
LOCALHOST_CONSUMER_CONTRACT_ADDRESS=0x5FbDB2315678afecb367f032d93F642f64180aa3 npm run localhost-push-request
> the-graph-phat-contract@1.0.0 localhost-push-request
> hardhat run --network localhost ./scripts/localhost/push-request.ts

Pushing a request...
Received event [ResponseReceived]: {
  reqId: BigNumber { value: "1" },
  target: '0x011c23b3AadAf3D4991f3aBeE262A34d18e9fdb5',
  value: BigNumber { value: "70" }
}
```

If you check back the tab where the Phat Contract is listening for new requests, the console log may look similar to below:

```bash
Received event [MessageQueued]: {
  tail: 0n,
  data: '0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000011c23b3aadaf3d4991f3abee262a34d18e9fdb5'
}
handle req: 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000011c23b3aadaf3d4991f3abee262a34d18e9fdb5
[1]: 0x011c23b3AadAf3D4991f3aBeE262A34d18e9fdb5
Request received for profile 0x011c23b3AadAf3D4991f3aBeE262A34d18e9fdb5
{"data":{"account":{"id":"0x011c23b3aadaf3d4991f3abee262a34d18e9fdb5","ERC721tokens":[{"id":"0x00703f9b11f2ac02d391a11e7b97c6ee80cd8563/0x2bd","identifier":"701","contract":{"id":"0x00703f9b11f2ac02d391a11e7b97c6ee80cd8563"}},{"id":"0x008f5a13d37db25d1bf7e7115747450e12e471b9/0x13fc","identifier":"5116","contract":{"id":"0x008f5a13d37db25d1bf7e7115747450e12e471b9"}},{"id":"0x0144ecf966096108b03148d0071df6c70c051a52/0x149f","identifier":"5279","contract":{"id":"0x0144ecf966096108b03148d0071df6c70c051a52"}},{"id":"0x015fcab6a246cfc0679c33ef0b9d9ef947d0bde4/0x1782","identifier":"6018","contract":{"id":"0x015fcab6a246cfc0679c33ef0b9d9ef947d0bde4"}},{"id":"0x0191c41dbceb20a612b25137133ca719e84f7933/0x11f","identifier":"287","contract":{"id":"0x0191c41dbceb20a612b25137133ca719e84f7933"}},{"id":"0x0191c41dbceb20a612b25137133ca719e84f7933/0x120","identifier":"288","contract":{"id":"0x0191c41dbceb20a612b25137133ca719e84f7933"}},{"id":"0x0191c41dbceb20a612b25137133ca719e84f7933/0xd8e","identifier":"3470","contract":{"id":"0x0191c41dbceb20a612b25137133ca719e84f7933"}},{"id":"0x0208517aa68e7c72769af76f4cfdeea9fa4ef4b9/0x213","identifier":"531","contract":{"id":"0x0208517aa68e7c72769af76f4cfdeea9fa4ef4b9"}},{"id":"0x026dce20bf77e08ca8aceb6b239cc54bb9d638ac/0x237","identifier":"567","contract":{"id":"0x026dce20bf77e08ca8aceb6b239cc54bb9d638ac"}},{"id":"0x032d96756697af7ec02ce03d39001b39f7a5d849/0x1a4","identifier":"420","contract":{"id":"0x032d96756697af7ec02ce03d39001b39f7a5d849"}},{"id":"0x038cc0f103c380400482d87be0d3abcc4d9b2225/0x2ed","identifier":"749","contract":{"id":"0x038cc0f103c380400482d87be0d3abcc4d9b2225"}},{"id":"0x039483c56aad5ee68a92eff1a1b666f2893c623e/0xf9d","identifier":"3997","contract":{"id":"0x039483c56aad5ee68a92eff1a1b666f2893c623e"}},{"id":"0x03ef30e1aee25abd320ad961b8cd31aa1a011c97/0x17a1","identifier":"6049","contract":{"id":"0x03ef30e1aee25abd320ad961b8cd31aa1a011c97"}},{"id":"0x03ef30e1aee25abd320ad961b8cd31aa1a011c97/0xcf1","identifier":"3313","contract":{"id":"0x03ef30e1aee25abd320ad961b8cd31aa1a011c97"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1000","identifier":"4096","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x100b","identifier":"4107","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x107d","identifier":"4221","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x10de","identifier":"4318","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x11aa","identifier":"4522","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x12c5","identifier":"4805","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x139a","identifier":"5018","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x144","identifier":"324","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x144e","identifier":"5198","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x14a9","identifier":"5289","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x14c0","identifier":"5312","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1531","identifier":"5425","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x153e","identifier":"5438","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1569","identifier":"5481","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x158c","identifier":"5516","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x15ee","identifier":"5614","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x161f","identifier":"5663","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x164d","identifier":"5709","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x16db","identifier":"5851","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1735","identifier":"5941","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1742","identifier":"5954","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1764","identifier":"5988","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1793","identifier":"6035","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x18b7","identifier":"6327","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1926","identifier":"6438","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1940","identifier":"6464","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1988","identifier":"6536","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x199a","identifier":"6554","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1a8e","identifier":"6798","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1b4","identifier":"436","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1be3","identifier":"7139","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1beb","identifier":"7147","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1d83","identifier":"7555","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1dc0","identifier":"7616","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1dd8","identifier":"7640","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}},{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429/0x1e45","identifier":"7749","contract":{"id":"0x04b4786c3bb42387235a63628b7a4cb178817429"}}]}}}
ERC-721 NFTs owned on ETH Check... Result [50]
{"data":{"account":{"id":"0x011c23b3aadaf3d4991f3abee262a34d18e9fdb5","ERC721tokens":[]}}}
Has a NounsDAO NFT Check... Result [50]
{"data":{"account":{"domains":[{"name":"sissitian.eth"},{"name":"ariahuang.eth"},{"name":"hugovault.eth"},{"name":"hugosu.eth"},{"name":"dominichuang.eth"}]}}}
Has ENS Domains Check... Result [70]
{"data":{"delegations":[]}}
Has Delegated Votes on Snapshot Check... Result [70]
response: 0,1,70
JS Execution output: 0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000046
```

:tada: **Congratulations!**&#x20;

You've completed deploying and testing The Graph Phat Contract successfully in a local testnet. Now let's move to deploying to an EVM Testnet and connecting a deployed Phat Contract on PoC6 Testnet to visualize how this works autonomously.
{% endtab %}

{% tab title="Testnet" %}
{% hint style="danger" %}
**Important**

This guide references the `mumbai` testnet chain.&#x20;

The`mumbai` testnet is [deprecated since 2024/04/08](https://polygon.technology/blog/introducing-the-amoy-testnet-for-polygon-pos), meaning the steps to deploy to a testnet will no longer work out of the box.

You can opt to use the [`amoy`](https://polygon.technology/blog/introducing-the-amoy-testnet-for-polygon-pos) testnet or any other EVM testnet instead.
{% endhint %}

In the previous [Quick Start](../airstack/quick-start.md) section, we installed the dependencies. Now it is time to deploy and test to an EVM public testnet.&#x20;

The following steps will be performed:

* Deploy the EVM Consumer Contract to the target EVM chain
  * The EVM Consumer Contract will request actions to be executed off-chain by the Phat Contract
* Deploy The Graph Phat Contract to the Phala PoC6 Testnet
  * Once deployed, update the `ATTESTOR_ROLE` in the EVM Consumer Contract to the `Attestor Address` in the Phat Contract 2.0 UI Dashboard
* Send a `request(address target)` transaction to get a trust score about an EVM target address
* See The Graph Phat Contract respond with an action reply with a score for the target address

### Minimum Requirements

* [ ] Create a [Phala Dashboard Profile](../create-a-dashboard-profile.md) on Phala PoC6 Testnet
  * [ ] Add funds to the EVM Gas Account to pay TX fees on target EVM Testnet Chain
* [ ] Finished the [Quick Start](quick-start.md)
* [ ] (Recommended) Go through the `Local` tab deployment process
* [ ] Burner Account for EVM Consumer Contract deployment

### Deployment

In this example, we will use Polygon Mumbai Testnet as the target EVM Testnet Chain, but this can be changed to any EVM testnet of the developers choice.

#### Install Dependencies & Compile Contracts <a href="#user-content-install-dependencies--compile-contracts" id="user-content-install-dependencies--compile-contracts"></a>

```sh
# install dependencies
$ npm install

# compile contracts
$ npm run compile
```

#### Deploy to Polygon Mumbai Testnet <a href="#user-content-deploy-to-polygon-mumbai-testnet" id="user-content-deploy-to-polygon-mumbai-testnet"></a>

With the contracts successfully compiled, now we can begin deploying first to Polygon Mumbai Testnet. If you have not gotten `MATIC` for Mumbai Testnet then get `MATIC` from a [faucet](https://bit.ly/3ZyFoT3). Ensure to save the address after deploying the Consumer Contract because this address will be use in the "Configure Client" section of Phat Contract 2.0 UI. The deployed address will also be set to the environment variable `MUMBAI_CONSUMER_CONTRACT_ADDRESS`.

<pre class="language-sh"><code class="lang-sh"><strong>npm run test-deploy
</strong></code></pre>

```sh
# deploy contracts to testnet mumbai
npm run test-deploy
# > the-graph-phat-contract@1.0.0 test-deploy
# > hardhat run --network mumbai ./scripts/mumbai/deploy.ts
#
# Deploying...
#
# 🎉 Your Consumer Contract has been deployed, check it out here: https://mumbai.polygonscan.com/address/0xEE2F3526686D27f682ecb6E3dC91cd8c972Cf355
#
# You also need to set up the consumer contract address in your .env file:
#
# MUMBAI_CONSUMER_CONTRACT_ADDRESS=0xEE2F3526686D27f682ecb6E3dC91cd8c972Cf355
#
# Done
```

#### **(Optional) Verify Contract on Polygon Mumbai Testnet**

Ensure to update the `mumbai.arguments.ts` file with the constructor arguments used to instantiate the Consumer Contract. If you add additional parameters to the constructor function then make sure to update the `mumbai.arguments.ts` file.

> **Note**: Your contract address will be different than `0xEE2F3526686D27f682ecb6E3dC91cd8c972Cf355` when verifying your contract. Make sure to get your actual contract address from the console log output after executing `npm run test-deploy`.

```sh
npm run test-verify -- <MUMBAI_CONSUMER_CONTRACT_ADDRESS>
```

```sh
npm run test-verify -- 0xEE2F3526686D27f682ecb6E3dC91cd8c972Cf355
# > the-graph-phat-contract@1.0.0 test-verify
# > hardhat verify --network mumbai --constructor-args mumbai.arguments.ts 0xEE2F3526686D27f682ecb6E3dC91cd8c972Cf355
#
# Nothing to compile
# No need to generate any newer typings.
# Successfully submitted source code for contract
# contracts/OracleConsumerContract.sol:OracleConsumerContract at 0xEE2F3526686D27f682ecb6E3dC91cd8c972Cf355
# for verification on the block explorer. Waiting for verification result...
#
# Successfully verified contract OracleConsumerContract on Etherscan.
# https://mumbai.polygonscan.com/address/0xEE2F3526686D27f682ecb6E3dC91cd8c972Cf355#code
```

#### Deploy Phat Contract to PoC6 Testnet <a href="#user-content-deploy-phat-contract-to-poc5-testnet" id="user-content-deploy-phat-contract-to-poc5-testnet"></a>

For customizing your Phat Contract, checkout Phat Contract custom configurations in [Cusomizing Your Phat Contract](../featured-blueprints/customizing-your-phat-contract.md) to learn more before deploying to PoC6 testnet.

Now that are Phat Contract has built successfully, let's deploy to Phala PoC6 Testnet with the following command:

```shell
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn upload --coreSettings='{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
# If polkadot-account.json is in the root of project
npx @phala/fn upload -a ./polkadot-account.json --coreSettings='{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
```

Here is the expected output:

> Note: your contract IDs will vary and not be the same as the IDs below.

```bash
npx @phala/fn upload -a ./polkadot-account.json --coreSettings='{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
# ? Please enter your client RPC URL https://polygon-mumbai.g.alchemy.com/v2/JLjOfWJycWFOA0kK_SJ4jLGjtXkMN1wc
# ? Please enter your consumer address 0xEE2F3526686D27f682ecb6E3dC91cd8c972Cf355
# ? Please Enter hahaha account password [hidden]
# ✓ Compiled successfully.
# ✓ Connected to the endpoint: wss://poc6.phala.network/ws
#
# You are connecting to a testnet.
#
# ✓ Your Brick Profile contract ID: 0x2a9f9a07886e11e1c5d63a176e3f75253d6765aadb90beb112fb3e55f7c98ea8
# ✓ The ActionOffchainRollup contract has been instantiated: 0xc9b96a665c3f1730606760f056b78bbb493f31a2b5406f8dd19e138561177336
# ? Please select an external account: [1] 0x20050cae178a72e7c5adc207a060a16e65bbb7cf. https://polygon-mumbai.g.alchemy.com/v2/JLjOfWJycWFOA0kK_SJ4jLGjtXkMN1wc
# ✓ Checking your settings
# ? Please enter your project name My Phat Contract 6
# ✓ 🎉 Your workflow has been added, you can check it out here: https://bricks.phala.network/workflows/0x2a9f9a07886e11e1c5d63a176e3f75253d6765aadb90beb112fb3e55f7c98ea8/6
# Your Attestor address: 0x4a8e621202af9206959017c3795721f327f2ef28
# Your WORKFLOW_ID: 6
```

Go to the [Phala Dashboard](https://dashboard.phala.network) and you can see your newly deployed Phat Contract.

<figure><img src="../../../../.gitbook/assets/DeployedTheGraphPC.png" alt=""><figcaption></figcaption></figure>

#### **Interact with Consumer Contract on Polygon Mumbai**

Test Consumer Contract on Mumbai with a few tests to check for malformed requests failures, successful requests, and set the attestor.

```sh
npm run test-set-attestor
```

```sh
npm run test-set-attestor
# > the-graph-phat-contract@1.0.0 test-set-attestor
# > hardhat run --network mumbai ./scripts/mumbai/set-attestor.ts
#
# Setting attestor...
# 🚨NOTE🚨
# Make sure to set the Consumer Contract Address in your Phat Contract 2.0 UI dashboard (https://bricks.phala.network)
# - Go to the 'Configuration' tab and update the 'Client' box
# - Set value to 0xEE2F3526686D27f682ecb6E3dC91cd8c972Cf355
# Done
```

Test pushing a malform request.

```sh
npm run test-push-malformed-request
```

```sh
npm run test-push-malformed-request
# > the-graph-phat-contract@1.0.0 test-push-malformed-request
# > hardhat run --network mumbai ./scripts/mumbai/push-malformed-request.ts
#
# Pushing a malformed request...
# Done
```

We can visualize the response from the Phat Contract in the block explorer.

<figure><img src="../../../../.gitbook/assets/malformreq-thegraph-pc.png" alt=""><figcaption></figcaption></figure>

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

The next 2 images will show the request to the Consumer Contract with a reply from the Phat Contract, and the last picture shows what the Phat Contract replied with.

<figure><img src="../../../../.gitbook/assets/push-request-thegraph.png" alt=""><figcaption></figcaption></figure>

Here is the emitted event `ResponseReceived` with the score `70` for `target` address `0x011c23b3AadAf3D4991f3aBeE262A34d18e9fdb5.`

<figure><img src="../../../../.gitbook/assets/thegraph-pc-reply-info.png" alt=""><figcaption></figcaption></figure>

#### Update Phat Contract on Phala PoC6 Testnet <a href="#user-content-update-phat-contract-on-phala-poc5-testnet" id="user-content-update-phat-contract-on-phala-poc5-testnet"></a>

Sometimes you may have had a bug in your script or you want to test things out on the fly without deploying a whole new Phat Contract. The `npx @phala/fn update` command will update your Phat Contract easily in the command line.&#x20;

Now let's update the Phat Contract:

```bash
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn update
# If polkadot-account.json is in the root of project
npx @phala/fn update -a ./polkadot-account.json
```

```bash
npx @phala/fn update -a ./polkadot-account.json
# ? Please Enter hahaha account password [hidden]
# ✓ Compiled successfully.
# ✓ Connected to the endpoint: wss://poc6.phala.network/ws
#
# You are connecting to a testnet.
#
# ✓ Your Brick Profile contract ID: 0x2a9f9a07886e11e1c5d63a176e3f75253d6765aadb90beb112fb3e55f7c98ea8
# ✓ The JavaScript code for workflow 6 has been updated.
```

:tada: **Congratulations!** You have now completed a full testnet deployment and have a fully functional Phat Contract connected to The Graph to compute a score and return to your EVM Consumer Contract. The steps for mainnet deployment are nearly identical, but let's take a look at the process in the `Mainnet` tab.
{% endtab %}

{% tab title="Mainnet" %}
In the previous `Testnet` tab, you went through the full deployment process to connect The Graph Phat Contract to a Consumer Contract on an EVM Testnet Chain. Now it is time to take these talents to **Mainnet** :sunglasses:.&#x20;

The following steps will be performed:

* Deploy the EVM Consumer Contract to the target EVM  Mainnet chain
  * The EVM Consumer Contract will request actions to be executed off-chain by the Phat Contract
* Deploy The Graph Phat Contract to the Phala Mainnet
  * Once deployed, update the `ATTESTOR_ROLE` in the EVM Consumer Contract to the `Attestor Address` in the Phat Contract 2.0 UI Dashboard
* Send a `request(address target)` transaction to get a trust score about an EVM target address
* See The Graph Phat Contract respond with an action reply with a score for the target address

### Minimum Requirements

* [ ] Create a [Phala Dashboard Profile](../create-a-dashboard-profile.md) on Phala Mainnet
  * [ ] Add funds to the EVM Gas Account to pay TX fees on target EVM Mainnet Chain
* [ ] Finished the [Quick Start](quick-start.md)
* [ ] (Recommended) Go through the `Local` AND `Testnet` tabs to understand the deployment process fully
* [ ] Burner Account for EVM Consumer Contract deployment

### Deployment

In this example, we will use Polygon PoS Mainnet as the target EVM Mainnet Chain, but this can be changed to any EVM chain of the developer's choice.

#### Install Dependencies & Compile Contracts <a href="#user-content-install-dependencies--compile-contracts" id="user-content-install-dependencies--compile-contracts"></a>

```sh
# install dependencies
$ npm install

# compile contracts
$ npm run compile
```

#### Deploy to Polygon Mainnet <a href="#user-content-deploy-to-polygon-mumbai-testnet" id="user-content-deploy-to-polygon-mumbai-testnet"></a>

With the contracts successfully compiled, now we can begin deploying first to Polygon PoS Mainnet. If you have not gotten `MATIC` then get `MATIC` from an exchange or through their [Wallet Suite](https://wallet.polygon.technology/). Ensure to save the address after deploying the Consumer Contract because this address will be use in the "Configure Client" section of Phat Contract 2.0 UI. The deployed address will also be set to the environment variable `POLYGON_CONSUMER_CONTRACT_ADDRESS`.

<pre class="language-sh"><code class="lang-sh"><strong>npm run main-deploy
</strong></code></pre>

```sh
# deploy contracts to Polygon PoS mainnet
npm run main-deploy
# > the-graph-phat-contract@1.0.0 main-deploy
# > hardhat run --network polygon ./scripts/polygon/deploy.ts
#
# Deploying...
#
# 🎉 Your Consumer Contract has been deployed, check it out here: https://polygonscan.com/address/0x0b9aC89924483077899d2B52bc8AF794F546a1e9
#
# You also need to set up the consumer contract address in your .env file:
#
# POLYGON_CONSUMER_CONTRACT_ADDRESS=0x0b9aC89924483077899d2B52bc8AF794F546a1e9
# 
# Done
```

#### **(Optional) Verify Contract on Polygon Mainnet**

Ensure to update the `polygon.arguments.ts` file with the constructor arguments used to instantiate the Consumer Contract. If you add additional parameters to the constructor function then make sure to update the `polygon.arguments.ts` file.

> **Note**: Your contract address will be different than `0x0b9aC89924483077899d2B52bc8AF794F546a1e9` when verifying your contract. Make sure to get your actual contract address from the console log output after executing `npm run main-deploy`.

```sh
npm run main-verify -- <MUMBAI_CONSUMER_CONTRACT_ADDRESS>
```

```sh
npm run main-verify -- 0x0b9aC89924483077899d2B52bc8AF794F546a1e9
# > the-graph-phat-contract@1.0.0 main-verify
# > hardhat verify --network polygon --constructor-args polygon.arguments.ts 0x0b9aC89924483077899d2B52bc8AF794F546a1e9
#
# Nothing to compile
# No need to generate any newer typings.
# Successfully submitted source code for contract
# contracts/OracleConsumerContract.sol:OracleConsumerContract at 0x0b9aC89924483077899d2B52bc8AF794F546a1e9
# for verification on the block explorer. Waiting for verification result...
#
# Successfully verified contract OracleConsumerContract on Etherscan.
# https://polygonscan.com/address/0x0b9aC89924483077899d2B52bc8AF794F546a1e9#code
```

#### Deploy Phat Contract to Phala Mainnet <a href="#user-content-deploy-phat-contract-to-poc5-testnet" id="user-content-deploy-phat-contract-to-poc5-testnet"></a>

For customizing your Phat Contract, checkout Phat Contract custom configurations in [Customizing Your Phat Contract](../featured-blueprints/customizing-your-phat-contract.md) to learn more before deploying to Phala Mainnet.

Now that are Phat Contract has built successfully, let's deploy to Phala Mainnet with the following command:

<pre class="language-shell"><code class="lang-shell"># If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn upload --mode=production --coreSettings='{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
# If polkadot-account.json is in the root of project
<strong>npx @phala/fn upload --mode=production -a ./polkadot-account.json --coreSettings='{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
</strong></code></pre>

Here is the expected output:

> Note: your contract IDs will vary and not be the same as the IDs below.

```bash
npx @phala/fn upload --mode=production -a ./polkadot-account.json --coreSettings='{"apiUrl": "https://gateway.thegraph.com/api/", "apiKey": "cd22a01e5b7f9828cddcb52caf03ee79"}'
# ? Please enter your client RPC URL https://polygon-mainnet.g.alchemy.com/v2/UZpqlxsFm0aVm_euopH95rQ6YxiRa3VC
# ? Please enter your consumer address 0x0b9aC89924483077899d2B52bc8AF794F546a1e9
# ? Please Enter hahaha account password [hidden]
# ✓ Compiled successfully.
# ✓ Connected to the endpoint: wss://api.phala.network/ws
# ✓ Your Brick Profile contract ID: 0x6e96d8c209fc14b69533e3627c4766b6eeef8f77a25348b2d77b28c90b0bd012
# ✓ The ActionOffchainRollup contract has been instantiated: 0xe2ac2edc835de67f71f76ef686ebb4e48bdf0c2da2b6862329cca00c3c9b8349
# ? Please select an external account: [0] 0x8438ce1a6196b7edae83cbc2a58d33db6fae6bee. https://polygon-mainnet.g.alchemy.com/v2/W1kyx17tiFQFT2b19mGOqppx90BLHp0a
# ✓ Checking your settings
# ? Please enter your project name My Phat Contract 0
# ✓ 🎉 Your workflow has been added, you can check it out here: https://bricks.phala.network/workflows/0x6e96d8c209fc14b69533e3627c4766b6eeef8f77a25348b2d77b28c90b0bd012/0
# Your Attestor address: 0x2829d70d48516b7d1be2b5f5f424b41ce4da8056
# Your WORKFLOW_ID: 0
```

Go to the [Phat Contract 2.0 Dashboard](https://bit.ly/3LHccmR) and you can see your newly deployed Phat Contract.

<figure><img src="../../../../.gitbook/assets/deploy-thegraph-main.png" alt=""><figcaption></figcaption></figure>

#### **Interact with Consumer Contract on Polygon PoS Mainnet**

Consumer Contract on Mumbai with a few transactions to set the attestor, check for malformed requests failures, and successfully fulfilled requests.

```sh
npm run main-set-attestor
```

<pre class="language-sh"><code class="lang-sh">npm run main-set-attestor
<strong># > the-graph-phat-contract@1.0.0 main-set-attestor
</strong># > hardhat run --network polygon ./scripts/polygon/set-attestor.ts
#
# Setting attestor...
# 🚨NOTE🚨
# Make sure to set the Consumer Contract Address in your Phat Contract 2.0 UI dashboard (https://bricks.phala.network)
# - Go to the 'Configuration' tab and update the 'Client' box
# - Set value to 0x0b9aC89924483077899d2B52bc8AF794F546a1e9
# Done
</code></pre>

Try pushing a malform request to ensure failures behave appropriately.

```sh
npm run main-push-malformed-request
```

```sh
npm run main-push-malformed-request
# > the-graph-phat-contract@1.0.0 main-push-malformed-request
# > hardhat run --network polygon ./scripts/polygon/push-malformed-request.ts
#
# Pushing a malformed request...
# Done
```

We can visualize the response from the Phat Contract in the Polygonscan block explorer.

<figure><img src="../../../../.gitbook/assets/malform-request-pc-main.png" alt=""><figcaption></figcaption></figure>

Test pushing a valid request that will get a valid reply of a trust score value for a `target` address.

```sh
npm run main-push-request
```

```sh
npm run main-push-request
# > the-graph-phat-contract@1.0.0 main-push-request
# > hardhat run --network polygon ./scripts/polygon/push-request.ts
#
# Pushing a request...
# Done
```

The next 2 images will show the request to the Consumer Contract with a reply from the Phat Contract, and the last picture shows what the Phat Contract replied with.

<figure><img src="../../../../.gitbook/assets/push-request-thegraph-main.png" alt=""><figcaption></figcaption></figure>

Here is the emitted event `ResponseReceived` with the score `206` for `target` address `0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` (aka vitalik.eth)

<figure><img src="../../../../.gitbook/assets/thegraph-pc-reply-info-vitalik.png" alt=""><figcaption></figcaption></figure>

#### Update Phat Contract on Phala Mainnet <a href="#user-content-update-phat-contract-on-phala-poc5-testnet" id="user-content-update-phat-contract-on-phala-poc5-testnet"></a>

Sometimes you may have had a bug in your script or you want to test things out on the fly without deploying a whole new Phat Contract. The `npx @phala/fn update` command will update your Phat Contract easily in the command line.&#x20;

Now let's update the Phat Contract:

```bash
# If you did not export your Polkadot account in a 
# polkadot-account.json file in the root of project
npx @phala/fn update --mode=production
# If polkadot-account.json is in the root of project
npx @phala/fn update --mode=production -a ./polkadot-account.json
```

<pre class="language-bash"><code class="lang-bash">npx @phala/fn update --mode=production -a ./polkadot-account.json
<strong># ? Please Enter hahaha account password [hidden]
</strong># ✓ Compiled successfully.
# ✓ Connected to the endpoint: wss://api.phala.network/ws
# ✓ Your Brick Profile contract ID: 0x6e96d8c209fc14b69533e3627c4766b6eeef8f77a25348b2d77b28c90b0bd012
# ✓ The JavaScript code for workflow 0 has been updated.
</code></pre>

:tada: **Congratulations!** You have now completed a full mainnet deployment and have a fully functional Phat Contract connected to The Graph to compute a score and return to your EVM Consumer Contract.
{% endtab %}
{% endtabs %}





