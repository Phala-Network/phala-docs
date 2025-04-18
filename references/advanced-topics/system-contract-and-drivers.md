# System Contract and Drivers

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

## Introduction <a href="#introduction" id="introduction"></a>

The system contract is responsible for the access control of each cluster. Only the cluster owner is able to implement and deploy the system contract during the creation of the cluster.

Also, the enable the flexible management of the future features of Phat Contract, we refer to the design of the Linux kernel and enable cluster owner to dynamically register drivers to system contract to different things. For example, the Phat Contract tokenomics is implemented as a [driver](https://github.com/Phala-Network/phala-blockchain/tree/master/crates/pink-drivers/tokenomic) so each cluster owner can replace it with his/her own tokenomics in the future.

> This feature is not finalized yet so can be changed any time.

## System Contract Examples <a href="#system-contract-examples" id="system-contract-examples"></a>

Check our [crates](https://github.com/Phala-Network/phala-blockchain/tree/master/crates/pink-drivers) for the current implementation of the system contract and drivers.
