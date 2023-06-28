# LensAPI Oracle

### Introduction

The Lens Protocol is a Web3 social graph on the Polygon blockchain. It is designed to empower creators to own the links between themselves and their community, forming a fully composable, user-owned social graph. The protocol is built from the ground up with modularity in mind, allowing new features and fixes to be added while ensuring immutable user-owned content and social relationships.

With the rise of SocialFi, there is an increasing need for web3 oracles that can bring data of all types on-chain via APIs. Phala Network's LensAPI Oracle is a solution designed to meet this demand, providing developers with a programmable oracle template that can deploy custom, no-code oracles in minutes.

### Prerequisites

Before you begin, make sure you have the following:

* Familiarity with Solidity and the Lens Protocol
* Phala Network's native $PHA tokens for staking

### Step 1: Define your oracle

The LensAPI Oracle allows your smart contract to query Lens user and post stats using profile IDs. To begin, navigate to the [LensAPI Oracle deployment page](https://bricks.phala.network/blueprint/lens-oracle/deployment) on the Phat Bricks App.&#x20;

Define the fields you want to request from the Lens API. The supported data fields are:

* User Stats API
  * Total followers
  * Total followings
* Post Stats API
  * Total posts
  * Total comments
  * Total mirrors
  * Total publications
  * Total collects

You can also add custom Javascript expressions to enhance your query if necessary. &#x20;

<figure><img src="../../.gitbook/assets/1_DLLIeuw8zXGV3I7pUtRL-g.gif" alt=""><figcaption><p>Configure the oracle</p></figcaption></figure>

### Step 2: Deploy the Oracle

If it's your first time using Phat Bricks, you will need to create a Bricks user profile to manage your deployed projects. You will also need some $PHA token to pay the gas fee on the Phala Blockchain.&#x20;

The oracle sends data to Polygon via on-chain transactions so the UI will ask you to fund a pre-generated Polygon gas fee account with some MATIC to pay the gas fees for your oracle.

Finally, the LensAPI Oracle Phat Contract operates on a stake-to-compute model, where a minimum amount of 10 $PHA tokens are required for staking to deploy the oracle on Phala Network.

### Step 3: Connect Your Smart Contract

Connecting your smart contracts on Polygon to the oracle you just deployed can be done in a few lines of code. Below is a code snippet demonstrating how to request and receive data from the LensAPI Oracle in Solidity, and you can find the full sample [here](https://github.com/Phala-Network/phat-bricks/blob/master/evm/contracts/TestLensOracle.sol):

```solidity
    function request(string calldata profileId) public {
        // assemble the request
        uint id = nextRfequest;
        requests[id] = profileId;
        _pushMessage(abi.encode(id, profileId));
        nextRequest += 1;
    }

    function _onMessageReceived(bytes calldata action) internal override {
        require(action.length == 32 * 3, "cannot parse action");
        (uint respType, uint id, uint256 data) = abi.decode(
            action,
            (uint, uint, uint256)
        );
        if (respType == TYPE_RESPONSE) {
            emit ResponseReceived(id, requests[id], data);
            delete requests[id];
        } else if (respType == TYPE_ERROR) {
            emit ErrorReceived(id, requests[id], data);
            delete requests[id];
        }
    }
```

Once your consumer contract is deployed, don't forget to turn back to the oracle project detail page, and configure your Polygon consumer contract address to authorize the access.

### Links

* [Video tutorial](https://www.youtube.com/watch?v=C6kCpItmT6o)
* [LensAPI Oracle deployment page](https://bricks.phala.network/blueprint/lens-oracle/deployment) on Phat Bricks App
