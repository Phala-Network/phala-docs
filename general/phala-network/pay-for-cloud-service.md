# Pay for Cloud Service

## Introduction <a href="#introduction" id="introduction"></a>

This version is written by [Samuel Häfner](https://samuelhaefner.github.io/). It complements Phala Supply-end Tokenomics v0.9 and defines the _Demand-End Tokenomics_ in Phala Network, e.g, how developers and end-users pay for the computing services. It will be released as Phat Contract goes live. The exact problems addressed by this tokenomics are:

* Computing power allocations among contract clusters and their end-users (contract deployers);
* The algorithm for clusters-workers matching;
* The mechanism of worker incentivization.

## Main characters <a href="#main-characters" id="main-characters"></a>

| Character                          | Description                                                                                                                                                | Types            |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Contract Clusters (abbr. Clusters) | The runtime environments for specific contracts. A contract cluster is created and managed by its owner, and is backed by one or more workers.             | On-chain entity  |
| Workers                            | The machines that contribute computing power to Phala Network. These were previously named _miners_. Anyone with the appropriate hardware can participate. | Physical machine |
| End-users                          | The users or developers who deploy the Phat contracts to the contract cluster.                                                                             | On-chain entity  |
| Contracts                          | The Phat contract instances.                                                                                                                               | On-chain entity  |

## How to pay for the computing services <a href="#how-to-pay-for-the-computing-services" id="how-to-pay-for-the-computing-services"></a>

This section consists of 2 parts: query tokenomics and transaction tokenomics. It applies to all the public good clusters that are managed by Phala team. In the future, users will be allowed to create their clusters and define their own rules.

> Every contract must have some stake

### Query tokenomics <a href="#query-tokenomics" id="query-tokenomics"></a>

Phat Contract utilizes a very simple tokenomics for queries. The rules can be summarized below:

* The share of computing power a contract receives on each worker equals the stake’s share of that in the cluster;
* Anyone can stake to any contract;
* The stake can be adjusted or withdrawn on-the-fly instantly.

It can be summarized as a one-liner:

`The % of your stake = The % of your computing power share you receive`

Usually, end-users will estimate the workload of the application, and then decide the amount to stake to get enough computing power. However, on Phala Network, the estimation turns out to be so tricky that the help of additional tools may be required. There will be a typical resource requirement of a few baseline applications to end-users as a reference in Phat Contract’s UI.

### Transaction tokenomics <a href="#transaction-tokenomics" id="transaction-tokenomics"></a>

The transaction tokenomics’ goal is to mitigate DoS attacks by charging some transaction fee (also called “gas fee”). Since the transaction is rarely used in Phat Contract, we tend to offer a minimum interface to developers. (Users will mostly interact with Phat Contract by queries, while the transaction is used to deploy and configure Phat Contracts by the developer.)

Phat Contract adopts the same transaction payment mechanism as the vanilla ink! contracts - when sending a transaction call, it must attach some “gas fee” to the transaction.

In the execution of the transaction in the VM:

* Each instruction will charge some fee until it finishes or the supplied gas fee is exhausted.
* If there is any gas fee left, the blockchain will return the remaining token to the caller.

This mechanism can mitigate the Halting Problem, preventing the VM from trapping in the infinite loop.

In the actual implementation, the transaction comes with a `gasLimit` and a `gasPrice`. The execution of the instructions is measured by `gas`, which should never exceed `gasLimit`. The user pays `gasLimit * gasPrice` first, and after the execution, if there is any remaining gas, the chain will refund the user `remainingGas & gasPrice`. Both Ethereum and ink! adopt the same mechanism.

## How it works <a href="#how-it-works" id="how-it-works"></a>

It is different from the Supply-end Tokenomics which mainly fixes the problem of how to incentivize workers to join and contribute to the network. Phat Contract’s tokenomics focus is on computing resource allocation.

Here is the structure diagram of Phala’s demand end - Phat Contract’s tokenomics, you can easily understand how it works.

| Layers       | Characters           | Functions                                                                                                                                                                                                                                                               |
| ------------ | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First Layer  | Clusters & Workers   | Allocates the network’s computing resources across different clusters. Here, Phala employs a staking-based approach.                                                                                                                                                    |
| Second Layer | Clusters & Contracts | Clusters allocate their computing power to the jobs that they receive from their end-users. The particular allocation mechanism at this stage is mostly left to the cluster owners. Phala provides a default staking-based implementation for the public good clusters. |

### Demand-end <a href="#demand-end" id="demand-end"></a>

#### **First layer**

Adding up the performance scores across all workers in the network as $P$, where the performance score of a worker is proportional to the number of computations that the worker can handle per minute.

* Let $P$ be the total computing power in the network that may be distributed;
* Phala network reserves a fraction $$0 ≤ α ≤ 1$$ of the total computing power $$P$$ for end-users to deploy general Phat contracts;
* Each cluster owner needs to stake PHA to obtain the computing power in the network;
* Time is divided into eras, in each era $$t$$, the computing power reserved for clusters is proportional to the percentage of the stake amount of each cluster in total StakePool;
* The reserved computing power $$P_i$$ for contract cluster $$i$$ then translates into a list of specific workers to which contract cluster $$i$$ can upload its code.

For example, assume there is 100,000 PHA in StakePool, which are staked by Cluster A (50,000 PHA), Cluster B (30,000 PHA), and Cluster C (20,000 PHA). The mechanism of the first layer will allocate the whole computing power as 5:3:2 to Cluster A, B, and C. Then the mechanism will package workers as collections with fixed performance scores that match with clusters' needs randomly and assign the worker collections to Cluster A, B, and C. Each worker in the corresponding cluster can get the same share of computing power as the cluster to which it belongs.

Staking happens through a dedicated staking module to which all PHA holders can contribute. The module might have a cap on the total stake above which no further stake is accepted. The developer can dynamically adjust this cap, and:

* A cluster can remain funded forever
* End-users can take out their stakes at any time after the unbending period

#### **Second Layer**

Once the individual clusters are allocated with their workers, the clusters need to allocate the jobs from their end-users to the respective workers. Cluster owners have full discretion on job allocation.

So far, the second layer is not yet fully operational, but Phala suggests a reverse-fee model on this layer. Under this model:

* Cluster $$i$$ may require their users to pay PHA, fiat, or their own cluster token CTO to use their services.
* End-users are free to choose the amount, and the amount determines the weight that the worker attaches to a call of the contract when scheduling the incoming jobs.

Clusters may keep lists of authorized users that can call contracts for free. In any case, the cluster developer will be able to build a set of controlling contracts to approve or deny the contract deployment and execution requests based on their individual rules.

> As the cluster owner for all public good clusters, the Phala team will follow the second model in these clusters. Refer to the [leading section](broken-reference) for more details.

### Clusters - Workers Matching <a href="#clusters---workers-matching" id="clusters---workers-matching"></a>

#### **What’s the problem**

Once clusters $i$ are allocated with their respective computing power $P$, the workers need to be allocated to the individual clusters.

For an allocation $A\_t$ to be feasible, each worker must be matched with exactly one cluster.

The Phala Cluster-to-Worker matching algorithm seeks to find among the feasible allocations an allocation that maximizes the allocated computing power to the different clusters subject to their budget constraints.

#### **Basic matching method**

Phala implements an algorithm that provides a solution to this problem, in addition, takes into account that the clusters might have preferences over the allocations satisfying:

* Each worker must be matched with exactly one cluster
* Maximizes the allocated computing power to the different clusters subject to their budget constraints

The algorithm proceeds as follows:

At the beginning of each era, each contract cluster is presented with an ordered list of all available workers, $$L_{it} = {\ell_{it1}, …., \ell_{itm_t} }$$. That is each element in $$L_{it}$$ is unique and satisfies $$\ell_{itk} \in{1,…m_t}$$. For every contract cluster, the order of the list is drawn randomly yet the contract clusters are free to rearrange the list as they please.

The algorithm,

* First, it rearranges the different contract clusters so that their stakes are ordered; i.e., $$S_{1t}\ge S_{2t}\ge S_{3t}\ge …S_{n_tt}$$, where contract clusters with identical stakes are ordered randomly.
* Then, the algorithm goes through the contract clusters in decreasing order of their stakes and assigns them to their most preferred workers that have not been assigned before and that are still in their budget set.
* **What if a worker doesn’t match with any contract clusters?**
  * As every contract cluster has all workers on its list, all contract clusters will be matched to some workers and the algorithm stops as soon as the least-staked contract cluster is assigned its workers. The workers that remain unmatched after this last step are then matched to the Phala contract cluster for general Phat contracts.
* **Changing Factors**
  * New clusters
    * The resulting allocation will be the same from era to era, if the set of workers, the set of clusters, and their stakes do not change, and the developers submit the same preferences. If another cluster comes in at some point, then we want to reallocate workers without changing the overall allocation too dramatically. The design proposed above ensures that the more you stake the less you are affected by such a new entry.
    * In particular, if the new entrant at $$t + 1$$ has a stake of size $$\hat s$$, then the budget of all remaining clusters is scaled, yet this rescaling is less dramatic the more stake a cluster holds and the remaining clusters $$i$$ for which $$s_{it} > \hat s$$ holds still get their most preferred workers (up to their new budget).
  * Fake clusters
    * One might also be worried about workers trying to manipulate their popularity measure by registering fake clusters. The algorithm prevents this by _**giving preference to higher-staked clusters over lower-staked ones**_, making such manipulation attempts costly. In particular, it is the function $$g(.)$$, discussed in the next section, that can be used to steer how much the popularity of a worker affects its pay. So, if there is reason to worry that manipulations occur, $$g(.)$$ can in principle be changed at any time by governance to a function that does not change very much in its argument.

### Supply End - Worker Side <a href="#supply-end---worker-side" id="supply-end---worker-side"></a>

The remuneration of a worker depends on the security of the TEE, the computing power that it contributes to the network, and its general popularity.

The former is objectively measurable, and the latter is determined based on the lists that the clusters submit to the matching algorithm.

To enhance Workers’ competitiveness in the system, here are several metrics that impact workers:

#### **Popularity**

* `Points` - we assign points to a worker according to the ranks that he takes in these lists. Specifically, we give $$m_t$$ points to the first worker on a list, $$m_t − 1$$ to the second, and so on.
* `Lists` - To measure the popularity of a worker in an era $$t$$, we collect the lists $${L_{it}}$$$$n_t\atop i=1$$ that the clusters submit to the cluster-worker matching algorithm.

#### **Security and computing power**

* We measure `the security of a worker` from the Remote Attestation report from Intel and denote it by $$C ≥ 0$$ in the following, meaning that a higher $$C$$ corresponds to higher confidence in the worker.
* `The computing power of a worker` is measured by the variable $$P ≥ 0$$, meaning that a higher $$P$$ corresponds to better performance.

#### **Stake**

Workers that want to become active have to put down a stake $$S ≥ 0$$. The stake may depend on the security and the computing power of a worker.

#### **Slashing**

If a worker misbehaves, the worker gets slashed. Depending on the severity of misbehavior, the slash may take on different sizes. The specifics of the slashing scheme are subject to governance. Let $$s_{it} ≥ 0$$ be the slash that is applied to worker $$i$$ in era $$t$$.

#### **Remuneration**

Worker remuneration is tracked via a so-called `value promise`, $$V_t ≥ 0$$.

* When a Worker becomes active, in round $$t = T$$, its initial value is zero.
* Then, in every round $$t ≥ T$$ in which the Worker is still active, the value promise is increased by $$*f(C, P)+g(b_{it})*$$, where $$*f(., .)*$$ and $$*g(.)*$$ are increasing in their respective arguments.

The specific functional forms of $$f$$ and $$g$$ are subject to governance.

**a.) Intermediate payouts**

