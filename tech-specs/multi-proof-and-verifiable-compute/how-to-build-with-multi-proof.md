# How to Build with Multi-Proof

With Multi-Proof JS SDK, things would become pretty easy to run a task and generate TEE-proof for it. You still can do it with our [Rust SDK](https://docs.phala.network/references/ai-agent-contract-sdks/getting-started) with more flexibility.

Before we dive into the steps, here is a brief explanation of why you can simply write JavaScript code and run it inside a TEE environment:

<figure><img src="../../.gitbook/assets/Build-Multi-Proof.png" alt=""><figcaption></figcaption></figure>

On top of [SideVM](https://docs.phala.network/references/advanced-topics/sidevm), which is a core component of Phala underlying infrastructure to run WASM smart contract in TEE environment, we integrated [QuickJS](https://bellard.org/quickjs/), which is a small and embeddable JavaScript engine. The QuickJS engine was compiled to a WASM binary and run in SideVM, when you submit your Javascript code, it will actually run in QuickJS engine, and essentially run it in a TEE environment. We exported bunch of useful data from Rust SDK that you can use in JS SDK by inject those data into customer's Javascript code when it being execute, one of them is the private key derived from Rust smart contract engine which you can use sign data.

Now, let's break down step by step to see how you can generate a TEE-proof with JavaScript:

To make the whole progress as easy as possible, we have built a CLI called [jtee](https://github.com/tolak/jtee) to help user create and run JavaScript project on Phala TEE workers.

1.  We haven published `jtee` to npm public registry so now you can use it with `npx`, for more details you can head to the source code repo on [Github](https://github.com/tolak/jtee). You can simply create a project by issuing the following command in terminal:

    ```bash
    $ npx jtee new  <my-jtee-project>
    ```
2.  As the diagram show above, each Javascript code is running in a seperate SideVM and Javascript engine deployed by developer. For the next step is to deploy the engine for your project, the purpose to do so is to have a dedicated private key that only be used for this project.

    Before run deploy command, you need to prepare a Phala blockchain account with enough balance and the node endpoint in the .env file like below in your project root directory. You can check your account balance at [Phala blockchain explorer](https://polkadot.js.org/apps/#/accounts).

    ```bash
    PHALA_ACCOUNT_URI="elegant capable test bar uncover comic speed cabin tattoo company cabin layer"
    PHALA_RPC=wss://poc6.phala.network/ws
    ```

    Then, execute the following command to deploy the engine, the corresponding account will be the deployer of the engine contract:

    ```bash
    $ npx jtee deploy
    ```

    You finally will get the contract ID if everything went well, contract ID would be used when execute Javascript code in the engine:

    ```
    ✅ Contract uploaded & instantiated:  0x9caa44c6686d1c1e17b4885a96faa6d055055930a248531950b0c11217cebf51
    ```

    If you really want to dig into the details of how the engine manage the key derivation and script running, check the code [here](https://github.com/tolak/jtee/blob/main/engine/lib.rs).
3.  The last and final step is to run your Javascript code in the engine. Simple type `jtee run` at the root director of your project.

    ```jsx
    $ npx jtee run
    ```

    This will 1) First compile your project to a single Javascript file from entry file located at app/index.js to dist/index.js , 2) Then upload the code and execute the it in the Javascript engine you deployed on last step. Note that only the engine deployer have the permission to execute Javascript code using this engine, which can protect your from other malicious code upload by attacker.

Now, let’s take a look of the code in `app/index.js` to see what you can do with the `key`

```typescript
async function main() {
    // The account public key in Phala network you used to deploy the engine
    console.log('executor owner:', jtee.owner);

    // The account derived inside TEE for your project which you can use to
    // submit transaction to Ethereum
    console.log('executor account:', jtee.account);

    // ! NEVER print the key to log
    // The private key of jtee account above, never revealed to outside
    const key = jtee.key;

    // Now you can create transaction data and sign it with `key`,
    // Make sure have ETH in the executor account before send tx to blockchain
    // For example, call method Flipper.flip() of solidity contract `contract/Flipper.sol`
    /*
    const abi = [
        "function flip() public",
    ];
    const wallet = new ethers.Wallet(key, new ethers.JsonRpcProvider(process.env.ETHEREUM_RPC | '<http://127.0.0.1:8488>'));
    const flipper = new ethers.Contract('0x...', abi, wallet);
    await flipper.flip();
    */
}

main().catch(console.error);
```

The code is super simple, the only new thing for you probably is the object `jtee` if you have build with `ethers` package before. `jtee` object was injected by the engine which exported several objects that you can use in your script. `jtee.account` is the corresponding account of the `jtee.key`. Which you can use to submit transaction to blockchain (**Before that, don't forget top-up native asset to this account**). `jtee.key` is the private key derived from engine, the security of the key is guranteed by TEE but you should take care of it and **never print it to logs**. The rest commented code is the example to call smart contract located in `contract/Flipper.sol` using [ethers.js](https://docs.ethers.org/). In real use case, your probably need to construct transaction data from your own smart contract, and the `TEE-proof` which we mentioned few times is also not a concrete form, because your code already run in a trusted environment, and `jtee.key` can be used to create the certification to prove the code has run as expected and returned a legitimate result. In the context of verify them on Ethereum, an ECDSA signature is enough.
