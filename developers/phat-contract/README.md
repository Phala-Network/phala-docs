---
description: >-
  Phat Contracts are the programs running off-chain on Phala Network that
  developers can use to implement a broad range of features for their dApps.
cover: ../../.gitbook/assets/phat-contract-banner.png
coverY: 0
---

# Phat Contract Introduction

## Why bring computation Off-Chain?

On-chain computation has severe limitations and is often prohibitively expensive. For example, Smart Contracts cannot easily perform actions across different blockchains, nor can they interface directly with off-chain data sources hence the need for bridges and oracles. Furthermore, use cases like Smart Contract automation require input from programs running off-chain. For these reasons, robust dApp use cases generally demand that a significant portion of the stack be off-chain.&#x20;

## Phat Contracts vs. Smart Contracts

Given the stark technical constraints of building on-chain, it’s generally optimal to keep the on-chain contracts as small and compact as possible, and implement the more robust logic off-chain.

Phat Contracts are run on a tamper-proof distributed network that uses the Phala blockchain to always ensure the fidelity of deployed contracts and their execution. This allows Phat Contracts to circumvent the limitations of Smart Contracts _**while retaining**_ trustlessness, verifiability, and permisionlessness.

Phat Contracts are not meant to replace Smart Contracts, instead, they are the missing decentralized computation unit for decentralized applications.&#x20;

## A Developer Experience for Everyone

Users can build and deploy Phat Contract in a few different ways depending on their needs and ability.&#x20;

### [**Phat Bricks**](../bricks-and-blueprints/)

The no-code experience for Phat Contract, Phat Bricks allows developers can choose from a library of pre-fabricated solutions to deploy and integrate with their dApp in minutes.

### [**Native Phat Contact**](../build-on-phat-contract/)

For developers with a background in Rust, ink!, typescript, or Javascript looking for a more customizable developer experience, Native Phat Contract is the tool for you.
