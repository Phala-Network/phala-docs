# ⁉️ FAQ

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../cloud/getting-started/getting-started.md).
{% endhint %}

## :page\_facing\_up: (Legacy) Phat Contract Development <a href="#how-to-set-arguments-when-instantiating-the-contract-in-phat-contract-ui" id="how-to-set-arguments-when-instantiating-the-contract-in-phat-contract-ui"></a>

***

### How can I set arguments when instantiating the contract in Phat Contract UI? <a href="#how-to-set-arguments-when-instantiating-the-contract-in-phat-contract-ui" id="how-to-set-arguments-when-instantiating-the-contract-in-phat-contract-ui"></a>

***

* Currently the Phat Contract Console does not support specifying arguments during contract instantiation
* **Workaround**: you can implement a `config(&mut self, argument0, ...)` function and set the contract state with transactions after the instantiation

### Phat UI reports an error before deploying the contract. <a href="#phat-ui-reports-an-error-before-deploying-the-contract" id="phat-ui-reports-an-error-before-deploying-the-contract"></a>

***

The Phat UI checks the contract’s validity before uploading it to the cluster. However, sometimes the contract output by `cargo-contract` may be invalid. We’ve listed common errors and solutions below:

#### **Error: gas instrumentation failed: unsupported instruction: F32Load(2, 4)**

or sometimes “use of floating point type in locals is forbidden”

This error occurs when the contract or its dependencies use floating point operations not allowed by the ink runtime.

* To find the source of the problem, try recompiling the contract with `--keep-debug-symbols`, then convert the wasm file to wat using `wasm2wat my_contract.wasm > my_contract.wat`, and search for `f32` or `f64` in my\_contract.wat to find the function using these instructions.
* If the floating point operations are necessary, see the section [“How to do floating point calculations”](../developers/support/broken-reference/) for more information.

#### **Error: sign extension operations support is not enabled**

