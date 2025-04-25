---
description: For users that want to bring their own domain for their CVM.
---

# Setting Up Custom Domain

If you prefer video content, check the YouTube tutorial here.

{% embed url="https://youtu.be/arQg6nXnSpc" %}

## Prerequisites

* Host your domain on [Cloudflare](https://dash.cloudflare.com/)
* Have access to the Cloudflare account with API token

## Create Cloudflare API Token

If you have not generated an API Token for your custom domain management then follow these steps:

<details>

<summary>Create API Token</summary>

### :one: **Go to your Cloudflare Dashboard**

In your dashboard, select the domain you'd like to use and find the option to **Get Your API Token**

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

### :two: Create API Token

Select the **Create Token** button as shown below

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

### :three: Select a Template

The next page will have several templates. Select the template to **Edit zone DNS** as shown below

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

### :four: Finalize API Token Creation

Next select your domain in the **Zone Resources** section then click **Continue to summary** button as shown below

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

Congrats! You've now created your API Token to use for your environment variable.

</details>

## Deployment

{% hint style="info" %}
For more details, checkout the [github repository](https://github.com/Dstack-TEE/dstack-examples/blob/main/custom-domain/dstack-ingress/README.md) for the dstack-ingress dstack examples.
{% endhint %}

For this deployment example, we will be an `nginx` application where the `dstack-ingress` container that will forward traffic the `TARGET_ENDPOINT` that points to the `nginx` application with an exposed port `80` . It is important to know that this can change based on how your docker app's compose file is configured.

<details>

<summary>Why <code>TARGET_ENDPOINT</code> Matters</summary>

*   **Tells the proxy where to send traffic**\
    When a request arrives at `https://your-custom-domain`, `dstack-ingress` decrypts TLS and then forwards the HTTP payload to exactly the URL in `TARGET_ENDPOINT`.

    ```
    https://pastebin.example.com  →  dstack-ingress  →  http://app:80
    ```

- **Decouples host networking from container internals**\
  Your app can stay on port 80 (or 3000, or the exposed port of your app), and you never have to re-map messy host ports. The ingress simply forwards traffic to “app:80” over the Docker bridge network.

* **Enables dynamic, multi-service gateways**\
  If you later add more services behind the same ingress (e.g. `api-service:4000`), you only need to change their corresponding `TARGET_ENDPOINT` or add routing rules—no firewall or host-port juggling required.

In the following example, we will show a more complex configuration for an ElizaOS Deployment where the docker app has a Postgresql + pgvector container that serves as a DB for the ElizaOS `eliza` container. The `SERVER_PORT` is expected to be port `3000` in this example where the `dstack-ingress` will forward traffic through the `DOMAIN` environment variable.

```yaml
version: '3.8'
services:
  postgres:
    image: ankane/pgvector:latest
    environment:
        - POSTGRES_PASSWORD=postgres
        - POSTGRES_USER=postgres
        - POSTGRES_DB=eliza
        - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
        - postgres-data:/var/lib/postgresql/data
    ports:
        - "127.0.0.1:5432:5432"
    healthcheck:
        test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
        interval: 5s
        timeout: 5s
        retries: 5
    restart: always
    networks:
      - eliza-network

  eliza:
    image: hashwarlock/elizaos:beta0
    command: sh -c "bun run start"
    volumes:
      - /var/run/tappd.sock:/var/run/tappd.sock
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - SERVER_PORT=${SERVER_PORT}
      - POSTGRES_URL=postgres://postgres:postgres@postgres:5432/eliza
    depends_on:
      postgres:
        condition: service_healthy
    restart: always
    networks:
      - eliza-network

  dstack-ingress:
    image: kvin/dstack-ingress@sha256:5cbf6eff9983fad4018de90ed11b0593c84f2022ddfc64b9eb513d1ba79970c7
    ports:
      - "443:443"
    environment:
      - DOMAIN=${DOMAIN}
      - GATEWAY_DOMAIN=${GATEWAY_DOMAIN}
      - CERTBOT_EMAIL=${CERTBOT_EMAIL}
      - CLOUDFLARE_API_TOKEN=${CLOUDFLARE_API_TOKEN}
      - SET_CAA=true
      - TARGET_ENDPOINT=http://eliza:3000
    volumes:
      - /var/run/tappd.sock:/var/run/tappd.sock
      - cert-data:/etc/letsencrypt
    restart: unless-stopped
    networks:
      - eliza-network

networks:
  eliza-network:
    driver: bridge

volumes:
  postgres-data:
  cert-data:

```

</details>

Now on to the deployment. Go to you Phala Cloud Dashboard and deploy a new CVM. Select **docker-compose.yml** option for deployment then take the past the docker compose file below into the **Advanced** tab of the CVM configration page.

```yaml
services:
  dstack-ingress:
    image: kvin/dstack-ingress@sha256:5cbf6eff9983fad4018de90ed11b0593c84f2022ddfc64b9eb513d1ba79970c7
    ports:
      - "443:443"
    environment:
      - CLOUDFLARE_API_TOKEN=${CLOUDFLARE_API_TOKEN}
      - DOMAIN=${DOMAIN}
      - GATEWAY_DOMAIN=${GATEWAY_DOMAIN}
      - CERTBOT_EMAIL=${CERTBOT_EMAIL}
      - SET_CAA=true
      - TARGET_ENDPOINT=http://app:80
    volumes:
      - /var/run/tappd.sock:/var/run/tappd.sock
      - cert-data:/etc/letsencrypt
    restart: unless-stopped
  app:
    image: nginx  # Replace with your application image
    restart: unless-stopped
volumes:
  cert-data:  # Persistent volume for certificates
```

Explanation of environment variables:

* `CLOUDFLARE_API_TOKEN`: Your Cloudflare API token
* `DOMAIN`: Your custom domain (i.e. `your-domain.com` )
* `GATEWAY_DOMAIN`: The dstack gateway domain. (e.g. `_.dstack-prod5.phala.network` for Phala Cloud **prod5** server)
* `CERTBOT_EMAIL`: Your email address used for Let's Encrypt email notifications
* `TARGET_ENDPOINT`: **Where the ingress should forward all incoming traffic**—i.e. the upstream service application:port. In this case, we point to the `nginx` app on port `80`.&#x20;
* `SET_CAA`: Set to `true` to enable CAA record setup

Now copy and paste the docker-compose.yaml code above into the **Advanced** Tab similar to the screnshot below.

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

Next you need to grab your Cloudflare API Token for your domain, and fill in your environment variables. For this example, deploy to **prod5** ( domai&#x6E;**:**`dstack-prod5.phala.network`).

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

Click **Create** button and your CVM will deploy in a couple minutes with the custom domain. Here is an example of a custom domain deployed to [phala.incipient.ltd. ](https://phala.incipient.ltd)

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

**Congratulations!** You've successfully deployed your CVM with a custom domain. Your application is now secured with Zero Trust HTTPS, thanks to the seamless integration of Cloudflare DNS and Let's Encrypt.  If you are interested in the verification of this process check the [#domain-attestation-and-verification](setting-up-custom-domain.md#domain-attestation-and-verification "mention").

## Knowledge

Now you have the knowledge base on the custom domain deployment with a basic nginx dstack application. The features you have used to enable your custom domain are defined below:

* Automatic SSL certificate provisioning and renewal via Let's Encrypt
* Cloudflare DNS configuration for CNAME, TXT, and CAA records
* Nginx reverse proxy to route traffic to your application
* Certificate evidence generation for verification

<details>

<summary>Read The Full Explanation</summary>

The dstack-ingress system provides a seamless way to set up custom domains for dstack applications with automatic SSL certificate management. Here's how it works:

1. **Initial Setup**:
   * When first deployed, the container automatically obtains SSL certificates from Let's Encrypt using DNS validation
   * It configures Cloudflare DNS by creating necessary CNAME, TXT, and optional CAA records
   * Nginx is configured to use the obtained certificates and proxy requests to your application
2. **DNS Configuration**:
   * A CNAME record is created to point your custom domain to the dstack gateway domain
   * A TXT record is added with application identification information to help dstack-gateway to route traffic to your application
   * If enabled, CAA records are set to restrict which Certificate Authorities can issue certificates for your domain
3. **Certificate Management**:
   * Select the **Create Token** button as shown below
   * SSL certificates are automatically obtained during initial setup
   * A scheduled task runs twice daily to check for certificate renewal
   * When certificates are renewed, Nginx is automatically reloaded to use the new certificates
4. **Evidence Generation**:
   * The system generates evidence files for verification purposes
   * These include the ACME account information and certificate data
   * Evidence files are accessible through a dedicated endpoint

</details>

### Domain Attestation and Verification

The dstack-ingress system provides mechanisms to verify and attest that your custom domain endpoint is secure and properly configured. This comprehensive verification approach ensures the integrity and authenticity of your application.

#### Evidence Collection

When certificates are issued or renewed, the system automatically generates a set of cryptographically linked evidence files:

1. **Access Evidence Files**:
   * Evidence files are accessible at `https://your-domain.com/evidences/`
   * Key files include `acme-account.json`, `cert.pem`, `sha256sum.txt`, and `quote.json`
2. **Verification Chain**:
   * `quote.json` contains a TDX quote with the SHA-256 digest of `sha256sum.txt` embedded in the report\_data field
   * `sha256sum.txt` contains cryptographic checksums of both `acme-account.json` and `cert.pem`
   * When the TDX quote is verified, it cryptographically proves the integrity of the entire evidence chain
3. **Certificate Authentication**:
   * `acme-account.json` contains the ACME account credentials used to request certificates
   * When combined with the CAA DNS record, this provides evidence that certificates can only be requested from within this specific TEE application
   * `cert.pem` is the Let's Encrypt certificate currently serving your custom domain

You can check the example of the deployment at [phala.incipient.ltd/evidences/](https://phala.incipient.ltd/evidences/).

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

### CAA Record Verification

If you've enabled CAA records (`SET_CAA=true`), you can verify that only authorized Certificate Authorities can issue certificates for your domain:

```bash
dig CAA your-domain.com
```

The output will display CAA records that restrict certificate issuance exclusively to Let's Encrypt with your specific account URI, providing an additional layer of security.

### TLS Certificate Transparency

All Let's Encrypt certificates are logged in public Certificate Transparency (CT) logs, enabling independent verification:

**CT Log Verification**:

* Visit [crt.sh](https://crt.sh/) and search for your domain
* Confirm that the certificates match those issued by the dstack-ingress system
* This public logging ensures that all certificates are visible and can be monitored for unauthorized issuance
