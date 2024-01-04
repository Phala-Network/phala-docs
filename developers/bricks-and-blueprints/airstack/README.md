# ✈ Airstack

The Airstack template allows for users to request data from Airstack’s API to compute a trust/risk score and send to an on-chain consumer contract.

## Requirements Before Deployment

There are a couple steps to complete before deploying the Airstack Template.

* Create a [Phat Contract 2.0 Profile](https://app.gitbook.com/o/uC1n4EsT23m6ZTklOdXG/s/mFxKaTU233OXZzSqmqjx/\~/changes/60/developers/bricks-and-blueprints/create-a-phat-contract-profile)
  * Generate and fund an EVM account for the target chain you plan to deploy your Consumer Contract to
* Deploy the Consumer Contract (The right side of the diagram above) on an EVM chain that will connect to the deployed Phat Contract
* (Optional) Create API Key from Airstack. See how to get an API Key [here](https://bit.ly/airstack-api-key). By default a rate-limited key is provided with no guarantee of service if limit is exhausted.

## Features and Benefits

With the ability to bring Airstack’s data on-chain with customized logic performed on the data, developers can now securely connect their indexed data to their web3 dApps. There are many features and benefits that can be built. For example:

* Web3 Social
  * Spam Filter
  * Recommendation Engine
  * Trust Score
  * Web3 Social Actions based on data from Airstack’s API
* Token Gating
* Web3 Marketing Technology, etc.

## Resources

* [Airstack Phat Contract Code Template](https://bit.ly/pc-airstack-repo)
* [Airstack Docs](https://docs.airstack.xyz/airstack-docs-and-faqs/)
