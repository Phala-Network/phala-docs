---
description: >-
  A limitless oracle that is scalable, cheap, and easy to deploy with a familiar
  developer experience.
---

# ✨ Phat Contract Starter Kit

The Phat Contract Starter Kit is your one-stop solution to connect any API to your smart contract. It offers wide-ranging support for all EVM-compatible blockchains, including but not limited to Ethereum, Polygon, Arbitrum, Avalanche, Binance Smart Chain, Optimism, and zkSync.

<figure><img src="../../../.gitbook/assets/case-self-owned-oracles.jpg" alt=""><figcaption></figcaption></figure>

This starter kit empowers you to initiate the data request from the smart contract side. The request is then seamlessly sent to your script for processing. You have the liberty to call any APIs to fulfill the request and define the response data structure that will be replied to your smart contract.

### Features <a href="#features" id="features"></a>

* Wide support for all mainstream blockchains
*   **Verifiable and decentralized**: every Oracle is running on decentralized infrastructure that require no operations and can be easily verified\


    <figure><img src="../../../.gitbook/assets/RA-Attested-Verifiable.png" alt=""><figcaption></figcaption></figure>
*   **Support private data**: your Oracle state is protected by cryptography and hardware\


    <figure><img src="../../../.gitbook/assets/Cross-chain-e2ee.png" alt=""><figcaption></figcaption></figure>
* **No extra cost**: the only cost is the gas fee of response data which is sent as a transaction
* **High frequency**: the request is synced to Oracle within one minute, and the latency of response is only limited by blockchain’s block interval

### Use cases & Examples <a href="#use-cases--examples" id="use-cases--examples"></a>

You could use the Oracle to:

* [**Create a Telegram / Discord trading bot with Phat Contract**](https://github.com/pacoyang/phatbot)
* [**Cross-chain DEX Aggregator**](file:///Users/hashwarlock/Projects/Phala/phat-contract-starter-kit/assets/case-cross-chain-dex-aggregator.jpg)
* [**Bring Web2 services & data on-chain**](file:///Users/hashwarlock/Projects/Phala/phat-contract-starter-kit/assets/case-contract-controlled-web2-service.jpg)
* **Web3 Social Integrations**
  * [**LensAPI Oracle**](https://github.com/Phala-Network/lensapi-oracle-consumer-contract)
  * [**Lens Phite**](https://github.com/aeyshubh/lens-Phite2)
  * [**Mint NFT based on LensAPI Oracle data**](file:///Users/hashwarlock/Projects/Phala/phat-contract-starter-kit/assets/LensAPI-Oracle.png)
  * [**Lens Treasure Hunt**](https://github.com/HashWarlock/lensapi-oracle-devdao-workshop)
* [**Get Randomness on-chain from drand.love and post with Telegram bot**](https://github.com/HashWarlock/phat-drand-tg-bot)
* **Trustless HTTPS requests w/** [**TLSNotary**](https://tlsnotary.org/) **integration**
* [**Connect to Phat Contract Rust SDK**](file:///Users/hashwarlock/Projects/Phala/phat-contract-starter-kit/assets/Oracle-Rust-SDK.png) to access all features

### Resources <a href="#resources" id="resources"></a>

* [**What’s Oracle**](https://ethereum.org/en/developers/docs/oracles/)
* **Frontend Templates**
  * [**Scaffold ETH2**](https://github.com/scaffold-eth/scaffold-eth-2)
    * [**Phat Scaffold ETH2**](https://github.com/HashWarlock/phat-scaffold-eth)
  * [**Create ETH App**](https://github.com/paulrberg/create-eth-app)
  * [**Nexth Starter Kit**](https://nexth.vercel.app/)
* [**Technical design doc**](https://github.com/Phala-Network/phat-offchain-rollup)
