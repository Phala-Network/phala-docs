# LensAPI Oracle

### Introduction

The Lens Protocol is a modular web3 social graph on Polygon that allows creators to own their community links and user-generated content while maintaining immutability. This protocol enables users to own and migrate their data across platforms, freeing them from being locked to a specific network.

With the rise of SocialFi, there is an increasing need for web3 oracles that can read data from APIs. The LensAPI Oracle, powered by the Phala Network, is a solution designed to meet this demand. It provides developers with a programmable web3 oracle that can deploy custom, no-code oracles in just five minutes.

### Prerequisites

Before you begin, make sure you have the following:

* Familiarity with Solidity and the Lens Protocol
* Phala Network's native $PHA tokens for staking

### Step 1: Define your oracle

The LensAPI Oracle allows your smart contract to query a Lens profile stats data with the profile id. To begin with, navigate to the [LensAPI Oracle deployment page](https://bricks.phala.network/blueprint/lens-oracle/deployment) on the Phat Bricks App. Define the stats field you want to request from the Lens API. The supported data fields are:

* User Stats API
  * Total followers
  * Total followings
* Post Stats API
  * Total posts
  * Total comments
  * Total mirrors
  * Total publications
  * Total collects

You can also add custom Javascript expressions if necessary.

<figure><img src="../../.gitbook/assets/1_DLLIeuw8zXGV3I7pUtRL-g.gif" alt=""><figcaption><p>Configure the oracle</p></figcaption></figure>

### Step 2: Deploy the Oracle

Next, follow the instruction to deploy the LensAPI Oracle. If it's your first time to use Phat Bricks, you will need to create a Bricks user profile to manage your deployed projects. You will need some $PHA token to pay the gas fee on the Phala Blockchain. This step will be skipped if you already have a user profile.

The oracle sends data back to Polygon. So if you haven't done before, the UI ask you to charge a pre-generated Polygon gas fee account with some MATIC to pay the gas fee for your oracle.

Finally, the LensAPI Oracle Phat Contract operates on a stake-to-compute model, where a minimum amount of 10 $PHA tokens are required for staking to deploy the oracle on the Phala Network.

### Step 3: Connect Your Smart Contract

Connect your smart contracts on Polygon to request the oracle you just deployed. This can be done in a few lines of code. Below is a code snippet demonstrating how to request and receive data from the LensAPI Oracle in Solidity, and you can find the full sample [here](https://github.com/Phala-Network/phat-bricks/blob/master/evm/contracts/TestLensOracle.sol):

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
