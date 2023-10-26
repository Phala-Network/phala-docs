---
description: >-
  Phat Contracts are the programs running off-chain on Phala Network that
  developers can use to implement a broad range of features for their dApps.
cover: ../../.gitbook/assets/phat-contract-banner.png
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# 🟩 Phat Contract Introduction

## Why bring computation Off-Chain?

On-chain computation has severe limitations and is often prohibitively expensive. For example, Smart Contracts cannot easily perform actions across different blockchains, nor can they interface directly with off-chain data sources hence the need for bridges and oracles. Furthermore, use cases like Smart Contract automation require input from programs running off-chain. For these reasons, robust dApp use cases generally demand that a significant portion of the stack be off-chain.

## Phat Contracts vs. Smart Contracts

Given the stark technical constraints of building on-chain, it’s generally optimal to keep the on-chain contracts as small and compact as possible, and implement the more robust logic off-chain.

Phat Contracts are run on a tamper-proof distributed network that uses the Phala blockchain to always ensure the fidelity of deployed contracts and their execution. This allows Phat Contracts to circumvent the limitations of Smart Contracts _**while retaining**_ trustlessness, verifiability, and permissionlessness.

Phat Contracts are not meant to replace Smart Contracts, instead, they are the missing decentralized computation unit for decentralized applications.

## A Developer Experience for Everyone

Users can build and deploy a Phat Contract in a few different ways depending on their needs and ability.

### [**Phat Contract 2.0**](../bricks-and-blueprints/)

Phat Contract 2.0 allows developers to write scripts to deploy as a Phat Contract in TypeScript. This allows for your deployed script to respond to data requests initiated from the on-chain smart contract side. The request is transparently sent to your script for processing. You are free to call any APIs to fulfill the request. Finally, you can freely define the response data structure that will be replied to your smart contract.

### [**Phat Contract Rust SDK**](../build-on-phat-contract/)

For developers with a background in Rust, [ink!](https://use.ink) looking for a more customizable developer experience, the Phat Contract Rust SDK is the tool for you.
