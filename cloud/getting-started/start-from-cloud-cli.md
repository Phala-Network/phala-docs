# Quick Start

## Prerequisites

* Docker installed and running
* [Bun](https://bun.sh) installed
* Docker Hub account for publishing images
* [Phala Cloud](https://cloud.phala.network/register?invite=PHALAWIKI) API key

## Installation

Clone the CLI repo

```bash
git clone --recurse-submodules https://github.com/Phala-Network/tee-cloud-cli.git
```

```bash
# Install dependencies
bun install

# Build
bun run build
```

### Generate a Phala Cloud API Key

Log into your dashboard and select the logo in the top left corner.

<figure><img src="../../.gitbook/assets/Screenshot 2025-02-27 at 11.42.32.png" alt=""><figcaption></figcaption></figure>

Click your username and select "API Tokens".

<figure><img src="../../.gitbook/assets/Screenshot 2025-02-27 at 11.45.13.png" alt=""><figcaption></figcaption></figure>

Click Create Token and then copy your newly generated API Key.

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### Launch a CVM with a Dstack Example

Now we want to set the API Key for the CLI and launch our first CVM. Take the API Key you copied down then set it with the `teecloud set-apikey`command.

```bash
teecloud set-apikey your-phala-cloud-api-key
```

Deploy one of the Dstack examples under the examples folder. This example with launch the timelock-nts example where a key is derived within the TEE then after 5 minutes, the private key is released.

```bash
# Deploy the timelock-nts example
teecloud deploy -c ./examples/timelock-nts/docker-compose.yml -n timelock-nts
```

Example Output:

```bash
Deploying CVM ...
Deployment successful
App Id: cc3ee84d7e708aed326d5df6d22296f65b4fd99e
App URL: https://cloud.phala.network/dashboard/cvms/app_cc3ee84d7e708aed326d5df6d22296f65b4fd99e
```

#### You should see the CVM in your Dashboard now. Go and check the details.

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Click on the Containers tab and get check out the logs.

<figure><img src="../../.gitbook/assets/Screenshot 2025-02-27 at 11.52.24.png" alt=""><figcaption></figcaption></figure>

You'll have access to your logs from your newly deployed Confidential VM in Phala Cloud.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

For more information on the Timelock-NTS example, check out the information in the [Dstack Examples Repo](https://github.com/Dstack-TEE/dstack-examples/blob/main/timelock-nts/README.md).

## Conclusion

Congratulations! You have deployed your first CVM into the Phala Cloud. Let's move to more meaningful examples.

