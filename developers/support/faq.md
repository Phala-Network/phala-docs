# Common Issues

## How can I set arguments when instantiating the contract in Phat Contract UI? <a href="#how-to-set-arguments-when-instantiating-the-contract-in-phat-contract-ui" id="how-to-set-arguments-when-instantiating-the-contract-in-phat-contract-ui"></a>

***

* Currently the Phat Contract Console does not support specifying arguments during contract instantiation
* **Workaround**: you can implement a `config(&mut self, argument0, ...)` function and set the contract state with transactions after the instantiation

## Phat UI reports an error before deploying the contract. <a href="#phat-ui-reports-an-error-before-deploying-the-contract" id="phat-ui-reports-an-error-before-deploying-the-contract"></a>

***

The Phat UI checks the contract’s validity before uploading it to the cluster. However, sometimes the contract output by `cargo-contract` may be invalid. We’ve listed common errors and solutions below:

#### **Error: gas instrumentation failed: unsupported instruction: F32Load(2, 4)**

or sometimes “use of floating point type in locals is forbidden”

This error occurs when the contract or its dependencies use floating point operations not allowed by the ink runtime.

* To find the source of the problem, try recompiling the contract with `--keep-debug-symbols`, then convert the wasm file to wat using `wasm2wat my_contract.wasm > my_contract.wat`, and search for `f32` or `f64` in my\_contract.wat to find the function using these instructions.
* If the floating point operations are necessary, see the section [“How to do floating point calculations”](broken-reference) for more information.

#### **Error: sign extension operations support is not enabled**

Upgrade cargo-contract to version 1.5.2 or higher once [this PR](https://github.com/paritytech/cargo-contract/pull/904) has been merged.

## Avoiding FP Instructions in JSON Parsing. <a href="#avoiding-fp-instructions-in-json-parsing" id="avoiding-fp-instructions-in-json-parsing"></a>

***

A common case that introduces FP instructions is parsing JSON in a contract. Either serde or serde\_json are designed to be able to handle FP numbers. In theory, if you don’t use it to deal with FP data, the compiler and wasm-opt should be able to optimize the FP instructions away for many cases. However, in practice, if you use serde\_json, it always emits FP instructions in the final output wasm file.

If your JSON document contains FP numbers, you can skip this section and go to [“How to do floating point calculations”](broken-reference) for solutions. If your JSON document does not contain FP numbers, here are some suggestions for removing the instructions:

* Use the crate [pink-json](https://crates.io/crates/pink-json) instead of `serde_json`.
* Don’t deserialize to `json::Value` or `serde::Value`. These are dynamically typed values and make it impossible for the compiler to optimize the code paths that contain FP ops. Instead, mark concrete types with `#[derive(Deserialize)]` and deserialize to them directly.
* If using `pink-web3` and loading `Contract` from its JSON ABI, you may encounter FP problems in a function like `_ZN5serde9__private2de7content7Content10unexpected17h5ce9c505c30bc609E` from serde. To fix this, you can patch `serde` as shown below.

```
[patch.crates-io]
serde = { git = "https://github.com/kvinwang/serde.git", branch = "pink" }
```

## Cannot compile with "lib name not found" error.

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
