# Supported Chains

Phat Contract can technically connect to any blockchain for reading and writing operations, as it can effortlessly read from arbitrary blockchain nodes and trigger signed transactions via RPC calls. However, in practice, supporting a specific blockchain requires the corresponding Phat Contract RPC client, serialization library, and signing library to facilitate read and write operations. Presently, EVM and Substrate blockchains have more extensive library support.

### EVM blockchains

At the Native Phat Contract level, it is possible to interact with any EVM-compatible blockchains through their RPC nodes, including:

* Ethereum
* Polygon
* Arbitrum
* BSC
* Optimism
* any other EVM-compatible blockchains

Learn more in the advanced topic section.

### Substrate blockchains

Native Phat Contract fully supports Substrate-based blockchains, including:

* Polkadot
* Kusama
* Phala Network
* Astar
* any other Substrate-based blockchains

You can learn more about Phat Contract's cross-chain capabilities and how to implement them in the advanced topics section:

{% content-ref url="../advanced-topics/cross-chain-solutions.md" %}
[cross-chain-solutions.md](../advanced-topics/cross-chain-solutions.md)
{% endcontent-ref %}

### Expanding Support to Additional Blockchains

Supporting additional blockchains does not necessitate any changes to Phala Network's infrastructure. Developers can independently implement their RPC client, serialization, and signing libraries in Native Phat Contract and share them with the community.

The following blockchains are expected to receive support soon:

* Cosmos-based blockchains
* Solana
* Move-based blockchains

Let us know which blockchain you would like to see supported in the `#phat-contract` channel on our [Discord server](https://discord.gg/phala).
