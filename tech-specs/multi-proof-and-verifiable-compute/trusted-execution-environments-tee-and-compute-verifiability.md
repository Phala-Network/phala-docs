# Trusted Execution Environments (TEE) and Compute Verifiability

<figure><img src="../../.gitbook/assets/TEE-Compute-Verifiability.png" alt=""><figcaption></figcaption></figure>

Until now, the Phala network has more than 30K TEE devices registered and running, becoming the biggest TEE network in Web3.

A TEE is a secure area within the main processor of a device. It ensures external processes or computations, even those with higher privileges, cannot access or alter the data inside it. This isolative feature directly wheels in a trust-minimized environment, heightening the protection against potential security threats.

<figure><img src="../../.gitbook/assets/TEE.png" alt=""><figcaption></figcaption></figure>

The unassailable security of TEEs is not just limited to protecting critical data. They also authenticate and verify the data computations that take place within them. This feature illuminates the foreground of TEEs in multi-proof systems, addressing the challenge of computing verifiability.

Phala currently only supports Intel SGX (Software Guard Extension) as the TEE hardware, and will support Intel TDX and NVIDIA GPU TEE soon. Check [here](https://sgx101.gitbook.io/sgx101/sgx-bootstrap/overview) for more info about SGX.

## How are TEE Devices Being Verified?

Verification is the cornerstone of guaranteeing TEE's trust-minimized environment. Verifying a TEE device (in Phala's context, Intel SGX device), generally refers to verifying the hardware information of the device, which includes checking if the CPU is genuine hardware manufactured by vendors such as Intel, the cert-chain is valid and provided by the manufacture that can be trusted. Verification of the TEE device before running any program in it (Enclave) is necessary because it can provide security guarantees from a hardware perspective that the program is running the actual copy of the code that the user expects through [**Remote Attestation**](https://sgx101.gitbook.io/sgx101/sgx-bootstrap/attestation#remote-attestation-primitives).

Currently, Phala enforces the verification on the Phala blockchain when the TEE device (the worker) is going to register. Recently we have been searching the Zero Knowledge-based TEE device verification, which aims to leverage the ZK technique to verify TEE devices off-chain in a trustless manner.

1. **Verified on Phala Blockchain**: Employing Phala Blockchain positions an extra layer of transparency and trust in the verification process. The verification process's details are recorded on the blockchain, allowing users to transparently view and verify the operations. Check the code [here](https://github.com/Phala-Network/phala-blockchain/tree/master/crates/sgx-attestation) if you wanna explore more.
2.  **Verified on Ethereum with a ZK DCAP Verifier**: Verification of TEEs on Ethereum directly is expensive in gas cost, but we can only verify the ZKP on-chain of a DCAP verifier, where we move the heavy computation to off-chain. Check the PoC code [here](https://github.com/tolak/zk-dcap-verifier) to see how we verify DCAP based on RiscZero zkVM with a local prover.\


    <figure><img src="../../.gitbook/assets/TEE-ZKProver.png" alt=""><figcaption></figcaption></figure>

## How to Generate TEE-Proof for Programs

Unlike generating ZKP (Zero Knowledge Proof), which needs to have a specific circuit for the proven program, TEE-proof generation is cheaper in the cost of computation. When thinking about the TEE-proof generation, we need to get out of that Zero-Knowledge mindset for a moment. Here are two considerations when proving the program execution result is trust in TEE:

1.  If the execution environment is trust

    As we mentioned earlier, every TEE device was verified when registered on the Phala blockchain. A bunch of items will be checked, and finally, we will evaluate a confidential level according to the check. See [here](https://docs.phala.network/compute-providers/basic-info/confidence-level-and-sgx-function) for more information.
2.  If the key used to sign the proof is secure

    Since we already guarantee the execution environment is trusted, the data signed by the key derived in the environment should be trusted too. By introducing [Key Hierarchy](https://docs.phala.network/developers/advanced-topics/blockchain-infrastructure/secret-key-hierarchy#key-hierarchy-management) and [Key Rotation](https://github.com/Phala-Network/phala-blockchain/pull/810) mechanisms, the safety of the key is guaranteed in both cryptographic and economic ways. Check this [article](https://medium.com/phala-network/technical-analysis-of-why-phala-will-not-be-affected-by-the-intel-sgx-chip-vulnerabilities-e045b0189dc2) for the analysis of Phala security design.

With the above two premises, the TEE-proof generation is pretty simple. Every multi-proof program running on the system will have a dedicated app key which is derived from WASM Virtual Machine - SideVM, the SideVM is running inside TEE. Every user can deploy a Javascript Engine for themselves, the key will be injected when developer upload their Javascript code to the JS engine where developer can use this key to sign transaction in their Javascript code. To generate the TEE-proof, the program needs to use this key to sign the output of the execution result of their business logic. For example, if you are going to verify the TEE proof on Ethereum, you can sign the result with the ECDSA signature scheme. See **How to Build with Multi-Proof** section for how to generate TEE-proof with JS SDK.

## Comparison: TEE Compute Verification vs. ZK Compute Verification

While TEE-Proofs and ZK-Proofs share the same goal of ensuring computational integrity and verifiability, they differ in their construction and operation:

1. **Computation Cost**: The computation cost for generating a TEE-Proof is significantly lower than for a ZK-Proof. While a ZK-Proof requires intricate cryptographic operations and a relatively large amount of computational resources, a TEE-Proof is generated as a result of computation inside a TEE. This makes the TEE-Proof computation incredibly efficient, providing an edge, especially for systems dealing with more extensive calculations.
2. **Proof Size and On-Chain Verification Cost**: ZK-Proofs, architected based on elliptic curve cryptography, the proof sizes differ from different proof systems, some of them are extremely expensive. While TEE-Proofs are more cost-efficient to compute, they come with const proof sizes, e.g. the length of the signature, meaning they occupy small space and cost less to verify on-chain.
3. **Security, Liveness, and Complexity**: Both TEE-Proofs and ZK-Proofs ensure robust security. However, ZK-Proofs, based on cryptographic hardness assumptions, offer mathematically guaranteed security but are complex to create and verify. TEE-Proofs, on the other hand, are simpler to produce and validate but trust in the TEE hardware and the integrity of the software it runs to provide the desired security level. Phala network adds an extra economic security guarantee on top of the default TEE security infrastructure, making the whole system more robust.

## What's Next?

Now you already have a fundamental understanding of the underlying techniques of TEE, if you are a developer, please follow the next section to see how you can develop multi-proof with our JS SDK.
