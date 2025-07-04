# ❓ FAQs

## Does Dstack support GCP / Azure

Dstack is open for PR to add that support. Currently it’s focusing on bare metal because it offers the most fine grained control and access to the vanilla TDX.

## How does KMS key generation work and how can it be modified?

The key generation logic is implemented in the onboard service:\
Reference: https://github.com/Dstack-TEE/dstack/blob/master/kms/src/onboard\_service.rs#L50

## How does on-chain KMS work and how can I customize its governance?

The KMS contract allows for customizable ownership and governance:

* During deployment, you can specify an owner
* After deployment, ownership can be transferred using transferOwnership function\
  Reference: https://github.com/Dstack-TEE/dstack/blob/master/kms/auth-eth/hardhat.config.ts#L96

## Where can I find KMS deployment instructions?

Complete deployment documentation is available here:

Reference: https://github.com/Dstack-TEE/dstack/blob/master/docs/deployment.md

## How does the current data encryption system work?

The system uses Linux's built-in LUKS (Linux Unified Key Setup) for disk encryption:\
Reference: https://github.com/Dstack-TEE/dstack/blob/master/tdxctl/src/fde\_setup.rs#L437-L442

## Where is the deployment function located in the Dstack-TEE codebase, and can it be integrated with custom tools?

The deployment logic for Dstack-TEE is part of its Rust-based implementation, there are multiple services involved in the deployment pipeline. [Dstack-TEE GitHub repository](https://github.com/Dstack-TEE/dstack) contains the core services (e.g., vmm, gateway, kms, meta-dstack).

## Can I run a Docker image directly in a TEE without setting up all Dstack components?

Yes, you can run a Docker image in a TEE using the Dstack SDK without setting up all components, but with limitations. The SDK provides a base VM image that runs a minimal VM containing your Docker container. The essential components are kms (key management service) and vmm (TEE runtime), which must be included. Optional components like dstack-gateway (for TLS support) can be skipped if you don’t need features like encrypted communication. Configure the SDK with your Docker image and the required components as per the documentation.
