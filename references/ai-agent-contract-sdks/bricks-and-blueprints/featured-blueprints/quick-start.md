# 🏃‍♂️ Quick Start

{% hint style="danger" %}
**Important**

This guide references the `mumbai` testnet chain.&#x20;

The`mumbai` testnet is [deprecated since 2024/04/08](https://polygon.technology/blog/introducing-the-amoy-testnet-for-polygon-pos), meaning the steps to deploy to a testnet will no longer work out of the box.

You can opt to use the [`amoy`](https://polygon.technology/blog/introducing-the-amoy-testnet-for-polygon-pos) testnet or any other EVM testnet instead..
{% endhint %}

<figure><img src="../../../../.gitbook/assets/case-self-owned-oracles.jpg" alt=""><figcaption><p>Visual of how Phat Contract connects to EVM Consumer Contract</p></figcaption></figure>

To kickstart your journey with the Phat Contract Starter Kit, install the `@phala/fn` CLI tool.&#x20;

You can do this using your node package manager (`npm`) or use node package execute (`npx`). For the purpose of this tutorial, we will be using `npx`.

Once you have the CLI tool installed, you can create your first Phala Oracle template with the following command...

:octagonal\_sign: **Not so fast!** What is it exactly that we are building? :octagonal\_sign:

> **What are we building?**
>
> The artifact we are compiling is a JavaScript file, serving as the Phat Contract Oracle's tailored logic. This script is designed to respond to requests initiated from the Consumer Contract. The diagram provided above offers a visual representation of this request-response interaction.
>
> **Why is it important?**
>
> In the context of the off-chain environment, on-chain Smart Contracts are inherently limited. Their functionality is confined to the information available to them within the on-chain ecosystem. This limitation underscores the critical need for a secure off-chain oracle, such as the Phat Contract. This oracle is capable of fetching and transforming data, thereby enhancing the intelligence and awareness of Smart Contracts about on-chain activities. This is a pivotal step towards bridging the gap between the on-chain and off-chain worlds, making Smart Contracts not just smart, but also informed.

Let's continue by initializing a new project with `@phala/fn`.

```sh
npx @phala/fn@latest init example
? Please select one of the templates for your "example" project: 
❯ phat-contract-starter-kit: Send data from any API to your smart contract with Javascript. 
  lensapi-oracle-consumer-contract: Send data from Lens API to your smart contract to empower your Web3 Social dApp. 
  vrf-oracle: TEE-guarded Verifiable Random Function template to bring randomness to your smart contract. 
  airstack-phat-contract: Request an account’s data from Airstack’s API to compute trust score and send to your Web3 dApp on-chain. 
  thegraph-phat-contract: Connect your subgraphs from The Graph to your on-chain dApps via Phat Contract.  
```

After creating a Phala Oracle template, `cd` into the new project and install the package dependencies. You can do this with the following command:

```sh
npm install
```

Now, build the default Phala Oracle function with this command:

```sh
npx @phala/fn build
```

To simulate the expected result locally, run the Phala Oracle function now with this command.

> Go to [https://playground.ethers.org](https://playground.ethers.org) to `decode` and `encode` the hexstring you want to pass into your Phat Contract `main` function.
>
> In this example, the hexstring  `0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000` represents types `uint id` and `string reqData`
>
> Here is what you will enter in the playground:
>
> * `utils.defaultAbiCoder.decode(['uint id', 'string reqData'], '0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000')`
> * `[ BigNumber { value: "1" }, "0x01", id: BigNumber { value: "1" }, reqData: "0x01" ]`
>
> You can easily validate this by encoding the types and data with the `utils.defaultAbiCoder.encode()` function like below.
>
> * `utils.defaultAbiCoder.encode(['uint id', 'string reqData'], [1, "0x01"])`
> * `"0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000"`

```bash
npx @phala/fn run dist/index.js -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000 https://api-mumbai.lens.dev
```

> **What are the ingredients for the yarn run-function command?**
>
> Our Phat Contract script, now fully constructed, is ready for a trial run. This simulation mirrors the live script's operation when deployed on the Phala Network.
>
> The command's first parameter is a `HexString`, representing a tuple of types `[uintCoder, bytesCoder]`. This serves as the entry function. The second parameter is a `string`, embodying the configurable secrets fed into the main function.
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
>   // ...
> }
> ```

<details>

<summary>How the query looks under the hood</summary>

* HTTP Endpoint: [https://api-v2-mumbai-live.lens.dev](https://api-mumbai.lens.dev/)
* Profile ID: `0x01`
* Expected Graphql Query:

```graphql
query Profile {
  profile(request: { profileId: "0x01" }) {
    stats {
        totalFollowers
        totalFollowing
        totalPosts
        totalComments
        totalMirrors
        totalPublications
        totalCollects
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

Finally, run the local end-to-end tests with this command. Here we will simulate locally the interaction between the Phat Contract and the Consumer Contract with hardhat.

```sh
npm run localhost-test
```

:tada: Congratulations! You have successfully completed the quick start. For the next steps, you will learn how to deploy your Phala Oracle and connect to the consumer contract for the EVM testnet chain to start testing the request-response model live.

For a deeper dive into the details, click [here](https://github.com/Phala-Network/phat-contract-starter-kit/blob/main/GETTING\_STARTED.md), or continue reading to learn about the valuable features the Phala Oracle can offer to your on-chain consumer contract.
