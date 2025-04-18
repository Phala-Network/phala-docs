# SideVM

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

## About SideVM <a href="#about-sidevm" id="about-sidevm"></a>

SideVM is the core extension of Phat Contract. Despite the advantages above, the raw Phat Contract still has limitations compared with current Web2 backend programs:

* Lifecycle limitation. The Phat Contract execution is triggered when users send on-chain transactions or off-chain queries to it, and the instance is destroyed when the execution finishes. This makes it impossible to do async requests or keep a long-live network connection;
* Program environment limitation. The Phat Contract inherits the limitations of Ink! and only supports `no_std` crates. This also limits the resources a contract can use (e.g. listening to a port for connections).

SideVM is proposed to tackle these limitations. It runs in a different runtime. This means it can continuously execute, support `std` library, and listen to the port.

## Prepare Environment <a href="#prepare-environment" id="prepare-environment"></a>

The SideVM support is already equipped to our public testnet. But it requires manual authorization to your contract to enable it to call the `start_sidevm()` function. Contact us is the `#dev` channel in our [Discord server](https://discord.gg/phala-network) to get support.

Also, you can run your local testnet following our tutorial and then do the testing.

## Play with it <a href="#play-with-it" id="play-with-it"></a>

### Programming SideVM <a href="#programming-sidevm" id="programming-sidevm"></a>

We use [https://github.com/Phala-Network/phat-contract-examples/tree/master/start\_sidevm](https://github.com/Phala-Network/phat-contract-examples/tree/master/start_sidevm) as an example. It contains both the Phat contract and the SideVM program under `sideprog` folder.

The SideVM part listens to a local port. It will be launched by this [line of code](https://github.com/Phala-Network/phat-contract-examples/blob/master/start_sidevm/lib.rs#L29) if called.

### Compile Phat Contract and SideVM Program <a href="#compile-phat-contract-and-sidevm-program" id="compile-phat-contract-and-sidevm-program"></a>

Just `make` under the folder and it will give you

1. SideVM program `sideprog.wasm`
2. Phat contract under `target/ink/start_sidevm.contract`

### Upload SideVM Program and Instantiate the Contract <a href="#upload-sidevm-program-and-instantiate-the-contract" id="upload-sidevm-program-and-instantiate-the-contract"></a>

We have a [frontend](https://phat.phala.network/) but it does not support the SideVM program upload yet. So we need to upload it manually.

### **Upload SideVM Program**

Use [Polkadot.js](https://polkadot.js.org/apps/) and change the endpoint to `Phala (PoC 6)` under `TEST NETWORKS`.

![](https://i.imgur.com/gerZoKj.png)

In `Developer` - `Extrinsics`, choose `phalaFatContracts` and `clusterUploadResource`. Change `resourceType` to `SidevmCode`, and drag your `sideprog.wasm` here.

Submit the transaction and you shall see its success.

**Interact with Phat UI**

Go to [https://phat.phala.network/](https://phat.phala.network/), click `sign in` and link your address. You need to ensure the `RPC Endpoint` is [wss://poc6.phala.network/ws](wss://poc5.phala.network/ws) and `Default PRuntime Endpoint` [https://phat-cluster-us.phala.network/poc6/pruntime/0xac5087e0](https://phat-cluster-us.phala.network/poc6/pruntime/0xac5087e0).

![](../../.gitbook/assets/SelectPoC6.png)

Click `Upload` and drag your `target/ink/start_sidevm.contract`. Choose the default constructor and Cluster `0x0000000000000000000000000000000000000000000000000000000000000000`. Click `Submit`. You should see something like

![](https://i.imgur.com/M8PoeTO.png)

**Start SideVM with Query**

You can directly interact with your contract with Contract UI.

The `start_sidevm` query is used to start the SideVM program. It contains the [invoke](https://github.com/Phala-Network/phat-contract-examples/blob/master/start_sidevm/lib.rs#L29) to `pink::start_sidevm()`.

From the Worker log, we can see

![](https://i.imgur.com/DWjOeyh.png)

Actually, we implemented the log server with SideVM too ([ref](https://github.com/Phala-Network/phala-blockchain/pull/855)).

### More Resources <a href="#more-resources" id="more-resources"></a>

We do not have many documents on SideVM yet, feel free to ask us directly.

* Previous SideVM design: [https://github.com/Phala-Network/rfcs/blob/main/pink-sidevm/pink-sidevm.md](https://github.com/Phala-Network/rfcs/blob/main/pink-sidevm/pink-sidevm.md)
* SideVM program examples under [https://github.com/Phala-Network/phala-blockchain/tree/master/crates/pink/sidevm/examples](https://github.com/Phala-Network/phala-blockchain/tree/master/crates/pink/sidevm/examples)
* Our SideVM-related PRs: [https://github.com/Phala-Network/phala-blockchain/pulls?q=sidevm+](https://github.com/Phala-Network/phala-blockchain/pulls?q=sidevm+)
