# LensAPI Oracle

### Introduction

The Lens Protocol is a Web3 social graph on the Polygon blockchain. It is designed to empower creators to own the links between themselves and their community, forming a fully composable, user-owned social graph. The protocol is built from the ground up with modularity in mind, allowing new features and fixes to be added while ensuring immutable user-owned content and social relationships.

With the rise of SocialFi, there is an increasing need for Web3 Oracles that can bring data of all types on-chain via APIs. Phala Network's LensAPI Oracle is a solution designed to meet this demand, providing developers with a programmable Oracle template that can deploy customizable, no-code Oracles in minutes.

### Prerequisites

Before you begin, make sure you have the following:

* Familiarity with Solidity and the Lens Protocol
* A [Phala wallet](../../introduction/basic-guidance/README.md)
* Phala Network's native $PHA tokens to
  * pay for the gas fee
  * stake to keep your Oracle running

### Step 1: Define Your Oracle

The LensAPI Oracle allows your smart contract to query Lens user and post stats using profile IDs. To begin, navigate to the [LensAPI Oracle deployment page](https://bricks.phala.network/blueprint/lens-oracle/deployment) on the Phat Bricks App. &#x20;

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

<figure><img src="../../.gitbook/assets/1_DLLIeuw8zXGV3I7pUtRL-g.gif" alt=""><figcaption><p>Configure the Oracle</p></figcaption></figure>

### Step 2: Deploy the Oracle

If it's your first time using Phat Bricks, you will need to create a Bricks user profile to manage your deployed projects. You will also need some $PHA token to pay the gas fee on the Phala Blockchain. &#x20;

The Oracle sends data to your contract via Polygon transactions so the UI will ask you to fund a pre-generated Polygon gas fee account with some MATIC to pay the gas fees for your Oracle.

Finally, the LensAPI Oracle Phat Contract operates on a stake-to-compute model, where a minimum amount of 10 $PHA tokens are required for staking to keep the Oracle running on Phala Network. The unstake functionality will be released in the future.

### Step 3: Connect Oracle to Your Smart Contract

Connecting your smart contracts on Polygon to the Oracle you just deployed can be done in a few lines of code.

The identity of Oracle is shown in the Project Details page as the `Oracle Endpoint` field.

<figure><img src="../../.gitbook/assets/bricks-oracle-endpoint.png" alt=""></figure>

Below is a code snippet demonstrating how to request and receive data from the LensAPI Oracle in Solidity, and you can find the full sample [here](https://github.com/Phala-Network/phat-bricks/blob/master/evm/contracts/TestLensOracle.sol):

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

### Step 4: Connect Smart Contract to Oracle

A deployed Oracle is meant to serve one smart contract client at a time. You can configure the client contract address in the Project Details page.

<figure><img src="../../.gitbook/assets/bricks-config-client.png" alt=""></figure>

This address can be updated any time.

> The Oracle will respond to all unanswered requests sent by the smart contract, this may cause unexpected gas fee cost.

### Links

* [Video tutorial](https://www.youtube.com/watch?v=C6kCpItmT6o)
* [LensAPI Oracle deployment page](https://bricks.phala.network/blueprint/lens-oracle/deployment) on Phat Bricks App
