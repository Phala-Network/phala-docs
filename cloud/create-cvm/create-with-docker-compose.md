# Create CVM with Docker Compose

## Advanced Deployment Options

Phala TEE Cloud provides a familiar Docker Compose experience within a secure TEE environment. To access these advanced configuration options:

1. Navigate to the deployment section in the Phala Cloud dashboard
2. Switch to the **Advanced** tab
3. Edit the Docker Compose configuration directly in the provided editor

## Docker Compose Capabilities

Deploying with Docker Compose on Phala TEE Cloud works just like on a standard server, with the added benefit of confidential computing. You can:

- Specify Docker image names and versions
- Configure port mappings to expose services
- Define environment variables
- Set up volume mounts for persistent storage
- Deploy multi-container applications within a single CVM

## Multi-Service Deployments

One of the key advantages of using Docker Compose is the ability to orchestrate multiple services that work together. All containers defined in your Docker Compose file will run within the same Confidential Virtual Machine (CVM), allowing for secure inter-service communication.

## Private Docker Images

For applications requiring additional security or proprietary code, Phala Cloud supports deployment from private Docker repositories.

➡️ [Learn more about private Docker image deployment](./create-with-private-docker-image)

## Example Configuration

![Docker Compose deployment interface](../../.gitbook/assets/cloud-compose-deployment.png)

The interface provides a full-featured editor with syntax highlighting to help you create and validate your Docker Compose configuration before deployment.
