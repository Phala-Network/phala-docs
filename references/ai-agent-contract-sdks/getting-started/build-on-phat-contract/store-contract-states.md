# Store Contract States

## Storage Hierarchy

## Overview <a href="#overview" id="overview"></a>

A Phat contract can utilize three kinds of storage solutions: local cache, contract state, and any external storage services with HTTP requests. We list the differences between the two native storage solutions in Phat Contract as follows.

<table><thead><tr><th width="157"></th><th width="109">Persistent</th><th width="113">Consistent</th><th width="221">Transparently Encrypted</th><th>Cost</th></tr></thead><tbody><tr><td>Local Cache</td><td>❌</td><td>❌</td><td>✅</td><td>Zero</td></tr><tr><td>Contract State</td><td>✅</td><td>✅</td><td>✅</td><td>Gas fee</td></tr></tbody></table>

### Local Cache <a href="#local-cache" id="local-cache"></a>

The local cache is stored in the worker’s memory. As its name, it should only be used as a cache since all cached data is not shared across different workers, and can be lost if the worker is down. Also, you may experience unexpected value cleanup if the memory usage of the worker is high.

The cache can be easily accessed in [Pink extension](use-pink-extension.md). You can read and write cache in query handlers, but reading cache in transaction handlers is forbidden: the result of cache reading is nondeterministic.

```rust
use pink::chain_extension::pink_extension_instance as ext;

#[ink(message)]
pub fn test(&self) {
    assert!(ext().cache_set(b"key", b"value").is_ok());
    assert_eq!(ext().cache_get(b"key"), Some(b"value".to_vec()));
    assert_eq!(ext().cache_remove(b"key"), Some(b"value".to_vec()));
    assert_eq!(ext().cache_get(b"key"), None);
}
```

### Contract State <a href="#contract-state" id="contract-state"></a>

Here is how you store simple values as your contract state:

```rust
#[ink(storage)]
pub struct MyContract {
    // Store a bool
    my_bool: bool,
    // Store some number
    my_number: u32,
}
```

Unlike other ink contracts in which such values are stored publicly on-chain, in Phat Contract, all your contract state is transparently encrypted for you.

> Technically speaking, your Phat contract state is not persistently stored anywhere (not even on chain). In Phat contract, any transaction handler functions must be deterministic, so any worker can restore the contract state by replaying all the historical transactions in order (since they are stored on chain). Such design is called Event Sourcing and you can learn more about it in Section 2.2 of our [whitepaper](https://files.phala.network/phala-paper.pdf).

#### External Storage Services <a href="#external-storage-services" id="external-storage-services"></a>

With its HTTP support, you can connect to any storage services you like in your Phat contract.

For simple key-value storage, [pink-s3](https://crates.io/crates/pink-s3) enables you to store data in any storage service with S3-API support.

```rust
fn s3_example() {

    use pink_s3 as s3;

    let endpoint = "s3.ap-southeast-1.amazonaws.com";
    let region = "ap-southeast-1";
    let access_key = "<Put your S3 access key here>";
    let secret_key = "<Put your S3 access secret key here>";

    let s3 = s3::S3::new(endpoint, region, access_key, secret_key)
        .unwrap()
        .virtual_host_mode(); // virtual host mode is required for newly created AWS S3 buckets.

    let bucket = "my-wallet";
    let object_key = "path/to/foo";
    let value = b"bar";

    s3.put(bucket, object_key, value).unwrap();

    let head = s3.head(bucket, object_key).unwrap();
    assert_eq!(head.content_length, value.len() as u64);

    let v = s3.get(bucket, object_key).unwrap();
    assert_eq!(v, value);

    s3.delete(bucket, object_key).unwrap();

}
```

Such storage service providers include:

* [Amazon S3](https://aws.amazon.com/s3/) - 5GB, 12 months free
* [4everland](https://www.4everland.org/bucket/) - 5GB free on IPFS and 100MB Free on Arweave
* [Storj](https://www.storj.io/) - 150GB free
* [Filebase](https://filebase.com/) - 5GB free

If you want a relational database like MySql, you can also use DBaaS services like

* [PingCap](https://www.pingcap.com/), which is based on TiDB
