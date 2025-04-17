# 👩‍💻 Getting Started

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}



<figure><img src="../../.gitbook/assets/AI-Agent-Contract.png" alt=""><figcaption></figcaption></figure>

## AI Agent Contract Overview

The AI Agent Contract is a general-purpose program written in TypeScript/JavaScript that is executed in a TEE (Trusted Execution Environment) on Phala's blockchain. Let's breakdown the process from a developers perspective.

* A developer builds their Agent Contract and publishes their code to IPFS.
* The Agent Contract is served through a gateway where users can make HTTP requests to the deployed agent.
* Phala's Agent Gateway will pull the script from IPFS by fetching the CID and executing the request in a TEE node on Phala's blockchain.

A visualization of the architecture is displayed below:

<figure><img src="../../.gitbook/assets/AI-Agent-Contract-Execution (1).png" alt=""><figcaption></figcaption></figure>
