# Build Your First AI Agent Contract

If you like video tutorials, here is one of our latest workshops on building your first AI Agent Contract. In this tutorial, you will learn:

* How to get an OpenAI API Key at https://red-pill.ai&#x20;
* Clone the AI Agent Contract template repo
* Build and test your Agent Script
* Launch and interact with your Agent Script through the Phala Agent Gateway

{% embed url="https://youtu.be/XX7NCKi7Y2I?si=GRORzY9acBDcy6UY" %}

<figure><img src="../../.gitbook/assets/AI-Agent-Contract-Execution.png" alt=""><figcaption><p>Agent Script executes in TEE Agent VM on Phala Network</p></figcaption></figure>

The RedPill AI Agent template is a **MINIMAL** template to build an AI Agent that can be hosted on Phala Network's decentralized hosting protocol. Unlike Vercel or other FaaS, it allows you to publish your AI Agent compiled code to IPFS and hosts it on a fully decentralized FaaS cloud with the following benefits:

* 💨 **Ship Fast**: Build and ship with familiar toolchain in minutes
* ⛑️ **Secure**: Execution guarded by rock solid TEE / Intel SGX
* 🔒 **Private**: Host API keys and user privacy at ease
* 💎 **Unstoppable**: Powered by IPFS and Phala's 35k+ decentralized TEE workers

This guide will focus on the following topics:

* **Build** and **Deploy** Your AI Agent Contract
  * Build and deploy your **Agent Contract** that is deployed to IPFS and served through the Phala Agent Gateway executed on Phala Network
* **Use**/**Interact** with Your AI Agent Contract
  * The Agent Gateway will fetch the Agent Contract code/prompt located on IPFS.
  * Interact with your agent hosted through Phala's Agent Gateway (https://wapo-testnet.phala.network/ipfs/\<CID>).

## Getting Started

### Prepare

Clone git repo or use [degit](https://www.npmjs.com/package/degit) to get the source code.

{% tabs %}
{% tab title="git" %}
```sh
git clone https://github.com/Phala-Network/ai-agent-template-redpill.git
```
{% endtab %}

{% tab title="degit" %}
```bash
npx degit github:Phala-Network/ai-agent-template-redpill#main ai-agent-template-redpill
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

Get an API Key from Redpill

> **Note**
>
> There is a default RedPill API Key provided in the .env.example file. This API key is rate limited and if you run into an error that displays `Insufficient funds`, reach out to the Phala Team on [discord](https://discord.gg/phala-network).
>
> * Go to [https://red-pill.ai/dashboard](https://red-pill.ai/dashboard) and claim your API Key by swapping some ETH for wGPT at [https://app.uniswap.org/explore/tokens/base/0x74F62Bc1961028C22b8080961c6534f4eDD49D6C](https://app.uniswap.org/explore/tokens/base/0x74F62Bc1961028C22b8080961c6534f4eDD49D6C)
> * Video Tutorial: [https://youtu.be/ZoJwbLNhbWE](https://youtu.be/ZoJwbLNhbWE)

In [default.json](https://github.com/Phala-Network/ai-agent-template-redpill/blob/main/secrets/default.json) file replace `YOUR_API_KEY` with your API Key. The default has a rate limit. If you want access to a RedPill code, reach out to the Phala Team.

```json
{
  "apiKey": "YOUR_REDPILL_API_KEY"
}
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
INPUT: {"method":"GET","path":"/ipfs/CID","queries":{"chatQuery":["Who are you?"],"model":["gpt-4o"]},"secret":{"apiKey":"sk-D3rWzPAe16RIB8r8GptK9vi6ozuYEnHY4Lpg2L2lap465ROo"},"headers":{}}
{"apiKey":"sk-D3rWzPAe16RIB8r8GptK9vi6ozuYEnHY4Lpg2L2lap465ROo"}
GET RESULT: {
  status: 200,
  body: `{"message":"I'm an AI language model created by OpenAI, here to help answer your questions and provide information on a wide range of topics. How can I assist you today?"}`,
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
✓ Compiled successfully.
  1.51 KB  dist/index.js
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
✔ Files stored at the following IPFS URI: ipfs://QmaUbZgNz9dZ5eGm87DDqegRtcBV7RdosxizYQcfe2bHRc
✔ Open this link to view your upload: https://b805a9b72767504353244e0422c2b5f9.ipfscdn.io/ipfs/bafybeifukvkuyztltpq2gi55nswzvwkpgrwrogwykm4ymoqeymh2pxoukm/

Agent Contract deployed at: https://wapo-testnet.phala.network/ipfs/QmaUbZgNz9dZ5eGm87DDqegRtcBV7RdosxizYQcfe2bHRc

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
  "apiKey": "YOUR_REDPILL_API_KEY"
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
{"data":{"apiKey":"<REDPILL_API_KEY>"},"succeed":true}

```

### Accessing Queries

To help create custom logic, we have an array variable named `queries` that can be accessed in the `Request` class. To access the `queries` array variable `chatQuery` value at index `0`, the syntax will look as follows:

```sh
const query = req.queries.chatQuery[0] as string;
```

Here is an example of adding a URL query named `chatQuery` with a value of `When did humans land on the moon`. `queries` can have any field name, so `chatQuery` is just an example of a field name and not a mandatory name, but remember to update your `index.ts` file logic to use your expected field name.

> [https://wapo-testnet.phala.network/ipfs/Qmc7EDq1X8rfYGGfHyXZ6xsmcSUWQcqsDoeRMfmvFujih3?key=51f265212c26086c&<mark style="background-color:yellow;">**chatQuery**</mark>=When%20did%20humans%20land%20on%20the%20moon](https://wapo-testnet.phala.network/ipfs/Qmc7EDq1X8rfYGGfHyXZ6xsmcSUWQcqsDoeRMfmvFujih3?key=51f265212c26086c\&chatQuery=When%20did%20humans%20land%20on%20the%20moon)

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

Congratulations! You have deployed and interacted with your first AI Agent Contract on Phala Network! Now let's move to a more Web3-centric agent to execute transactions onchain by importing  the [Viem SDK](https://viem.sh) into the AI Agent Contract.
