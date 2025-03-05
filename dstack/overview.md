---
icon: ufo
---

# Overview

{% hint style="info" %}
Dstack is a [Flashbots](https://www.flashbots.net/) X Project jointly produced by Phala Network and Flashbots.

It was inspired by [Andrew's](https://github.com/amiller) (Flashbots team) design of [Dstack](https://collective.flashbots.net/t/dstack-speedrunning-a-p2p-confidential-vm).

Check our [Acknowledgement](acknowledgement.md) for all of the key contributors that built out the Dstack SDK.
{% endhint %}

> [Phala Cloud](overview/phala-network/phala-cloud.md) is built on top of Dstack that enables developers to deploy programs to CVM (Confidential VM), and to follow the security best practices by default.

## Overview

The [Dstack SDK](https://github.com/dstack-TEE/dstack) is designed to simplify the steps for developers to deploy programs to CVM (Confidential VM), and to follow the security best practices by default. The main features include:

* Convert any docker container to a CVM image to deploy on supported TEEs
* Remote Attestation API and a chain-of-trust visualization on Web UI
* Automatic RA-HTTPS wrapping with content addressing domain on `0xABCD.dstack.host`
* Decouple the app execution and state persistent from specific hardware with decentralized Root-of-Trust

## Conclusion

Now that there is an introduction to the Dstack, we can begin the fun part of building on the SDK. There are a few ways to get started depending on your starting point. Let's take a look at the options in [Getting Started](getting-started/).
