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

The LangChain AI Agent template is a **MINIMAL** template to build an AI Agent that can be hosted on Phala Network's decentralized hosting protocol. Unlike Vercel or other FaaS, it allows you to publish your AI Agent compiled code to IPFS and hosts it on a fully decentralized FaaS cloud with the following benefits:

* 💨 **Ship Fast**: Build and ship with familiar toolchain in minutes
* ⛑️ **Secure**: Execution guarded by rock solid TEE / Intel SGX
* 🔒 **Private**: Host API keys and user privacy at ease
* 💎 **Unstoppable**: Powered by IPFS and Phala's 35k+ decentralized TEE workers

## Getting Started

{% hint style="info" %}
For this template to work, you will need to signup for a developer account on OpenAI and get and [OpenAI API Key](https://platform.openai.com/account/api-keys).
{% endhint %}

### Prepare

Clone git repo or use [degit](https://www.npmjs.com/package/degit) to get the source code.

{% tabs %}
{% tab title="git" %}
```sh
git clone https://github.com/Phala-Network/ai-agent-template-langchain.git
```
{% endtab %}

{% tab title="degit" %}
```bash
npx degit github:Phala-Network/ai-agent-template-langchain#main ai-agent-template-langchain
```
{% endtab %}
{% endtabs %}

Install dependencies

```shell
npm install
```

### Testing Locally

Create `.env` file with the default ThirdWeb API key for publishing your Agent Contract to IPFS

```sh
cp .env.example .env
```

Build your Agent

```sh
npm run build
```

Test your Agent locally

```sh
npm run test
```

Expected Test Results

```sh
INPUT: {"method":"GET","path":"/ipfs/CID","queries":{"chatQuery":["Who are you?"]},"secret":{"openaiApiKey":"OPENAI_API_KEY"},"headers":{}}
GET RESULT: {
  status: 200,
  body: '{"message":"I am Marvin Tong, a thought leader and innovator specializing in blockchain, AI, and decentralized technologies. I often share insights and groundbreaking ideas about these fields on platforms like Twitter, collaborating with prominent names and organizations to advance the multi-agent world and decentralized ecosystems. My proposals aim to integrate AI agents into environments like Phala Network and future scenarios, leveraging technologies such as Zero-Knowledge Proofs (ZKP) and Trusted Execution Environments (TEE). My vision includes creating practical and impactful advancements that shape the future of technology, exemplified through my work and presentations at prominent events such as ETHDenver."}',
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }
}
INPUT: {"method":"GET","path":"/ipfs/CID","queries":{"chatQuery":["What the latest direction of Phala?"]},"secret":{"openaiApiKey":"OPENAI_API_KEY"},"headers":{}}
GET RESULT: {
  status: 200,
  body: `{"message":"The latest direction of Phala Network primarily revolves around enhancing and integrating secure, decentralized computation with privacy-preserving technologies. Here are some of the key pillars of their current focus:\\n\\n1. **Multi-Agent AI Integration**: Phala Network is pushing towards creating and hosting AI agents using secure smart contracts, fostering a Multi-Agent world where different agents can operate and interact in a decentralized, privacy-preserving manner.\\n\\n2. **TEE and ZK Proofs Combination**: Recently, Phala has made strides in integrating Trusted Execution Environments (TEE) with Zero-Knowledge Proofs (ZKP). This combination aims to fortify the privacy and security guarantees of decentralized computations, offering a robust multi-prover strategy.\\n\\n3. **Expansion into Financial Markets**: There is a community-driven effort to get $PHA listed on the Binance futures market, indicating Phala Network's ambition to capture a larger slice of the cryptocurrency financial market and increase token utility.\\n\\n4. **Bug Bounty Programs**: Security remains a top priority, with substantial bounties being offered (totaling $60,500) for identifying and resolving runtime bugs within Phala's network, ensuring the platform's resilience and reliability.\\n\\n5. **AI and Decentralized Services**: Phala Network is actively involved in the decentralized AI space. Their work at events like ETHDenver highlights their commitment to developing practical, real-world AI solutions that leverage decentralization for enhanced security and privacy.\\n\\n6. **Community Engagement and Development**: Phala Network continues to invest in its community, promoting collaborative projects, hackathons, and educational events to foster innovation and collective growth.\\n\\nThese directions underscore Phala Network's commitment to creating a secure, scalable, and user-friendly platform that integrates advanced privacy technologies into the heart of decentralized applications."}`,
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }
}
Now you are ready to publish your agent, add secrets, and interact with your agent in the following steps:
- Execute: 'npm run publish-agent'
- Set secrets: 'npm run set-secrets'
- Go to the url produced by setting the secrets (e.g. https://wapo-testnet.phala.network/ipfs/QmPQJD5zv3cYDRM25uGAVjLvXGNyQf9Vonz7rqkQB52Jae?key=b092532592cbd0cf)
```

### Publishing Your Agent

Upload your compiled AI Agent code to IPFS.

```sh
npm run publish-agent
```

Upon a successful upload, the command should show the URL to access your AI Agent.

```sh
Running command: npx thirdweb upload dist/index.js
This may require you to log into thirdweb and will take some time to publish to IPFS...

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
✔ Files stored at the following IPFS URI: ipfs://QmYzBTdQNPewdhD9GdBJ9TdV7LVhrh9YVRiV8aBup7qZGu
✔ Open this link to view your upload: https://b805a9b72767504353244e0422c2b5f9.ipfscdn.io/ipfs/bafybeie6giqpm4fmxt4vzdfi6jlbxxlvjlal3cm57auubgcmuvm7xcqtli/

Agent Contract deployed at: https://wapo-testnet.phala.network/ipfs/QmYzBTdQNPewdhD9GdBJ9TdV7LVhrh9YVRiV8aBup7qZGu

If your agent requires secrets, ensure to do the following:
1) Edit the ./secrets/default.json file or create a new JSON file in the ./secrets folder and add your secrets to it.
2) Run command: 'npm run set-secrets' or 'npm run set-secrets [path-to-json-file]'
Logs folder created.
Deployment information updated in ./logs/latestDeployment.json
```

{% hint style="info" %}


**Note** that your latest deployment information will be logged to in file [`./logs/latestDeployment.json`](https://github.com/Phala-Network/ai-agent-template-redpill/blob/main/logs/latestDeployment.json). This file is updated every time you publish a new Agent Contract to IPFS. This file is also used to get the IPFS CID of your Agent Contract when setting secrets for your Agent Contract.

Here is an example:

```
{
  "date": "2024-08-29T18:47:55.108Z",
  "cid": "QmaUbZgNz9dZ5eGm87DDqegRtcBV7RdosxizYQcfe2bHRc",
  "url": "https://wapo-testnet.phala.network/ipfs/QmaUbZgNz9dZ5eGm87DDqegRtcBV7RdosxizYQcfe2bHRc"
}
```
{% endhint %}

{% hint style="warning" %}


**Did Thirdweb fail to publish?**

If ThirdWeb fails to publish, please signup for your own ThirdWeb account to publish your Agent Contract to IPFS. Signup or login at [https://thirdweb.com/dashboard/](https://thirdweb.com/dashboard/)

Whenever you log into ThirdWeb, create a new API key and replace the default API Key with yours in the [.env](https://github.com/Phala-Network/ai-agent-template-redpill/blob/main/.env) file.

```
THIRDWEB_API_KEY="YOUR_THIRDWEB_API_KEY"
```
{% endhint %}

### Accessing The Published Agent

Once published, your AI Agent is available at the URL: `https://wapo-testnet.phala.network/ipfs/<your-cid>`. You can get it from the "Publish to IPFS" step.

You can test it with `curl`.

```sh
curl https://wapo-testnet.phala.network/ipfs/<your-cid>
```

### Adding Secrets

By default, all the compiled JS code is visible for anyone to view if they look at IPFS CID. This makes private info like API keys, signer keys, etc. vulnerable to be stolen. To protect devs from leaking keys, we have added a field called `secret` in the `Request` object. It allows you to store secrets in a vault for your AI Agent to access.

To add your secrets,

1. Edit the [default.json](https://github.com/Phala-Network/ai-agent-template-redpill/blob/main/secrets/default.json) file or create a new JSON file in the `./secrets` folder and add your secrets to it.

```sh
{
  "apiKey": "YOUR_OPENAI_API_KEY"
}
```

2. Run command to set the secrets

```sh
npm run set-secrets
# or if you have a custom JSON file
npm run set-secrets <path-to-json-file>
```

Expected output:

```sh
Use default secrets...
Storing secrets...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   199    0    68  100   131    121    234 --:--:-- --:--:-- --:--:--   356
{"token":"5d9faaed6be5414a","key":"a3a8a4ef2c057d5c","succeed":true}

Secrets set successfully. Go to the URL below to interact with your agent:
https://wapo-testnet.phala.network/ipfs/QmaUbZgNz9dZ5eGm87DDqegRtcBV7RdosxizYQcfe2bHRc?key=a3a8a4ef2c057d5c
Log entry added to secrets.log
```

{% hint style="info" %}
**Note** that all your secrets will be logged in file [`./logs/secrets.log`](https://github.com/Phala-Network/ai-agent-template-redpill/blob/main/logs/secrets.log). This file is updated every time you add new secrets to your Agent Contract. If you have not published an Agent Contract, yet, this command will fail since there is not a CID to map the secrets to.

Here is an example:

```sh
2024-08-29T18:54:16.643Z, CID: [QmaUbZgNz9dZ5eGm87DDqegRtcBV7RdosxizYQcfe2bHRc], Token: [5d9faaed6be5414a], Key: [a3a8a4ef2c057d5c], URL: [https://wapo-testnet.phala.network/ipfs/QmaUbZgNz9dZ5eGm87DDqegRtcBV7RdosxizYQcfe2bHRc?key=a3a8a4ef2c057d5c]
```
{% endhint %}

The API returns a `token` and a `key`. The `key` is the id of your secret. It can be used to specify which secret you are going to pass to your frame. The `token` can be used by the developer to access the raw secret. You should never leak the `token`.

To verify the secret, run the following command where `key` and `token` are replaced with the values from adding your `secret` to the vault.

```sh
curl https://wapo-testnet.phala.network/vaults/<key>/<token>
```

Expected output:

```sh
{"data":{"openaiApiKey":"<OPENAI_API_KEY>"},"succeed":true}
```

### Accessing Queries

To help create custom logic, we have an array variable named `queries` that can be accessed in the `Request` class. To access the `queries` array variable `chatQuery` value at index `0`, the syntax will look as follows:

```sh
const query = req.queries.chatQuery[0] as string;
```

Here is an example of adding a URL query named `chatQuery` with a value of `Who are you`. `queries` can have any field name, so `chatQuery` is just an example of a field name and not a mandatory name, but remember to update your `index.ts` file logic to use your expected field name.

> &#x20;[https://wapo-testnet.phala.network/ipfs/QmYzBTdQNPewdhD9GdBJ9TdV7LVhrh9YVRiV8aBup7qZGu?key=815cab7189f6110e&<mark style="background-color:yellow;">chatQuery</mark>=Who%20are%20you](https://wapo-testnet.phala.network/ipfs/QmYzBTdQNPewdhD9GdBJ9TdV7LVhrh9YVRiV8aBup7qZGu?key=815cab7189f6110e\&chatQuery=Who%20are%20you)&#x20;

### Debugging Your Agent

To debug your agent, you can use the following command:

```
curl https://wapo-testnet.phala.network/logs/all/ipfs/<CID>
```

After executing this command then you should see some output in the terminal to show the logs of requests to your agent.

```
2024-09-04T03:18:34.758Z [95f5ec53-3d71-4bb5-bbb6-66065211102c] [REPORT] END Request: Duration: 166ms
2024-09-04T03:18:34.758Z [95f5ec53-3d71-4bb5-bbb6-66065211102c] [INFO] 'Is signature valid? ' true
2024-09-04T03:18:34.758Z [95f5ec53-3d71-4bb5-bbb6-66065211102c] [INFO] 'Verifying Signature with PublicKey ' '0xC1BF8dB4D06416c43Aca3deB289CF7CC0aAFF540'
2024-09-04T03:18:34.758Z [95f5ec53-3d71-4bb5-bbb6-66065211102c] [REPORT] START Request: GET /ipfs/QmfLpQjxAMsppUX9og7xpmfSKZAZ8zuWJV5g42DmpASSWz?key=0e26a64a1e805bfd&type=verify&data=tintinland%20message%20to%20sign&signature=0x34c4d8c83406e7a292ecc940d60b34c9b11024db10a8872c753b9711cd6dbc8f746da8be9bc2ae0898ebf8f49f48c2ff4ba2a851143c3e4b371647eed32f707b1b
2024-09-04T03:17:15.238Z [768b6fda-f9f1-463f-86bd-a948e002bf80] [REPORT] END Request: Duration: 183ms
2024-09-04T03:17:15.238Z [768b6fda-f9f1-463f-86bd-a948e002bf80] [INFO] 'Signature: 0x34c4d8c83406e7a292ecc940d60b34c9b11024db10a8872c753b9711cd6dbc8f746da8be9bc2ae0898ebf8f49f48c2ff4ba2a851143c3e4b371647eed32f707b1b'
2024-09-04T03:17:15.238Z [768b6fda-f9f1-463f-86bd-a948e002bf80] [INFO] 'Signing data [tintinland message to sign] with Account [0xC1BF8dB4D06416c43Aca3deB289CF7CC0aAFF540]'
2024-09-04T03:17:15.238Z [768b6fda-f9f1-463f-86bd-a948e002bf80] [REPORT] START Request: GET /ipfs/QmfLpQjxAMsppUX9og7xpmfSKZAZ8zuWJV5g42DmpASSWz?key=0e26a64a1e805bfd&type=sign&data=tintinland%20message%20to%20sign
2024-09-04T03:16:38.507Z [3717d307-bff0-4fc0-bc98-8f66c33dd46f] [REPORT] END Request: Duration: 169ms
2024-09-04T03:16:38.507Z [3717d307-bff0-4fc0-bc98-8f66c33dd46f] [REPORT] START Request: GET /ipfs/QmfLpQjxAMsppUX9og7xpmfSKZAZ8zuWJV5g42DmpASSWz?key=0e26a64a1e805bfd
2024-09-04T03:15:00.375Z [793f58f9-f24f-4580-8ebc-04debb7d727f] [REPORT] END Request: Duration: 158ms
2024-09-04T03:15:00.375Z [793f58f9-f24f-4580-8ebc-04debb7d727f] [REPORT] START Request: GET /ipfs/QmfLpQjxAMsppUX9og7xpmfSKZAZ8zuWJV5g42DmpASSWz?key=0e26a64
a1e805bfd
```

To create logs in your Agent Contract, you can use the following syntax in your `index.ts` file.

```
// info logs
console.log('info log message!')
// error logs
console.error('error log message!')
```

For more information check the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/API/console) on `console` object.
