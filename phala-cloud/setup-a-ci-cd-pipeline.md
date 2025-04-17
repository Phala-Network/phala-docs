# 🛳️ Setup a CI/CD Pipeline

## Setting Up a CI/CD Pipeline with GitHub Actions for Phala Cloud

### Introduction

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that automates your build, test, and deployment pipeline ([Understanding GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)). In this guide, we will outline how to set up a CI/CD pipeline for a Phala Cloud application using GitHub Actions. We will use the [**Phala Cloud TEE Starter Template**](https://github.com/Phala-Network/cloud-tee-starter-template) repository as a basis, enabling automatic Docker image builds, publishing to Docker Hub, and deployment (or upgrade) of a Confidential Virtual Machine (CVM) on Phala Cloud.&#x20;

By the end, you will have a workflow that on each code update will:&#x20;

* Build a Docker image
* Push it to your Docker registry
* Deploy the docker application to Phala Cloud&#x20;

Throughout the guide, we reference official GitHub Actions documentation for further reading on key concepts.

### Prerequisites

Before setting up the pipeline, make sure you have the following prerequisites:

* **Phala Cloud Starter Repository** – Fork the [cloud-tee-starter-template](https://github.com/Phala-Network/cloud-tee-starter-template) repository to your GitHub account. This contains a sample Phala Cloud application and a template workflow.
* **Phala Cloud Account** – Sign up for Phala Cloud (a redeem code may be required) and obtain access to the Phala Cloud Dashboard. You will need this to create an API key for deployment.
* **Phala Cloud CLI (**[**phala)**](tee-cloud-cli/) – No local installation is required, as the GitHub Actions workflow will install the CLI. However, familiarity with the [Phala Cloud CLI](tee-cloud-cli/) is useful. (The CLI will be used within the workflow to deploy to Phala Cloud.)
* **Docker Hub (or Container Registry) Account** – You need a container registry to push the Docker image. This guide assumes Docker Hub. Ensure you have a Docker Hub username and Personal Access Token (or password) for CI usage. (It’s recommended to use a token for CI/CD rather than your password.)
* **Basic GitHub Actions Knowledge** – Understanding the basics of GitHub Actions (workflow files, jobs, and steps) will help. If you are new to Actions, see GitHub’s [_Understanding GitHub Actions_](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions) guide for an overview.

### 1. Configuring Repository Secrets

To allow GitHub Actions to access credentials and configuration values securely, set up the following **repository secrets** in your forked repository. GitHub encrypts secrets and makes them available to workflows at runtime ([Using secrets in GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/security-guides/encrypted-secrets)).

**Add Secrets in GitHub:** On GitHub, navigate to **Settings** > **Secrets and variables** > **Actions**, then click **“New repository secret”** for each of the following secrets:

* **`DOCKER_REGISTRY_USERNAME`** – Your Docker Hub username (or registry account username).
* **`DOCKER_REGISTRY_PASSWORD`** – Your Docker Hub password or Personal Access Token (use a token for better security) . You can generate a Docker Hub access token in your Docker Hub account settings.
* **`PHALA_CLOUD_API_KEY`** – The API key for your Phala Cloud account. Obtain this from the Phala Cloud Dashboard: log in and use the **“Create Token”** function to generate an API key. Follow the guide on [how to generate a Phala Cloud API Key](../cloud/getting-started/start-from-cloud-cli.md#generate-a-phala-cloud-api-key).
* **`APP_NAME`** – A name for your application deployment on Phala Cloud (e.g. `"my-tee-app"`). Choose a short name with no special characters (letters, numbers, and hyphens are allowed). This name identifies your CVM in Phala Cloud.
* **`DOCKER_IMAGE`** – The full Docker image name (including registry and namespace) that will be built and pushed. For Docker Hub, this is typically `<your-username>/<image-name>`  (For example: `alice/my-tee-app`.)

These secrets will be used by the GitHub Actions workflow to log in to Docker Hub, push the image, and authenticate to Phala Cloud. Ensure all values are correct to avoid any authentication errors during the workflow. Once these secrets are configured, you’re ready to set up the CI/CD workflow.

### 2. Creating the GitHub Actions Workflow

Next, we will create a GitHub Actions workflow file that defines the CI/CD pipeline. In your repository, create a new file at `.github/workflows/deploy.yml` (or you can modify the existing one from the template if present). This YAML file will contain the instructions for building the Docker image and deploying to Phala Cloud.

#### 2.1 Define Workflow Triggers

First, specify when the workflow should run. In our case, we want to trigger the pipeline on code pushes to the main branch (for relevant files) and also allow manual triggers:

```yaml
on:
  push:
    branches: [ main ]
    paths:
      - "api-server/pyproject.toml"
      - "api-server/Dockerfile"
  workflow_dispatch:
```

* **Push to main** – We use `on: push` with `branches: [main]` so that any push to the main branch starts the pipeline. We can also restrict it to run only when certain files change. In the example above, the workflow is filtered to run only if files like the Dockerfile or other key files in the `api-server` directory change. This prevents unnecessary deployments for changes that don’t affect the application (you can adjust this path list as needed).
* **Manual trigger** – The `workflow_dispatch:` key enables manually running the workflow from the GitHub Actions tab. This is useful if you want to redeploy without pushing new code, or if you disabled auto triggers during testing. (See GitHub’s docs on [manually running workflows](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow) for more details on using `workflow_dispatch`.)

With these triggers in place, the workflow will run automatically on merges to main (for specified files) and anytime you manually trigger it via the GitHub UI.

#### 2.2 Build and Push the Docker Image

The first job in the workflow will compile your application into a Docker image and publish it to Docker Hub (or your chosen registry). Below is a breakdown of the steps involved:

1.  **Check Out the Code:** Use the official checkout action to pull the repository code into the runner environment. This is typically the first step in any workflow:

    ```yaml
    - name: Checkout repository  
      uses: actions/checkout@v4
    ```

    This makes the repository files (including the Dockerfile and source code) available for the next steps.
2.  **Log in to Docker Registry:** Authenticate to Docker Hub using the credentials stored in our secrets. This is done with Docker’s login action:

    ```yaml
    - name: Log in to Docker Hub  
      uses: docker/login-action@v3  
      with:  
        registry: docker.io  
        username: ${{ secrets.DOCKER_REGISTRY_USERNAME }}  
        password: ${{ secrets.DOCKER_REGISTRY_PASSWORD }}
    ```

    Here we specify the Docker Hub registry (`docker.io`). The username and password are provided from our GitHub secrets. This step will log in the GitHub runner to Docker Hub so it can push images. (If using a different registry, adjust the `registry` URL accordingly.)
3.  **Build and Push Image:** Build the Docker image and push it to the registry in one step using Docker’s build-push action. For example:

    ```yaml
    - name: Build and push Docker image  
      uses: docker/build-push-action@v5  
      with:  
        context: ./api-server  
        file: ./api-server/Dockerfile  
        push: true  
        tags: ${{ secrets.DOCKER_IMAGE }}:latest, ${{ secrets.DOCKER_IMAGE }}:${{ github.sha }}
    ```

    Let’s break this down:

    * `context` and `file` tell the action where the Dockerfile is and what to build (here we point to the `api-server` directory and its Dockerfile).
    * `push: true` means after building, push the image to the registry.
    * `tags` specifies the image tags. We tag the image with `latest` and also with the Git commit SHA for traceability. The base name of the image (`secrets.DOCKER_IMAGE`) was set in our secrets (e.g., `docker.io/alice/my-tee-app`), so the resulting images will be `docker.io/alice/my-tee-app:latest` and `docker.io/alice/my-tee-app:<git-sha>`.

    After this step, the Docker image of your application is built and uploaded to Docker Hub under your account.

#### 2.3 Set Up Phala Cloud CLI in the Workflow

With the container published, the next part of the pipeline deals with deploying that container image to Phala Cloud. Phala Cloud provides a CLI (`phala` command) for interacting with the platform. In the workflow, we need to install and authenticate this CLI:

1.  **Install Phala CLI:** The Phala CLI is a Node.js-based tool distributed via npm. We can install Node.js and the CLI in one step on the Ubuntu runner. For example:\


    ```yaml
    - name: Install Phala Cloud CLI  
      run: |  
        sudo apt-get update && sudo apt-get install -y nodejs  
        sudo npm install -g pnpm bun  
    ```

    \
    Then, since the CLI is packaged under the `phala` namespace on npm, we can run it using `npx phala ...`. (In this example we install **bun** as well, which is an alternative JavaScript runtime. The key is that we get a Node.js environment so that `npx` is available. The template installs `bun` and uses `npx` interchangeably, which sets up the environment to run the Phala CLI.)
2.  **Authenticate to Phala Cloud:** Use the Phala CLI to log in using the API key we set as a secret. For example:\


    ```yaml
    - name: Authenticate to Phala Cloud  
      run: npx phala auth login ${{ secrets.PHALA_CLOUD_API_KEY }}
    ```

    \
    This command uses the Phala CLI to authenticate the CLI with your Phala Cloud account using the API key. After this, the CLI is authorized to deploy and manage your CVMs. You might optionally run `npx phala auth status` or `phala cvms ls` to verify the login was successful (the template runs a `cvms ls` to list your CVMs as a sanity check).

#### 2.4 Deploy (or Upgrade) the Application on Phala Cloud

Now for the core deployment step. We will use the Phala CLI to create or update a Confidential Virtual Machine running our new Docker image.

1.  **Prepare the Deployment Definition:** The Phala Cloud CLI uses a Docker Compose file to define the application’s services. In the template, there is a `docker-compose.yml` (located in the `api-server` directory) that describes how to run the app’s container. We need to update this compose file to reference the newly built image tag (so it uses the image we just pushed). This can be done with a simple text replacement. For example, if the compose file uses an environment variable placeholder for the image name, we replace it:\


    ```yaml
    - name: Update Docker Compose  
      run: sed -i "s|\${DOCKER_IMAGE}|${{ secrets.DOCKER_IMAGE }}:latest|g" api-server/docker-compose.yml
    ```

    \
    The above command replaces any occurrence of `${DOCKER_IMAGE}` in the compose file with the actual image name (including the `:latest` tag) that we just pushed. Ensure the compose file’s `image:` field is set to `${DOCKER_IMAGE}` (or similar) so that this replacement works. After this, the compose file now points to your latest Docker image.
2.  **Deploy to Phala Cloud:** Finally, run the Phala CLI to deploy the application using the compose file. For the first deployment, you will **create** a new CVM. The command format is:\


    ```bash
    phala cvms create --name <app-name> --compose <path-to-docker-compose.yml> [--env-file <envfile>] [--vcpu <vCPUs>] [--memory <MB>] [--disk-size <GB>] [--teepod-id <id>] [--image <base-image>]
    ```

    \
    In our workflow, it might look like:\


    ```yaml
    - name: Deploy to Phala Cloud  
      run: |  
        npx phala cvms create \  
          -n ${{ secrets.APP_NAME }} \  
          -c api-server/docker-compose.yml \  
          --skip-env \  
          --vcpu 1 --memory 1024 --disk-size 20 \  
          --teepod-id 3 --image dstack-0.3.5
    ```

    \
    Let’s explain the options used:

    * `-n ${{ secrets.APP_NAME }}` sets the name of the app/CVM to the value of our **APP\_NAME** secret (e.g. “my-tee-app”). This name is what you’ll see in the Phala Cloud dashboard.
    * `-c api-server/docker-compose.yml` points to the compose file we just updated, describing the container to run.
    * `--skip-env` indicates we are not providing a separate environment variable file. (If your app needs environment variables, you could store them in an `.env` file and use `--env-file` instead of `--skip-env`.) ([GitHub - Phala-Network/phala-cloud-cli: npx phala free. A CLI to interact with Phala Cloud.](https://github.com/Phala-Network/tee-cloud-cli))
    * The `--vcpu`, `--memory`, `--disk-size` options allocate resources for the CVM (in this example, 1 vCPU, 1 GB RAM, 20 GB disk). Adjust these as needed for your app’s requirements.
    * `--teepod-id 3` and `--image dstack-0.3.5` select the TEE node (teepod) and base TEE image to use. These values may come from Phala Cloud’s available options. In this template, `teepod-id 3` and the `dstack-0.3.5` base image are defaults for the environment. You can consult Phala Cloud’s documentation for other options (for example, different TEE hardware or base images).

    This `phala cvms create` command will request Phala Cloud to launch a new CVM with the given name and configuration. If successful, the new application will be running on Phala Cloud.\


    **On Updates (Upgrades):** For subsequent deployments (e.g., after code changes), you may not want to create a new CVM each time. Instead, you can upgrade the existing CVM to use the new image. The Phala CLI provides an `upgrade` command for this:\


    ```bash
    phala cvms upgrade <app-id> --compose <new-docker-compose.yml> [--env-file ...]
    ```

    \
    This assumes you know the `app-id` of the existing CVM. You can get the app ID from the Phala Cloud dashboard or by running `phala cvms list`. For example:\


    ```bash
    phala cvms upgrade app_123456 --compose ./api-server/docker-compose.yml --env-file ./.env
    ```

    \
    would upgrade the CVM with ID `app_123456` to use the updated compose file. In a CI/CD scenario, you could script the workflow to detect if the app already exists (perhaps by name) and then run `upgrade` instead of `create`. The provided template uses `create` with a fixed name, which will fail if the name is already taken. In practice, you might run `phala cvms list` and conditionally call create or upgrade. (This logic can be added as an enhancement to the workflow.)

### 3. Running the Pipeline and Verifying Deployment

Once your workflow file is ready and secrets are configured, push the workflow (and any code changes) to the repository’s main branch. This should trigger the GitHub Actions workflow. You can monitor the progress in the **Actions** tab of your repository. The workflow will go through the build, push, and deploy steps described above.

If the workflow completes successfully, your application should now be deployed on Phala Cloud. It’s time to verify that everything worked:

_Phala Cloud Dashboard showing a deployed CVM named after the APP\_NAME with a running status. The Phala Cloud dashboard lists your Virtual Machines and their statuses._

* **Phala Cloud Dashboard:** Log in to the Phala Cloud web dashboard and navigate to your list of CVMs (Virtual Machines). You should see an entry for your app (with the name you set in **APP\_NAME**). Its status should be “Running” if deployment succeeded. You can click on it to see details such as resource usage, logs, and the endpoint URL.
* **Application Endpoint:** Phala Cloud will provide a public URL or endpoint for your deployed service (often with a specific port, e.g., port 7681 for web services). Open that URL in your browser or use `curl` to test it. You should be able to reach your application (for example, if it’s a web API, call its health check endpoint). This confirms that the Docker image is running in the Phala enclave.
* **Phala CLI Verification (optional):** You can also use the CLI to double-check status. For example, run `phala cvms list` to see your deployments, or `phala cvms status <app-id>` to get the status of the specific CVM. This is not necessary if the dashboard shows the app as running, but it’s a good way to script checks.

### 4. Troubleshooting

Setting up a CI/CD pipeline can involve a few hurdles. Here are some common issues and how to address them:

* **Authentication Failures:** If the Docker login or Phala Cloud auth steps fail, double-check that your secrets are correctly configured and named. A typo in a secret name or a wrong value (e.g., expired API key or wrong Docker token) will cause authentication to be denied. Update the secret in GitHub and re-run the workflow.
* **Docker Build Errors:** If the build step fails, inspect the workflow logs to see the Docker build output. Common issues include syntax errors in the `Dockerfile` or missing files. Test building the image locally to reproduce the issue. The template’s `api-server/Dockerfile` should work out-of-the-box, but any modifications could introduce errors. Fix any Dockerfile issues and push a new commit to trigger the pipeline again.
* **Deployment Failures:** If the `phala cvms create` command fails, the CLI’s output (visible in the Actions log) will indicate the problem. It could be due to an invalid compose file, insufficient resources, or a name conflict. Ensure the compose file is correct (after the image replacement) and that your APP\_NAME is unique. If the name is already in use, either delete the existing CVM or switch to using the upgrade command as noted above.
* **Debugging Workflows Locally:** It can be helpful to test the GitHub Actions workflow on your local machine. You can use the [`act`](https://github.com/nektos/act) tool to run GitHub Actions workflows locally. This requires Docker on your local machine. By populating an `.env` file with the same secrets (`DOCKER_REGISTRY_USERNAME`, `DOCKER_REGISTRY_PASSWORD`, etc.), you can simulate the workflow and catch issues faster. Keep in mind that deploying to Phala Cloud via `act` will still perform real actions (it will call the Phala API), so use it carefully.

### 5. Additional Resources

* **Phala Cloud Documentation:** For more information on Phala Cloud and CVM deployments, refer to the official Phala Cloud user guide.
* **Phala Cloud CLI Reference:** The [**Phala** **Cloud CLI** repository](https://github.com/Phala-Network/phala-cloud-cli) is open source. You can consult its README and examples for advanced CLI commands and options. This is helpful to understand all flags available for `phala cvms` commands and other capabilities like retrieving attestation reports, etc.
* **GitHub Actions Documentation:** GitHub’s official docs on Actions are an excellent resource if you want to customize or extend your CI/CD pipeline. In particular, see the guides on [workflow syntax and configuration](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) and the [security best practices for actions](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to protect secrets (we referenced some of these above).

By following this outline, you should be able to set up a robust CI/CD pipeline for your Phala Cloud application. Every code change can be seamlessly built into a Docker image and deployed to a secure Phala Cloud environment. Happy deploying!
