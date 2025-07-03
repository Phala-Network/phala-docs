# Table of contents

## Home

* [👾 Phala Network Docs](README.md)

## Overview

* [⚖️ Phala Network](overview/phala-network.md)
  * [💎 Phala Cloud](overview/phala-network/phala-cloud.md)
  * [🥷 Dstack](overview/phala-network/dstack.md)
  * [🔐 GPU TEE](overview/phala-network/gpu-tee.md)
* [💎 PHA Token](overview/pha-token/README.md)
  * [🪙 Introduction](overview/pha-token/introduction.md)
  * [👐 Delegation](overview/pha-token/delegation/README.md)
    * [Delegate to StakePool](overview/pha-token/delegation/delegate-to-stakepool.md)
    * [What is Vault](overview/pha-token/delegation/whats-vault.md)
    * [What is Share](overview/pha-token/delegation/whats-share.md)
    * [WrappedBalances & W-PHA](overview/pha-token/delegation/wrappedbalances-and-w-pha.md)
    * [Examples of Delegation](overview/pha-token/delegation/examples-of-delegation.md)
    * [Use Phala App to Delegate](overview/pha-token/delegation/use-phala-app-to-delegate.md)
    * [Estimate Your Reward](overview/pha-token/delegation/estimate-your-reward.md)
  * [🗳️ Governance](overview/pha-token/governance/README.md)
    * [Governance Mechanism](overview/pha-token/governance/governance-mechanism.md)
    * [Join the Council](overview/pha-token/governance/join-the-council.md)
    * [Voting for Councillors](overview/pha-token/governance/voting-for-councillors.md)
    * [Apply for Project Funding](overview/pha-token/governance/apply-for-project-funding.md)
    * [Phala Treasury](overview/pha-token/governance/khala-treasury.md)
    * [Phala Governance](overview/pha-token/governance/khala-governance.md)
    * [Setting Up an Account Identity](overview/pha-token/governance/setup-account-identity.md)

## Phala Cloud

* [🚀 Getting Started](cloud/getting-started/getting-started.md)
  * [Create Your Phala Cloud Account](cloud/getting-started/sign-up-for-cloud-account.md)
  * [Your First CVM Deployment](cloud/getting-started/start-from-cloud-ui.md)
  * [Explore Templates](phala-cloud/getting-started/explore-templates/README.md)
    * [Launch an Eliza Agent](phala-cloud/getting-started/explore-templates/launch-an-eliza-agent.md)
    * [Start from Template](phala-cloud/getting-started/explore-templates/start-from-template.md)
  * [Core Concepts Refresher](phala-cloud/getting-started/core-concepts-refresher.md)
* [🪨 TEEs, Attestation & Zero Trust Security](phala-cloud/tees-attestation-and-zero-trust-security/README.md)
  * [Attestation](phala-cloud/tees-attestation-and-zero-trust-security/attestation.md)
  * [Security Architecture](phala-cloud/tees-attestation-and-zero-trust-security/security-architecture.md)
* [🥷 Phala Cloud User Guides](phala-cloud/phala-cloud-user-guides/README.md)
  * [Deploy and Manage CVMs](phala-cloud/phala-cloud-user-guides/create-cvm/README.md)
    * [Deploy CVM with Docker Compose](phala-cloud/phala-cloud-user-guides/create-cvm/create-with-docker-compose.md)
    * [Set Secure Environment Variables](phala-cloud/phala-cloud-user-guides/create-cvm/set-secure-environment-variables.md)
    * [Deploy Private Docker Image to CVM](phala-cloud/phala-cloud-user-guides/create-cvm/create-with-private-docker-image.md)
    * [Debugging and Analyzing Logs](phala-cloud/phala-cloud-user-guides/create-cvm/debugging-and-analyzing-logs/README.md)
      * [Check Logs](phala-cloud/phala-cloud-user-guides/create-cvm/debugging-and-analyzing-logs/check-logs.md)
      * [Private Log Viewer](phala-cloud/phala-cloud-user-guides/create-cvm/debugging-and-analyzing-logs/private-log-viewer.md)
      * [Debug Your Application](phala-cloud/phala-cloud-user-guides/create-cvm/debugging-and-analyzing-logs/debug-your-application.md)
    * [Application Scaling & Resource Management](phala-cloud/phala-cloud-user-guides/create-cvm/resize-resource.md)
    * [Upgrade Application](phala-cloud/phala-cloud-user-guides/create-cvm/upgrade-application.md)
    * [Deployment Cheat Sheet](phala-cloud/phala-cloud-user-guides/create-cvm/deployment-cheat-sheet.md)
  * [Building with TEE](phala-cloud/phala-cloud-user-guides/building-with-tee/README.md)
    * [Access Your Applications](phala-cloud/phala-cloud-user-guides/building-with-tee/access-your-applications.md)
    * [Expose Service Port](phala-cloud/phala-cloud-user-guides/building-with-tee/expose-service-port.md)
    * [Setting Up Custom Domain](phala-cloud/phala-cloud-user-guides/building-with-tee/setting-up-custom-domain.md)
    * [Secure Access Database](phala-cloud/phala-cloud-user-guides/building-with-tee/access-database.md)
    * [Create Crypto Wallet](phala-cloud/phala-cloud-user-guides/building-with-tee/create-crypto-wallet.md)
    * [Generate Remote Attestation](phala-cloud/phala-cloud-user-guides/building-with-tee/generate-ra-report.md)
    * [Verify Remote Attestation](phala-cloud/phala-cloud-user-guides/building-with-tee/verify-remote-attestation.md)
  * [Advanced Deployment Options](phala-cloud/phala-cloud-user-guides/advanced-deployment-options/README.md)
    * [Deploy CVM with Phala Cloud CLI](phala-cloud/phala-cloud-user-guides/advanced-deployment-options/start-from-cloud-cli.md)
    * [Deploy CVM with Phala Cloud API](phala-cloud/phala-cloud-user-guides/advanced-deployment-options/deploy-cvm-with-phala-cloud-api.md)
    * [Setup a CI/CD Pipeline](phala-cloud/phala-cloud-user-guides/advanced-deployment-options/setup-a-ci-cd-pipeline.md)