A worker can always request an intermediate payout.

Let $$w_{it} ≥ 0$$ be the intermediate payout of bidder $$i$$ in round $$t$$. The intermediate payout may never be greater than the value promise in that round net of the slashes and payouts in earlier rounds:

$$w_it ≤ \displaystyle\sum_{τ=\underline{T}}^{t} [f(C,P) + g(b_{iτ}) − s_{iτ} ] − \displaystyle\sum_{τ=\underline{T}}^{t-1} w_{iτ}$$.

Because $$w_{it} ≥ 0$$, the above condition implies that, as soon as the slashes exceed the value promise net of previous payouts, no new payouts can be requested.

**b.) Final payout**

A worker can stay in the StakePool either until his stake plus value promise net of slashes and payouts becomes negative, or until he decides to leave.

That is, a worker will be excluded from the StakePool in time $$T$$ if and only if

$$S +\displaystyle\sum_{t=\underline{T}}^{\overline{T}} [f(C, P) + g(b_{it}) − s_{it} − w_{it}] ≤ 0$$.

If, on the other hand, a worker decides to leave the set of active workers, he receives a final payout, $$W$$.

If a worker leaves in period $$t = T$$, then the final payout amounts to

$$W = S + \displaystyle\sum_{t=\underline{T}}^{\overline{T}} [f(C, P) + g(b_{it}) − s_{it} − w_{it}]$$.
