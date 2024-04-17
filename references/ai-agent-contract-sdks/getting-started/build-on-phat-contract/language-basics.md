# Language Basics

The Phat Contract is written in ink! language, which is extended from Rust language (more language support will be provided in the future). It is finally compiled into WebAssembly (WASM), which also takes [security](https://training.linuxfoundation.org/blog/webassembly-security-now-and-in-the-future/) into consideration when designed, then you can upload and deploy them.

Rust is thought to be a hard language, but no worries! It deserves the effort since Rust is fast and helps prevent many million-dollar bugs. Also, I sincerely believe one day you will find it charming since all your enemy is just the Rust compiler itself😼.

The prospering ecosystem is another reason to use Rust-based ink! to develop your contract. There are many secure and high-performance libraries for you to use without building all the wheels from scratch.

This section will not teach you about Rust and ink! language itself. Instead, it provides some helpful links and comments to get you prepared quickly.

## Rust <a href="#rust" id="rust"></a>

### Tooling <a href="#tooling" id="tooling"></a>

When using Rust, you will always rely on the following official tools to manage your toolchain and compile your projects:

* [rustup](https://rustup.rs/), which helps you install and manage different versions of Rust compilers;
* cargo, the package manager is installed automatically along with the Rust compiler. Each Rust project contains a `Cargo.toml` file to describe its metadata and dependencies, and `cargo` downloads the dependencies and builds the project for you. The [cargo book](https://doc.rust-lang.org/cargo/reference/index.html) can help, and ensure you understand the [\[dependencies\]](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html) and [\[features\]](https://doc.rust-lang.org/cargo/reference/features.html) sections in `Cargo.toml` before going on.

### Language Basics <a href="#language-basics" id="language-basics"></a>

The best material is surely the official [Rust book](https://doc.rust-lang.org/book/).

* For a beginner, learning the first 6 sections is enough for your journey in the Phat Contract world;
* I also recommend finishing the 7 - 10 sections when you decide to go a little deeper.

There are also many [books recommended by the community](https://www.reddit.com/r/rust/comments/sjclfb/best\_book\_to\_learn\_rust/) for more advanced topics.

## ink! <a href="#ink" id="ink"></a>

ink! is the default contract programming language in the Polkadot ecosystem. The native ink! contracts can run on different blockchains (like Polkadot and Phala), but Phala adds its secret ingredient called [pink-extension](https://github.com/Phala-Network/phala-blockchain/tree/master/crates/pink) (short for Phala ink! Extension) to form Phat Contract which is only functional in Phala cloud.

> Phat Contract is the superset of ink! contract.

### ink! Macros <a href="#ink-macros" id="ink-macros"></a>

The difference between an ink! contract and a normal Rust program are the macros in it. As shown in our example contract, you need to annotate the Rust code with ink! macros so the compiler can learn your contract structure. For example,

```
#[ink(storage)]
pub struct OnchainState;
```

`#[ink(storage)]` tells us the following struct `OnchainState` saves the contract states and needs to be stored on-chain. And

```
#[ink(message)]
pub fn query_handler(&self, from: AccountId) {
    // actual implementation
}
```

`#[ink(message)]` means the following functions are meant to be called by other contracts or users in different ways.

For a complete list of these macros and a more detailed tutorial, refer to the [official document](https://ink.substrate.io/).

### Use Crates in Your Contract <a href="#use-crates-in-your-contract" id="use-crates-in-your-contract"></a>

> If you do not know what’s Crate, you may need to go over your Rust book.

[crates.io](https://crates.io/) is the market for Rust crates. While only the crates with `no_std` support can be used in your ink! contract. The reason is [explained by the official](https://ink.substrate.io/faq#why-is-rusts-standard-library-stdlib-not-available-in-ink).

We will further provide crate recommendations for different use cases in the following [section](broken-reference).
