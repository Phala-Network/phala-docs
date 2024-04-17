# ⚖️ Scale Blockchains with AI Coprocessor

## Background

Phala's journey into this new domain began with the advent of [AutoGPT](https://news.agpt.co/) and [Langchain](https://www.langchain.com/), catalyzed by [OpenAI](https://openai.com/)'s release of the [GPT-4](https://chat.openai.com/) model. This model wasn't just another step in AI's evolution; it was a giant leap towards creating entities that could not only understand and execute complex tasks but do so continuously, learning and adapting from each iteration. Here lay the foundation of an agent – not just a program, but a digital being capable of acting autonomously on behalf of its user.

## Why AI x Blockchain/Crypto?

With the advancements of autonomous AI Agents, a new paradigm had started to form, and thought leaders in Blockchain started to realize the potential synergies that AI x Blockchain can offer. For example, [Vitalik's blog post](https://vitalik.eth.limo/general/2024/01/30/cryptoai.html) about AI x Blockchain sparked a new realization. AI Agents can serve as an intelligent interface to Blockchain, and help AI understand the blockchain world while ensuring their behavior (i.e. signed messages and transactions) matches their intentions and avoid being tricked or scammed.

<figure><img src="../.gitbook/assets/AIxBlockchain.png" alt=""><figcaption><p>Diagram from Vitalk's Blog</p></figcaption></figure>

In this intersection of AI x Blockchain, AI Agents are missing some key elements that Blockchain could solve given the right architecture. Phala's Blockchain-TEE hybrid system has the answer to make AI Agents act like Smart Contracts by providing the following features for AI Agents:

* Hosted on decentralized platform to ensure service availability.
* Governed by smart contracts. This involves prompt management and access control.
* Free to call each other to form complex applications, while the callers need to cover the cost during callee execution.
* The secrecy of prompts are protected by TEE.
* Highly user interactive with low latency requirements and require no gas fee.

All of these leads to a system that allow AI Agents to run in TEE workers, but are fully controlled by on-chain smart contracts. This is what Phala is good at.

## The Phala Network Advantage

<figure><img src="../.gitbook/assets/AI-Agent-DePIN (1).png" alt=""><figcaption></figcaption></figure>

The key value proposition Phala offers for AI Agents:

* **Agentize** **Blockchain**: create AI Agents for popular web3 services and smart contracts
* **Decentralized and Private by Default**: Powered by the largest TEE network, fully transparent & privacy preserving
* **Easily Funded**: Get funded on Agent Wars with innovation ideas
* **Powerful**: Code in fully customizable Javascript & WASM runtime
* **Rich Integration**: OpenAI, LangChain, [io.net](http://io.net/), etc
