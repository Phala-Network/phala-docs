---
description: Host your AI Agent Contract on Phala's decentralized serverless cloud.
---

# Build Your AI Agent Contract with OpenAI

## [AI Agent Contract Template with OpenAI](https://github.com/Phala-Network/ai-agent-template-openai/tree/main)

### Architecture Overview

<figure><img src="../../.gitbook/assets/Screenshot 2024-04-04 at 11.02.11.png" alt=""><figcaption></figcaption></figure>

## 🤖 What Is This?!

***

<figure><img src="https://camo.githubusercontent.com/f987f154eda1f80db0292cec9244816487663790326499f66cca9d7262abee8f/68747470733a2f2f7777772e6a6c7772616e676c6572666f72756d732e636f6d2f666f72756d2f6174746163686d656e74732f7a6f6f6c616e6465722d6769662e3332353239392f" alt=""><figcaption></figcaption></figure>

The OpenAI AI Agent template is a **MINIMAL** template to build an AI Agent that can be hosted on Phala Network's decentralized hosting protocol. Unlike Vercel or other FaaS, it allows you to publish your AI Agent compiled code to IPFS and hosts it on a fully decentralized FaaS cloud with the following benefits:

* 💨 Ship Fast: Build and ship with familiar toolchain in minutes
* ⛑️ Secure: Execution guarded by rock solid TEE / Intel SGX
* 🔒 Private: Host API keys and user privacy at ease
* 💎 Unstoppable: Powered by IPFS and Phala's 35k+ decentralized TEE workers

## Getting Started

***

### Prepare

