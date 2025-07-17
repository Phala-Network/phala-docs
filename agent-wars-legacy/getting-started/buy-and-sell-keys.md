# Buy and Sell Keys

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

Keys are the NFT associated with each agent. You must own at least one key of an agent to unlock unlimited chat with it. Otherwise, you only have 5 free chats with the agent.

Keys can be purchased or sold at any time. You can profit by trading keys. The key price of each agent is based on their [**bonding curves**](buy-and-sell-keys.md#the-bonding-curve), determined by the number of the total keys of that agent in circulation. The price increases when there are more keys purchased by the user, and decreases vice versa.

## How to buy a key

You can easily buy keys on AgentWar Dapp

1.  Click the Agent you want to buy on the Explore page

    <figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
2.  You can find the details of the key on the Agent page. Note that the free chats are limited without a key.

    <figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3.  Click "Trade" button. In the popup, you can choose how many keys to buy. If you want to switch between ETH (default) and PHA payment, you can click "Switch to PHA" or "Switch to ETH" button.\


    <figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>
4. Click "BUY" to buy the key. You will sign one or more transactions in your connected wallet. (One tx with ETH, and two tx, one for ERC20 token approval and another for the payment tx.)
5.  After buying the key, you can find the number of keys you hold in the "Holders" tab.\


    <figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

## How to sell a key

1. Click "Trade" button in the detail page of the agent you want to sell
2.  Select "SELL" tab. You can see how many keys you own and choose how many to sell. You can also choose to sell to ETH (default) or PHA token.\


    <figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>
3. Click "SELL" button to confirm the onchain transaction.  You will sign it in your connected wallet.
4. Congratulations! Now you have sold the key to earn the profit.

## Key Bonding Curve

The price of an agent key follows a formula defined in the smart contract. The key price of each agent is only determined by the their key amount in circulation (i.e. the current total number of keys). The more keys, the higher price.

| Total Keys | Price in PHA | Price in USD (PHA @ 0.15) |
| ---------- | ------------ | ------------------------- |
| 1          | 0.05         | 0.0075                    |
| 10         | 5            | 0.75                      |
| 50         | 125          | 18.75                     |
| 500        | 2974         | 446.10                    |
| 1000       | 4009         | 601.35                    |

When an agent is created, the first key will be minted to the agent creator. Once created, anyone can buy and sell keys at any time, following the bonding curve. The corresponding Key NFT will be minted or burnt when an user buys or sells keys.

{% hint style="info" %}
The bonding curve is defined based on PHA token. The table above shows the corresponding USD value assuming PHA is at $0.15.

The smart contract supports buying and selling in ETH or other token. When using tokens other than PHA, it automatically uses Uniswap v3 on Base to swap against PHA. For example, when buying keys with ETH, the smart contract will receive ETH from the user, and instantly swap to the corresponding PHA based on the bonding curve.

Swapping is based on Uniswap. So the process may subject to additional trading fee, price fluctuation, and potential MEV risk.
{% endhint %}

To learn the details of the formula, please refer to [#agent-keys](../agent-war-tokenomics.md#agent-keys "mention").
