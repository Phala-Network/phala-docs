# Quick Start

## Hardware

{% tabs %}
{% tab title="Rent Hardware" %}
> We currently recommend using [<img src="https://wiki.phala.network/images/docs/quick-start/mine-phala/signet__on-dark-blue-bg.png" alt="VULTR Bare Metal" data-size="line"> ](https://www.vultr.com/products/bare-metal/)[VULTR](https://www.vultr.com/products/bare-metal/). Worker on VULTR [documentation](https://wiki.phala.network/en-us/general/mining/paas-miner/).

Support is not limited to VULTR, as long as the provider allows you to set the required [BIOS settings](https://wiki.phala.network/en-us/mine/khala-mining/hardware-requirements/#check-your-bios) and offers an Intel® SGX [supported CPU](https://wiki.phala.network/en-us/mine/khala-mining/hardware-requirements/#2-confirm-the-cpu-supports-intel-sgx).
{% endtab %}

{% tab title="Own Hardware" %}
> Ensure your BIOS and operating system is ready according to our [hardware and setup documentation](https://wiki.phala.network/en-us/mine/khala-mining/hardware-requirements).
{% endtab %}
{% endtabs %}

## Wallet <a href="#wallet" id="wallet"></a>

If you do not have a wallet yet, [create one](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fkhala-api.phala.network%2Fws#/accounts) (+ Add account) and install the [Polkadot{.js} extension](https://polkadot.js.org/extension) for your browser.

> Have the details of your Wallet (address, seed) ready when installing the worker.

## Quick Start <a href="#quick-start" id="quick-start"></a>

<img src="https://user-images.githubusercontent.com/37558304/145892648-bc3562f8-47e0-4cc9-a8a1-05b1ee8baab1.png" alt="Phala Network" data-size="line"> Ubuntu 21.10 GUI worker setup script \[v0.01]

```
wget -O - https://raw.githubusercontent.com/Phala-Network/solo-mining-scripts/improvement-test/gui.sh | bash
```

If you experience an issues with the installation script, you can always install the worker manually from our [GitHub repository](https://github.com/Phala-Network/solo-mining-scripts#manual-installation).

## Manage Workers <a href="#manage-workers" id="manage-workers"></a>

Create a pool if you do not have one yet. Once the worker is registered, you can add them to your pool.

> We have a detailed guide on how to use the Khala App here.

## Troubleshoot <a href="#troubleshoot" id="troubleshoot"></a>

[General](https://github.com/Phala-Network/solo-mining-scripts#navigate) [Investigate](https://github.com/Phala-Network/solo-mining-scripts#investigating-the-issue) Confidence Level [Stuck Worker](https://github.com/Phala-Network/solo-mining-scripts/tree/main#khala-node-stops-synching) [Forum](https://forum.phala.network/c/mai/42-category/42)
