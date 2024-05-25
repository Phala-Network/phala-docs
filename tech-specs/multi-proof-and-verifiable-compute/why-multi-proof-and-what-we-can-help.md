# Why Multi-Proof and What We Can Help

## The Need for Multi-Proof Systems

We can not guarantee any single cryptography system is 100% secure. At the same time, the current Zero-Knowledge (ZK) solution is secure theoretically but still does not guarantee system-wide bug-free operation, especially from an engineering perspective, which remains challenging due to the complexity of ZK implementation. Here's where multi-proof systems come into play, to hedge the bugs in ZK implementation, a hardware solution, Trusted Execution Environment (TEE), can be used as a 2-factor verifier to offer double security to ZK projects like zk-Rollups. Inspired by Vitalik Buterin's [presentation](https://hackmd.io/@vbuterin/zk\_slides\_20221010#/) and a recent [post](https://ethresear.ch/t/2fa-zk-Rollups-using-sgx/14462) by Justin Drake. By having a multi-proof system, we can notably improve the robustness of security and interoperability in the blockchain network. Take zk-Rollups for example, a TEE-based prover (an entity that produces the proof) can bring several benefits.

1. **Hardware-grade safety:** The TEE prover merely supplements ZKP. In the worst-case scenario, zk-Rollup's security is robust.
2. **Unstoppable:** We deploy 'N' provers, requiring just 1-of-N approval on L1 and incentivizing the TEE provers appropriately.
3. **Low cost:** Gas consumption is minimal, requiring just an ECDSA verification. The L1 contracts experience minimal changes, and the Prover is uncomplicated: simple state transition function execution in TEE.

<figure><img src="../../.gitbook/assets/Why-Multi-Proof.png" alt=""><figcaption></figcaption></figure>

### Use Cases

Let's delve into some practical examples at the intersection of multi-proof systems. The practical real-world applications of multi-proof technology can be particularly seen in:

1.  **TEE-Proof for ZK-Rollups**: zk-Rollup can run a separate STF (state transition function) in TEE, and the result returned by STF will be signed by SGX prover (check this [article](https://phala.network/posts/introducing-phala-sgxprover-a-twofactor-authentication-solution-for-zkrollups) for more details), then submitted on-chain verifier along with the ZKP, the security levels can be significantly improved while ensuring computational efficiencies.\


    <figure><img src="../../.gitbook/assets/Use-Cases-Multi-Proof.png" alt=""><figcaption></figcaption></figure>
2. **TEE-Proof for ZK/MPC Bridges**: ZK/MPC bridges also can run the copy of the relayer in TEE, instead generate proof or MPC signature, the program can generate TEE-proof and submit it to the destination chain. The inclusion of TEE-proof provides secondary security, strengthening the system against potential breaches and leaks.
3.  **TEE-Proof for zkVM-based application**: a zkVM-based application can simply move their guest code to TEE, guest code often has no relation to ZK primitive. We can generate the TEE proof for the output of the guest code, which can be used to provide a secondary security guarantee for the zkVM.\


    <figure><img src="../../.gitbook/assets/Use-Cases-Multi-Proof-2.png" alt=""><figcaption></figcaption></figure>
