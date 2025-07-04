# ETHGlobal San Francisco

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

## Phala Hackathon Guide at ETHGlobal San Francisco

Welcome to the Phala Hackathon Guide! This guide will provide you with all the necessary information to get started building on our platform. Whether you're a seasoned developer or new to the ecosystem, this guide will help you navigate through the essential steps and resources to build on our TEE Docker SDK.

{% hint style="info" %}
Check out the an TEE Docker SDK we deployed called the [TEE Docker SDK Cheat Sheet](https://bit.ly/dstack-cheat-sheet)!
{% endhint %}

### Introduction

Welcome to the Hackathon guide for Phala's TEE Docker SDK. If you are a Docker expert then this new developer-friendly SDK is your oyster. You now have the ability to deploy your docker containers within a TEE and utilize the JS & Python SDKs to have TEE functions to do:

* **Remote Attestations**

{% tabs %}
{% tab title="JS SDK" %}
<pre class="language-typescript"><code class="lang-typescript"><strong>// Tappd Client
</strong><strong>const client = new TappdClient(endpoint)
</strong><strong>// Remote Attestation
</strong>const getRemoteAttestation = await client.tdxQuote('dataString')
</code></pre>
{% endtab %}

{% tab title="Python SDK" %}
```python
# Tappd Client
client = AsyncTappdClient(endpoint)
# Remote Attestation
result = await client.tdx_quote('dataString')
```
{% endtab %}
{% endtabs %}

* **Derive Key Account**

{% tabs %}
{% tab title="JS SDK" %}
```typescript
// Tappd Client
const client = new TappdClient(endpoint)
// Derive Key Account
const randomDeriveKey = await client.deriveKey('/', 'dataString')
```
{% endtab %}

{% tab title="Python SDK" %}
```python
# Tappd Client
client = AsyncTappdClient(endpoint)
# Derive Key Account
result = await client.derive_key('/', 'dataString')
```
{% endtab %}
{% endtabs %}

### Requirements

* [node](https://nodejs.org/en) >= v18.18.x or [python](https://www.python.org/) 3
* [Docker](https://www.docker.com/) or [OrbStack](https://docs.orbstack.dev/quick-start) for local docker deployments with a TEE Attestation simulator

### Getting Started <a href="#getting-started" id="getting-started"></a>

{% tabs %}
{% tab title="JS SDK" %}


First, run the TEE Attestation Simulator:

```bash
docker run --rm -p 8090:8090 phalanetwork/tappd-simulator:v0.0.1
```

Next, download the dependencies with `yarn`

```shell
yarn
```

Build the docker image

```shell
docker build -t nextjs-viem-dstack-template .
```

After the build is successful, run your docker image to connect to the TEE Attestation Simulator

> **NOTE**: Your docker image hash will be different than the one listed below.

```shell
docker run --rm -p 3000:3000 61a7efb8f25c
```

Now you can go to your browser and see a frontend UI like below:

<figure><img src="../../.gitbook/assets/image (9) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Python SDK" %}
Run the TEE Remote Attestation Simulator:

```bash
docker run --rm -p 8090:8090 phalanetwork/tappd-simulator:latest
```

Build the python docker container:

```bash
docker build -t python-dstack-template .
```

Run the python docker container:

```bash
docker run --rm -p 3000:3000 -e DSTACK_SIMULATOR_ENDPOINT='http://host.docker.internal:8090' [python-docker-image-hash]
```

Now make a request to get the remote attesation and derived key account

```bash
curl http://127.0.0.1:3000
```
{% endtab %}
{% endtabs %}

### Ideas to Build

With the ability to deploy docker in TEE, you are now free to use Phala as your base to exploring the many different prizes available at [ETH Global](https://ethglobal.com/events/sanfrancisco2024/prizes/).

* **Web2 in, Web3 out**
  * Build a product that takes a Web2 technology and make it Web3 with the use of TEE functions Remote Attestation & Derive Key Account
  * Encumber Web2 Accounts for delegated access
  * Bind Web2 business logic onchain
* **What Do You Meme-coin??**
  * Build an innovative product that solves a key memecoin funnel issue and convert users to your memecoins easier
  * Launch a unique memecoin that aims to solve something for a good cause
  * Create the end all, be all of memecoins that will last decades down the road
* **Use AI to enhance the Web3 Experience**
  * Run the many LLMs written in python and available on [huggingface](https://huggingface.co/)
  * Build a competitor to the infamous AI memecoins with an objective to provide misinformation to the competition, and surpass the current leaders in AI memecoins
  * Train your own small LLM and push attestations onchain for proof of training, etc.
* **Launch Verifiable Products**
  * Use Remote Attestation and Derive Key Account signatures to harden the connection between a user and onchain smart contracts
  * Add AI to be able to detect if a frontend is malicious or not
  * Build a product for data provenance based on attested data pipelines







