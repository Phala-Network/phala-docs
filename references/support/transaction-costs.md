---
description: >-
  This page describes the costs to interact with low level Phat Contract (rust
  sdk). It may not reflect that in a higher level (e.g. Javascript-based Phat
  Contract).
---

# Transaction Costs

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

\
There are two types of the costs when interacting with a low level Phat Contract. The both costs may occur in transaction execution. Query is always free to user.

## Concepts

### Storage Deposit

Storage Deposit is charged for every added byte stored in the cluster (contract storage). Correspondingly, when you free some bytes from the storage, you can get refunded at the same rate. Now the rate is fixed at around 1 PHA per kbyte. (See [#parameters](transaction-costs.md#parameters "mention") for details.)

### Ink Gas Fee

The gas fee is charged for every gas used to execute on-chain transaction. Typically a transaction takes less than 1 PHA.

Like EVM, the executed code in a transaction is measured by the virtual machine in a unit called `gas`. (`weight` in ink terminology). You must pay the gas fee calculated by `gas * gasPrice` to execute the transaction. Currently, `gasPrice` is a constant. (See [#parameters](transaction-costs.md#parameters "mention") for details.)

### Fee Structure

The total fee required is defined by the sum of the gas fee and the storage deposit (could be negative):

```
fee = gas * gasPrice + storageDeposit
```

### Storage Deposit Limit and Gas Limit

It's hard to predict how much fee will be charged before actually executing the transaction. So Phat Contract requires you to specify a limit to the gas and Storage Deposit. It ensures you will never pay more than expectation.

You need to specify `gasLimit` and `storageDepositLimit` when sending a transaction, which can be estimated by an estimation API. Then the max fee is defined below:

```
maxFee = gasLimit * gasPrice + storageDepositLimit
```

The VM charges you `maxFee` before executing a transaction. Once executed, the VM will refund the remaining fee to your account (`maxFee - fee`).  If the transaction runs out of the gas or Storage Deposit, the transaction will be revered with an error (`OutOfGas` or `StorageDepositLimitExhausted`).

## Transaction

A typical transaction takes less than 1 PHA, unless you store large chunk of data in the storage.

A regular transaction may involve gas fee and storage deposit. The gas fee (`gas * gasPrice`) is usually less than 1 PHA. The storage deposit fee is a bit more complex.

When you add an entry to the contract storage like below, you will be charged a small storage deposit. It takes a few bytes to store the key and the value.

```rust
fn set(&mut self) {
  // If the kv takes 50 bytes storage, the deposit would be 0.05 PHA.
  self.a_map.insert("key".to_string(), "value".to_string())
}
```

However, you may also remove the storage item like below. In this case, the caller will get a refund as the storage deposit.

```rust
fn clear(&mut self) {
  // If the kv takes 50 bytes storage, the refund would be 0.05 PHA.
  self.a_map.remove("key".to_string())
}
```

## Contract Deployment

Deploy (instantiate in ink terminology) a contract may take anywhere from <0.1 PHA to >1000 PHA.

In low level Phat Contract, you need to upload the WASM code to the storage before instantiating it. Usually the uploading step takes much more than instantiation.

{% hint style="info" %}
The uploaded code takes twice the space in the storage. For example, if you upload a 500kb WASM file, it stores around 1mb file in the storage. You will need to pay 1000 PHA as the storage deposit.
{% endhint %}

Once the code is uploaded, you can instantiate the contract with the code hash. The VM will call the constructor function to initialize the contract. This step happens in the same way as executing a transaction. It will charge you gas fee as usual. It may also charge you additional storage deposit, if you write to the storage in the constructor.

Typically, you pay a relatively large storage deposit for uploading, and a small gas fee for instantiating. However, sometimes you may deploy existing contracts. So you only pay a minor fee in the instantiating step, not the uploading step.

{% hint style="info" %}
It's possible to free the storage deposit for uploaded contracts, but it's a rare case in the reality. Every uploaded code has a reference counter. If there's no contract instance referring your code, you can get the storage deposit back. To terminate a contract to reduce the reference, call `env.terminate_contract()` ([doc](https://docs.rs/ink_env/latest/ink_env/fn.terminate_contract.html))
{% endhint %}

## Parameters

```
gasPrice = 5
depositPerByte = 1 * PHA/KB = 1.000953674316 PHA
depositPerItem = 0.030517578125 PHA
```
