# 👩‍💻 Getting Started

{% hint style="danger" %}
WARNING: AI Agent Contract Docs are now legacy documentation that will not be maintained moving forward. We recommend using [Dstack](broken-reference) instead to build on Phala Network.
{% endhint %}



<figure><img src="../../.gitbook/assets/AI-Agent-Contract.png" alt=""><figcaption></figcaption></figure>

## AI Agent Contract Overview

The AI Agent Contract is a general-purpose program written in TypeScript/JavaScript that is executed in a TEE (Trusted Execution Environment) on Phala's blockchain. Let's breakdown the process from a developers perspective.

* A developer builds their Agent Contract and publishes their code to IPFS.
* The Agent Contract is served through a gateway where users can make HTTP requests to the deployed agent.
* Phala's Agent Gateway will pull the script from IPFS by fetching the CID and executing the request in a TEE node on Phala's blockchain.

A visualization of the architecture is displayed below:

<figure><img src="../../.gitbook/assets/AI-Agent-Contract-Execution (1).png" alt=""><figcaption></figcaption></figure>