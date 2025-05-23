---
icon: robot-astromech
---

# Getting Started

There are several ways to get started building with Phala Cloud:

* [Start from Cloud UI](start-from-cloud-ui.md) - The easiest way with no coding required
* [Start from Cloud CLI](start-from-cloud-cli.md) - For developers who prefer command-line tools
* [Start from Template](start-from-template.md) - Build on top of existing templates
* [Start from Scratch](start-from-scratch.md) - Full control for advanced users

Before diving into these steps, let's take a look at the requirements needed to build on Phala Cloud.

### Requirements

* Docker([Docker Desktop](https://www.docker.com/products/docker-desktop/) or [OrbStack](https://orbstack.dev/)): Phala Cloud supports the deployment of **ANY** Docker images. Check out how to build & publish to Docker Hub (i.e. [Docker Tutorial](https://docs.docker.com/get-started/introduction/build-and-push-first-image/))
* With full Docker support, you can build in **ANY** language you prefer. We have built out an SDK to make it easy for TypeScript/JavaScript and Python programs to call the Phala Cloud SDK functions, but this can be done for **ANY** programming language.
  * Check the code to see how the RPC calls are constructed
    * [TypeScript/JavaScript](https://github.com/Leechael/tappd-simulator/blob/main/sdk/js/src/index.ts)
    * [Python](https://github.com/Leechael/tappd-simulator/blob/main/sdk/python/src/dstack_sdk/client.py)
* For deployment on Real TEE Server, must publish docker image with OS/arch `linux/amd64`. For local TEE simulator, you can build in **ANY** OS/arch since they won't be running on real TEE hardware.

### Join Phala Cloud Community

We welcome your feedback and contributions! If you have feature requests, want to report issues, or are interested in contributing to Phala Cloud, please visit our [Github page](https://github.com/Phala-Network/phala-cloud-community) for more information.
