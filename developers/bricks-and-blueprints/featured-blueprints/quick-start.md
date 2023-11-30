# 🏃♂ Quick Start

<figure><img src="../../../.gitbook/assets/case-self-owned-oracles.jpg" alt=""><figcaption><p>Visual of how Phat Contract connects to EVM Consumer Contract</p></figcaption></figure>

To kickstart your journey with the Phat Contract Starter Kit, you have 2 options:

1.  Create a template from the [`phat-contract-starter-kit`](https://bit.ly/46wkeY0) template repo. Click on the "**Use this template**" button in the top right corner of the webpage. Then skip the `npx @phala/fn init example` step.&#x20;

    <div>

    <figure><img src="http://localhost:63342/markdownPreview/1918810453/fileSchemeResource/ccbdfbfcaa2bb6682c484f7931b15633-UseThisTemplate.png?_ijt=3r011jj4sfe0bnqfa8f27fg7eh" alt=""><figcaption></figcaption></figure>

     

    <figure><img src="../../../.gitbook/assets/UseThisTemplate.png" alt=""><figcaption></figcaption></figure>

    </div>
2. Install the `@phala/fn` CLI tool. You can do this using your node package manager (`npm`) or use node package execute (`npx`). For the purpose of this tutorial, we will be using `npx`.

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
```

After creating a Phala Oracle template, `cd` into the new project and install the package dependencies. You can do this with the following command:

```sh
npm install
```

Now, build the default Phala Oracle function with this command:

```sh
npm run build-function
```

To simulate the expected result locally, run the Phala Oracle function now with this command.

```bash
npm run run-function -- -a 0x0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000043078303100000000000000000000000000000000000000000000000000000000 https://api-mumbai.lens.dev
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
