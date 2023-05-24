# Phat Contract Console

Phat Contract UI provides an easy way to upload your contract, instantiate it and interact with it.

* For public testnet, visit [https://phat.phala.network](https://phat.phala.network/)
* For Closed Beta, visit [https://phat-cb.phala.network](https://phat-cb.phala.network/)

Before you use it, make sure you have prepared your test account, or follow our [tutorial](generate-test-account.md) to create one.

> Never use your personal accounts for testing in case of unexpected financial losses.

## Connect Wallet <a href="#connect-wallet" id="connect-wallet"></a>

<figure><img src="../../.gitbook/assets/phat-ui.png" alt=""><figcaption></figcaption></figure>

On the homepage, click _Connect Wallet_ in the right top corner, and choose the wallet you are using. The browser will pop up an _Authorize_ window. Click Yes to allow authorization. Then you can connect to one of your accounts in the _Select Account_ window.

## Connect to Blockchain <a href="#connect-to-blockchain" id="connect-to-blockchain"></a>

<figure><img src="../../.gitbook/assets/phat-ui-endpoint-setting.png" alt=""><figcaption></figcaption></figure>

Click the green dot beside your account will tell you the information about the current chain you are connecting to.

<figure><img src="../../.gitbook/assets/phat-ui-connection-info.png" alt=""><figcaption></figcaption></figure>

By default, the UI will connect to

* [PoC-5 Testnet](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fpoc5.phala.network%2Fws#/explorer)
* or [Closed Beta Testnet](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fphat-beta.phala.network%2Fkhala%2Fws#/explorer)

You can connect to any other chains by filling in the RPC Endpoint and click _Connect_. The UI will automatically read the cluster information from the chain and fill in the PRuntime for you, but you can always set it to other workers.

> **Why two endpoints**
>
> Unlike other blockchains like Ethereum where you have to call your contracts through on-chain transactions, Phat Contracts are finally deployed to the off-chain Secure Workers so you can interact with them directly without submitting any transactions. So the UI will ask for two endpoints, one to connect to the blockchain and another to the worker directly.

To connect to our mainnet or your local testnet, you need to specify two endpoints here:

* An RPC endpoint to connect to one of the Phala blockchain nodes to read the chain state and send transactions;
* A pRuntime endpoint to directly connect to one of our Workers where the [off-chain computation](https://medium.com/phala-network/fat-contract-introduce-off-chain-computation-to-smart-contract-dfc5839d5fb8) really happens;

## Claim Test Tokens <a href="#claim-test-tokens" id="claim-test-tokens"></a>

Once the account is connected, you can find the _Get Test-PHA_ button on the right side of the page. You can request 100 test tokens by clicking it. Please do so if you haven’t done it yet. The operations below require tokens as the transaction fee.

> **For Closed Beta**
>
> The button will lead you to the `#faucet` channel in our Discord server. Post your account there to get the test tokens.

## Upload and Instantiate the Contract <a href="#upload-and-instantiate-the-contract" id="upload-and-instantiate-the-contract"></a>

Choose `Upload` and locate your `phat_hello.contract` file (you can download it from previous section). The UI will load the metadata of your contract and list all the constructor functions in the `Init Selector` section.

<figure><img src="../../.gitbook/assets/phat-ui-upload.png" alt=""><figcaption></figcaption></figure>

> **About Cluster**
>
> Phala has over 10k Secure Workers. They are organized into Clusters so you can use their computing power easily without knowing the underlying details.
>
> In our testnet, we have prepared a public good Cluster which anyone can deploy their contracts to.

After you click the `Submit`, it will upload the contract WASM to the blockchain through transaction (the UI will ask for your permission).

> **What happened**
>
> Your contract code is uploaded to the blockchain with transaction, that’s why your signature is needed. The code is public, together with your instantiation arguments, this is meant to so that everyone can verify the initial state of the contract.
>
> The blockchain will automatically push the contract code to the workers belong to the cluster you choose and instantiate it.

After the successful instantiation, you shall see the metadata of the deployed contract.

<figure><img src="../../.gitbook/assets/phat-ui-metadata.png" alt=""><figcaption></figcaption></figure>

Also, you can expand the lower bar to see the raw events when deploying the contract.

<figure><img src="../../.gitbook/assets/phat-ui-events.png" alt=""><figcaption></figcaption></figure>

## Interact with Your Contract <a href="#interact-with-your-contract" id="interact-with-your-contract"></a>

Scroll down the webpage and you can see all the interfaces of this contract, with their function names, types, and descriptions.

The interfaces are divided into two types, labeled by `TX` and `QUERY` respectively. This contract only contains one `QUERY` handler. We will cover the `TX` handler in the following section. The phat-hello contract has only one `QUERY` interface `get_eth_balance()`.

<figure><img src="../../.gitbook/assets/phat-ui-input.png" alt=""><figcaption></figcaption></figure>

Click the run icon to send the request to the contract. For example, we can invoke the `get_eth_balance()` to get the current balance of a certain ETH address. The Polkadot.js extension will ask for your permission in the first click to encrypt your following traffic to the contract.

> **What happened**
>
> Every transaction or query to the contract is encrypted, thus needs your signature. To save your efforts for signing every query (since query can be frequent), we implement a certificate mechanism to keep your query signature valid for 15 minutes.

The `QUERY` returns immediately since it involves no on-chain transactions. Click the bottom status bar to see the execution result.

<figure><img src="../../.gitbook/assets/phat-ui-result.png" alt=""><figcaption></figcaption></figure>

Congrats🎉! You have finished the basic tutorial of Phat Contract!
