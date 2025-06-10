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

## Features

The [Dstack SDK](https://github.com/dstack-TEE/dstack) is designed to simplify the steps for developers to deploy any dockerized app to an Intel TDX Server running Dstack. It does the following things to make your app secure with security best practices:

* Make minimal code changes to existing docker deployments and deploy in a TEE
* Remote Attestation via single http call
* Automatically secure your http port with e2e encrypted IO with TEE-managed HTTPS
* Encrypted storage enabled by default
* Persisted key and secret access with KMS (Key Management Service)

## Conclusion

Now that we are familiar with the features that Dstack can provide, let's dive into how to get started with running Dstack on a compatible Intel TDX server. If you do not have access to hardware, you can check the [hardware requirements](hardware-requirements.md) or skip the hardware setup & use Phala Cloud by [signing up for your account](../cloud/getting-started/sign-up-for-cloud-account.md).
