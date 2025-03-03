
# Expose Service Port

In Docker, you can specify the **HTTP ports** you want to expose by [**configuring port publishing**](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/#publishing-ports) using the format **HOST_PORT:CONTAINER_PORT**. This configuration forwards requests sent to **HOST_PORT** to the container’s program listening on **CONTAINER_PORT**.

When deploying your Docker program to Phala TEE Cloud, the process remains the same. You should specify the port mapping in the Docker Compose file using the **ports** field, as shown below:

```yaml
services:
  web:
    build: .
    ports:
      - "80:8000"
  db:
    image: postgres
    ports:
      - "8001:5432"
```

After deployment, you will see two public endpoints on the dashboard. These URLs can be used to publicly access the service running in Docker. Behind the scenes, our cloud platform parses the Docker Compose file and automatically configures the network forwarding.

<figure><img src="../../.gitbook/assets/cloud-network-page.png" alt="network-page"><figcaption></figcaption></figure>

**🎉 Congratulations! You've successfully deployed your application into a TEE. If you're interested in learning more, such as how to prove your application's integrity to others or manage application logs, keep reading.**
