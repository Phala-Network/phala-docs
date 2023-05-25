# Environment Setup

## Supported Operating Systems <a href="#supported-operating-systems" id="supported-operating-systems"></a>

The Phat Contract uses Rust-based ink! language, and is finally compiled to WebAssembly (WASM for short).

* You can get your contract compiled on both macOS and Linux distributions (we use Ubuntu 22.04 as the default Linux distribution);
* For Windows users, we recommend to setup a Linux development environment with virtual machine ([video tutorial](https://www.youtube.com/watch?v=x5MhydijWmc)).

> **Note**
>
> If you are deploying a local testnet on your development machine, the Mac M1/M2 chips are not supported at this time. In this case, you will have to deploy to the live testnet at through [DevPHAse](https://github.com/l00k/devphase), [swanky phala](../getting-started/swanky-phala-cli-tool.md), or [Phat UI](https://phat.phala.network).
>
> Information to connect to the Phala Live Testnet PoC5
>
> * RPC Endpoint: wss://poc5.phala.network/ws
> * Cluster ID: 0x0000000000000000000000000000000000000000000000000000000000000001
> * Worker: 0x94a2ded4c7...2ffd4bae9b63
> * pRuntime URL: [https://poc5.phala.network/tee-api-1](https://poc5.phala.network/tee-api-1)

## Install Toolchains

Phat Contract shares exactly the same toolchains as ink!.

### Rust <a href="#rust" id="rust"></a>

A prerequisite for compiling Phat Contracts is to have Rust and Cargo (Rust’s project manager) installed.

The Rust official recommends using `rustup` tool to install and manage different Rust versions. Here’s [an installation guide](https://doc.rust-lang.org/cargo/getting-started/installation.html).

### ink! <a href="#ink" id="ink"></a>

We recommend installing [`cargo-contract`](https://github.com/paritytech/cargo-contract). It’s a CLI tool that helps set up and manage contracts written with ink!.

Then you can install the `cargo-contract` with

```
# use the `--force` to ensure you are updated to the most recent version
cargo install cargo-contract --force
```

Then check your `cargo-contract` and ensure it’s updated to `2.x` with ink! 4 support

```
cargo contract --version
# cargo-contract-contract 2.1.0-unknown-x86_64-unknown-linux-gnu
```
