---
description: >-
  Phat Contracts are the programs running off-chain on Phala Network that
  developers can use to implement a broad range of features for their dApps.
cover: ../../.gitbook/assets/phat-contract-banner.png
coverY: 0
---

# Phat Contract Introduction

## Why bring computation Off-Chain?

Performing computation on-chain is difficult and expensive, and for robust dApp use-cases the level of computation needed is often simply impossible to do on-chain. Smart Contracts are an essential component of any decentralized application, but the challenges posed by doing work on-chain limit their functionality. For example, Smart Contracts cannot easily perform actions across different blockchains, nor can they interface directly with the internet hence the need for bridges and oracles. Furthermore, Smart Contracts are incredibly limited in the intensity of the computation they can perform, and any program running on-chain can’t produce results until consensus is reached.

## Phat Contracts vs. Smart Contracts

Given the stark technical constraints of building on-chain, it’s generally optimal to keep the on-chain contracts as small and compact as possible, and implement the more robust logic off-chain.

Phat Contracts are run on a tamper-proof distributed network that uses the Phala blockchain to always ensure the fidelity of deployed contracts and their execution. This allows Phat Contracts to circumvent the limitations of Smart Contracts _**while retaining**_ trustlessness, verifiability, and permisionlessness.

Phat Contracts are not meant to replace Smart Contracts, instead, they are the missing decentralized computation unit for decentralized applications. Explore all of Phat Contracts features here.

## A Developer Experience for Everyone

Users can build and deploy Phat Contract in a few different ways.

* [**Phat Bricks**](../bricks-and-blueprints/)
  * Our no-code experience for Phat Contract, developers can choose from a library of pre-fabricated solutions to deploy and integrate with their dApp in minutes.
* [**Native Phat Contact**](../build-on-phat-contract/)
  * For developers with a background in Rust, ink!, typescript, or Javascript looking for a more customizable developer experience, Native Phat Contract is the tool for you.