* [🚢 Be Production Ready](phala-cloud/be-production-ready/README.md)
  * [CI/CD Automation](phala-cloud/be-production-ready/ci-cd-automation/README.md)
    * [CI/CD Integration Best Practices](phala-cloud/be-production-ready/ci-cd-automation/ci-cd-integration-best-practices.md)
    * [Setup a CI/CD Pipeline](phala-cloud/be-production-ready/ci-cd-automation/setup-a-ci-cd-pipeline.md)
  * [Production Checklist](phala-cloud/be-production-ready/production-checklist.md)
  * [Troubleshooting Guide](phala-cloud/be-production-ready/troubleshooting.md)
  * [Glossary](phala-cloud/be-production-ready/glossary.md)
* [🔒 Use Cases](cloud/use-cases/use-cases.md)
  * [TEE with AI](cloud/use-cases/tee_with_ai.md)
  * [TEE with FHE and MPC](cloud/use-cases/tee_with_fhe_and_mpc.md)
  * [TEE with ZK and ZKrollup](cloud/use-cases/tee_with_zk_and_zkrollup.md)
* [📋 References](phala-cloud/references/README.md)
  * [Phala Cloud CLI Reference](phala-cloud/references/tee-cloud-cli/README.md)
    * [phala](phala-cloud/references/tee-cloud-cli/phala/README.md)
      * [auth](phala-cloud/references/tee-cloud-cli/phala/auth.md)
      * [cvms](phala-cloud/references/tee-cloud-cli/phala/cvms.md)
      * [docker](phala-cloud/references/tee-cloud-cli/phala/docker.md)
      * [simulator](phala-cloud/references/tee-cloud-cli/phala/simulator.md)
  * [Cloud API (beta)](phala-cloud/references/cloud-api-beta/README.md)
    * ```yaml
      type: builtin:openapi
      props:
        models: true
      dependencies:
        spec:
          ref:
            kind: openapi
            spec: phala-cloud-api
      ```
  * [Phala Cloud Pricing](phala-cloud/references/phala-cloud-pricing.md)
* [❓ FAQs](cloud/faqs.md)

***

* [⚙️ CVM Management](management.md)
* [🔄 Deploy Docker App in TEE](migration.md)

## Dstack

* [Overview](dstack/overview.md)
* [Local Development Guide](dstack/local-development.md)
* [Getting Started](dstack/getting-started.md)
* [Hardware Requirements](dstack/hardware-requirements.md)
* [Design Documents](dstack/design-documents/README.md)
  * [Whitepaper](dstack/design-documents/whitepaper.md)
  * [Decentralized Root-of-Trust](dstack/design-documents/decentralized-root-of-trust.md)
  * [Key Management Service](dstack/design-documents/key-management-protocol.md)
  * [Zero Trust HTTPs (TLS)](dstack/design-documents/tee-controlled-domain-certificates.md)
* [Acknowledgement](dstack/acknowledgement.md)
* [❓ FAQs](dstack/faqs.md)

## LLM in GPU TEE

* [👩‍💻 Host LLM in GPU TEE](gpu-tee/llm-in-tee.md)
* [🔐 GPU TEE Inference API](gpu-tee/inference-api.md)
* [🏎️ GPU TEE Benchmark](gpu-tee/benchmark.md)
* [❓ FAQs](gpu-tee/faqs.md)

## Tech Specs

