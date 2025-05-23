# Setup a CI/CD Pipeline

This is a starter template for building a Phala Cloud TEE application easily with CI/CD instead of manually local build and deploy. You can fork this repository to start your own Cloud TEE application.

### 📋 Prerequisites

* Fork the GitHub repository [`cloud-tee-starter-template`](https://github.com/Phala-Network/cloud-tee-starter-template)&#x20;
* Phala Cloud account ([Sign up with Redeem Code](https://cloud.phala.network/register?invite=beta))
* Docker Hub/Registry account, to push the built docker image to the registry

### 🔧 Step 1: Configure Repository Secrets

1. Go to your repo **Settings → Secrets and variables → Actions**
2. Add these required secrets:

| Secret Name                | Description                                             | How to Get                                                                                  |
| -------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `DOCKER_REGISTRY_USERNAME` | Your container registry username                        | From your Docker Hub/Registry account                                                       |
| `DOCKER_REGISTRY_PASSWORD` | Registry password/access token                          | [Generate access token](https://docs.docker.com/docker-hub/access-tokens/)                  |
| `PHALA_CLOUD_API_KEY`      | Phala Cloud authentication key                          | From [Phala Cloud Dashboard](https://cloud.phala.network/dashboard/tokens) → "Create Token" |
| `APP_NAME`                 | Deployment name (e.g., `my-tee-app`)                    | Choose name without special characters except `-`                                           |
| `DOCKER_IMAGE`             | Full image path (e.g., `docker.io/username/image-name`) | Follow registry naming conventions                                                          |

The above secrets are required for the deployment workflow to work. And you can add more secrets to the repository as needed. These secrets will be used in the deployment workflow to build the docker image and deploy to Phala TEE Cloud. Once the secrets are added, you can trigger the deployment workflow anytime.

### 🚀 Step 2: Deployment Workflow

The GitHub Action will automatically:

1. Build Docker image from Dockerfile, `api-server/Dockerfile` in this example.
2. Push built docker image to your container registry
3. Update the docker compose file with the new image
4. Deploy to Phala TEE Cloud using `phala` CLI with the name you set in `APP_NAME` with the updated docker compose file.

#### Trigger Conditions:

```yaml
on:
  push:
    branches: [main]
    paths:  # Only trigger when these files change, you can add more files to the list
      - "api-server/pyproject.toml"
      - "api-server/Dockerfile"
  workflow_dispatch:  # Manual trigger available
```

If you want to deploy to Phala TEE Cloud manually, you can trigger the workflow manually from the GitHub Actions page.

#### Docker Image Build and Publish:

Here the docker image that will be used is built and published to the Docker registry. After this is done, the docker image is updated in the `./api-server/docker-compose.yml` file.

```yaml
- name: Log in to GitHub Container Registry
  uses: docker/login-action@v3
  with:
    registry: ${{ env.DOCKER_REGISTRY }}
    username: ${{ env.DOCKER_REGISTRY_USERNAME }}
    password: ${{ env.DOCKER_REGISTRY_PASSWORD }}

- name: Build and Push Docker image
  uses: docker/build-push-action@v5
  with:
    context: api-server
    file: api-server/Dockerfile
    push: true
    tags: |
      ${{ env.DOCKER_IMAGE }}:latest
          ${{ env.DOCKER_IMAGE }}:${{ github.sha }}
- name: Update Docker Compose
  run: |
    sed -i "s|\${DOCKER_IMAGE}|${DOCKER_IMAGE}|g" ./api-server/docker-compose.yml
```

#### Phala Cloud Github Action:

Next, you will see where the `PHALA_CLOUD_API_KEY` and the `APP_NAME` will be used when configuring your CVM for deployment.

```yaml
- name: Deploy to Phala Cloud
  uses: Leechael/phala-deploy-action@v2
  with:
    # Required parameters
    phala-api-key: ${{ secrets.PHALA_CLOUD_API_KEY }}
    
    # Optional parameters (with defaults)
    cvm-name: ''
    compose-file: './api-server/docker-compose.yml'  # Default: './docker-compose.yml'
    vcpu: '4'                         # Default: '2'
    memory: '4096'                    # Default: '2048'
    disk-size: '10'                   # Default: '40'
    envs: |                           # Environment variables in YAML format (will be converted to dotenv)
      EXAMPLE_ENV_VAR: 'none'
    app-id: ${{ secrets.APP_ID }}     # App ID of existing CVM to (if updating)
    node-id: ''                       # Node ID (Teepod ID)
    base-image: ''                    # Base image to use for the CVM
```

Lastly, the Phala deploy action will launch the CVM based on the configuration. Some important information for the action:

<table><thead><tr><th>Parameter Name</th><th width="324.671875">Description</th><th>Value</th></tr></thead><tbody><tr><td><code>phala-api-key</code></td><td>The API key for your Phala Cloud account. Obtain this from the Phala Cloud Dashboard: log in and use the <strong>“Create Token”</strong> function to generate an API key. Follow the guide on <a href="https://docs.phala.network/phala-cloud/getting-started/start-from-cloud-cli#generate-a-phala-cloud-api-key">how to generate a Phala Cloud API Key</a>.</td><td>string (i.e phat_kekwhfh)</td></tr><tr><td><code>cvm-name</code></td><td>The name of the app/CVM to the value of our <strong>APP_NAME (if set)</strong> secret (e.g. “my-tee-app”). This name is what you’ll see in the Phala Cloud dashboard.</td><td>string (i.e my-app)</td></tr><tr><td><code>compose-file</code></td><td>The docker compose file that will be our docker application deployed to the CVM.</td><td>file path (i.e. <code>./api-server/docker-compose.yml</code>)</td></tr><tr><td><code>vcpu</code></td><td>Number of vCPUs for the CVM</td><td>string|number (i.e. "2")</td></tr><tr><td><code>memory</code></td><td>Amount of memory for the CVM</td><td>string|number in MB (i.e. "2048")</td></tr><tr><td><code>disk-size</code></td><td>Amount of disk storage for the CVM</td><td>string|number in GB (i.e. "20")</td></tr><tr><td><code>envs</code></td><td>Encrypted environment variables for the CVM</td><td><code>KEY: VALUE</code></td></tr><tr><td><code>app-id</code></td><td>(For upgrades) The app ID of the CVM. This is used for upgrades</td><td><code>app-id</code></td></tr><tr><td><code>node-id</code></td><td>The TEE node (teepod) ID of the TEE server. (Can leave empty)</td><td>string|number (i.e. "3")</td></tr><tr><td><code>base-image</code></td><td>Dstack base image used to deploy the CVM</td><td>string (i.e. <code>dstack-0.3.5</code> or <code>dev-dstack-0.3.5</code>)</td></tr></tbody></table>

### ✅ Step 3: Verify The Deployment

After successful workflow run once the workflow is triggered and the deployment is successful, you can verify the deployment on [Phala Cloud Dashboard](https://cloud.phala.network/dashboard).

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

And then you can see the deployment details on the dashboard and visit the endpoint to test the application.

### 🛠️ Troubleshooting

Common issues:

1. **Authentication Errors**: Verify all secrets are correctly set
2. **Docker Build Failures**: Check `api-server/Dockerfile` syntax
3. **Debug Github Actions Locally**: You can debug the Github Actions locally by running `act` command. The `act` can be installed from https://github.com/nektos/act. The secerts you need to set are the same as the ones in the repository secrets to local `.env` file in the root of the repository.
