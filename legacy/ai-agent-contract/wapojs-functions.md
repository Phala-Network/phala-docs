# WapoJS Functions

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

Here is a list of the available functions for developers to utilize when building on the AI Agent Contract.

```typescript
/**
* Derives a secret key from a salt. The same app with the same salt on the same worker will always
* derive the same secret. However, the same app with the same salt on different workers will derive
* different secrets.
*/
deriveSecret(salt: Uint8Array | string): Uint8Array;

/**
* Hashes a message using the specified algorithm.
* @param algrithm - The name of the hash algorithm to use.
*    Supported values are "blake2b128", "blake2b256", "blake2b512", "sha256", "keccak256"
* @param message - The message to hash, either as a Uint8Array or a string.
*/
hash(algrithm: 'blake2b128' | 'blake2b256' | 'blake2b512' | 'sha256' | 'keccak256', message: Uint8Array | string): Uint8Array;

/**
* Non-cryptographic hashing, current only supported wyhash64 64-bit hash. Non-cryptographic algorithms
* are optimized for speed of computation over collision-resistance or seurity.
*
* @param algrithm - The name of the hash algorithm to use.
*    Supported values are "wyhash64"
* @param message - The message to hash, either as a Uint8Array or a string.
*/
nonCryptographicHash(algrithm: 'wyhash64', message: Uint8Array | string): Uint8Array;

/**
* Concatenates multiple Uint8Array objects into a single Uint8Array.
*
* @param arrays - The arrays to concatenate.
*/
concatU8a(arrays: Uint8Array[]): Uint8Array;
```