* [⛓️ Blockchain](tech-specs/blockchain/README.md)
  * [Blockchain Entities](tech-specs/blockchain/blockchain-entities.md)
  * [Cluster of Workers](tech-specs/blockchain/cluster-of-workers.md)
  * [Secret Key Hierarchy](tech-specs/blockchain/secret-key-hierarchy.md)

## References

* [🔐 Setting Up a Wallet on Phala](references/basic-guidance/README.md)
  * [Acquiring PHA](references/basic-guidance/get-pha-and-transfer.md)
* [🌉 SubBridge](references/subbridge/README.md)
  * [Cross-chain Transfer](references/subbridge/cross-chain-transfer.md)
  * [Supported Assets](references/subbridge/supported-assets.md)
  * [Asset Integration Guide](references/subbridge/asset-integration-guide.md)
  * [Technical Details](references/subbridge/technical-details.md)
* [👷 Community Builders](references/community-builders.md)
* [🤹 Hackathon Guides](references/hackathon-guides/README.md)
  * [ETHGlobal Singapore](references/hackathon-guides/ethglobal-singapore.md)
  * [ETHGlobal San Francisco](references/hackathon-guides/ethglobal-san-francisco.md)
  * [ETHGlobal Bangkok](references/hackathon-guides/ethglobal-bangkok.md)
* [🤯 Advanced Topics](references/advanced-topics/README.md)
  * [Cross Chain Solutions](references/advanced-topics/cross-chain-solutions.md)
  * [System Contract and Drivers](references/advanced-topics/system-contract-and-drivers.md)
  * [Run Local Testnet](references/advanced-topics/run-local-testnet.md)
  * [SideVM](references/advanced-topics/sidevm.md)
* [🆘 Support](references/support/README.md)
  * [Available Phala Chains](references/support/endpoints.md)
  * [Resource Limits](references/support/resource-limits.md)
  * [Transaction Costs](references/support/transaction-costs.md)
  * [Compatibility Matrix](references/support/compatibility-matrix.md)
  * [Block Explorers](references/support/block-explorers.md)
  * [Faucet](references/support/faucet.md)
* [⁉️ FAQ](references/faq.md)

## Compute Providers

* [🙃 Basic Info](compute-providers/basic-info/README.md)
  * [Introduction](compute-providers/basic-info/introduction.md)
  * [Gemini Tokenomics (Worker Rewards)](compute-providers/basic-info/worker-rewards.md)
  * [Budget balancer](compute-providers/basic-info/budget-balancer.md)
  * [Staking Mechanism](compute-providers/basic-info/staking-mechanism.md)
  * [Requirements in Phala](compute-providers/basic-info/requirements-in-phala-khala.md)
  * [Confidence Level & SGX Function](compute-providers/basic-info/confidence-level-and-sgx-function.md)
  * [Rent Hardware](compute-providers/basic-info/rent-hardware.md)
  * [Error Summary](compute-providers/basic-info/error-summary.md)
* [🦿 Run Workers on Phala](compute-providers/run-workers-on-phala/README.md)
  * [Solo Worker Deployment](compute-providers/run-workers-on-phala/solo-worker-deployment.md)
  * [PRBv3 Deployment](compute-providers/run-workers-on-phala/prbv3-deployment.md)
  * [Using PRBv3 UI](compute-providers/run-workers-on-phala/using-prbv3-ui.md)
  * [PRB Worker Deployment](compute-providers/run-workers-on-phala/prb-worker-deployment.md)
  * [Switch Workers from Solo to PRB Mode](compute-providers/run-workers-on-phala/switch-workers-from-solo-to-prb-mode.md)
  * [Headers-cache deployment](compute-providers/run-workers-on-phala/headers-cache-deployment.md)
  * [Archive node deployment](compute-providers/run-workers-on-phala/archive-node-deployment.md)
