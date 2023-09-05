# Phat Contract Verification

Contract Verification is an important piece of decentralized world, as we already talk about that on Unlocking the Importance and Nuances of Verified Smart Contract. This section will give you a glance of how to build verified Phat Contract and upload to Patron, then share it over the Internet.

## What is Patron?

Patron is a smart contract verification service offered by the Brushfam team. It features a command-line interface (CLI) tool that allows for seamless verification of smart contract builds with a single command. To learn more about how to get started with Patron, visit **[here](https://patron.works/getting-started)**.

## Installation

You need additional installation for the patron cli tool:

```bash
cargo install patron --git https://github.com/brushfam/patron-backend
```

It might take a few minutes to finish. Once it is done, you need to call `patron auth` for initialization. This step only requires you to sign an authentication message once at zero cost.

![Connect wallet for Patron](../../.gitbook/assets/verifiying-your-phat-contract-with-patron-01.jpg)

After that, you will see a message said “Authentication completed” in the terminal. Congrats, that’s all you need on preparation!

## Configuring and Performing Verifiable Building

You need create a `Deploy.toml` file along side with your `cargo.toml`. You will get similar results like the screenshot below:

![Folder structure for Phat Contract with Patron](../../.gitbook/assets/verifiying-your-phat-contract-with-patron-02.jpg)

There are two lines in the `Deploy.toml` file:

```toml
rustc_version = "1.69.0"
cargo_contract_version = "3.2.0"
```

The first line is `rust_version`, it should match what you define in your `rust-toolchain.toml` file. For now please set to `1.69.0`.

The second line is `cargo_contract_version`. For Phat Contract, we need set to `3.2.0` here. If you want to find the full list of supported cargo contract versions, you can check that [here](https://hub.docker.com/r/paritytech/contracts-verifiable/tags).

After setting up the `Deploy.toml` file, you just perform the `patron build` in your terminal and wait for it to complete.

## Deploying to Phala Blockchain

When you see a message like this in the terminal, you now have successfully created a verifiable build.

![Message when your Phat Contract compiled successfully on Patron](../../.gitbook/assets/verifiying-your-phat-contract-with-patron-03.jpg)

You can get a link on Patron as well. Let’s open this link in browser, you will see the code hash, build log, also details of source code on screen. You can click the “Deploy with Phala”.

![If you want deploy this example project, visit here: [https://patron.works/codeHash/ec87cd09b3546a55c17f6252d1efac00c201c6c32130875c5504a1eb0f45556a](https://patron.works/codeHash/ec87cd09b3546a55c17f6252d1efac00c201c6c32130875c5504a1eb0f45556a)](../../.gitbook/assets/verifiying-your-phat-contract-with-patron-04.jpg)

Clicking on the button, will navigate to the Phat Contract UI:

![The landing page when you deploy Phat Contract via Patron](../../.gitbook/assets/verifiying-your-phat-contract-with-patron-05.jpg)

Because we can find the verified build on Patron via code hash, we don’t need update the artifact manually. You can just click “fetch”, “upload”, then the contract bytecode will upload to Phala Blockchain automatically.

The next step is to instantiate. Click “Instantiate”, and a signing request will pop up. Again, you will need to wait for a while until the success message appears.

You can follow the steps annotation on the screenshot.

![Step guide of deploying Phat Contract](../../.gitbook/assets/verifiying-your-phat-contract-with-patron-06.jpg)

Click the “go next” button and you can interact with your Phat Contract instance now. You can see the “Verified by Patron” label beside the code hash.

![Sceenshot of Phat Contract Deploy successfully](../../.gitbook/assets/verifiying-your-phat-contract-with-patron-07.jpg)

## Final Words

You can checkout the example project here: [https://github.com/Leechael/phalaworld-phat-contract-build](https://github.com/Leechael/phalaworld-phat-contract-build)

For more discussion about this topic, and you stuck into some issues, you can reach us on Discord.
