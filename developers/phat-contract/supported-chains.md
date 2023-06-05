# Supported Chains

Phat Contract can technically connect to any blockchain for reading and writing operations, as it can effortlessly read from arbitrary blockchain nodes and trigger signed transactions via RPC calls. However, in practice, supporting a specific blockchain requires the corresponding Phat Contract RPC client, serialization library, and signing library to facilitate read and write operations. Presently, EVM and Substrate blockchains have more extensive library support.

### EVM blockchains

Phat Contract fully supports EVM blockchains. At the blueprint level, the first blueprint LensAPI Oracle offers support for:

* Polygon: provided out-of-the-box

At the Native Phat Contract level, it is possible to interact with any EVM-compatible blockchains through their RPC nodes, including:

* Ethereum
* Polygon
* Arbitrum
* BSC
* Optimism
* and any EVM-compatible blockchains

Learn more in the advanced topic.

{% content-ref url="../advanced-topics/cross-chain-solutions.md" %}
[cross-chain-solutions.md](../advanced-topics/cross-chain-solutions.md)
{% endcontent-ref %}

### Substrate blockchains

Native Phat Contract fully supports Substrate-based blockchains, such as:

* Polkadot
* Kusama
* Phala Network
* Astar
* and any Substrate-based blockchains

However, there are currently no blueprints targeting Substrate. The introduction of Substrate-targeted blueprints is anticipated in the near future.

Learn more in the advanced topic.

{% content-ref url="../advanced-topics/cross-chain-solutions.md" %}
[cross-chain-solutions.md](../advanced-topics/cross-chain-solutions.md)
{% endcontent-ref %}

### Add more blockchain

Supporting additional blockchains does not necessitate any changes to the Phala Network infrastructure. Developers can independently implement their RPC client, serialization, and signing libraries in Native Phat Contract and share them with the community.

The following blockchains are expected to receive support soon:

* Cosmos-based blockchains
* Solana
* Move-based blockchains

Let us know which blockchain you would like to see supported in the `#phat-contract` channel on our [Discord server](https://discord.gg/phala).
