# Phat Contract

## What is Phat Contract <a href="#what-is-phat-contract" id="what-is-phat-contract"></a>

Phat Contract is an innovative programming model enabling [_Off-chain Computation_](https://medium.com/phala-network/fat-contract-introduce-off-chain-computation-to-smart-contract-dfc5839d5fb8). It’s also known as Fat Contract as a practice of the “Fat Protocol & Thin Application” concept, and for its rich functionalities compared with existing smart contracts. Phat Contract uses Rust-based [ink! language](https://paritytech.github.io/ink/).

> **Hint**
>
> Every Phat contract is naturally a _distributed_ program since it has multiple instances across every worker in a cluster. All these instances can handle the users' requests concurrently, but they can also cause troubles when they try to update the contract state at the same time.
>
> This is why we recommend beginners to start with building stateless applications which is free of the problems above.

<figure><img src="../../.gitbook/assets/phat-offchain-comp.png" alt=""><figcaption></figcaption></figure>

Although with the name of “contract”, Phat Contract is more like the Web3 version of [Amazon Lambda](https://aws.amazon.com/lambda/) backed by the decentralized Phala computing cloud and meant to support complex computation with low latency and cost.

You can easily deploy your Phat contract to multiple workers in Phala Network, with each instance handling users' requests in parallel. The contract is running in Secure Enclave, and all its states and input/output are transparently encrypted.

Phat Contract is not meant to replace the smart contracts, instead, it tries to be the missing decentralized computation unit for them. For example, instead of implementing an [ERC-20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) token with Phat Contract (whose balance has to be stored on-chain), we recommend deploying your ERC-20 contract on Ethereum and using Phat Contract to operate it.

## When will you need it <a href="#when-will-you-need-it" id="when-will-you-need-it"></a>

> When a single smart contract is not ENOUGH for your DApp, implement the rest logic with Phat Contract.

Since the on-chain storage and execution can be expensive (from both monetary and performance perspectives), it’s reasonable to keep the on-chain contract small and compact and implement the other logic elsewhere. The existing DApps usually implement their own backend logic as normal programs and deploy them to centralized services like AWS (Amazon Web Services).

<figure><img src="../../.gitbook/assets/web2-stack.png" alt=""><figcaption></figcaption></figure>

With the computing service from Phala and its Phat Contract, you can run your backend programs on a decentralized infrastructure with privacy, performance, and low cost.

<figure><img src="../../.gitbook/assets/web3-stack.png" alt=""><figcaption></figcaption></figure>
