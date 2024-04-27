# Build Your First AI Agent Contract

In this guide you will learn about the two components that make up AI Agent Contract:

* The "**Agent Script**": Prompts and code written in TypeScript/JavaScript to define the agent running on Phala Network.
* The "**Agent DAO**": Regulates the Agent Script's access keys, tokenomic, access control, and market. The Agent DAO is deployed on a Smart Contract EVM Chains.

<figure><img src="../../.gitbook/assets/AI-Agent-Contract-Components.png" alt=""><figcaption><p>Agent DAO regulates Agent Script</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/AI-Agent-Contract-Execution.png" alt=""><figcaption><p>Agent Script executes in TEE Agent VM on Phala Network</p></figcaption></figure>

The diagrams above shows the architecture of the AI Agent Contract with the first diagram showing the Agent DAO regulates the Agent Script. Then the second diagram shows how the Agent Script is executed on Phala Network's serverless backend.&#x20;

This guide will focus on the following topics:

* **Build** Your AI Agent Contract
  * Build your **Agent Script** that is deployed to IPFS and served through the Phala Agent Gateway executed on Phala Network.
  * Build your **Agent DAO** to "**regulate**" your deployed agent by enabling access control through access keys for communication, governance, tokenomics, and optionally run token-gating logic.
* **Launch** Your AI Agent Contract
  * Deploy your Agent DAO to an EVM Chain.
  * The Agent DAO will store where the Agent Script code/prompt is located on IPFS.
    * Automatically host on the Phala Agent Gateway (https://agents.phala.network/\<chain>/\<contract-id>).
    * Subscribe to external agents for cross-communication.
* **Use**/Interact with Your AI Agent Contract
