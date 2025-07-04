# ❓ FAQs

## ❓ FAQs

### What is Phala TEE Cloud?

Phala TEE Cloud is a platform that provides Trusted Execution Environment (TEE) virtual machines. These VMs offer hardware-level isolation through Intel TDX technology, allowing for secure and private computation.

### How are the VMs provisioned?

Each application gets one CVM (Confidential Virtual Machine), which is one TDX. TDX is a VM technology that provides hardware-level isolation powered by Intel CPU.

### What are the limitations of the TEE environment in Phala? Can my app access file and network IO?

* Apps in CVM cannot directly access the host file/network IO.
* Internet access for the app is allowed but must go through the proxy module.
* Local filesystem access within the CVM is supported, similar to how a docker container accesses its host machine.
* Direct access to the host's filesystem is not allowed when deployed on Phala Cloud

### How can I serve a REST API in Phala's TEE environment?

You need a web server for serving REST APIs. Requests will be forwarded through a proxy module (dstack-gateway) to CVM. Exposed ports in the docker-compose file will generate a public endpoint for accessing your service.

### Can I run an app with a database inside the container?

Yes, local disk access is supported within the container environment, allowing you to run an app with a database.

### Can the encrypted environment variable be accessed by any other part, including the host OS?

No, it's encrypted on the client side and sent to the CVM using X25519 encryption scheme. The variables can only be decrypted inside the CVM.

### Can Docker logs be accessed by any other part, including the host OS?

Currently, the logs are not end-to-end encrypted. However, you can decide whether to make them public under **Advanced Features → Public Logs** during deployment. If you choose public, anyone with the log URL can view them, and the Log URL can be inferred from your instance ID in the public endpoints. If you choose private, no one can access the logs, and you'll need to configure a log viewer to view them elsewhere.

### Is application data persistent on the disk?

