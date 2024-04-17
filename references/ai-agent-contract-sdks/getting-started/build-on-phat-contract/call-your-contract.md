# Call Your Contract

## Query and Transaction <a href="#query-and-transaction" id="query-and-transaction"></a>

You can call your Phat Contract in two ways: on-chain _transactions_ and off-chain _queries_. A Phat contract supports both types of input, but they are very different.

We recommend using more queries in your contracts and only using the transactions to set some important configurations. This is because many unique features of Phat Contract are only available in query handler functions.

|                       | Transaction | Query |
| --------------------- | ----------- | ----- |
| Encrypted             | ✅           | ✅     |
| Posted on chain       | ✅           | ❌     |
| Direct to worker      | ❌           | ✅     |
| Read contract state   | ✅           | ✅     |
| Change contract state | ✅           | ❌     |
| No gas fee            | ❌           | ✅     |
| Latency               | 6s          | 0s    |
| Deterministic         | ✅           | ❌     |
| Internet Access       | ❌           | ✅     |

## Handle Query and Transaction <a href="#handle-query-and-transaction" id="handle-query-and-transaction"></a>

Despite the obscure underlying mechanism, from the code side, handling the queries and transactions can be really easy in Phat Contract.

```
#[ink(message)]
pub fn query_handler(&self, arg1: AccountId, arg2: u32) {
    // actual implementation
}

#[ink(message)]
pub fn transaction_handler(&mut self, arg1: AccountId, arg2: u32) {
    // actual implementation
}
```

In Phat Contract, defining a user request handler is as simple as labeling a function with `#[ink(message)]`. The only difference between a transaction handler and a query handler is how they refer to the contract state:

* Query handler holds immutable reference `&self`, they can read the current contract states but should not change them;
* Transaction handler holds mutable reference `&mut self`, so they are allowed to update the contract states.

### Available Functionalities <a href="#available-functionalities" id="available-functionalities"></a>

Phat Contract has unique capabilities, and they are provided as functions in [pink-extension](https://github.com/Phala-Network/phala-blockchain/tree/master/crates/pink) (short for Phala ink! Extension). You can use all these functions in your query handler functions, but some of them are disabled in transaction handlers since they can lead to inconsistent on-chain states.

Check the detailed list in the following [section](broken-reference).

## Learn More about Query <a href="#learn-more-about-query" id="learn-more-about-query"></a>

For all existing smart contracts, a user needs to send a transaction on-chain and wait for it to be processed by the contract.

The most significant difference between Phat Contract and other smart contracts is that it runs off-chain. This enables it to directly receive and process users' off-chain requests (called _Query_), other than the traditional on-chain transactions. For the first time, you can process these two kinds of requests in one contract.

> If you do not know what’s transaction and how they are processed in traditional smart contracts, refer to [Ethereum’s introduction on smart contract](https://ethereum.org/en/developers/docs/smart-contracts/). The transactions are processed in exactly the same way in Phat Contract.

<figure><img src="../../../../.gitbook/assets/general-node-design.png" alt=""><figcaption></figcaption></figure>

Since queries are never submitted on-chain, it has unique features compared with transactions:

* it is never recorded on-chain, thus volatile. So query handling logic is not allowed to change the contract states on-chain (but you are free to read these states when processing queries);
* it requires no gas fee for users to send queries to a contract;
* there is zero latency in query processing since it does not need to wait for block production.

Both the advantages and disadvantages of the query are clear:

* Pros: Query removes the performance and functional limitations on transaction processing, while still able to read the contract states;
* Cons: You need to be extremely careful when you allow queries to affect your contract states since concurrent query handling can lead to unexpected execution results.

That’s why we choose to start with stateless DApp building: it totally avoids the weakness of the query. We leave the stateful application building as an advanced topic.
