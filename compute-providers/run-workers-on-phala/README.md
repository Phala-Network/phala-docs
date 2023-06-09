# Run Workers on Phala

Welcome to the Phala Worker Ecosystem! You've decided to embark on a long journey, and the workload ahead of you is phat... ha!

Anyhow, in this wiki, you will be taught the essentials from A to Z to set up your node. This include terminology, typical debugging steps, SGX and so forth. 

{% hint style="warning" %}
However much we however try to help you, ***__you must know standard system administration with Linux__***. 
{% endhint %}

## Solo vs PRB

When running Phala nodes, you are given two options: Solo or PRB installations. If you find yourself to be hosting less than 3 servers, it is recommended to operate a **Solo** miner.

![Comparison](https://i.imgur.com/rcTIeKZ.png)


## Pre-requisite Knowledge
 
You should be apt and knowledgeable of the following:
- Docker
- Docker-compose
- Apt and Ubuntu 22.04 LTS basic commands
- Curl (*Optional but recommended*)
- Firewall w/ UFW or IPTables (*Optional but recommended*)
- Disk Partitioning and chkdsk

Not that this is NOT an all-inclusive list. These are simply some recommendations to know before throwing yourself into becoming a compute provider. Whilst the Phala team does its best to provide the best of software, some issues may be for you and you only to find resolution. 

## Starting your journey