Upgrade cargo-contract to version 1.5.2 or higher once [this PR](https://github.com/paritytech/cargo-contract/pull/904) has been merged.

### Avoiding FP Instructions in JSON Parsing. <a href="#avoiding-fp-instructions-in-json-parsing" id="avoiding-fp-instructions-in-json-parsing"></a>

***

A common case that introduces FP instructions is parsing JSON in a contract. Either serde or serde\_json are designed to be able to handle FP numbers. In theory, if you don’t use it to deal with FP data, the compiler and wasm-opt should be able to optimize the FP instructions away for many cases. However, in practice, if you use serde\_json, it always emits FP instructions in the final output wasm file.

If your JSON document contains FP numbers, you can skip this section and go to [“How to do floating point calculations”](../developers/support/broken-reference/) for solutions. If your JSON document does not contain FP numbers, here are some suggestions for removing the instructions:

* Use the crate [pink-json](https://crates.io/crates/pink-json) instead of `serde_json`.
* Don’t deserialize to `json::Value` or `serde::Value`. These are dynamically typed values and make it impossible for the compiler to optimize the code paths that contain FP ops. Instead, mark concrete types with `#[derive(Deserialize)]` and deserialize to them directly.
* If using `pink-web3` and loading `Contract` from its JSON ABI, you may encounter FP problems in a function like `_ZN5serde9__private2de7content7Content10unexpected17h5ce9c505c30bc609E` from serde. To fix this, you can patch `serde` as shown below.

```
[patch.crates-io]
serde = { git = "https://github.com/kvinwang/serde.git", branch = "pink" }
```

### Cannot compile with "lib name not found" error.

***

<pre class="language-shell" data-overflow="wrap"><code class="lang-shell"><strong>2023-07-11T09:42:45.848016Z INFO cargo_contract::crate_metadata: Fetching cargo metadata for Cargo.toml thread 'main' panicked at 'lib name not found', /home/USER/.cargo/registry/src/github.com-1ecc6299db9ec823/cargo-contract-1.5.0/src/crate_metadata.rs:65:25 note: run with RUST_BACKTRACE=1 environment variable to display a backtrace
</strong></code></pre>

After checking the version, it shows:

<pre><code><strong>$ cargo contract --version cargo-contract 1.5.0-unknown-x86_64-unknown-linux-gnu
</strong></code></pre>

Solution: upgrade to the latest cargo contract. [Reference](https://github.com/paritytech/cargo-contract#installation):

```shell
cargo install --force --locked cargo-contract
```

### Who is charged for calling methods on contract?

***

There are two types of method calling:

1. **off-chain query**: there is not cost for caller, but someone needs to stake to that contract in advance so it can get the CPU time to process your queries
2. **on-chain transaction**: when you send the tx, some transaction fee will be charged directly; also for your tx to be finally executed in our worker, some in-cluster balance will be charged as real gas fee

### Encrypted contract state is not available on the blockchain, but is the contract itself available on the blockchain?

***

* Contract state is not stored on-chain, it’s volatile in SGX workers’ memory. So to get access to the contract state, there must be at least one active worker to which that contract is deployed
  * Contracts are deployed to a cluster, and then all the workers in that cluster - We have enabled dynamic cluster: to add workers to a cluster. This is achievable since the root key is in GKs, so they can derive the cluster key any time and share to incoming workers
* All the transactions are stored on-chain, including
  * The transaction to upload the code to workers, such transaction is deliberately kept public so users can easily examine the contract code
    * The (encrypted) transaction to instantiate code, this contains the constructor function to call and the arguments
    * All the (encrypted) transactions that update the contract states

### Does the stake associated with a contract decrease as more computation is done from contract calls?

***

No. The stake to a contract does not change with contract calls. You can always have the full refund. But if other contracts get more stake then your computing power percentage will decrease correspondingly. This only applies to the public cluster. If we create dedicated cluster for our partners then any stake can take all the CPU time

### Error on Ubuntu 22.04 Exception: Failed to start pherry component. \<PATH>/pherry: error while loading shared libraries: libssl.so.1.1: cannot open shared object file: No such file or directory

***

Manually pulling deb package and installing fixes issue. Reference from [askubuntu](https://askubuntu.com/questions/1403619/mongodb-install-fails-on-ubuntu-22-04-depends-on-libssl1-1-but-it-is-not-insta).&#x20;

```sh
wget http://security.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.20_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.20_amd64.deb
```

## :computer: Phala Compute Infrastructure&#x20;

***

### How do the token economics of Phala Network work?

***

> _**Note**: At the time of writing this, &#x65;_&#x76;erything below except the **Demand L1** tokenomic is up and running

1. **Supply**: The contributors (miners in the past) receive reward by keeping serving the network. It follows a model similar to other PoS like Filecoin, which allows the system to punish the bad behavior. The liveness of the worker is checked by on-chain random heartbeat.
2. **Demand L1**: The developer can stake to get a percentage of the ownership of the compute resource. Once they stake, they can request to "hire" the workers they prefer to form a **cluster**, and get the worker assigned automatically by the system. This part is described in the tokenomic paper, but not fully implemented yet.
3. **Demand L2**: Once the developer hired some workers in a **cluster**, they can use the resources. If it's fully used by a single developer, no further tokenomic is required. But if someone wants to create a **public cluster**, just like the one we launched earlier this year, we need another tokenomic to distribute the resources to individual permissionlessly. As Joshua described, now it's a "stake to compute" model. You can stake some % of the token, and get access to the corresponding portion of the compute resources within the cluster.
4. **Resource Accounting**: The last piece of the map is to account the resources, especially when using a **public cluster**. In Phala Network the major resource is the CPU time. So we run a variant of Completely Fair Scheduler (CFS) used by the Linux kernel to ensure the CPU consumed by each contract is pro rata to their stake in the cluster. It's further combined with WASM gas metering to achieve "time slice" allocation in the cluster.

### How are Phat Contract Contract Keys managed/handled from Gatekeepers to Cluster of node(s)?

***

There are several keys involved in this process, and all these keys are generated inside pRuntime in TEE.

* WorkerKey, every pRuntime, no matter it’s worker or GK, generates it during the initialization and publish the pk on-chain during worker registration (GK must be first registered as worker)
  * All the key sharing between workers are done through encrypted channel. And this channel is established using the WorkerKeys of two parties. Two workers first generate the common working key using ECDH on their WorkerKeys, then using the working key to encrypt the real contents
* MasterKey, generated by the first registered GK, and shared to all the other GKs. The MasterKey pk is published on chain, so any GK can sign the messages with MasterKey for others to verify. All the GKs behave exactly the same so they are duplications to each other
  * MasterKey is the root key for all the following contract-related keys
* ClusterKey, generated by GK by deriving the MasterKey with cluster info. The ClusterKey is shared by GK to all the Workers in the cluster during cluster creation through the encrypted channels
* ContractKey, generated by cluster workers by deriving the ClusterKey with contract info. Since all the cluster workers have the ClusterKey, they will generate the same ContractKey for each contract.
