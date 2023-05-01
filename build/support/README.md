# Support

## Get questions answered <a href="#get-questions-answered" id="get-questions-answered"></a>

You can post your questions to

* [Substrate and Polkadot StackExchange](https://substrate.stackexchange.com/), remember to add the `phat-contract` tag;
* or join our [Discord server](https://discord.gg/phala) and get an immediate response in the `#dev` channel.

## Question List <a href="#question-list" id="question-list"></a>

### How to set arguments when instantiating the contract in Phat Contract UI? <a href="#how-to-set-arguments-when-instantiating-the-contract-in-phat-contract-ui" id="how-to-set-arguments-when-instantiating-the-contract-in-phat-contract-ui"></a>

* Now the Phat Contract Console does not support specifying arguments during contract instantiation
* **Workaround**: you can implement a `config(&mut self, argument0, ...)` function and set the contract state with transactions after the instantiation

### Phat UI reports an error before deploying the contract <a href="#phat-ui-reports-an-error-before-deploying-the-contract" id="phat-ui-reports-an-error-before-deploying-the-contract"></a>

The Phat UI checks the contract’s validity before uploading it to the cluster. However, sometimes the contract output by `cargo-contract` may be invalid. We’ve listed common errors and solutions below:

### **Error: gas instrumentation failed: unsupported instruction: F32Load(2, 4)**

or sometimes “use of floating point type in locals is forbidden”

This error occurs when the contract or its dependencies use floating point operations not allowed by the ink runtime.

* To find the source of the problem, try recompiling the contract with `--keep-debug-symbols`, then convert the wasm file to wat using `wasm2wat my_contract.wasm > my_contract.wat`, and search for `f32` or `f64` in my\_contract.wat to find the function using these instructions.
* If the floating point operations are necessary, see the section [“How to do floating point calculations”](broken-reference) for more information.

### **Error: sign extension operations support is not enabled**

Upgrade cargo-contract to version 1.5.2 or higher once [this PR](https://github.com/paritytech/cargo-contract/pull/904) has been merged.

### Avoiding FP Instructions in JSON Parsing <a href="#avoiding-fp-instructions-in-json-parsing" id="avoiding-fp-instructions-in-json-parsing"></a>

A common case that introduces FP instructions is parsing JSON in a contract. Either serde or serde\_json are designed to be able to handle FP numbers. In theory, if you don’t use it to deal with FP data, the compiler and wasm-opt should be able to optimize the FP instructions away for many cases. However, in practice, if you use serde\_json, it always emits FP instructions in the final output wasm file.

If your JSON document contains FP numbers, you can skip this section and go to [“How to do floating point calculations”](broken-reference) for solutions. If your JSON document does not contain FP numbers, here are some suggestions for removing the instructions:

* Use the crate [pink-json](https://crates.io/crates/pink-json) instead of `serde_json`.
* Don’t deserialize to `json::Value` or `serde::Value`. These are dynamically typed values and make it impossible for the compiler to optimize the code paths that contain FP ops. Instead, mark concrete types with `#[derive(Deserialize)]` and deserialize to them directly.
*   If using `pink-web3` and loading `Contract` from its JSON ABI, you may encounter FP problems in a function like `_ZN5serde9__private2de7content7Content10unexpected17h5ce9c505c30bc609E` from serde. To fix this, you can patch `serde` as shown below.

    ```
    [patch.crates-io]
    serde = { git = "https://github.com/kvinwang/serde.git", branch = "pink" }
    ```

### How to do Floating Point Calculations <a href="#do-fp" id="do-fp"></a>

TODO
