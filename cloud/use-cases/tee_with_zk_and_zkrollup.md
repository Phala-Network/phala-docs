# Building Multi-Proof System with ZK and TEE

## Introduction

<figure><img src="../../.gitbook/assets/Intro-Multi-Proof.png" alt=""><figcaption></figcaption></figure>

In the blockchain space, our vision is to bring privacy, security, and verifiability to users. Our ultimate goal is to design a system that can simultaneously fulfill these attributes. However, relying on a single proof system to achieve this is impractical for several reasons:

- No single cryptographic system can be guaranteed to be 100% secure. For instance, zero-knowledge proofs (zk) can have soundness bugs that are difficult to detect, while Multi-Party Computation (MPC) is susceptible to collusion risks between nodes.
- Privacy in zkRollups cannot be fully guaranteed because sequencers can extract user transaction data during proof generation.
- Verifiability in Fully Homomorphic Encryption (FHE) computations is challenging because the FHE server may not perform computations correctly, and without knowing the correct result, we cannot verify its accuracy.

## The Need for Multi-Proof Systems

In the blockchain space, our vision is to bring privacy, security, and verifiability to users. Our ultimate goal is to design a system that can simultaneously fulfill these attributes. However, relying on a single proof system to achieve this is impractical for several reasons:

* No single cryptographic system can be guaranteed to be 100% secure. For instance, zero-knowledge proofs (zk) can have soundness bugs that are difficult to detect, while Multi-Party Computation (MPC) is susceptible to collusion risks between nodes.
* Privacy in zkRollups cannot be fully guaranteed because sequencers can extract user transaction data during proof generation.
* Verifiability in Fully Homomorphic Encryption (FHE) computations is challenging because the FHE server may not perform computations correctly, and without knowing the correct result, we cannot verify its accuracy.

There are several benefits we can gain by introducing TEE:

1. **Hardware-grade safety:** The privacy, confidentiality, and data integrity is guaranteed by hardware secure enclave.
2. **No computation overhead:** Applications run TEE have nearly same speed compare with running in normal CPU env
3. **Low verification cost:** The Gas consumption to verify TEE proof is minimal, requiring just an ECDSA verification.

We can not guarantee any single cryptography system is 100% secure. At the same time, the current Zero-Knowledge (ZK) solution is secure theoretically but still does not guarantee system-wide bug-free operation, especially from an engineering perspective, which remains challenging due to the complexity of ZK implementation. Here's where multi-proof systems come into play, to hedge the bugs in ZK implementation, a hardware solution, Trusted Execution Environment (TEE), can be used as a 2-factor verifier to offer double security to ZK projects like zk-Rollups. Inspired by Vitalik Buterin's [presentation](https://hackmd.io/@vbuterin/zk\_slides\_20221010#/) and a recent [post](https://ethresear.ch/t/2fa-zk-Rollups-using-sgx/14462) by Justin Drake.

<figure><img src="../../.gitbook/assets/Why-Multi-Proof.png" alt=""><figcaption></figcaption></figure>

## Case Studies

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><span data-gb-custom-inline data-tag="emoji" data-code="1f680">🚀</span> Phala Network: Run zk-Rollup STF (state transition function) in TEE</td><td><a href="../../.gitbook/assets/Use-Cases-Multi-Proof.png">Use-Cases-Multi-Proof.png</a></td><td><a href="https://phala.network/posts/introducing-phala-sgxprover-a-twofactor-authentication-solution-for-zkrollups">Phala SGXProver</a></td></tr><tr><td><span data-gb-custom-inline data-tag="emoji" data-code="1f512">🔒</span> Primus: Build Trustless zkTLS with TEE</td><td><a href="../../.gitbook/assets/tee_zktls.png">tee_zktls.png</a></td><td><a href="https://medium.com/@primuslabs/primus-x-phala-network-build-trustless-zktls-with-tee-332a26d48c83">Primus zkTLS</a></td></tr></tbody></table>