Yes, the data you write to the filesystem inside Docker will persist on the disk and be encrypted. Restarting or upgrading will not affect data recovery. To save data on disk, you need to [configure volumes](https://docs.docker.com/reference/compose-file/volumes/) in the Docker Compose file and write data to the correct path.

### Can I deploy / manage / upgrade CVMs programmatically?

Yes. Please check our Cloud API docs here: https://cloud-api.phala.network/docs\
API examples: https://github.com/Leechael/phala-cloud-api-example/tree/main/js\
Or set CI/CD pipline for you instance: https://docs.phala.network/phala-cloud/be-production-ready/ci-cd-automation/setup-a-ci-cd-pipeline

### Does the “update” feature sync the latest Docker image?

No. By default, Docker does not proactively update the image unless the image reference is changed (e.g., by modifying the tag or the hash), even if an update is triggered. This is because the update feature is essentially equivalent to running: `docker compose down && docker compose up`. To ensure the image is actually updated, it's recommended to always update the tag. Additionally, for best security practices, it's advised to include the image hash to trace the TEE proof back to the exact Docker image file.

### Does a CVM support multiple containers?

Yes, you can deploy multiple containers per CVM through the docker compose file.

### Q: Does the cloud support firewall?

You can apply any firewall rules in your containers. For example, you can add a Nginx to apply IP address filters or WAF rules. There’s no cloud level firewall currently.

### Q: Does it support Terraform deployment?

Current no. There’s a public tracking issue for Terraform: https://github.com/Phala-Network/phala-cloud-community/issues/15

### Q: Can CVM accept arbitrary TCP / TLS connection?

The cloud CVM supports to expose both HTTP-over-TLS (Zero Trust HTTPS), and TCP-over-tls. You can check our example to expose ssh or other TCP ports here: https://github.com/Dstack-TEE/dstack-examples/tree/main/tcp-port-forwarding

Under the hood, the TEE wraps the tcp ports you have exposed in docker with TLS. The gateway then routes the TLS traffic based on SNI, the domain name attached to the every TLS connection. TLS is needed because it's the only way to multiplex the tcp traffic. When using the tcp-port-forwarding example, it automatically helps you set up the domain and TLS certificate securely in TEE (thus “Zero Trust”), and reverse-proxy the incoming traffic to your tcp port. You can also manually accept TLS traffic in your CVM and handle the certificate on the application level.

### Is there a simulator or free tier available for testing?

We have built a Phala cloud cli so you don’t need to touch the raw docker command. The doc is available here: https://docs.phala.network/phala-cloud/references/tee-cloud-cli/phala/simulator.

### Is Phala Cloud based on serverless functions or traditional VMs? What are the startup and shutdown times?

Phala Cloud uses a VM-based model, not serverless functions. While exact boot time can vary, users can create a CVM to measure startup latency. For most scenarios, it's best to keep a small instance running continuously and scale up during traffic spikes. Spinning up a new VM for every request may not be efficient. There is currently no TEE-based serverless function, but the team is open to collaborating on building one.

### How can I access my docker volume data after deploy?

The docker volume is persisted in the TEE encrypted volume. By default it's not accessible by humans or the cloud. However, if your business logic requires to expose the volume or part of the volume, you can do it with your backend code manually. For example if you want to allow users to upload images and download it later, you can implement a simple backend web server with file uploading and static file serving. Here are the example tutorials from Flask ([upload](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/), [static file serving](https://flask.palletsprojects.com/en/stable/tutorial/static/)). And it's also easy to find the tutorials for other web servers (nginx, express, etc).

### Can I send encrypted values (like API keys) through the Phala Cloud API for deployment?

Yes, Phala Cloud supports sending encrypted values (e.g., Twitter API keys/secrets) through the API. You must encrypt the variables locally before sending them. The encrypted values can then be included in your deployment request.

You can also send them through the feature of Encrypted Environment Variable. If you use CLI, you can set it like [here](https://github.com/Phala-Network/phala-cloud-cli?tab=readme-ov-file#environment-variables-management), or if you on the Cloud UI, use the "Encrypted Environment Variables" feature during VM creation.

### How long does it take to deploy a Docker image in Phala Cloud?

Deployment time depends on the Docker image size and decompression requirements:

* A small Python-based image (e.g., kennethreitz/httpbin) typically takes about 1-2 minutes.
* A larger image like ElizaOS/Eliza (1.4GB) takes 20-25 minutes, with most time spent decompressing after a fast pull.

### How fast can a simple program (e.g., multiplying two numbers) execute in a TEE?

Execution speed for a simple operation like multiplying two numbers within a TEE depends on the setup. If the TEE environment (e.g., a Docker container) is already running, execution is near-instantaneous (milliseconds), similar to non-TEE environments. However, if deployment or cold start is required, the total time includes the container pull and decompression (1-2 minutes, as above). For a function-as-a-service (FaaS) experience with seconds-scale execution, the TEE server must be pre-deployed and running, not started on-demand.

### Can I update specific environment variables for a deployed Docker image without changing the entire set?

Currently, Phala Cloud does not support updating individual environment variables—you must update all variables together. However, this feature is on the development roadmap. As a workaround:

Use two separate environment files: one for static variables (e.g., required for the app to run) and another for dynamic, user-editable variables (e.g., trading parameters).

Alternatively, integrate a dedicated HTTPS API endpoint within your deployed instance to allow users to update specific variables without redeploying.\
Discuss custom solutions with the Phala team if this is critical for your use case.

### How can I deploy multiple Docker instances on a single VM to optimize costs?

You can deploy multiple Docker instances on a single Phala Cloud VM using a "Docker-in-Docker" approach, similar to what large clients have implemented (e.g., running 150+ instances). To do this:

Step 1: Create a larger VM (e.g., 10 vCPUs, 20GB RAM).\
Step 2: Deploy your Dockerized images inside this VM, adjusting ports or configurations as needed to avoid conflicts.\
Step 3: Use custom environment variables per instance for differentiation, for example, set the image name or version through environment variable.\
This reduces overhead (e.g., from multiple OS instances) and can lower costs. Phala can assist with implementation—reach out for support.

### What endpoint do I use to view logs for a specific instance?

To access logs for a specific instance, if you use Cloud UI, you can check the log on the container page. If you use the Cloud API, you can use the endpoint GET /api/v1/cvms/app\_\<app\_id>/composition. This returns details about all containers within the Compute VM (CVM), including the log endpoint for each. Replace \<app\_id> with your instance’s unique identifier. Find the full API specification at https://cloud-api.phala.network/docs. Ensure you authenticate with your API key in the x-api-key header.

### Can I set my own TLS certificate for my CVM network access?

Yes, you can. For example, after config the certs, you expose the `- 8080:443` in docker compose file. To access your service over TLS certs, you must use the public endpoint generated in network section and add the character 's' behind the port number. Like `<id>-<port>[s].<base_domain>`.

### How does Phala Cloud ensure that the data in a CVM isn’t accessed by other programs running in the same machine?

Phala Cloud CVM uses a hardware root key unique to the TEE platform, from which individual encryption keys are derived for each application. This key hierarchy ensures that each TEE app has its own distinct key, preventing other programs in the same TEE from accessing your encrypted data. Additionally, you should attest the programs running on Phala Cloud (e.g., via remote attestation) to verify they’re not malicious, enhancing security.

### How can others verify that my application is running inside a TEE?

Once the application is successfully launched, you can prove this by providing the RA Report, which can be exported through an endpoint by your Docker application. check [this\
article](https://phala.network/posts/how-to-generate-attestation-repport-and-prove-your-application-runs-in-tee) for more details.

### What’s the best approach to verify Phala Cloud Attestation Report in a smart contract?

You can verify the Attestation Report with [Automata's on-chain DCAP verifier](https://github.com/automata-network/automata-dcap-attestation) written in Solidity and deployed on multiple blockchains.

To verify the report, user can get the report hex data from Phala Cloud dashboard “Attestation” tab, and call the smart contract method verifyAndAttestOnChain, check the example [here](https://github.com/Leechael/ra-quote-explorer/blob/37a86a96f0f5059359b33fdb61b1f507fd1ca291/src/components/onchain_attestation.tsx#L152).

## Pricing and Resources

### What is the current pricing structure for Phala Cloud?

Check the [pricing page](https://cloud.phala.network/pricing) for more details.

### What kind of user levels do we have on Phala Cloud?

* **Free**: User who registered on Phala Cloud, but have limit resource can be used.
* **Pro**: Paid users with self-service capabilities
* **Enterprise**: Customized pricing, available through Business Development only

#### What are the resource limits for the Free tier users?

User under **Free** tier can only create one single CVM. User can verify their account and set up payment to remove the limit.

### What is the billing granularity for Phala Cloud? Is it by hour or minute?

Phala Cloud bills by seconds. The pricing page displays hourly rates for ease of understanding, but actual billing is based on precise second-level usage.

### What happens if my balance reaches zero?

Phala follows a no-surprise policy:

* Existing clients will have a 2-month grace period after reaching zero balance
* Your VMs will not be shut down without your consent during this period
* The Business Development team will contact you to confirm pricing and terms

### Are there any anti-spam measures?

Yes, Phala implements several measures:

* Payment verification is required even for free VMs to prevent automated registrations
* LLM APIs are not provided for free without a specific reason
* Free VMs may be offered when they don't impact paying users
