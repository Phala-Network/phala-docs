---
icon: robot-astromech
---

# Getting Started

{% hint style="warning" %}
We are in progress of migrating docs for Phala Cloud Docs. In the meantime, checkout the full guide [here](https://phala-network.github.io/phala-cloud-community/docs/).
{% endhint %}

There are a couple ways to get started building with Dstack.&#x20;

* Start from Scratch
* Build from a Template

Before diving into the these steps, lets take a look at the requirements needed to build on Dstack.

### Requirements

* Docker([Docker Desktop](https://www.docker.com/products/docker-desktop/) or [OrbStack](https://orbstack.dev/)): Dstack supports the deployment of **ANY** Docker images. Check out how to build & publish to Docker Hub (i.e. [Docker Tutorial](https://docs.docker.com/get-started/introduction/build-and-push-first-image/))
* With full Docker support, you can build in **ANY** language you prefe&#x72;**.** We have built out an SDK to make it easy for TypeScript/JavaScript and Python programs to call the Dstack SDK functions, but this can be done for **ANY** programming language.
  * Check the code to see how the RPC calls are constructed
    * [TypeScript/JavaScript](https://github.com/Leechael/tappd-simulator/blob/main/sdk/js/src/index.ts)
    * [Python](https://github.com/Leechael/tappd-simulator/blob/main/sdk/python/src/dstack_sdk/client.py)
* For deployment on Real TEE Server, must publish docker image with OS/arch `linux/amd64`. For local TEE simulator, you can build in **ANY** OS/arch since they won't be running on real TEE hardware.

