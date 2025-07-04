# ⚖️ Phala Network

Confidential AI Inference stands as a cornerstone for safeguarding sensitive data and ensuring secure AI model execution in Web3. Through the implementation of LLM models within Trusted Execution Environments (TEE), Phala Network delivers private and verifiable AI computations. This robust approach addresses fundamental challenges in the Web3 ecosystem: data privacy protection, secure execution guarantees, and computational verifiability. Such capabilities are essential for applications where the protection of user data and model integrity is paramount.

## **What Sets Phala Apart:**

* **We Don't Trust Any Provider**: Our **security model** goes beyond traditional cloud solutions (e.g., AWS, Azure, GCP). **Phala does not trust any cloud platform, hardware provider, or even its users,** ensuring true zero-trust.
* **User-Friendly & Affordable**: With **easy integration**, developers can migrate their **Web2 software** into a zero-trust environment. By using TEE as part of our hybrid infrastructure, developers can select the **level of proof** they need based on their use case, making the system both flexible and affordable.
* **Web3 Standard Compatibility**: Phala is fully **decentralized, privacy-focused**, and auditable. Our SDK enables your programs to **easily integrate with blockchains**, providing seamless co-processing and interaction with Web3 systems.

## **How It Works**

<figure><img src="../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Phala introduces a **new root-of-trust** beyond traditional hardware-based models.
* We implement a combination of **TEE, MPC, ZKP (FHE)** and **blockchain game theory** to build this **new root-of-trust**.
* Our system offers **auditable computation**, ensuring that anyone can verify the integrity of execution results, creating a **tamper-proof** environment.

## **The Solution**

Phala provides a comprehensive suite of tools and infrastructure to make zero-trust computing **easy to access**, **build**, and **verify**:

* **Easy Access to Computers**: [Phala Cloud](https://cloud.phala.network/register?invite=PHALAWIKI) provides access to TEE hardware, including **Intel TDX**, **Intel SGX**, **AMD SEV**, and **NVIDIA H100/H200 (TEE)**, offering secure and verifiable computation at scale. Phala Cloud supports deployment of any Docker application into TEE environments, making it easy to migrate existing workloads to confidential computing.
* **Easy to Build**: [Dstack](../dstack/overview.md) is the TEE SDK developed by Phala and Flashbots jointly
  * **Docker / VM migration into TEE**, allowing developers to move existing workloads into a zero-trust environment.
  * **Serverless edge functions**: Leverage pre-built templates to create **serverless, privacy-preserving functions** that run in secure TEEs.
* **Easy to Prove**: Phala offers **on-chain attestation** for auditable logs of off-chain computations, ensuring integrity and transparency. Developers can prove the correctness of their computations in a verifiable, decentralized way.

## **The Future is Here (Use Cases)**

* **Web2 to Web3**: Easily transition Web2 software to **Web3 standards**, with seamless connectivity to smart contracts across blockchains.
* **Intelligence-Based Economy**: Solutions like **MEV, Intent-centric applications**. Flashbots uses TEE for decentralized MEV-boost on Ethereum. Uniswap is using TEE to build a DeFi-native Ethereum L2, becoming a hub for liquidity across chains.
* **Defense in Depth**: Projects like **Lit Protocol (MPC)**, **Zama (FHE)**, and **Scroll (ZKP)** use TEE to enhance their security and privacy, strengthening their defenses.
* **Decentralized AI**: With **NVIDIA's GPU TEEs**, decentralized AI platforms like **NEAR AI, Sentient, Zero Gravity, Ritual, Morpheus**, and **Autonolas** use TEEs to run LLMs in secure, verifiable, and privacy-focused environments as part of their infrastructure.
