---
icon: robot-astromech
---

# Getting Started

There are a couple ways to get started building with Dstack.&#x20;

* Start from Scratch
* Build from a Template

Before diving into the these steps, lets take a look at the requirements needed to build on Dstack.

### Requirements

* Docker([Docker Desktop](https://www.docker.com/products/docker-desktop/) or [OrbStack](https://orbstack.dev/)): Dstack supports the deployment of **ANY** Docker images. Check out how to build & publish to Docker Hub (i.e. [Docker Tutorial](https://docs.docker.com/get-started/introduction/build-and-push-first-image/))
* With full Docker support, you can build in **ANY** language you prefer**.** We have built out an SDK to make it easy for TypeScript/JavaScript and Python programs to call the Dstack SDK functions, but this can be done for **ANY** programming language.
  * Check the code to see how the RPC calls are constructed
    * [TypeScript/JavaScript](https://github.com/Leechael/tappd-simulator/blob/main/sdk/js/src/index.ts)
    * [Python](https://github.com/Leechael/tappd-simulator/blob/main/sdk/python/src/dstack\_sdk/client.py)
* For deployment on Real TEE Server, must publish docker image with OS/arch `linux/amd64`. For local TEE simulator, you can build in **ANY** OS/arch since they won't be running on real TEE hardware.

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Start From Scratch</td><td></td><td></td><td><a href="start-from-scratch.md">start-from-scratch.md</a></td></tr><tr><td>Build From Template</td><td></td><td></td><td><a href="build-from-template.md">build-from-template.md</a></td></tr></tbody></table>

