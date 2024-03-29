# Troubleshooting

## Quick Links <a href="#quick-links" id="quick-links"></a>

[General](https://github.com/Phala-Network/solo-mining-scripts#navigate) | [Investigate](https://github.com/Phala-Network/solo-mining-scripts#investigating-the-issue) | [Confidence Level](https://wiki.phala.network/en-us/mine/solo/4-0-faq/#confidence-level) | [Stuck Worker](https://github.com/Phala-Network/solo-mining-scripts/tree/main#khala-node-stops-synching) | [Forum](https://forum.phala.network/c/mai/42-category/42)

\
👇 You can also join our Discord or Telegram worker group to discuss your issue. 👇

* [Discord](https://discord.gg/C6E4hQjk)
* [Telegram](https://t.me/phalaworker)
* [Forum](https://forum.phala.network/c/mai/42-category/42)
* [GitHub](https://github.com/Phala-Network/solo-mining-scripts)

## General <a href="#general" id="general"></a>

Most symptoms are solved by restarting your node. If you experience issues running your node, try stopping the node by:

```
sudo phala stop
```

And attempt a restart with

```
sudo phala start
```

If you still have issues attempt to [update the script](solo-scripts-guidance/update-your-workers-node.md).

## Investigating the Issue <a href="#investigating-the-issue" id="investigating-the-issue"></a>

Get an overview of your worker’s status first.

```
sudo phala status
```

In case your node is stuck, a typical scenario would look like the following:

<figure><img src="https://user-images.githubusercontent.com/37558304/147273109-d4d1d5e3-5098-43d1-99f5-2ba995ecd1b6.png" alt=""><figcaption></figcaption></figure>

(image showing stuck node on the worker)

With the symptom in the scenario above, the right method to solve the issue would be restarting the `node` container only, with the commands mentioned [here](troubleshooting.md#general), and restarting the containers.

Now check the status of the node again.

If the local node block height is empty first, check if all required containers are running.

```
sudo docker ps
```

You should have three containers running as shown in this example:

<figure><img src="https://user-images.githubusercontent.com/37558304/145825263-50d69b7e-a7e1-45c9-9eca-cc2d7d3a6b69.png" alt=""><figcaption></figcaption></figure>

(image showing the worker node’s running docker containers)

To get the most recent logs of each container, you may execute:

```
docker logs <container_ID/container_name> -n 100 -f
```

Note that `<container_ID/container_name>` must be replaced with the container you wish the receive the logs from. In the example above the `container_ID` is `8dc34f63861e` and `container_name` would be `phala-pherry`.

\
If you attempt to post on the phala forum and do not know where the issue lies, please post the logs of all three docker containers. Copy-paste the container logs from the terminal into the forum post.

### < 3 running containers <a href="#3-running-containers" id="3-running-containers"></a>

If a container is missing (<3 are running), you may attempt to restart it separately with the respective commands below.

> Use the applicable command to restart your missing container.

```
sudo phala start node
```

```
sudo phala start pruntime
```

```
sudo phala start pherry
```

## Advanced Troubleshooting <a href="#advanced-troubleshooting" id="advanced-troubleshooting"></a>

In some cases, it might be beter to reinstall the mining script. To do this, first uninstall the script:

```
sudo phala uninstall
```

And delete the mining script repository by executing:

```
rm -rf $HOME/solo-mining-scripts-main
```

Now you may reinstall the mining script.

```
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
sudo apt install wget unzip
cd ~
```

```
wget https://github.com/Phala-Network/solo-mining-scripts/archive/refs/heads/main.zip
unzip main.zip
rm -r main.zip #cleaning up the installation
cd solo-mining-scripts-main/ #note this depends on your current directory
sudo ./phala.sh install
```

You may now [restart your node](troubleshooting.md#general).

## Peer Connectivity <a href="#peer-connectivity" id="peer-connectivity"></a>

Some users running nodes may find their nodes are struggling to connect to peers, which causes nodes to be dropped from the network. You can check your node connections through executing:

```
sudo docker logs -f phala-node
```

For an optimal setup, you should have between 40 and 50 peers.

If you have insufficient peers do the following:

* Check your firewall settings
* Ensure there are no NAT or Policy-based filters

Feel free to read [NAT](https://en.wikipedia.org/wiki/Network\_address\_translation) for more information if you are curious about the root causes. Also, do not hesitate to look for existing [Phala forum posts](https://forum.phala.network/c/mai/42-category/42) before posing your issue if you are stuck.

## Driver Issues <a href="#driver-issues" id="driver-issues"></a>

### DCAP driver Installation <a href="#dcap-driver-installation" id="dcap-driver-installation"></a>

ℹ️ The most common issue is that your motherboard may not support a DCAP driver. In this case, the script cannot automatically install the `isgx` driver and results in the following error message.

<figure><img src="https://user-images.githubusercontent.com/37558304/143471619-1116c12f-7ef5-4313-93a5-51f3ed30c355.png" alt=""><figcaption></figcaption></figure>

(image of the terminal showing the DCAP driver error message)

In this case, prior to running `sudo phala start`, you need to manually install the `isgx` driver:

```
sudo phala install isgx
```

## Khala Node Stops Synching <a href="#khala-node-stops-synching" id="khala-node-stops-synching"></a>

If the Khala Chain stops synching and is stuck at a specific block and does not continue to sync, we advise you first to [restart your node](troubleshooting.md#general).

If the synchronization still fails, you may try to delete the khala chain database on your worker’s node. It is located in `/var/khala-dev-node/chains/khala`.

<figure><img src="https://user-images.githubusercontent.com/37558304/143770078-26a3c457-ce1d-447c-8e26-81ea0e1beb9b.png" alt=""><figcaption></figcaption></figure>

(image showing the khala blockchain files of the worker node)

It is located in `/var/khala-dev-node/chains/khala`.

First, stop your node with:

```
sudo phala stop
```

To delete the khala blockchain database on your node, execute the following commands:

```
rm -rf /var/khala-dev-node/chains/khala
```

To delete the Kusama blockchain , run:

```
rm -rf /var/khala-dev-node/chains/polkadot
```

## Deleting the Mining Scripts <a href="#deleting-the-mining-scripts" id="deleting-the-mining-scripts"></a>

If you encounter any issues uninstalling the mining scripts and all dependencies except the drivers, you may delete them by executing the following commands:

```
sudo rm -r /opt/phala
sudo rm -r ~/solo-mining-scripts-main
sudo rm ~/main.zip
```

You can [follow this tutorial](./) to redownload and reinstall the new phala mining scripts.
