# Create CVM with Private Docker Images

> **Note:** This feature requires DStack version 0.3.5 or later

## Overview

Phala Cloud enables secure deployment of private Docker images from popular container registries, maintaining confidentiality throughout the deployment process. This capability is essential for organizations with proprietary code or sensitive applications.

## Configuration Methods

### Method 1: Using the Phala Cloud UI

The most straightforward approach is configuring registry access through the user interface:

1. Navigate to **Advanced Features** in the Phala Cloud dashboard
2. Select **Private Container Registry**
3. Enter your registry credentials
4. Save your configuration

![Private Docker registry configuration](../../.gitbook/assets/cloud-private-docker.png)

> 💡 **Security Note:** All authorization information is protected with end-to-end encryption, ensuring your credentials remain confidential.

### Method 2: Using Encrypted Secrets

For automated deployments or enhanced security, you can set registry credentials as encrypted environment variables:

#### Docker Hub Registry

- To download images from Docker Registry, you need to set the following encrypted environment variables: DSTACK_DOCKER_USERNAME and DSTACK_DOCKER_PASSWORD.
- To download images from AWS ECR Private Registry, you need to set the following encrypted environment variables: DSTACK_AWS_ACCESS_KEY_ID, DSTACK_AWS_SECRET_ACCESS_KEY, and DSTACK_AWS_REGION, DSTACK_AWS_ECR_REGISTRY.

## Setting with Phala Cloud API

When using Phala Cloud API to deploy, you still need to set above environment variables.

Check the [Phala Cloud API](https://cloud-api.phala.network/docs) for more details.

## Troubleshooting

If you encounter issues with private image deployment:

1. Verify your credentials are correct and have not expired
2. Ensure the image exists in the specified registry
3. Check that your account has pull permissions for the image
4. Review the CVM logs for detailed error messages

For additional assistance, join our support groups: 🌍 [Global](https://t.me/+nbhjx1ADG9EyYmI9), 🇨🇳 [Chinese](https://t.me/+4PcAE9qTZ1kzM2M9).