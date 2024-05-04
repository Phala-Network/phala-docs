---
description: Host your AI Agent Contract on Phala's decentralized serverless cloud.
---

# Build Your AI Agent Contract with LangChain

## [AI Agent Contract Template with LangChain](https://github.com/Phala-Network/ai-agent-template-langchain)

### Architecture Overview

<figure><img src="../../.gitbook/assets/Screenshot 2024-04-04 at 11.02.11.png" alt=""><figcaption></figcaption></figure>

## 🤖 What Is This?!

***

<div align="center">

<img src="https://www.jlwranglerforums.com/forum/attachments/zoolander-gif.325299/" alt="" height="240">

</div>

The LangChain AI-Agent template is a **MINIMAL** template to build an AI Agent that can be hosted on Phala Network's decentralized hosting protocol. Unlike Vercel or other FaaS, it allows you to publish your AI-Agent compiled code to IPFS and hosts it on a fully decentralized FaaS cloud with the following benefits:

* 💨 **Ship Fast**: Build and ship with familiar toolchain in minutes
* ⛑️ **Secure**: Execution guarded by rock solid TEE / Intel SGX
* 🔒 **Private**: Host API keys and user privacy at ease
* 💎 **Unstoppable**: Powered by IPFS and Phala's 35k+ decentralized TEE workers

## Getting Started

***

### Prepare

