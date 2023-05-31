# Manage the Worker

> We highly recommend reading about our staking mechanism before using the [Phala App](https://app.phala.network/mining/).

Workers and pool owners can use the Phala App to manage Workers/ Workers and StakePools. It also provides an overview of the status of all the managed Workers and Stake Pools.

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

> 1. The same Khala account the Workers run on, as the pool Owner and Worker operator.
> 2. `worker public key`: The Worker must be ready and synced. This worker must use the same Khala Account as the one you use for the Khala App.

If you do not have a wallet yet, [create one](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fkhala-api.phala.network%2Fws#/accounts) (+ Add account) and install the [Polkadot{.js} extension](https://polkadot.js.org/extension) for your browser.

* [Khala Wallet](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fkhala-api.phala.network%2Fws#/accounts)
* [Polkadot{.js} extension](https://polkadot.js.org/extension)
* [Khala App](https://app.phala.network/mining/)

## Phala App Operations <a href="#phala-app-operations" id="phala-app-operations"></a>

### Create a Pool <a href="#create-a-pool" id="create-a-pool"></a>

1. Connect your Khala account.
2. Create StakePool
   * In the left menu, make sure you select ‘Mining.’
   * Click “Create Stakepool” in the top right corner;&#x20;
   * Click “Confirm” in the pop-up window;
   * Sign the transaction in the Polkadot{.js} Extension and wait;
   * The created pool will be listed in Stakepool;

### StakePool Settings <a href="#stakepool-settings" id="stakepool-settings"></a>

> Note that the StakePool configuration is optional.

* Set the Payout
  * Click “Set Payout Pref” of the target pool;
  * Type in the payout in the pop-up window; the default payout is 0, and it can be set between 0-100%;
  * Click “Confirm” to send the transaction;
  * The payout value will be updated in the Stakepool list;
* Set Staking Capacity
  * Click “Set Cap” of the target pool;
  * Type in the Staking capacity in the pop-up window; the default capacity is unlimited, and it can be set between “Total Stake Now” to unlimited number;
  * Submit the transaction;
  * The capacity value will be updated in the Stakepool list;

### Add a Worker <a href="#add-a-worker" id="add-a-worker"></a>

* Select `...` (next to “Info”) “Add Worker” (highlighted red) in the target pool;
* Copy & paste your `worker public key` of your worker in the pop-up window;
* Submit the transaction;
* Your worker will now be listed;

### Staking/Delegating <a href="#staking-delegating" id="staking-delegating"></a>

* After creating the StakePool, you can invite other Stakers to invest or stake yourself;
* To stake yourself
  * Click “Stake” of the target pool;
  * Click “Contribute” in the pop-up window;
  * Type in the amount to stake, it should be less than your “Transferrable Balance” and “Pool Cap Gap”;
  * Submit the transaction;
  * Click the “Stake” of the target pool, and you should see the change of “Locked” amount in “Your Stake Info”;

### Start Mining <a href="#start-mining" id="start-mining"></a>

* Click “Start” of the Worker in “Ready” state;
* Type in the stake amount for the Worker, it should be more than “Smin” and less than “Smax” and “Pool Free Balance”. Noted that you **CAN NOT** change the stake amount during mining;
* Submit the transaction;
* The Worker state should transit from “Ready” to “Mining”;

### Claim your Rewards <a href="#claim-your-rewards" id="claim-your-rewards"></a>

* Click “Claim” of the target pool;
* You can see your rewards from this pool, including “Owner Reward” and “Staker Reward”;
* Choose your account to claim the rewards;
* Submit the transaction;
* Your account balance should be increased accordingly;

## Other Operations <a href="#other-operations" id="other-operations"></a>

### Withdraw Staking <a href="#withdraw-staking" id="withdraw-staking"></a>

* Click “Stake” of the target pool;
* Click “Withdraw” in the pop-up window;
* Type in the amount to withdraw;
* Submit the transaction;
* You may wait for at most 14 days to get all your staking (check staking mechanism. You can check the frozen amount in the “Withdraw Queue” of “Stake” pop-up;

### Stop Mining <a href="#stop-mining" id="stop-mining"></a>

* Click “Stop” of the Worker in “Mining” or “Unresponsive” state;
* Submit the transaction;
* The Worker state should transit to “CoolingDown”;

### Remove Worker <a href="#remove-worker" id="remove-worker"></a>

* Click “Remove” of the Worker in its “Ready” state;
* Submit the transaction;
* The Worker should be removed from the list;

## Explanations of Fields <a href="#explanations-of-fields" id="explanations-of-fields"></a>

### Stakepool List <a href="#stakepool-list" id="stakepool-list"></a>

1. You can click “Create Pool” to create a new StakePool if the list is empty;
2. Fields
   * Owner Reward: The owner reward from the payout which can be claimed immediately;
   * Total Shares: The total staking amount;
   * Free Stake: The free staking amount;
   * Releasing Stake: The total staking amount of the pool Workers in “CoolingDown” state;
3. “Show this only” Button: only show the Workers of the target pool;

### Worker List <a href="#worker-list" id="worker-list"></a>

1. You can click “Add Worker” to add a new Worker if the list is empty;
2. Fields
   * Mining Core: The number of CPU cores in use;
   * State: Includes Ready, Mining, Unresponsive and CoolingDown (will turn to Ready after 7 days);
   * Total Reward: All the historical rewards of the Worker;

### Staking Info <a href="#staking-info" id="staking-info"></a>

1. Withdraw Queue lists all the funds to be withdrawn, ordered by the issue time. Noted that unmet withdrawal requests can cause **ALL** the Workers to stop mining.
   * Staker: The Staker sending the withdrawal requests.
   * Shares: The reminder funds to be withdrawn.
   * Countdown: If there are still Shares after Countdown reaching 0, all the Workers in the pool will be forced into a 7-day freeze period.
2. Your Stake Info
   * Locked: Your staking amount in this pool.
   * Shares: Your staking amount in use.