* [🏃‍♀️ Run Workers on Khala - Archived](compute-providers/run-workers-on-khala/README.md)
  * [Solo Scripts Guidance - Archived](compute-providers/run-workers-on-khala/solo-scripts-guidance/README.md)
    * [Installing Khala Solo Scripts - Archived](compute-providers/run-workers-on-khala/solo-scripts-guidance/installing-phala-mining-tools.md)
    * [Worker Confidence Level - Archived](compute-providers/run-workers-on-khala/solo-scripts-guidance/worker-confidence-level.md)
    * [Configure the Worker - Archived](compute-providers/run-workers-on-khala/solo-scripts-guidance/configure-the-worker.md)
    * [Deploy the Worker - Archived](compute-providers/run-workers-on-khala/solo-scripts-guidance/deploy-the-worker.md)
    * [Monitor Worker's Status - Archived](compute-providers/run-workers-on-khala/solo-scripts-guidance/monitor-workers-status.md)
    * [Accelerate Khala Syncing - Archived](compute-providers/run-workers-on-khala/solo-scripts-guidance/accelerate-khala-syncing.md)
    * [Update your Worker's Node - Archived](compute-providers/run-workers-on-khala/solo-scripts-guidance/update-your-workers-node.md)
  * [PRBv3 Deployment Guide - Archived](compute-providers/run-workers-on-khala/prbv3-deployment.md)
  * [Using PRBv3 UI - Archived](compute-providers/run-workers-on-khala/using-prbv3-ui.md)
  * [Migration from PRBv2 to v3 - Archived](compute-providers/run-workers-on-khala/migration-from-prbv2-to-v3.md)
  * [Headers-cache deployment - Archived](compute-providers/run-workers-on-khala/headers-cache-deployment.md)
  * [Archive node deployment - Archived](compute-providers/run-workers-on-khala/archive-node-deployment.md)
  * [PRBv2 Deployment Guide - Archived](compute-providers/run-workers-on-khala/deployment-guide-for-prbv2.md)
  * [PRB Worker Deployment - Archived](compute-providers/run-workers-on-khala/prb-worker-deployment.md)
  * [How to switch from Solo scripts to PRB worker - Archived](compute-providers/run-workers-on-khala/how-to-switch-from-solo-mining-to-prb-mining.md)
  * [Khala Worker Rewards - Archived](compute-providers/run-workers-on-khala/khala-worker-rewards.md)
  * [Troubleshooting - Archived](compute-providers/run-workers-on-khala/troubleshooting.md)
* [🛡️ Gatekeeper](compute-providers/gatekeeper/README.md)
  * [Collator](compute-providers/gatekeeper/collator.md)
  * [Gatekeeper](compute-providers/gatekeeper/gatekeeper.md)

## Web Directory

* [Discord](https://discord.gg/phala-network)
* [GitHub](https://github.com/Phala-Network/)
* [Twitter](https://twitter.com/PhalaNetwork)
* [YouTube](https://www.youtube.com/@PhalaNetwork)
* [Forum](https://forum.phala.network/)
* [Medium](https://medium.com/phala-network)
* [Telegram](https://t.me/phalanetwork)

## Legacy

* [Information](legacy/information.md)
* [⚒️ Phala SDK](legacy/phala-sdk.md)
* [👨‍🚀 Builders Program](legacy/builders-program.md)
* [🥷 AI Agent Contract](legacy/ai-agent-contract/README.md)
  * [WapoJS Functions](legacy/ai-agent-contract/wapojs-functions.md)
  * [Phala Agent Gateway](legacy/ai-agent-contract/phala-agent-gateway.md)

## AI Agent Contract (Legacy)

* [👩‍💻 Getting Started](ai-agent-contract-legacy/getting-started/README.md)
  * [Build Your First AI Agent Contract](ai-agent-contract-legacy/getting-started/build-your-first-ai-agent-contract.md)
  * [Build An Agent to Transact Onchain](ai-agent-contract-legacy/getting-started/build-an-agent-to-transact-onchain.md)
  * [Build Your AI Agent Contract with OpenAI](ai-agent-contract-legacy/getting-started/build-your-ai-agent-contract-with-openai.md)
  * [Build Your AI Agent Contract with LangChain](ai-agent-contract-legacy/getting-started/build-your-ai-agent-contract-with-langchain.md)
  * [Integrate with 3rd Party API with HTTP Request](ai-agent-contract-legacy/getting-started/integrate-with-3rd-party-api-with-http-request.md)
  * [Run a Local Testnet With Docker](ai-agent-contract-legacy/getting-started/run-a-local-testnet-with-docker.md)
  * [AI Agent Contract Templates](ai-agent-contract-legacy/getting-started/ai-agent-contract-templates.md)
* [🧙‍♂️ Examples](ai-agent-contract-legacy/examples/README.md)
  * [Create a Weather Agent w/ Function Calling](ai-agent-contract-legacy/examples/create-a-weather-agent-w-function-calling.md)
* [⛓️ Supported Chains](ai-agent-contract-legacy/supported-chains.md)
* [FAQ](ai-agent-contract-legacy/faq.md)

## Agent Wars (Legacy)

* [📜 Introduction](agent-wars-legacy/agent-wars-introduction.md)
* [💸 Tokenomics](agent-wars-legacy/agent-war-tokenomics.md)
* [▶️ Getting Started](agent-wars-legacy/getting-started/README.md)
  * [Wallet Setup & Get PHA](agent-wars-legacy/getting-started/wallet-setup-and-get-pha.md)
  * [Buy and Sell Keys](agent-wars-legacy/getting-started/buy-and-sell-keys.md)
* [🧑‍🏫 Tutorial](agent-wars-legacy/tutorial.md)
