# 🔐 GPU TEE

The implementation for running LLMs in GPU TEE is available in the [private-ml-sdk](https://github.com/nearai/private-ml-sdk) GitHub repository. This project is built by Phala Network and was made possible through a grant from NEARAI. The SDK provides the necessary tools and infrastructure to deploy and run LLMs securely within GPU TEE.

<figure><img src="../../.gitbook/assets/private-ml-sdk.png" alt=""><figcaption></figcaption></figure>

## Introduction

A TEE as a general hardware-based confidential computation infrastructure can offer a practical solution compared to other cryptographic methods like ZK and FHE in AI Inference:

* The computational overhead is significantly lower, with nearly native speed of execution
* Verification using TEEs is also more economical compared to ZKPs. An ECDSA signature suffices for on-chain verification, reducing the complexity and cost of ensuring computation integrity.
* NVIDIA's series of GPUs such as H100 and H200 natively support TEEs, providing hardware-accelerated secure environments for AI workloads. This native support ensures seamless integration and optimized performance for AI fine-tuning and inference.

<figure><img src="../../.gitbook/assets/confidential-ai-inference-overview.png" alt=""><figcaption></figcaption></figure>

Our TEE-based solution can provide following features for AI Inference:

1. **Tamper-Proof Data**: Ensuring that user request/response data cannot be altered by a middleman is fundamental. This necessitates secure communication channels and robust encryption mechanisms.
2. **Secure Execution Environment**: Both hardware and software must be protected against attacks. This involves leveraging TEE that provides isolated environments for secure computation.
3. **Open Source and Reproducible Builds**: The entire software stack, from the operating system to the application code must be reproducible. This allows auditors to verify the integrity of the system.
4. **Verifiable Execution Results**: The results of AI computations must be verifiable, ensuring that the outputs are trustworthy and have not been tampered with.

## Study Cases

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Host DeepSeek-R1 in GPU TEE</strong></td><td><a href="https://phala.network/posts/absolute-0-ccp-use-deepseek-r1-with-gpu-tee-for-verified-ai-security">https://phala.network/posts/absolute-0-ccp-use-deepseek-r1-with-gpu-tee-for-verified-ai-security</a></td><td><a href="../../.gitbook/assets/host-deepseek-r1-in-gpu-tee.png">host-deepseek-r1-in-gpu-tee.png</a></td></tr></tbody></table>

## What's Next?

1. [**Host LLM in GPU TEE**](../../gpu-tee/llm-in-tee.md).
2. [**GPU TEE Inference API**](../../gpu-tee/inference-api.md)
3. [**Benchmark of running LLM in TEE**](../../gpu-tee/benchmark.md).
