# Setting Up Custom Domain

If you prefer to use your own custom domain, this page will guide you through setting this up in minutes.

## Custom Domain Setup for dstack Applications

This is a solution for setting up custom domains with automatic SSL certificate management for dstack applications using Cloudflare DNS and Let's Encrypt.

### Overview

This project enables you to run dstack applications with your own custom domain, complete with:

* Automatic SSL certificate provisioning and renewal via Let's Encrypt
* Cloudflare DNS configuration for CNAME, TXT, and CAA records
* Nginx reverse proxy to route traffic to your application
* Certificate evidence generation for verification

<details>

<summary>How It Works</summary>

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

### Prerequisites

* Host your domain on [Cloudflare](https://dash.cloudflare.com/) and have access to the Cloudflare account with API token

### Create Cloudflare API Token

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

### Deployment

{% hint style="info" %}
For more details, checkout the [github repository](https://github.com/Dstack-TEE/dstack-examples/blob/main/custom-domain/dstack-ingress/README.md) for the dstack-ingress dstack examples.
{% endhint %}

First you will go to your Phala Cloud Dashboard and deploy a new CVM. Select **docker-compose.yml** option for deployment then take the past the docker compose file below into the **Advanced** tab of the CVM configration page.

```yaml
services:
  dstack-ingress:
    image: kvin/dstack-ingress@sha256:8dfc3536d1bd0be0cb938140aeff77532d35514ae580d8bec87d3d5a26a21470
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
* `DOMAIN`: Your custom domain
* `GATEWAY_DOMAIN`: The dstack gateway domain. (e.g. `_.dstack-prod5.phala.network` for Phala Cloud)
* `CERTBOT_EMAIL`: Your email address used in Let's Encrypt certificate requests
* `TARGET_ENDPOINT`: The plain HTTP endpoint of your dstack application
* `SET_CAA`: Set to `true` to enable CAA record setup

#### Deploy to Phala Cloud

If you prefer video content, check the YouTube tutorial here.

{% embed url="https://youtu.be/arQg6nXnSpc" %}

Here is how it should look like in the dashboard.

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

Next you need to grab your Cloudflare API Token for your domain, and fill in your environment variables. For this example, deploy to **prod5**.

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

Click **Create** button and your CVM will deploy in a couple minutes with the custom domain. Here is an example of a custom domain deployed to [phala.incipient.ltd. ](https://phala.incipient.ltd)

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

## Domain Attestation and Verification

The dstack-ingress system provides mechanisms to verify and attest that your custom domain endpoint is secure and properly configured. This comprehensive verification approach ensures the integrity and authenticity of your application.

### Evidence Collection

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
