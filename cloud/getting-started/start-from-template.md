# Build From Template

There are a couple templates that we offer to allow you to get started without any heavy lifting. The steps to get started are simple and easy to test in a few minutes.

{% hint style="info" %}
### Before You Start

Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) or [OrbStack](https://orbstack.dev/) started before you begin.
{% endhint %}

{% tabs %}
{% tab title="next.js Template" %}
## Installation

Clone the template repo.

```bash
git clone https://github.com/Phala-Network/nextjs-viem-tee-sim-template.git
```

## Build and Deploy Locally

Build the docker image.

```bash
docker build -t my-dapp:latest .
```

Now that the docker image is built, let's start testing against the TEE Simulator. First we must pull the latest TEE Simulator in docker, and run it with the following commands.

```bash
docker pull phalanetwork/tappd-simulator:latest
docker run --rm -p 8090:8090 phalanetwork/tappd-simulator:latest
```

With the simulator up and running, we can now start our docker app to test out the functionality.

```bash
docker run --rm -p 3000:3000 my-dapp:latest
```

Now we can go to `http://localhost:3000` and see our deployed application.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-07 at 23.15.11.png" alt=""><figcaption></figcaption></figure>

### Call the APIs

We can test to see if our functions work by calling the API calls with

* http://localhost:3000/api/tdxquote
* http://localhost:3000/api/account/address
* http://localhost:3000/api/signMessage
* http://localhost:3000/api/signTypedData
* http://localhost:3000/api/signTransaction

We should see the results similar to the following screenshots.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-07 at 23.31.56.png" alt=""><figcaption><p>/api/tdxQuote</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-07 at 23.15.11 (1).png" alt=""><figcaption><p>/api/account/address</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-07 at 23.32.07.png" alt=""><figcaption><p>/api/signMessage</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-07 at 23.32.40.png" alt=""><figcaption><p>/api/signTypedData</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-07 at 23.46.39.png" alt=""><figcaption><p>/api/sendTransaction</p></figcaption></figure>
{% endtab %}

{% tab title="Python Template" %}
## Installation

Clone the template repo.

```bash
git clone https://github.com/Phala-Network/python-tee-sim-template.git
```

## Build and Deploy Locally

Build the docker image.

```bash
docker build -t my-dapp:latest .
```

Now that the docker image is built, let's start testing against the TEE Simulator. First we must pull the latest TEE Simulator in docker, and run it with the following commands.

```bash
docker pull phalanetwork/tappd-simulator:latest
docker run --rm -p 8090:8090 phalanetwork/tappd-simulator:latest
```

With the simulator up and running, we can now start our docker app to test out the functionality.

```bash
docker run --rm -p 3000:3000 my-dapp:latest
```

Now we can go to `http://localhost:3000` and see our deployed application.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-07 at 19.44.10.png" alt=""><figcaption><p>/</p></figcaption></figure>

### Call the APIs

We can test to see if our functions work by calling the API calls with

* http://localhost:3000/api/derivekey
* http://localhost:3000/api/tdxquote

We should see the results similar to the following screenshots.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-07 at 19.44.26.png" alt=""><figcaption><p>/derivekey</p></figcaption></figure>
{% endtab %}
{% endtabs %}



## Conclusion

The last 2 tutorials were key to understanding the basics of deploying a Docker app on a TEE Server. Now you are ready to start building on Dstack! For more info on the design of Dstack, check out the [Design Documents](../../design-documents/).
