# Features

## Compared with Smart Contract <a href="#compared-with-smart-contract" id="compared-with-smart-contract"></a>

The existing smart contract solutions have many limitations:

* High latency with a limited number of instructions to execute;
* No database support;
* No network access;
* Few libraries;

Phat Contract is meant to be the missing computational unit for existing smart contracts, so you do not need to deploy your backend programs to a centralized cloud anymore.

<figure><img src="../../.gitbook/assets/fat-features.jpeg" alt=""><figcaption></figcaption></figure>

The Phat Contract inherits the self-enforcing and tamper-proof nature of smart contracts while introducing more advantages including:

* Privacy-preserving with performance. It’s safe to store and process your secret data in Phat Contract since it’s backed by hardware-based encryption throughout its lifecycle;
* Zero latency, zero gas fee. The interactions with Phat Contract can involve no on-chain transactions, thus achieving millisecond-level read and write responses with no gas fee;
* Connectivity with HTTP requests. Phat Contract natively supports HTTP requests. Use it to connect any existing Web2 services to store data and build Oracle, or an RPC node of other blockchains for easy and safe cross-chain operations;
* Freedom to use libraries in the Rust ecosystem. Write your contract with Rust-based [ink! language](https://paritytech.github.io/ink/) and use libraries with `no_std` support. We will support `std` in the future Phat Contract version then you can use any libraries you like.

## Compared with Web2 Serverless Services <a href="#compared-with-web2-serverless-services" id="compared-with-web2-serverless-services"></a>

Phat Contract provides the same functionalities as our Web2 counterparts but opens up more possibilities with its Web3 nature.

* Enforced execution of general-purpose programs. The enforcement of execution is the core feature of smart contracts: the developers cannot tamper or stop their programs after deployment, which builds the trust base. With Phat Contract, we bring this to more general-purpose programs. Never under-estimate this since it’s why cryptocurrencies can have value;
* Decentralized and trustless infrastructure. Our infrastructure design is totally public and all its code is available for you to check. To process your sensitive data in Phat Contract implies no trust in the Phala team, but in the code and Secure-Enclave-based hardware;
* Easier integration with other blockchains. We provide contract templates for easy and safe interactions with existing blockchains. Also, you can safely delegate your chain accounts to the trustless Phat Contract with no worry about privacy leakage;
* Open contract ecosystem. The most typical difference between contracts and Web2 programs is that they are naturally public: you are free to call any existing contracts to compose your own apps with little effort.
