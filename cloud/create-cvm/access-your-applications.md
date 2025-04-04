
# Access Your Applications

To export your service publicly, you need to configure the PORT exposing when deploying your application. After deployment, click **View Details** in the top-right corner of the CVM instance card and switch to the **Network** tab below. You will see the list of **Endpoint** there. These URLs are generated automatically by parsing the PORT configurations in the Docker Compose file. The format for the URL prefix is `<app id or instance id>-<port>.<server cluster>.phala.network`.

<figure><img src="../../.gitbook/assets/cloud-network-page.png" alt="access-cvm"><figcaption></figcaption></figure>

## Setting Up Your Custom Domain

If you prefer to use your own domain name, follow these steps:

1. Configure your DNS records to point to our proxy server. Add a CNAME record that points your domain to the Phala Cloud proxy server.

2. Establish a complete trust chain by either:
   - Generating a Remote Attestation (RA) report with certificate data
   - Implementing a mechanism where a key inside your TEE application signs the certificate for each session

This approach ensures your users can verify the authenticity of your application running in a trusted execution environment.

For a practical implementation, check out our [custom domain configuration example](https://github.com/Dstack-TEE/dstack-examples/tree/main/custom-domain) in the dstack-examples repository.
