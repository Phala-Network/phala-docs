# 🪞 Mirrored Price Feeds Agent

In blockchains, a price feed stores prices for Smart Contracts. Using trusted sources is crucial, so we're careful about which price feeds we interact with. ChainLink is famous for this, but isn't everywhere yet. While we can use ChainLink's prices, we need a reliable solution. Phat Contract has addressed this with the Mirrored Price Feed.

## Different from other Price Feed solutions

* **Phat Contract as relayers, not aggregators**. The Phat Contract is a simple relayer. Thanks to Phala's [trustless infrastructure](../../../tech-specs/blockchain/), each node can handle relaying tasks separately and securely.
* **Effortless**. Using Phala's Mirrored Price Feed is easy because it has the same ABI as ChainLink, which is widely used. This means if your Smart Contract can work with the ChainLink feed, it will work with Phala's Mirrored Price Feed.
