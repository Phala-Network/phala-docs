# ⚡ Confidential AI Inference

TEE as a general hardware-based confidential computation infrastructure can offer a practical solution compared to other cryptographic methods like ZK and FHE in AI Inference:

- The computational overhead is significantly lower, with nearly native speed of execution
- Verification using TEEs is also more economical compared to ZKPs. An ECDSA signature suffices for on-chain verification, reducing the complexity and cost of ensuring computation integrity.
- Native Support by NVIDIA in the series of GPUs such as H100 and H200 natively support TEEs, providing hardware-accelerated secure environments for AI workloads. This native support ensures seamless integration and optimized performance for confidential AI inference.

<figure><img src="../.gitbook/assets/confidential-ai-inference-overview.png" alt=""><figcaption></figcaption></figure>

Our TEE-based solution can provide following features for AI Inference:

1. **Tamper-Proof Data**: Ensuring that user request/response data cannot be altered by a middleman is fundamental. This necessitates secure communication channels and robust encryption mechanisms.
2. **Secure Execution Environment**: Both hardware and software must be protected against attacks. This involves leveraging TEE that provides isolated environments for secure computation.
3. **Open Source and Reproducible Builds**: The entire software stack, from the operating system to the application code must be reproducible. This allows auditors to verify the integrity of the system.
4. **Verifiable Execution Results**: The results of AI computations must be verifiable, ensuring that the outputs are trustworthy and have not been tampered with.

## Table of Contents:

1. **[Getting Started](../confidential-ai/getting-started.md "mention")**.
2. **[Host LLM in TEE](../confidential-ai/host-LLM-in-TEE.md "mention")**.
2. **[Implementation](../confidential-ai/implementation.md "mention")**.
3. **[Benchmark](../confidential-ai/benchmark.md "mention")**.