Clone git repo or use [degit](https://www.npmjs.com/package/degit) to get the source code.

{% tabs %}
{% tab title="git" %}
```sh
git clone https://github.com/Phala-Network/ai-agent-template-langchain.git
```
{% endtab %}

{% tab title="degit" %}
```sh
npx degit github:Phala-Network/ai-agent-template-langchain#main ai-agent-template-langchain
```
{% endtab %}
{% endtabs %}

Install dependencies

```shell
npm install
```

### Testing Locally

Create `.env` file and add your OpenAI API Key

```shell
cp .env.local .env
```

In `.env` file replace `YOUR_OPENAI_KEY` with your API Key

```
OPENAI_API_KEY="YOUR_OPENAI_KEY"
```

Build your Agent

```shell
npm run build
```

Test your Agent locally

```shell
npm run test
```

Expected Test Results

```shell
User: Who are you?
    Answer:
GET RESULT: {
  status: 200,
  body: '\n' +
    '    <!DOCTYPE html>\n' +
    '    <html lang="en">\n' +
    '        <head>\n' +
    '            <meta charset="utf-8" />\n' +
    '            <title>TestUI</title>\n' +
    '        </head>\n' +
    '        <body>\n' +
    '            <div align="center">\n' +
    '                <p>I am Marvin Tong, a blockchain enthusiast and advocate for decentralized technologies.</p>\n' +
    '            </div>\n' +
    '        </body>\n' +
    '    </html>',
  headers: {
    'Content-Type': 'text/html; charset=UTF-8',
    'Access-Control-Allow-Origin': '*'
  }
}

User: What the latest direction of Phala?
    Answer:
POST RESULT: {
  status: 200,
  body: '\n' +
    '    <!DOCTYPE html>\n' +
    '    <html lang="en">\n' +
    '        <head>\n' +
    '            <meta charset="utf-8" />\n' +
    '            <title>TestUI</title>\n' +
    '        </head>\n' +
    '        <body>\n' +
    '            <div align="center">\n' +
    '                <p>The latest direction of Phala includes introducing AI Agent Contracts, hosting AI agents with Phala Network like smart contracts to build a Multi-Agents World. They are also incorporating a host runtime from RiscZero to their js runtime, marking a milestone for TEE+ZKP multi-prover strategy. Additionally, they are actively engaging with other platforms like binance for potential listings and offering bounties for finding runtime bugs. Overall, Phala is focused on pushing the boundaries of decentralized AI services and innovation in the Web3 space.</p>\n' +
    '            </div>\n' +
    '        </body>\n' +
    '    </html>',
  headers: {
    'Content-Type': 'text/html; charset=UTF-8',
    'Access-Control-Allow-Origin': '*'
  }
}
```

### Publish Your AI Agent

Upload your compiled AI Agent code to IPFS.

```shell
npm run publish
```

Upon a successful upload, the command should show the URL to access your AI Agent.

> AI Agent deployed at: https://agents.phala.network/ipfs/QmQu9AmBL13tyGpxgg5ASt96WQ669p63rnJRWiAo9st8ns/0
>
> Make sure to add your secrets to ensure your AI Agent works properly.

<details>

<summary>New to thirdweb?</summary>

We use [thirdweb Storage](https://thirdweb.com/dashboard/infrastructure/storage) to host IPFS contents. If you are new to thirdweb, the command will guide you to create your account or login to your existing account from the browser. (You may need to forward port 8976 if you are accessing a remote console via SSH.)

</details>

### Access the Published AI Agent

Once published, your AI Agent is available at the URL: `https://agents.phala.network/ipfs/<your-cid>`. You can get it from the "Publish to IPFS" step.

You can test it with `curl`.

```bash
curl https://agents.phala.network/ipfs/<your-cid>
```

### Add Secrets

By default, all the compiled JS code is visible for anyone to view if they look at IPFS CID. This makes private info like API keys, signer keys, etc. vulnerable to be stolen. To protect devs from leaking keys, we have added a field called `secret` in the `Request` object. It allows you to store secrets in a vault for your AI-Agent to access.

#### How to Add Secrets

The steps to add a `secret` is simple. We will add the [OpenAI](https://platform.openai.com/docs/quickstart?context=node) API Key in this example by creating a secret JSON object with the `openaiApiKey`:

```json
{"openaiApiKey": "<OPENAI_API_KEY>"}
```

Then in your frame code, you will be able to access the secret key via `req.secret` object:

```js
async function POST(req: Request): Promise<Response> {
    const apiKey = req.secret?.openaiApiKey
}
```

**Note**: Before continuing, make sure to publish your compiled AI-Agent JS code, so you can add secrets to the CID.

**Open terminal** Use `curl` to `POST` your secrets to `https://agents.phala.network/vaults`. Replace `IPFS_CID` with the CID to the compile JS code in IPFS, and replace `<OPENAI_API_KEY>` with your OpenAI API key.

> Note that you can name the secret field name something other than `openaiApiKey`, but you will need to access the key in your `index.ts` file with the syntax `req.secret?.<your-secret-field-name> as string`

The command will look like this:

```shell
curl https://agents.phala.network/vaults -H 'Content-Type: application/json' -d '{"cid": "IPFS_CID", "data": {"openaiApiKey": "<OPENAI_API_KEY>"}}'
# Output:
# {"token":"e85ae53d2ba4ca8d","key":"e781ef31210e0362","succeed":true}
```

The API returns a `token` and a `key`. The `key` is the id of your secret. It can be used to specify which secret you are going to pass to your frame. The `token` can be used by the developer to access the raw secret. You should never leak the `token`.

To verify the secret, run the following command where `key` and `token` are replaced with the values from adding your `secret` to the vault.

```shell
curl https://agents.phala.network/vaults/<key>/<token>
```

Expected output:

```shell
{"data":{"openaiApiKey":"<OPENAI_API_KEY>"},"succeed":true}
```

If you are using secrets, make sure that your URL is set in the following syntax where `cid` is the IPFS CID of your compiled JS file and `key` is the `key` from adding secrets to your vault.

```
https://agents.phala.network/ipfs/<cid>?key=<key>
```

Example: [https://agents.phala.network/ipfs/QmQu9AmBL13tyGpxgg5ASt96WQ669p63rnJRWiAo9st8ns/0?key=c0c0105ba56276cd\&chatQuery=When%20did%20humans%20land%20on%20the%20moon](https://frames.phatfn.xyz/ipfs/QmQu9AmBL13tyGpxgg5ASt96WQ669p63rnJRWiAo9st8ns/0?key=c0c0105ba56276cd\&chatQuery=When%20did%20humans%20land%20on%20the%20moon)

### Access Queries

To help create custom logic, we have an array variable named `queries` that can be accessed in the `Request` class. To access the `queries` array variable `chatQuery` value at index `0`, the syntax will look as follows:

```
const query = req.queries.chatQuery[0] as string;
```

The example at [https://agents.phala.network/ipfs/Qma2WjqWqW8wYG2tEQ9YFUgyVrMDA9VzvkkdeFny7Smn3R/0?key=686df81d326fa5f2\&chatQuery=When%20did%20humans%20land%20on%20the%20moon](https://agents.phala.network/ipfs/Qma2WjqWqW8wYG2tEQ9YFUgyVrMDA9VzvkkdeFny7Smn3R/0?key=686df81d326fa5f2\&chatQuery=When%20did%20humans%20land%20on%20the%20moon) will have a value of `When did humans land on the moon`. `queries` can have any field name, so `chatQuery` is just an example of a field name and not a mandatory name, but remember to update your `index.ts` file logic to use your expected field name.

## FAQ

<details>

<summary>What packages can I use in the ai-agent server?</summary>

* Most of the npm packages are supported: viem, onchainkit, ….
* Some packages with some advanced features are not supported:
  * Large code size. Compiled bundle should be less than 500kb.
  * Large memory usage, like image generation
  * Web Assembly
  * Browser only features: local storage, service workers, etc

</details>

<details>

<summary>What’s the spec of the Javascript runtime?</summary>

* The code runs inside a tailored [QuickJS engine](https://bellard.org/quickjs/)
* Available features: ES2023, async, fetch, setTimeout, setInterval, bigint
* Resource limits
  * Max execution time \~30s
  * Max memory usage: 16 mb
  * Max code size: 500 kb
  * Limited CPU burst: CPU time between async calls is limited. e.g. Too complex for-loop may hit the burst limit.

</details>

<details>

<summary>Why is the serverless platform secure?</summary>

* Your AI-Agent code on is fully secure, private, and permissionless. Nobody can manipulate your program, steal any data from it, or censor it.
* Security: The code is executed in the decentralized TEE network running on Phala Network. It runs code inside a secure blackbox (called enclave) created by the CPU. It generates cryptographic proofs verifiable on Phala blockchain. It proves that the hosted code is exactly the one you deployed.
* Privacy: You can safely put secrets like API keys or user privacy on Phala Network. The code runs inside TEE hardware blackboxs. The memory of the program is fully encrypted by the TEE. It blocks any unauthorized access to your data.
* Learn more at [Phala Network Homepage](https://phala.network)

</details>

<details>

<summary>What's TEE / Intel SGX?</summary>

* [TEE/SGX wiki](https://collective.flashbots.net/t/tee-sgx-wiki/2019)
* [Debunking TEE FUD: A Brief Defense of The Use of TEEs in Crypto](https://collective.flashbots.net/t/debunking-tee-fud-a-brief-defense-of-the-use-of-tees-in-crypto/2931)

</details>
