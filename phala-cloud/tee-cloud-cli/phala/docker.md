# docker

## Command: docker

#### Syntax

```
phala docker [options] [command]
```

### Description

The `phala docker`  command is used to your Docker images. Using this tool is optional, and it is okay to use the native docker CLI instead.

```bash
Usage: phala docker [options] [command]

Login to Docker Hub and manage Docker images

Options:
  -h, --help          display help for command

Commands:
  login [options]     Login to Docker Hub
  build [options]     Build a Docker image
  push [options]      Push a Docker image to Docker Hub
  generate [options]  Generate a Docker Compose file
  help [command]      display help for command
```

### Examples

* Display help

```bash
phala docker --help
```

* Login to Docker

> Note that the login will use the existing docker login session and will not require another login attempt.

```bash
phala docker login --username hashwarlock
```

<details>

<summary>Example Output</summary>

```bash
⟳ Logging in to Docker Hub as hashwarlock... ✓: Logged in as hashwarlock
✓ hashwarlock is logged in to Docker Hub
```

</details>

* Build a Dockerfile

> Note: During the build process, the logs of the build will be output to a file in the root directory of your project in the `.phala-cloud/logs/`folder.

```bash
phala docker build
```

<details>

<summary>Example Output</summary>

```bash
✔ Enter the Docker image name: elizas
✔ Enter the Docker image tag: v0.0.1o
✔ Default Dockerfile found at ~/eliza/Dockerfile                                                           │
✔ Enter the path to your Dockerfile: (Dockerfile)
Latest 10 lines (full log at ~/eliza/.phala-cloud/logs/elizas-build-2025-03-14T20-43-16-210Z.log):
--------------------------------------------------
#30 [builder  3/17] RUN apt-get update &&     apt-get install -y curl git python3 make g++ unzip build-essential nodejs &&     apt-get clean &&     rm -rf /var/lib/apt/lists/*
#30 CACHED
#31 [stage-1 13/13] COPY --from=builder /app/scripts ./scripts
#31 CACHED
#32 exporting to image
#32 exporting layers done
#32 writing image sha256:a74b8e777075afd7b09d2107bcbc26cc1f602d81a9cf6491d5d4476cad2a6da4 done
#32 naming to docker.io/hashwarlock/elizas:v0.0.1o done
#32 DONE 0.0s
View build details: docker-desktop://dashboard/build/orbstack/orbstack/gd75239yegh0twa3zkuq1macb

Operation completed. Full log available at: ~eliza/.phala-cloud/logs/elizas-build-2025-03-14T20-43-16-210Z.log
✓: Docker image hashwarlock/elizas:v0.0.1o built successfully
✓ Docker image hashwarlock/elizas:v0.0.1o built successfully
```

</details>

* Push Docker Image to Docker Hub

```bash
phala docker push --image hashwarlock/elizas:v0.0.1o
```

<details>

<summary>Example Output</summary>

```bash
Latest 10 lines (full log at ~/eliza/.phala-cloud/logs/elizas-push-2025-03-14T21-23-14-847Z.log):
--------------------------------------------------
1de7295ab7c5: Layer already exists
90e8688db369: Layer already exists
25d07e7c0ece: Layer already exists
bcba87ec50fa: Layer already exists
ba2b458ab48c: Layer already exists
2ccdaba7f460: Layer already exists
5bcbf42c7074: Layer already exists
7ff9bfab192e: Layer already exists
3e6ae445f28c: Layer already exists
c0f1022b22a9: Layer already exists
v0.0.1o: digest: sha256:1fa0685e564d67a451f4e7ce060e95da5ad740d937e69202fcc8957468a66a08 size: 3876

Operation completed. Full log available at: ~/eliza/.phala-cloud/logs/elizas-push-2025-03-14T21-23-14-847Z.log
✓: Docker image hashwarlock/elizas:v0.0.1o pushed successfully
✓ Docker image hashwarlock/elizas:v0.0.1o pushed successfully
```

</details>

* Generate a Basic Docker Compose File

```bash
phala docker generate --image elizas --tag v0.0.1o -e .env
```

<details>

<summary>Example Output</summary>

Command Output:

```bash
✔ File ~/eliza/docker-compose.yml already exists. Overwrite? No
✔ Enter alternative output path: ~/eliza/docker-generated-compose.yml
ℹ Generating Docker Compose file for elizas:v0.0.1o using env file: .env
✓ Backup of docker compose file created at: .phala-cloud/compose/elizas-v0.0.1o-tee-compose.yaml
✓ Docker Compose file generated successfully: ~/eliza/docker-generated-compose.yml
```

Generated File:

```yaml
version: '3.8'
services:
  app:
    image: hashwarlock/elizas:v0.0.1o
    container_name: app
    volumes:
      - /var/run/tappd.sock:/var/run/tappd.sock
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - SERVER_PORT=${SERVER_PORT}
      - POSTGRES_URL=${POSTGRES_URL}
      - EVM_CHAINS=${EVM_CHAINS}
      - BIRDEYE_API_KEY=${BIRDEYE_API_KEY}
      - COMMUNITY_MANAGER_DISCORD_APPLICATION_ID=${COMMUNITY_MANAGER_DISCORD_APPLICATION_ID}
      - COMMUNITY_MANAGER_DISCORD_API_TOKEN=${COMMUNITY_MANAGER_DISCORD_API_TOKEN}
      - SOCIAL_MEDIA_MANAGER_DISCORD_APPLICATION_ID=${SOCIAL_MEDIA_MANAGER_DISCORD_APPLICATION_ID}
      - SOCIAL_MEDIA_MANAGER_DISCORD_API_TOKEN=${SOCIAL_MEDIA_MANAGER_DISCORD_API_TOKEN}
      - LIAISON_DISCORD_APPLICATION_ID=${LIAISON_DISCORD_APPLICATION_ID}
      - LIAISON_DISCORD_API_TOKEN=${LIAISON_DISCORD_API_TOKEN}
      - PROJECT_MANAGER_DISCORD_APPLICATION_ID=${PROJECT_MANAGER_DISCORD_APPLICATION_ID}
      - PROJECT_MANAGER_DISCORD_API_TOKEN=${PROJECT_MANAGER_DISCORD_API_TOKEN}
      - DEV_SUPPORT_DISCORD_APPLICATION_ID=${DEV_SUPPORT_DISCORD_APPLICATION_ID}
      - DEV_SUPPORT_DISCORD_API_TOKEN=${DEV_SUPPORT_DISCORD_API_TOKEN}
      - INVESTMENT_MANAGER_DISCORD_APPLICATION_ID=${INVESTMENT_MANAGER_DISCORD_APPLICATION_ID}
      - INVESTMENT_MANAGER_DISCORD_API_TOKEN=${INVESTMENT_MANAGER_DISCORD_API_TOKEN}
    restart: always
```



</details>
