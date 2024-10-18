# ETHGlobal SF Hackathon Guide

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

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>
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







