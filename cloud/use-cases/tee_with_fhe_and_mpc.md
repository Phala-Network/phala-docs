# TEE as 2FA for FHE/MPC Systems

## Introduction

Fully Homomorphic Encryption (FHE) and Multi-Party Computation (MPC) are foundational technologies for privacy-preserving computation, enabling operations on encrypted data without decryption. However, their adoption in real-world systems, particularly blockchain and decentralized networks, faces challenges such as computational overhead, key management risks, and trust assumptions. This chapter explores how Phala Network's TEE can act as a 2FA mechanism to enhance the security and practicality of FHE/MPC workflows.

Check out earlier thoughts on **[SGX as 2FA for FHE/MPC](https://ethresear.ch/t/sgx-as-2fa-for-fhe-mpc/19780)** and **[Drawbacks in FHE Blockchain and how TEE can help](https://collective.flashbots.net/t/drawbacks-in-fhe-blockchain-and-how-tee-can-help-it/3642)**

## Challenges in FHE/MPC Systems

**Key Management Risks**
- Secure key generation, storage, and usage are critical vulnerabilities
- Key compromise threatens data confidentiality and computation integrity
- Software-based solutions remain susceptible to memory attacks and insider threats

**Performance Limitations**
- FHE introduces significant computational overhead, impractical for time-sensitive applications
- MPC reduces individual computation but increases network communication and coordination costs
- Both technologies face scalability challenges in high-throughput environments

**Trust Vulnerabilities**
- Systems rely on honest-majority assumptions that weaken with participant count
- Collusion attacks become feasible when economic incentives align for malicious actors
- Lack of accountability mechanisms when malicious behavior occurs
- Threshold schemes vulnerable to withholding attacks that prevent result finalization

## TEE as a 2FA Mechanism: Architectural Overview
TEEs provide hardware-enforced isolation for sensitive operations, combining the benefits of secure enclaves (e.g., Intel TDX) with cryptographic protocols. When integrated with FHE/MPC, TEEs act as a secondary trust layer, ensuring:

- **Secure Key Generation/Storage**: Cryptographic keys are generated and stored within the TEE, isolated from the host OS or untrusted applications.

- **Computation Integrity**: Critical operations (e.g., decryption of FHE results or MPC coordination) are verified within the TEE.

- **Attestation**: Remote parties can cryptographically verify that computations were executed in a genuine TEE.

### Workflow Example

- MPC nodes build a docker image and deploy it to [Phala Cloud](https://cloud.phala.network/register?invite=PHALAWIKI), see the [tutorial](../cloud/create-cvm/create-with-docker-compose.md).

1. A master key is generated inside an TEE and never exposed externally.

2. The MPC node signs a public verification key, which is shared with the network.

3. The MPC node generate a attestation proof that prove the key generation and storage are done in a genuine TEE.

For FHE Computation:

4. Users encrypt data using FHE and send to FHE server.

5. FHE finished the computation and encrypt the result with the MPC key.

6. The MPC nodes in TEE decrypting intermediate results and return the result to users.

## Case Studies

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><span data-gb-custom-inline data-tag="emoji" data-code="1f510">🔐</span> Fairblock: Building Unruggable AI with an MPC-TEE Hybrid Architecture</td><td><a href="../../.gitbook/assets/fairblock_tee_registry.png">fairblock_tee_registry.png</a></td><td><a href="https://github.com/Fairblock/Unruggable-AI">Fairblock GitHub</a></td></tr><tr><td><span data-gb-custom-inline data-tag="emoji" data-code="1f5f3">🗳️</span> Mind Network: Leverage TEE and FHE Build Blind Voting</td><td><a href="../../.gitbook/assets/fhe_blind_voting.png">fhe_tee_voting.png</a></td><td><a href="https://phala.network/posts/fhepowered-aifi-with-mind-network">Mind Network Case Study</a></td></tr></tbody></table>
