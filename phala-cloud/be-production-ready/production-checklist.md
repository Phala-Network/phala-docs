---
description: Production checklist for launch.
---

# Production Checklist

Ensure your application is ready for a reliable, secure, and observable production deployment on Phala Cloud. This checklist helps you avoid common pitfalls and design your app for TEE, covering restart tolerance, secret management, observability, and safe upgrades.

{% stepper %}
{% step %}
## Prepare Your App for Restart

### 1.1. Prepare Your App for Restart

Make sure your application can handle being stopped and started at any time. Avoid relying on in-memory state that would be lost on restart, and implement graceful shutdown handlers if possible so the app can clean up or save state when the container stops. This ensures a restart (or relocation to a new node) won’t corrupt your app’s workflow or data.

### 1.2. Persist data on volumes

Use [Docker volumes](https://docs.docker.com/reference/compose-file/services/#volumes) for any data that needs to persist across restarts or upgrades. Write files (databases, user uploads, etc.) to a mounted volume rather than the container’s ephemeral filesystem. Phala Cloud preserves these volumes and encrypts the data at rest, so restarting or upgrading your CVM will not lose your stored data.

Be sure to configure the volume in your docker-compose.yml to capture the right directories.
{% endstep %}

{% step %}
## Secrets Management

### 2.1. Use encrypted environment variables

Store secrets (API keys, tokens, passwords) as [_Encrypted Variables_](../phala-cloud-user-guides/create-cvm/set-secure-environment-variables.md) in your Docker Compose configuration. Phala Cloud’s deployment process encrypts your secrets on the client side and only decrypts them inside the TEE at runtime . This means even the Phala Cloud cannot read your plaintext secrets.

### 2.2. Prefer TEE-managed keys when possible

Phala’s TEE-managed keys are stable across restarts and upgrades, so your encrypted data remains accessible without manual key handling.

These keys are generated and sealed within the TEE using the Dstack SDK, and cannot be accessed or exported by anyone, not even you as the developer. This ensures that only the TEE can use the key, unlike Nitro or Azure KMS where the developer retains access. It eliminates the risk of accidental exposure while preserving seamless availability across lifecycle events.
{% endstep %}

{% step %}
## App Upgrade

### 3.1. Understand the Upgrade Flow

Phala Cloud handles upgrades by restarting your CVM with the new configuration (docker compose file and the secrets).

When you deploy an update, the platform will restart the CVM, pull your updated Docker images, and then start it again with the new configurations. Any defined volume data is reattached to the new instance, so it carries over seamlessly. The entire CVM and all containers in your Compose will reboot during an upgrade, meaning there will be a brief downtime for that instance.

### 3.2. Manage secrets during upgrades

If your secrets haven’t changed, you can skip re-entering them. Your CVM will reuse the previously stored encrypted variables. But if you update any secret, you must provide the full variable list again. The platform replaces all secrets during an upgrade. Partial updates will result in dropped variables, so always double-check that all required secrets are included.

### 3.3. Test for upgrade safety

Even though Phala Cloud preserves your disk data on upgrade, your app update itself could introduce bugs or incompatibilities. A common pitfall is deploying a new version that accidentally wipes or misinterprets existing data (for example, a flawed migration script or a logic error that deletes files).

To avoid surprises, always test the upgrade process in a staging environment or with sample data. Verify that your app comes back up correctly and that it handles existing persisted data as expected. This practice will catch any logical issues _before_ they impact your production users.

### 3.4. Use rolling deployments for zero downtime

Currently Phala Cloud doesn’t offer built-in support for rolling upgrades, but you can achieve minimal downtime by managing it yourself. If you run multiple CVMs with app-level load balancing, upgrade them one at a time to keep at least one instance online. This approach reduces downtime and makes it easier to resolve problems if something goes wrong, but it requires coordination in your deployment logic or orchestration setup.
{% endstep %}

{% step %}
## Observability

### 4.1. Export metrics from your app

Include a metrics exporter (such as Prometheus Node Exporter) as a sidecar container in your Docker Compose to collect system and application metrics. For example, running a Node Exporter will expose CPU, memory, and other host metrics for your CVM . Ensure your application also exposes any custom metrics or health endpoints needed for monitoring.

<details>

<summary>Example Docker Compose for node-exporter</summary>

```yaml
services:
  node_exporter:
    image: quay.io/prometheus/node-exporter:latest
    container_name: node_exporter
    command:
      - '--path.rootfs=/host'
    network_mode: host
    pid: host
    restart: unless-stopped
    volumes:
      - '/:/host:ro,rslave'
```

The config will expose the metrics under the endpoint `https://{appd-id}-9100.dstack-prod{n}.phala.network`  protected with TLS by default. You can then connect your Prometheus server to scrape the metrics.

You may also want to set up HTTP basic auth to limit the read access to yourself, as [described here.](https://stackoverflow.com/questions/74490690/node-exporter-basic-auth-docker-compose)

</details>

### 4.2. Plan for log access

Decide how you will handle application logs in production. By default, Phala Cloud treats logs as public. You have the option to disable Public Logs in the Advanced settings. If you keep logs private, set up a secure log viewer like [Dozzle](https://dozzle.dev/) or [Grafana Loki](https://grafana.com/oss/loki/) to forward logs to an external logging service so you can still debug issues.
{% endstep %}
{% endstepper %}
