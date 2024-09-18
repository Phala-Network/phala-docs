# ETHGlobal Hackathon Guide

## Phala Hackathon Guide at ETHGlobal Singapore

Welcome to the Phala Hackathon Guide! This guide will provide you with all the necessary information to get started building on our platform. Whether you're a seasoned developer or new to the ecosystem, this guide will help you navigate through the essential steps and resources.

### Introduction

The Phala Hackathon Guide will take you through the steps to build and deploy AI Agent Contracts. In this guide we will guide you through acquiring an OpenAI API Key through [RedPill](https://red-pill.ai/), set up an Agent Contract template to deploy and interact with, and learn a **new paradigm in transacting onchain** Agent Contract Template + Viem SDK where you can derive an ECDSA account within a TEE and utilize the account to sign/verify messages and transact on any EVM chain. These guides will provide the basic tools to start building on Phala Network.

**Note**: You can use any LLM API for your Agent Contract. You are not limited to only use RedPill. Also, the WapoJS Engine .

### Prizes

We have exciting prizes for the top project:

1. 1st Place: $3,000 + Ledger Nano X
2. 2nd Place: $1,500 + TEE Swag
3. 3rd Place: $500 + TEE Swag

**Bonus Bounty**: Reach the ETHGlobal finals, and you’ll snag another Ledger Nano X on us!

How to qualify for as a top project?

* (Strong Consideration) Integrate [Agent Contract with the Viem SDK](https://github.com/Phala-Network/ai-agent-contract-viem) to interact on-chain with any EVM Chain or other sponsor projects at ETHGlobal to create a unique product.
* (Strong Consideration) Build an AI x Web3 product with [RedPill Agent Contract Template](https://github.com/Phala-Network/ai-agent-template-redpill) or any other AI related templates we support located in our [docs](https://docs.phala.network/ai-agent-contract/getting-started/ai-agent-contract-templates)
* Deploy any custom Agent Contract that can be interacted with via HTTP requests

Each winner will get access to a Tier 2 Swag Bag provided by the Phala Team

### Important Dates

* **Hackathon Start**: September 20th
* **Submission Deadline**: September 22nd
* **Judging Period**: \[Judging Period]
* **Winners Announcement**: September 22nd

### Getting Started

To get started with Phala Network, follow these steps:

1. Determine what type of Agent Template build on:

* **Take the RedPill and access top AI LLMs**: Get an API Key on [RedPill](https://red-pill.ai/). (This requires a code to get access. Reach out to the Phala Team to get access. In the meantime, use the free developer API key that is rate limited.)
* **Try a New Paradigm in Transacting Onchain**: Build on the [viem Agent Contract Template](https://github.com/Phala-Network/ai-agent-contract-viem) where you can derive an account within a TEE and utilize the account to transact on any EVM chain.

2. **Explore Documentation**: Familiarize yourself with our [Developer Documentation](https://docs.phala.network/).
3. **Join the Community**: Connect with other developers on our [Discord Server](https://discord.gg/phala-network).

### Get API Key on RedPill

If you want to use the global hackathon RedPill API key, here are the details:

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
-d '{ "model": "gpt-3.5-turbo", "messages": [ { "role": "user", "content": "Hello world!" } ], "temperature": 1 }'
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

### Resources

Here are some additional resources to assist you:

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
