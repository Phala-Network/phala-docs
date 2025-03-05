# 👩‍💻 Getting Started

## Introduction

This chapter provides detailed technical information on the Confidential AI Inference, designed to ensure confidentiality, integrity, and verifiability of AI inference tasks. We use the TEE technologies provided by NVIDIA GPU TEE and Intel TDX to secure AI workloads, allowing developers to easily deploy their LLMs in a secure environment.

## Overview

Confidential inference addresses critical concerns such as data privacy, secure execution, and computation verifiability, making it indispensable for sensitive applications. As illustrated in the diagram below, people currently cannot fully trust the responses returned by LLMs from services like OpenAI or Meta, due to the lack of cryptographic verification. By running the LLM inside a TEE, we can add verification primitives alongside the returned response, known as a Remote Attestation (RA) Report. This allows users to verify the AI generation results locally without relying on any third parties.

<figure><img src="../.gitbook/assets/compare-llm-with-tee-or-not.png" alt=""><figcaption></figcaption></figure>

## Getting Started

We provide a public API endpoint for you to get the TEE attestation report and chat with the private AI.

### Get TEE Attestation Report

Send a GET request to https://inference-api.phala.network/v1/attestation/report to get the TEE attestation report.

The response will be like:

```sh
{
  "signing_address": "...",
  "nvidia_payload": "...",
  "intel_quote": "..."
}
```

The `signing_address` is the account address generated inside TEE that will be used to sign the chat response. You can go to https://etherscan.io/verifiedSignatures, click Verify Signature, and paste the `signing_address` and message response to verify it.

`nvidia_payload` and `intel_quote` are the attestation report from NVIDIA TEE and Intel TEE respectively. You can use them to verify the integrity of the TEE. See [Verify the Attestation](confidential-AI-API.md#verify-the-attestation) for more details.

### Chat With Private AI

We provide OpenAI-compatible API for you to send chat request to the LLM running inside TEE, where you just need to replace the API endpoint to `https://platform.openai.com/docs/api-reference/chat`.

Check the [confidential-AI-API.md](confidential-AI-API.md "mention") for more information.

Check the [host-LLM-in-TEE.md](host-LLM-in-TEE.md "mention") for how to host your own private LLM in TEE.

Check the [implementation.md](implementation.md "mention") for the technical details of the Confidential AI Inference.

## References

1. [HCC-Whitepaper](https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/HCC-Whitepaper-v1.0.pdf)
2. [Intel SGX DCAP Orientation](https://www.intel.com/content/dam/develop/public/us/en/documents/intel-sgx-dcap-ecdsa-orientation.pdf)
3. [Phala's dcap-qvl](https://github.com/Phala-Network/dcap-qvl)
4. [Automata's Solidity Implementation](https://github.com/automata-network/automata-dcap-attestation)
5. [Phala Nvidia H200 TEE Benchmark Paper](https://arxiv.org/pdf/2409.03992)
6. [Phala DeRoT Post on FlashBots forum](https://collective.flashbots.net/t/early-thoughts-on-decentralized-root-of-trust/3868)
7. [Phala Key Management Protocol Post on Flashbots forum](https://collective.flashbots.net/t/key-management-protocol-for-decentralized-root-of-trust/4004)
