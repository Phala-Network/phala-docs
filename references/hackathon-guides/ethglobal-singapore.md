# ETHGlobal Singapore

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

## Phala Hackathon Guide at ETHGlobal Singapore

Welcome to the Phala Hackathon Guide! This guide will provide you with all the necessary information to get started building on our platform. Whether you're a seasoned developer or new to the ecosystem, this guide will help you navigate through the essential steps and resources for build on Phala's Agent Contract.

{% hint style="info" %}
Check out the an Agent Contract we deployed called the [TEE Cheat Sheet](https://bit.ly/tee-cheat-sheet)!

* If you want to know how to host HTML pages with hono, check out the Agent Contract template [here](https://github.com/Phala-Network/ai-agent-template-hono-html).
{% endhint %}

### Introduction

Welcome to the Hackathon guide for Phala's Agent Contracts. We are offering you the **key** to connecting to multiple sponsor's bounties through our general-purpose program executing in a TEE (Trusted Execution) on Phala Network at **ZERO** cost & **NO** new wallet required.

**Why is Agent Contract Built DIFFERENT?!**

* &#x20;💨 **Ship Fast**: Build and ship with familiar toolchain in minutes
* &#x20;⛑️ **Secure**: Execution guarded by rock solid TEE
* &#x20;🔒 **Private**: Host API keys and user privacy at ease
* 💎 **Unstoppable**: Powered by IPFS and Phala's 40k+ decentralized TEE workers
* :fire: [**hono/tiny**](https://hono.dev/docs/api/presets#hono-tiny) **Support**: a small, simple, and ultrafast web framework built on Web Standards.
* 🧪 [**Vite Test Framework**](https://vitest.dev/guide/): Vite Testing Framework support, but you're free to change the test framework to your desire.

Here are our feature templates:

* [RedPill Agent Contract](https://github.com/Phala-Network/ai-agent-template-redpill) - Get your [FREE RedPill API Key](https://red-pill.ai/ethglobal) and access top LLMs from OpenAI, Anthropic, Meta, Gwen, Mistral, and Google to create a Web3 x AI project for the hackathon.
* [Viem SDK Agent Contract](https://github.com/Phala-Network/ai-agent-contract-viem) - Learn about a **new paradigm in transacting onchain** with the [Viem SDK](https://viem.sh) Agent Contract Template with key features to:
  * Derive an ECDSA account within a TEE
  * Sign/Verify Data with the derived account
  * Transact on any EVM chain

### Prizes

We have exciting prizes for the top project:

1. **1st Place**: $3,000 + Ledger Nano X
2. **2nd Place**: $1,500 + TEE Swag
3. **3rd Place**: $500 + TEE Swag

**Bonus Bounty**: Reach the ETHGlobal finals, and you’ll snag another Ledger Nano X on us!

How to qualify for as a top project?

* (Strong Consideration) Integrate [Agent Contract with the Viem SDK](https://github.com/Phala-Network/ai-agent-contract-viem) to interact on-chain with any EVM Chain or other sponsor projects at ETHGlobal to create a unique product.
* (Strong Consideration) Build an AI x Web3 product with [RedPill Agent Contract Template](https://github.com/Phala-Network/ai-agent-template-redpill) or any other AI related templates we support located in our [docs](https://docs.phala.network/ai-agent-contract/getting-started/ai-agent-contract-templates)
* Deploy any custom Agent Contract that can be interacted with via HTTP requests

### Important Dates

* **Hackathon Start**: September 20th
* **Submission Deadline**: September 22nd 9am
* **Judging Period**: 2 Hours and 30 Minutes
* **Winners Announcement**: September 22nd 3pm

### Getting Started

To get started with Phala Network

* **Take the RedPill and access top AI LLMs**: Get an API Key on [RedPill](https://red-pill.ai/ethglobal). This requires a code to get access. Reach out to the Phala Team to get access. In the meantime, use the free developer API key that is rate limited.
* **Try a New Paradigm in Transacting Onchain**: Build on the [viem Agent Contract Template](https://github.com/Phala-Network/ai-agent-contract-viem) where you can derive an account within a TEE and utilize the account to transact on any EVM chain.
* **Choose from a** [**List of Agent Contract Templates**](../../ai-agent-contract-legacy/getting-started/ai-agent-contract-templates.md) or build a custom Agent Contract that connect to any API or uses an SDK of your choosing!
* **Explore Documentation**: Familiarize yourself with our [Developer Documentation](https://docs.phala.network/).
* **Join the Community**: Connect with other developers on our [Discord Server](https://discord.gg/phala-network).

### Get API Key on RedPill

If you want to use the global hackathon RedPill API key, here are the details:

* Create a FREE API Key at [https://red-pill.ai/ethglobal](https://red-pill.ai/ethglobal)&#x20;
* Free Rate-Limited API Key
  * API Endpoint URL: [https://api.red-pill.ai/](https://api.red-pill.ai/)
  * API Key: `sk-qVBlJkO3e99t81623PsB0zHookSQJxU360gDMooLenN01gv2`
* Doc: [https://docs.red-pill.ai/getting-started/how-to-use](https://docs.red-pill.ai/getting-started/how-to-use)
* Supported Models: [https://docs.red-pill.ai/get-started/list-models](https://docs.red-pill.ai/get-started/list-models)

Before you start building, you'll need to set up your development environment. Here are the prerequisites:

1. **Node.js**: Install the latest version of Node.js from [nodejs.org](https://nodejs.org/).
2. **Code Editor**: Any code editor will work. We recommend using [Visual Studio Code](https://code.visualstudio.com/).

#### Test RedPill API

```
curl https://api.red-pill.ai/v1/chat/completions
-H "Content-Type: application/json"
-H "Authorization: Bearer <YOUR_REDPILL_API_KEY>"
-d '{ "model": "o1-preview", "messages": [ { "role": "user", "content": "Hello world!" } ], "temperature": 1 }'
```

### Set Up Your First Agent Contract

To set up your first Agent Contract, you can follow these resources:

* **A New Paradigm in Transacting Onchain**
  * **Viem SDK Template (Derive ECDSA Keys, Sign/Verify Data, Send TX)**: [AI Agent Contract Viem Template](https://github.com/Phala-Network/ai-agent-contract-viem)
* **AI Related Templates**
  * **RedPill Template**: [Build Your First AI Agent Contract](https://github.com/Phala-Network/ai-agent-template-redpill)
  * **OpenAI Template**: [Build Your AI Agent Contract with OpenAI](https://github.com/Phala-Network/ai-agent-template-openai)
  * **Anthropic Template**: [Anthropic Template Repo](https://github.com/Phala-Network/ai-agent-template-anthropic)
  * **LangChain**: [Build Your Agent Contract with LangChain](https://github.com/Phala-Network/ai-agent-template-langchain)
  * **Function Calling**: [Create a Weather Agent with Function Calling](https://github.com/Phala-Network/ai-agent-template-func-calling)
    * GitHub Repository: [AI Agent Template with Function Calling](https://github.com/Phala-Network/ai-agent-template-func-calling)
  * [**Brian**](https://www.brianknows.org/app/) **Template**: [Brian Agent Contract Template](https://github.com/Phala-Network/ai-agent-template-brian)
  * [**'mbd.xyz**](https://console.mbd.xyz/dashboard) **Template**: ['mbd.xyz Agent Contract Template](https://github.com/Phala-Network/ai-agent-template-mbd)
  * [**Chainbase**](https://console.chainbase.com/) **Template**: [Chainbase Agent Contract Template](https://github.com/Phala-Network/ai-agent-template-chainbase)
* **Frontend Hosting Template**
  * [**Hono HTML Agent Contract Template**](https://github.com/Phala-Network/ai-agent-template-hono-html)

### Getting Rugged By The WiFi?!

Run a local testnet with [`docker` support](https://docs.docker.com/desktop/). All you need to do to get a local testnet started is run:

{% hint style="danger" %}
Running the local testnet may return an error if port **`8000`** is already in use.
{% endhint %}

```shell
npm run dev
```

**Make a Request to Your Local Build**

```shell
# GET request
curl http://127.0.0.1:8000/local
# GET request with URL queries
curl http://127.0.0.1:8000/local?query1=one&query2=two
# POST request
curl http://127.0.0.1:8000/local -X POST -H 'content-type: application/json' -d '{"foo": "bar"}'
```

**Add Secrets to Your Local Build**

```shell
curl http://127.0.0.1:8000/vaults -H 'Content-Type: application/json' -d '{"cid": "local", "data": {"secretKey":"secretValue"}}'
```

**Check The Logs of Your Local Build**

```shell
curl 'http://127.0.0.1:8000/logs/all/local'
```

### Resources

Here are some additional resources to assist you:

* [**Hono Docs**](https://hono.dev/docs/api/presets#hono-tiny)
  * We recommend using [@hono/tiny](https://hono.dev/docs/api/presets#hono-tiny) to avoid a large bundle size and the 20MB final artifact limitation.
* [**Vite Test Framework**](https://vitest.dev/guide/)
* **Docs**: [Developer Documentation](https://docs.phala.network/ai-agent-contract/getting-started/build-your-first-ai-agent-contract)
  * [**Supported WapoJS Functions**](https://docs.phala.network/tech-specs/ai-agent-contract/wapojs-functions)
* **Workshop**: [Video](https://www.youtube.com/watch?v=APcuWVdqJ2U)
* **Tech Specs**: [Agent Contract Tech Specs](https://docs.phala.network/tech-specs/ai-agent-contract#wapojs)

### Support

If you need help, we're here for you:

* [Discord](https://discord.gg/phala-network): Join our Discord Server for real-time support.
* Forum: Post your questions on our Community Forum.
* [FAQ](https://docs.phala.network/ai-agent-contract/faq): Agent Contract development FAQ

We can't wait to see what you build at the Phala Hackathon. Happy coding!

***

### Best Practices

To ensure a smooth development experience and to make the most out of the Phala platform, consider the following best practices:

1. **Modular Code**: Write modular and reusable code to enhance maintainability.
2. **Security First**: Always prioritize security, especially when dealing with sensitive data.
3. **Documentation**: Document your code and APIs thoroughly to help others understand and contribute.
4. **Testing**: Implement comprehensive testing to catch bugs early and ensure reliability.
5. **Community Engagement**: Engage with the community to get feedback and improve your project.

### Submission Guidelines

To submit your project for the hackathon, follow these steps:

1. **Prepare Your Project**: Ensure your project is complete and well-documented.
2. **Create a Repository**: Host your project on GitHub or any other version control platform.
3. **Demo Video**: Include a short demo video showcasing your project and its features.

### Judging Criteria

Projects will be judged based on the following criteria:

1. **Technical excellence**: How smoothly everything works
2. **UX and design**: How great everything feels
3. **Potential impact**: How it is going to make the world a better place
4. **Wow factor**: How it would become the next big thing
5. **Business model**: How it would generate ROI

### Contact Us

If you have any questions or need further assistance, feel free to reach out:

* **Email**: [support@phala.network](mailto:support@phala.network)
* **Discord**: Join our [Discord Server](https://discord.gg/phala-network)
* **Forum**: Visit our [Community Forum](https://forum.phala.network/)

Thank you for participating in the Phala Hackathon. We look forward to seeing your innovative solutions and wish you the best of luck!

***

_Phala Network Team_
