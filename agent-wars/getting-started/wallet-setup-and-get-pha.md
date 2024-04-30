# Wallet Setup & Get PHA

Agent Wars is deployed on the [Base chain](https://www.base.org/), a popular high performance Ethereum L2 built by Coinbase. You will need to have two tokens to participate:

* **ETH**: needed to pay the gas fee on Base
* **PHA**: used to buy keys and create agents

## Set up wallets on Base chain

Agent Wars supports all EVM-compatible wallets. Recommended wallets include:

1. [Coinbase Wallet](https://chrome.google.com/webstore/detail/coinbase-wallet-extension/hnfanknocfeofbddgcijnmhnfnkdnaad?hl=en): desktop and mobile
2. [MetaMask](https://metamask.io/): desktop and mobile
3. [Rabby](https://rabby.io/): desktop only

For more information, please refer to [the official Base docs](https://docs.base.org/docs/using-base/).

{% hint style="info" %}
Soon, the Agent Wars dapp will come with Social Login Wallets, powered by Privy. You will be able to create an in-app wallet with your social accounts (Google, Facebook, etc).
{% endhint %}

## Get ETH on Base

ETH is the native token of the Base chain. You need to have ETH in your Base wallet to pay the gas fee. You can either buy ETH from centralized exchanges (e.g. [Coinbase](https://www.coinbase.com/), [Binance](https://www.binance.com/)), or bridge ETH from the Ethereum mainnet via the [Base Bridge](https://bridge.base.org/deposit).

{% hint style="info" %}
It's suggested to have at least $10 worth of ETH on Base to cover transaction gas fees. As of Apr 2024, a typical Base transaction takes $0.01 to $0.20 worth of gas in ETH.
{% endhint %}

## Get PHA on Base

You will need PHA on the Base chain to participate in Agent Wars. It's used to buy keys and create agents. You can easily obtain PHA in the following ways:

### Uniswap V3 (Recommended)

You can [buy and sell PHA on Uniswap V3](https://app.uniswap.org/explore/tokens/base/0x336c9297afb7798c292e9f80d8e566b947f291f0) on the Base chain.

### Bridge from Ethereum (Advanced)

You can bridge PHA token between Ethereum mainnet and Base chain with Wormhole bridge.

<details>

<summary>Wormhole Bridge Instructions</summary>

PHA is bridged from Ethereum to Base chain via [Wormhole](https://wormhole.com/) bridge. If you have PHA on Ethereum, you can easily bridge it to Base with Wormhole's UI, Portal Bridge:

1. Open [Portal Bridge (Advanced Bridge)](https://portalbridge.com/advanced-tools/#/transfer)
2. Select the chains: from **Ethereum** to **Base**
3. Connect your Web3 wallet
4. Search the token name `Phala` or the token address `0x6c5ba91642f10282b576d91922ae6448c9d52f4e`
5. Input the amount you want to bridge, and follow the instructions on the web page to proceed

</details>

{% hint style="info" %}
Soon, the Agent Wars dapp will support buying keys and creating agents with ETH. Once upgraded, you will be able to use your ETH balance to buy keys or create agents directly without manually purchasing PHA. The smart contracts will do the heavy lifting for you.
{% endhint %}

### Token Information

<table data-header-hidden><thead><tr><th width="218"></th><th></th></tr></thead><tbody><tr><td>Base ERC20</td><td><a href="https://basescan.org/token/0x336c9297afb7798c292e9f80d8e566b947f291f0">0x336c9297afb7798c292e9f80d8e566b947f291f0</a></td></tr><tr><td>Uniswap PHA/ETH</td><td><a href="https://basescan.org/address/0x03aC059Fd9eb9c2da65D745E923583F05bF388DB">0x03aC059Fd9eb9c2da65D745E923583F05bF388DB</a></td></tr><tr><td>Mainnet ERC20</td><td><a href="https://etherscan.io/token/0x6c5ba91642f10282b576d91922ae6448c9d52f4e">0x6c5ba91642f10282b576d91922ae6448c9d52f4e</a></td></tr></tbody></table>

<details>

<summary>Wormhole Bridge Technical Details</summary>

PHA is bridged from Ethereum to Base chain via [Wormhole](https://wormhole.com/) bridge. The bridged Wrapped ERC20 token is created by and managed by Wormhole on Base chain. The related smart contracts are audited as the other Wormhole bridged tokens.

</details>

