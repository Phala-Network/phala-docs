# ✅ Multi-Proof and Verifiable Compute

## Introduction

<figure><img src="../../.gitbook/assets/Intro-Multi-Proof.png" alt=""><figcaption></figcaption></figure>

In the blockchain space, our vision is to bring privacy, security, and verifiability to users. Our ultimate goal is to design a system that can simultaneously fulfill these attributes. However, relying on a single proof system to achieve this is impractical for several reasons:

- No single cryptographic system can be guaranteed to be 100% secure. For instance, zero-knowledge proofs (zk) can have soundness bugs that are difficult to detect, while Multi-Party Computation (MPC) is susceptible to collusion risks between nodes.
- Privacy in zkRollups cannot be fully guaranteed because sequencers can extract user transaction data during proof generation.
- Verifiability in Fully Homomorphic Encryption (FHE) computations is challenging because the FHE server may not perform computations correctly, and without knowing the correct result, we cannot verify its accuracy.

Let's take a look at how you can get started:

- As a background requirement, we suggest everyone start with [The Need for Multi-Proof Systems](./why-multi-proof-and-what-we-can-help.md) section.
- If you are a developer and hope to quickly go through how to build with our multi-proof system, you can jump to the [How to Build with Multi-Proof](./how-to-build-with-multi-proof.md) section.
- If you are doing research, and hope to get a deep understanding of the TEE and verifiable computing implemented with the Phala network, the [Trusted Execution Environments (TEE) and Compute Verifiability](./trusted-execution-environments-tee-and-compute-verifiability.md) section is for you.
