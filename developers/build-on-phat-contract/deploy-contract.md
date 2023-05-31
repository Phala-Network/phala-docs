# Deploy Contract

## Deploy Your First Contract <a href="#create-and-compile-your-first-contract" id="create-and-compile-your-first-contract"></a>

Now that you have created and compiled your `phat_hello` contract, let's deploy the contract to the [PoC5 Testnet](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fpoc5.phala.network%2Fws#/explorer). There are a couple ways to get you started.

{% tabs %}
{% tab title="Phat UI" %}
Go to the [Phat UI](https://phat.phala.network) website where you will see a landing page.

<figure><img src="../../.gitbook/assets/Phat-UI-landing-page.png" alt=""><figcaption><p>Phat UI Landing Page</p></figcaption></figure>

Next, you will connect your Polkadot wallet ([Talisman](https://talisman.xyz/download), [SubWallet](https://chrome.google.com/webstore/detail/subwallet-polkadot-extens/onhogfjeacnfoofkfgppdlbmlmnplgbn?hl=en\&authuser=0), or [Polkadot.js](https://chrome.google.com/webstore/detail/polkadot%7Bjs%7D-extension/mopnmbcafieddcagagdcbnhejhlodfdd/related))

<figure><img src="../../.gitbook/assets/Select-Polkadot-Wallet.png" alt=""><figcaption><p>Select a Polkadot Wallet</p></figcaption></figure>

For more info on these steps, check out the [Phat Contract Console ](../getting-started/phat-contract-console.md)section. Now that your account has PHA testnet tokens, upload the compile contract file `phat_hello.contract`

Here is a video example of the process. After the contract is deployed and instantiated into a cluster, choose any ETH address and query the balance.

{% embed url="https://youtu.be/NkLHXNEK8iI" %}
Deploy and Call your Phat Contract
{% endembed %}

The query of an ETH balance will look like this:

<figure><img src="../../.gitbook/assets/Query-ETH-Balance-Step1.png" alt=""><figcaption><p>Choose ETH Account to Query</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Query-ETH-Balance.png" alt=""><figcaption><p>Query ETH Balance</p></figcaption></figure>
{% endtab %}

{% tab title="Swanky Phala" %}
> If you have not installed `swanky phala` CLI tool, follow these [steps](../getting-started/swanky-phala-cli-tool.md) to get started.

Go to your development workspace and ensure that you have updated your `devphase.config.json` file to include the PoC5 Testnet info. Within`networks` , add the following:

```bash
"networks": {
    "phatUi": {
      "nodeUrl": "wss://poc5.phala.network/ws",
      "workerUrl": "https://poc5.phala.network/tee-api-1"
    }
  },
```

`phatUi` will be the `-n` flag value in the `swanky phala contract deploy` command.&#x20;

Next, you will execute the following command to deploy your `phat_hello` compiled contract.

{% code overflow="wrap" %}
```bash
swanky phala contract deploy -c phat_hello -l 0x0000000000000000000000000000000000000000000000000000000000000001 -n phatUi -o new
```
{% endcode %}

The flags available for this command are defined as follows:

```bash
➜  Norwhich git:(master) ✗ swanky help phala contract deploy                                                                                     ~/Projects/TestingEnv/Norwhich
Deploy contract

USAGE
  $ swanky phala contract deploy -c <value> -o <value> [-t InkCode|SidevmCode|IndeterministicInkCode] [-n <value>] [-l <value>] [-a <value>] [-p <value>]

FLAGS
  -a, --account=<value>      [default: alice] Account used to deploy (managed account key)
  -c, --contract=<value>     (required) Contract name
  -l, --cluster=<value>      Target cluster Id
  -n, --network=<value>      [default: local] Target network to deploy (local default)
  -o, --constructor=<value>  (required) Contract constructor to call (name)
  -p, --params=<value>...    [default: ] Arguments supplied to the message
  -t, --type=<option>        [default: InkCode]
                             <options: InkCode|SidevmCode|IndeterministicInkCode>

DESCRIPTION
  Deploy contract

EXAMPLES
  $ swanky phala contract deploy -c [CONTRACT_NAME] -t [CONTRACT_TYPE] -o [CONSTRUCTOR] -n [NETWORK] -l [CLUSTER_ID] -a [ACCOUNT] -p [..Args]
```
{% endtab %}
{% endtabs %}