Clone git repo or use [degit](https://www.npmjs.com/package/degit) to get the source code.

{% tabs %}
{% tab title="git" %}
```sh
git clone https://github.com/Phala-Network/ai-agent-template-openai.git
```
{% endtab %}

{% tab title="degit" %}
```sh
npx degit github:Phala-Network/ai-agent-template-openai#main ai-agent-template-openai
```
{% endtab %}
{% endtabs %}

Install dependencies

```
npm install
```

### Testing Locally

Create `.env` file and add your OpenAI API Key

```
cp .env.local .env
```

In `.env` file replace `YOUR_OPENAI_KEY` with your API Key

```
OPENAI_API_KEY="YOUR_OPENAI_KEY"
```

Build your Agent

```
npm run build
```

Test your Agent locally

```
npm run test
```

Expected Test Results

```

> phat-gpt-template@0.0.1 test
> tsx src/test.ts

INPUT: {"method":"GET","path":"/ipfs/QmVHbLYhhYA5z6yKpQr4JWr3D54EhbSsh7e7BFAAyrkkMf","queries":{"chatQuery":["Who are you?"],"openAiModel":["gpt-4o"]},"secret":{"openaiApiKey":"OPENAI_API_KEY"},"headers":{}}
GET RESULT: {
  status: 200,
  body: '\n' +
    '    <!DOCTYPE html>\n' +
    '    <html lang="en">\n' +
    '        <head>\n' +
    '            <meta charset="utf-8" />\n' +
    '            <title>AI Agent Contract Demo UI</title>\n' +
    '        </head>\n' +
    '        <body>\n' +
    '            <div align="center">\n' +
    '                <p>"OpenAI AI Agent Contract hosted on <a href="https://github.com/Phala-Network/ai-agent-template-openai">Phala Network</a>, an AI Coprocessor for hosting AI Agents."</p>\n' +
    '                <img src="https://i.imgur.com/8B3igON.png" width="600" alt="AI Agent Contract" />\n' +
    '                <p>I am an AI language model created by OpenAI, designed to assist with information, answer questions, and provide support on a wide range of topics. How can I help you today?</p>\n' +
    '            </div>\n' +
    '        </body>\n' +
    '    </html>',
  headers: {
    'Content-Type': 'text/html; charset=UTF-8',
    'Access-Control-Allow-Origin': '*'
  }
}
INPUT: {"method":"POST","path":"/ipfs/QmVHbLYhhYA5z6yKpQr4JWr3D54EhbSsh7e7BFAAyrkkMf","queries":{"chatQuery":["When did humans land on the moon?"],"openAiModel":["gpt-4o"]},"secret":{"openaiApiKey":"OPENAI_API_KEY"},"headers":{},"body":"{\"untrustedData\":{\"fid\":2,\"url\":\"https://fcpolls.com/polls/1\",\"messageHash\":\"0xd2b1ddc6c88e865a33cb1a565e0058d757042974\",\"timestamp\":1706243218,\"network\":1,\"buttonIndex\":2,\"castId\":{\"fid\":226,\"hash\":\"0xa48dd46161d8e57725f5e26e34ec19c13ff7f3b9\"}},\"trustedData\":{\"messageBytes\":\"d2b1ddc6c88e865a33cb1a565e0058d757042974...\"}}"}
POST RESULT: {
  status: 200,
  body: 'Not Implemented',
  headers: {
    'Content-Type': 'text/html; charset=UTF-8',
    'Access-Control-Allow-Origin': '*'
  }
}

To test in the SideVM playground go to https://phat.phala.network/contracts/view/0xf0a398600f02ea9b47a86c59aed61387e450e2a99cb8b921cd1d46f734e45409

Connect you polkadot.js account and select 'run_js' with the parameters:
- engine: SidevmQuickJSWithPolyfill
- js_code: Source code text of dist/index.ts
- args: {"method":"GET","path":"/ipfs/QmVHbLYhhYA5z6yKpQr4JWr3D54EhbSsh7e7BFAAyrkkMf","queries":{"chatQuery":["Who are you?"],"openAiModel":["gpt-4o"]},"secret":{"openaiApiKey":"OPENAI_API_KEY"},"headers":{}}
Watch video here for to see the visual steps of testing in Sidevm playground: https://www.youtube.com/watch?v=fNqNeLfFFME

Make sure to replace queries and secret with your values compatible with your AI Agent Contract.
```

#### Test in Sidevm Playground

{% embed url="https://youtu.be/fNqNeLfFFME" %}

### Publish Your AI Agent

Upload your compiled AI Agent code to IPFS.

```bash
npm run publish-agent
```

Upon a successful upload, the command should show the URL to access your AI Agent.

```
> phat-gpt-template@0.0.1 publish-agent
> phat-fn build --experimentalAsync && tsx scripts/publish.ts

✓ Compiled successfully.
  72.73 KB  dist/index.js

    $$\     $$\       $$\                 $$\                         $$\       
    $$ |    $$ |      \__|                $$ |                        $$ |      
  $$$$$$\   $$$$$$$\  $$\  $$$$$$\   $$$$$$$ |$$\  $$\  $$\  $$$$$$\  $$$$$$$\  
  \_$$  _|  $$  __$$\ $$ |$$  __$$\ $$  __$$ |$$ | $$ | $$ |$$  __$$\ $$  __$$\ 
    $$ |    $$ |  $$ |$$ |$$ |  \__|$$ /  $$ |$$ | $$ | $$ |$$$$$$$$ |$$ |  $$ |
    $$ |$$\ $$ |  $$ |$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |  $$ |
    \$$$$  |$$ |  $$ |$$ |$$ |      \$$$$$$$ |\$$$$$\$$$$  |\$$$$$$$\ $$$$$$$  |
     \____/ \__|  \__|\__|\__|       \_______| \_____\____/  \_______|\_______/ 

 💎 thirdweb v0.14.12 💎

- Uploading file to IPFS. This may take a while depending on file sizes.

✔ Successfully uploaded file to IPFS.
✔ Files stored at the following IPFS URI: ipfs://QmayeZxHXwJxABXaNshP6j8uBE6RedkhmEgiaXd1w1Jib3
✔ Open this link to view your upload: https://bafybeif3y2jpswse2n6s2cikwyjmbak4cxlpm6vrmgobqkgsmmn34l6m4i.ipfs.cf-ipfs.com/

AI Agent Contract deployed at: https://agents.phala.network/ipfs/QmayeZxHXwJxABXaNshP6j8uBE6RedkhmEgiaXd1w1Jib3

Make sure to add your secrets to ensure your AI-Agent works properly.
```

<details>

<summary>New to thirdweb?</summary>

We use [thirdweb Storage](https://thirdweb.com/dashboard/infrastructure/storage) to host IPFS contents. If you are new to thirdweb, the command will guide you to create your account or login to your existing account from the browser. (You may need to forward port 8976 if you are accessing a remote console via SSH.)

</details>

### Access the Published AI Agent

Once published, your AI Agent is available at the URL:&#x20;

> `https://agents.phala.network/ipfs/<your-cid>`.&#x20;
>
> You can get it from the "Publish to IPFS" step.

You can test it with `curl`.

```
curl https://agents.phala.network.xyz/ipfs/<your-cid>
```

### Add Secrets

By default, all the compiled JS code is visible for anyone to view if they look at IPFS CID. This makes private info like API keys, signer keys, etc. vulnerable to be stolen. To protect devs from leaking keys, we have added a field called `secret` in the `Request` object. It allows you to store secrets in a vault for your AI Agent to access.

#### How to Add Secrets

The steps to add a `secret` is simple. We will add the [OpenAI](https://platform.openai.com/docs/quickstart?context=node) API Key in this example by creating a secret JSON object with the `openaiApiKey`:

```json
{"openaiApiKey": "<OPENAI_API_KEY>"}
```

Then in your frame code, you will be able to access the secret key via `req.secret` object:

```js
async function GET(req: Request): Promise<Response> {
    const apiKey = req.secret?.openaiApiKey
}
```

**Note**: Before continuing, make sure to publish your compiled AI Agent JS code, so you can add secrets to the CID.

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

Example: [https://agents.phala.network/ipfs/Qma2WjqWqW8wYG2tEQ9YFUgyVrMDA9VzvkkdeFny7Smn3R/0?key=686df81d326fa5f2\&chatQuery=When%20did%20humans%20land%20on%20the%20moon](https://agents.phala.network/ipfs/Qma2WjqWqW8wYG2tEQ9YFUgyVrMDA9VzvkkdeFny7Smn3R/0?key=686df81d326fa5f2\&chatQuery=When%20did%20humans%20land%20on%20the%20moon)

### Access Queries

To help create custom logic, we have an array variable named `queries` that can be accessed in the `Request` class. To access the `queries` array variable `chatQuery` value at index `0`, the syntax will look as follows:

```
const query = req.queries.chatQuery[0] as string;
```

The example at [https://agents.phala.network/ipfs/Qma2WjqWqW8wYG2tEQ9YFUgyVrMDA9VzvkkdeFny7Smn3R/0?key=686df81d326fa5f2\&chatQuery=When%20did%20humans%20land%20on%20the%20moon](https://agents.phala.network/ipfs/Qma2WjqWqW8wYG2tEQ9YFUgyVrMDA9VzvkkdeFny7Smn3R/0?key=686df81d326fa5f2\&chatQuery=When%20did%20humans%20land%20on%20the%20moon) will have a value of `When did humans land on the moon`. `queries` can have any field name, so `chatQuery` is just an example of a field name and not a mandatory name, but remember to update your `index.ts` file logic to use your expected field name.

### FAQ

<details>

<summary>What packages can I use in the ai agent server?</summary>

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
  * Max execution time \~60s
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
