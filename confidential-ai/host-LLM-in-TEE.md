# Host LLM in TEE

Phala Network leverages NVIDIA's TEE GPU technology to provide confidential LLM inference services. By utilizing NVIDIA Blackwell's Confidential Computing capabilities, we ensure that AI model execution and data processing remain fully protected within secure enclaves. This solution enables organizations to run their LLM workloads with guaranteed privacy and security, preventing unauthorized access to both the model and user data during inference operations.

<figure><img src="../.gitbook/assets/hopper-arch-confidential-computing.jpeg" alt=""><figcaption></figcaption></figure>

*source: https://www.nvidia.com/en-us/data-center/solutions/confidential-computing/*

The following diagram illustrates the architecture of the Phala Confidential AI Inference (private LLM Node) service. To host your own private LLM in TEE, you only need to wrap your LLM inference code into a docker image, then deploy your own container to the TEE network. To make the LLM fully verifiable, you need make sure the docker image is reproducible.

<figure><img src="../.gitbook/assets/host-llm-in-TEE.png" alt=""><figcaption></figcaption></figure>

There are some basic requirements the confidential AI inference service must provide, including:

1. **Tamper-Proof Data**: Ensuring that user request/response data cannot be altered by a middleman is fundamental. This necessitates secure communication channels and robust encryption mechanisms.
2. **Secure Execution Environment**: Both hardware and software must be protected against attacks. This involves leveraging TEE that provides isolated environments for secure computation.
3. **Open Source and Reproducible Builds**: The entire software stack, from the operating system to the application code must be reproducible. This allows auditors to verify the integrity of the system.
4. **Verifiable Execution Results**: The results of AI computations must be verifiable, ensuring that the outputs are trustworthy and have not been tampered with.

## The Hardware & Software Requirements

To effectively use the Confidential AI Inference, the following requirements must be met:

**Hardware**: No specific hardware requirements for developers; We use NVIDIA H100/H200/B100 GPUs with TEE support and Intel CPUs with TDX support.

**Software**:

- Docker: For containerizing LLM deployments.
- The SDK achieves these goals through a combination of hardware-based TEEs, secure communication protocols, decentralized key management, and reproducible builds.
- TEE explorer: comming soon...

## Architecture

Our solution is designed to provide a secure and verifiable environment for AI inference. The key components include:

- **Deployment Portal**: Web interface for deploying LLM Docker containers.
- **Secure Compute Environment**: TEE-based execution environment.
- **Remote Attestation**: Verification of the TEE environment.
- **Secure Communication**: End-to-end encryption between users and LLM.
- **Key Management Service (KMS)**: Decentralized key management.

## Services

### Deployment Portal [coming soon]

The Deployment Portal provides a user-friendly interface for developers to deploy their LLM Docker containers.

**Components**:

- **Web Interface**: Provide the dashboard to allows users to upload and manage their Docker containers.
- **Deployment Automation**: Automates the process of deploying containers to the TEE network.
- **Logging**: Provide the logs for the users to monitor the status of their containers.

### Secure Compute Environment

The Secure Compute Environment provides a secure execution environment for AI inference tasks.

**Components**:

- **TEE Infrastructure**: Utilizes NVIDIA GPU TEE and Intel TDX for secure execution.
- **TEE Explorer**: Provide the TEE explorer to allows users to verify the integrity of the TEE environment.

### Remote Attestation

Remote Attestation handles remote attestation, ensuring the integrity of the TEE environment, we provide the interface to help user get the TDX quote and GPU attestation report and verify them by any supported tools.

**Components**:

- **TDX Quote Generation**: Measurement of BIOS, bootloader, rootfs, and OS kernel and docker image developer created.
- **GPU Attestation**: Measurement of GPU driver and configuration.

### Secure Communication

Secure Communication establishes a secure communication channel between users and the LLM.

**Components**:

- **RA-TLS Connection**: Establish the TLS connection between the user and the LLM based on RA report.

### Key Management Service (KMS)

The Key Management Service provides decentralized key management, avoiding vendor lock-in.

**Components**:

- **Key Derivation**: Generating application-specific encryption keys.
- **Key Rotation**: Ensuring regular and secure key updates.

Want to dive deeper? Check the [Implementation](./implementation.md "mention") for the technical details of the Confidential AI Inference.