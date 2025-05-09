# 👩‍💻 Host LLM in GPU TEE

## Overview

Private AI or called confidential AI addresses critical concerns such as data privacy, secure execution, and computation verifiability, making it indispensable for sensitive applications. As illustrated in the diagram below, people currently cannot fully trust the responses returned by LLMs from services like OpenAI or Meta, due to the lack of cryptographic verification. By running the LLM inside a TEE, we can add verification primitives alongside the returned response, known as a Remote Attestation (RA) Report. This allows users to verify the AI generation results locally without relying on any third parties.

<figure><img src="../.gitbook/assets/compare-llm-with-tee-or-not.png" alt=""><figcaption></figcaption></figure>

## Implementation

The implementation for running LLMs in GPU TEE is available in the [private-ml-sdk](https://github.com/nearai/private-ml-sdk) GitHub repository. This project is built by Phala Network and was made possible through a grant from NEARAI. The SDK provides the necessary tools and infrastructure to deploy and run LLMs securely within GPU TEE.

<figure><img src="../.gitbook/assets/private-ml-sdk.png" alt=""><figcaption></figcaption></figure>

## References

1. [HCC-Whitepaper](https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/HCC-Whitepaper-v1.0.pdf)
2. [Intel SGX DCAP Orientation](https://www.intel.com/content/dam/develop/public/us/en/documents/intel-sgx-dcap-ecdsa-orientation.pdf)
3. [Phala's dcap-qvl](https://github.com/Phala-Network/dcap-qvl)
4. [Automata's Solidity Implementation](https://github.com/automata-network/automata-dcap-attestation)
5. [Phala Nvidia H200 TEE Benchmark Paper](https://arxiv.org/pdf/2409.03992)
6. [Phala DeRoT Post on FlashBots forum](https://collective.flashbots.net/t/early-thoughts-on-decentralized-root-of-trust/3868)
7. [Phala Key Management Protocol Post on Flashbots forum](https://collective.flashbots.net/t/key-management-protocol-for-decentralized-root-of-trust/4004)
8. [Private ML SDK](https://github.com/nearai/private-ml-sdk)
