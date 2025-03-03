
# Deploy with Private Docker Image

Note: ONLY DStack-0.3.5 and later versions support this feature

## Setting with UI

Phala Cloud supports downloading private Docker images from Docker Registry and AWS ECR Private Registry. You need to set the authorization information in **Advanced Features** → **Private Container Registry.**.

💡 Note those authorization information will be encrypted at the E2E level.

<figure><img src="../../.gitbook/assets/cloud-private-docker.png" alt="private-docker"><figcaption></figcaption></figure>

## Setting with Encrypted Secrets

Another way is to setting those information through in **Encrypted Secrets**.

- To download images from Docker Registry, you need to set the following encrypted environment variables: DSTACK_DOCKER_USERNAME and DSTACK_DOCKER_PASSWORD.
- To download images from AWS ECR Private Registry, you need to set the following encrypted environment variables: DSTACK_AWS_ACCESS_KEY_ID, DSTACK_AWS_SECRET_ACCESS_KEY, and DSTACK_AWS_REGION, DSTACK_AWS_ECR_REGISTRY.

## Setting with Cloud API

When using Cloud API to deploy, you still need to set above environment variables.

Check the [Cloud API]({{ site.baseurl }}/docs/cloud-api) for more details.