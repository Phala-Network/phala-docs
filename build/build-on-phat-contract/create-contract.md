# Create Contract

## Create and Compile Your First Contract <a href="#create-and-compile-your-first-contract" id="create-and-compile-your-first-contract"></a>

In order to initialize a new Phat Contract project you can use our hello world template:

```
git clone https://github.com/Phala-Network/phat-hello
```

> **Contract Examples**
>
> More Phat contract examples can be found in [phat-contract-examples](https://github.com/Phala-Network/phat-contract-examples) and [awesome-phat-contracts](<../../.gitbook/assets/awesome phat contracts>) repositories.

This will create a folder `phat-hello` in your work directory. The folder contains a scaffold `Cargo.toml` and a `lib.rs`, which both contain the necessary building blocks for using Phat Contract.

The `lib.rs` contains our hello world contract ‒ an ETH balance reader.

In order to build the contract just execute this command in the `phat-hello` folder:

```
cargo contract build
```

As a result, you’ll get the following files in the `target/ink` folder of your contract: `phat_hello.wasm`, `metadata.json`, and `phat_hello.contract`. The `.contract` file combines the WASM and metadata into one file and needs to be used when instantiating the contract.

## Run Unit Tests Locally <a href="#run-unit-tests-locally" id="run-unit-tests-locally"></a>

Before you really upload and deploy your contract to the blockchain, you are encouraged to run local unit tests to check its correctness.

In the `phat-hello` folder, run

```
cargo test -- --nocapture
```

and ensure you see all tests passed.

> Do not use `cargo contract test` here, `cargo test` will give you more details if something goes wrong.
>
> `-- --nocapture` is optional to see the output during testing.

Now you have successfully compiled and locally test your first Phat Contract. Now it’s time to deploy it to a real blockchain.
