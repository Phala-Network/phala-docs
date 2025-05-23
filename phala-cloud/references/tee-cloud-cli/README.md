---
description: >-
  A command-line tool for managing Trusted Execution Environment (TEE)
  deployments on Phala Cloud, from local development to cloud deployment.
---

# Phala Cloud CLI Reference

## Phala Command Line Interface (CLI) Reference

### Usage <a href="#usage" id="usage"></a>

* [Dstack-TEE: Dstack](https://github.com/Dstack-TEE/dstack)
* Bun for runtime and package management
* TypeScript for type safety
* Commander.js for CLI interface
* Zod for runtime validation

## 🚀 Quick Start (5 Minutes) <a href="#f0-9f-9a-80-quick-start-5-minutes" id="f0-9f-9a-80-quick-start-5-minutes"></a>

#### **Install Prerequisites**:

```bash
# Install Bun
curl -fsSL https://bun.sh/install | bash

# Verify Docker is installed
docker --version
```

#### **Install TEE Cloud CLI**:

Install via npm or use npx/bunx

```bash
# Install the CLI globally
npm install -g phala
```

#### **Sign Up and Get API Key**:

To deploy applications to Phala Cloud, you'll need an API key:

* Visit [Phala Cloud](https://cloud.phala.network/login) to log into your Phala Cloud account. If you do not have an account, register [here](https://cloud.phala.network/register?invite=beta).
* After logging in, navigate to the "API Keys" section in your profile
* Create a new API key with an appropriate name (e.g., "CLI Access")
* Copy the generated API key - you'll need it for authentication
*   You can verify your API key using:

    ```bash
    phala auth login [your-phala-cloud-api-key]
    phala auth status
    ```

#### **Deploy Your First Confidential App**:

```bash
# Deploy the webshell Dstack example
phala cvms create
```

Provide a name and select from the drop down of examples

```bash
# ? Enter a name for the CVM: webshell
# ? Choose a Docker Compose example or enter a custom path:

#  lightclient
#   private-docker-image-deployment
#   ❯ webshell
#   custom-domain
#   prelaunch-script
#   timelock-nts
#   ssh-over-tproxy
#   Using example: webshell (~/phala-cloud-cli/examples/webshell/docker-compose.yaml)
#   ✔ Enter number of vCPUs (default: 1): 1

#   ✔ Enter memory in MB (default: 2048): 2048
#   ✔ Enter disk size in GB (default: 20): 20
#   ⟳ Fetching available TEEPods... ✓
#   ? Select a TEEPod: (Use arrow keys)
#   ❯ prod5 (online)
#   prod2 (online)
#   ℹ Selected TEEPod: prod5

#   ✔ Select an image: dstack-dev-0.3.5
#   ⟳ Getting public key from CVM... ✓
#   ⟳ Encrypting environment variables... ✓
#   ⟳ Creating CVM... ✓
#   ✓ CVM created successfully
#   ℹ CVM ID: 2755
#   ℹ Name: webshell
#   ℹ Status: creating
#   ℹ App ID: e15c1a29a9dfb522da528464a8d5ce40ac28039f
#   ℹ App URL: <https://cloud.phala.network/dashboard/cvms/app_e15c1a29a9dfb522da528464a8d5ce40ac28039f>
#    ℹ
#    ℹ Your CVM is being created. You can check its status with:
#    ℹ phala cvms status e15c1a29a9dfb522da528464a8d5ce40ac28039f
```

Now interact with your application in Phala Cloud by going to the url on port 7681 (Example of what a url at port 7681 would look like [https://e15c1a29a9dfb522da528464a8d5ce40ac28039f-7681.dstack-prod5.phala.network](https://e15c1a29a9dfb522da528464a8d5ce40ac28039f-7681.dstack-prod5.phala.network/))

#### **Check the CVM's Attestation**:

```bash
phala cvms attestation

# ℹ No CVM specified, fetching available CVMs...
# ⟳ Fetching available CVMs... ✓
# ✔ Select a CVM: testing (88721d1685bcd57166a8cbe957cd16f733b3da34) - Status: running
# ℹ Fetching attestation information for CVM 88721d1685bcd57166a8cbe957cd16f733b3da34...
# ⟳ Fetching attestation information... ✓
# ✓ Attestation Summary:

# or list the app-id
phala cvms attestation 88721d1685bcd57166a8cbe957cd16f733b3da34
```

## 🏗️ Development Workflow <a href="#f0-9f-8f-97-ef-b8-8f-development-workflow" id="f0-9f-8f-97-ef-b8-8f-development-workflow"></a>

### 1️⃣ Local Development <a href="#id-1-ef-b8-8f-e2-83-a3-local-development" id="id-1-ef-b8-8f-e2-83-a3-local-development"></a>

Develop and test your application locally with the built-in TEE simulator:

```bash
# Start the TEE simulator
phala simulator start

# Build your Docker image
phala docker build --image my-tee-app --tag v1.0.0

# Create an environment file
echo "API_KEY=test-key" > .env
echo "DEBUG=true" >> .env

# Generate and run Docker Compose
phala docker build-compose --image my-tee-app --tag v1.0.0 --env-file ./.env
phala docker run -c ./phala-compose.yaml -e ./.env

```

### 2️⃣ Cloud Deployment <a href="#id-2-ef-b8-8f-e2-83-a3-cloud-deployment" id="id-2-ef-b8-8f-e2-83-a3-cloud-deployment"></a>

Deploy your application to Phala's decentralized TEE Cloud:

```bash
# Set your Phala Cloud API key
phala auth login

# Login to Docker and Push your image to Docker Hub
phala docker login
phala docker build --image my-tee-app --tag v1.0.0
phala docker push --image my-tee-app --tag v1.0.0

# Deploy to Phala Cloud
phala cvms create --name my-tee-app --compose ./docker-compose.yml --env-file ./.env

# Access your app via the provided URL
```

## 💼 Real-World Use Cases for Confidential Computing <a href="#f0-9f-92-bc-real-world-use-cases-for-confidential-computing" id="f0-9f-92-bc-real-world-use-cases-for-confidential-computing"></a>

### 🏦 Financial Services <a href="#f0-9f-8f-a6-financial-services" id="f0-9f-8f-a6-financial-services"></a>

* **Private Trading Algorithms**: Execute proprietary trading strategies without revealing algorithms
* **Secure Multi-Party Computation**: Perform financial calculations across organizations without exposing sensitive data
* **Compliant Data Processing**: Process regulated financial data with provable security guarantees

### 🏥 Healthcare <a href="#f0-9f-8f-a5-healthcare" id="f0-9f-8f-a5-healthcare"></a>

* **Medical Research**: Analyze sensitive patient data while preserving privacy
* **Drug Discovery**: Collaborate on pharmaceutical research without exposing intellectual property
* **Health Record Processing**: Process electronic health records with HIPAA-compliant confidentiality

### 🔐 Cybersecurity <a href="#f0-9f-94-90-cybersecurity" id="f0-9f-94-90-cybersecurity"></a>

* **Secure Key Management**: Generate and store cryptographic keys in hardware-protected environments
* **Threat Intelligence Sharing**: Share cyber threat data across organizations without exposing sensitive details
* **Password Verification**: Perform credential validation without exposing password databases

### 🏢 Enterprise Applications <a href="#f0-9f-8f-a2-enterprise-applications" id="f0-9f-8f-a2-enterprise-applications"></a>

* **Confidential Analytics**: Process sensitive business data without exposure to cloud providers
* **IP Protection**: Run proprietary algorithms and software while preventing reverse engineering
* **Secure Supply Chain**: Validate and process sensitive supply chain data across multiple organizations

### 🌐 Web3 and Blockchain <a href="#f0-9f-8c-90-web3-and-blockchain" id="f0-9f-8c-90-web3-and-blockchain"></a>

* **Private Smart Contracts**: Execute contracts with confidential logic and data
* **Decentralized Identity**: Process identity verification without exposing personal information
* **Trustless Oracles**: Provide verified external data to blockchain applications

## 🧩 Project Structure <a href="#f0-9f-a7-a9-project-structure" id="f0-9f-a7-a9-project-structure"></a>

The Phala Cloud CLI is organized around core workflows:

1. **Authentication**: Connect to your Phala Cloud account
2. **TEEPod Info**: Fetch information about TEEPods (TEEPods are where your docker apps deploy to)
3. **Docker Management**: Build and manage Docker images for TEE
4. **TEE Simulation**: Local development environment
5. **Cloud Deployment**: Deploy to production and manage TEE Cloud deployments

## 📋 Example Dstack Applications <a href="#f0-9f-93-8b-sample-applications" id="f0-9f-93-8b-sample-applications"></a>

Explore these [example dstack applications](https://github.com/dstack-tee/dstack-examples) to understand different use cases for TEE deployment:

* **Timelock Encryption**: Encrypt messages that can only be decrypted after a specified time
* **Light Client**: A lightweight blockchain client implementation
* **SSH Over TEE Proxy**: Secure SSH tunneling through a TEE
* **Web Shell**: Browser-based secure terminal
* **Custom Domain**: Deploy with your own domain name
* **Private Docker Image**: Deploy using private Docker registries

## 🔒 Security <a href="#f0-9f-94-92-security" id="f0-9f-94-92-security"></a>

The TEE Cloud CLI employs several security measures:

1. **Encrypted Credentials**: API keys and Docker credentials are stored with encryption using a machine-specific key
2. **Restricted Permissions**: All credential files are stored with 0600 permissions (user-only access)
3. **No Validation Storage**: API keys are not validated during login, preventing unnecessary transmission
4. **Local Storage**: All credentials are stored locally in the `~/.phala-cloud/` directory

## 🔍 Troubleshooting <a href="#f0-9f-94-8d-troubleshooting" id="f0-9f-94-8d-troubleshooting"></a>

Common issues and solutions:

1. **Docker Build Fails**
   * Verify Docker daemon is running
   * Check Dockerfile path
   * Ensure proper permissions
2. **Simulator Issues**
   * Check if port 8090 is available
   * Verify Docker permissions
3. **Cloud Deployment Fails**
   * Validate API key
   * Confirm image exists on Docker Hub
   * Check environment variables

For detailed help:

```bash
phala --help
phala <command> --help
```
