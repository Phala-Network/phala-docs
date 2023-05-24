# Use Pink Extension

### Introduction <a href="#introduction" id="introduction"></a>

All the unique capabilities of Phat Contract are implemented in [pink-extension](https://github.com/Phala-Network/phala-blockchain/tree/master/crates/pink). Informally speaking:

$$
Phat\ Contract = ink! + Pink\ Extension
$$

It is worth noting that the Phat Contract is not a trivial extension of ink! contract since all these extra functions only work under the off-chain computation.

### Pink Extension Functions <a href="#pink-extension-functions" id="pink-extension-functions"></a>

| Functionality   | Function Name            | Query Support | Transaction Support |
| --------------- | ------------------------ | ------------- | ------------------- |
| Internet Access | http\_request            | ✅             | ❌                   |
| Crypto          | getrandom                | ✅             | ❌                   |
|                 | ecdsa\_sign\_prehashed   | ✅             | ✅                   |
|                 | ecdsa\_verify\_prehashed | ✅             | ✅                   |
|                 | sign (ecdsa/ed25519)     | ✅             | ✅                   |
|                 | sign (sr25519)           | ✅             | ❌                   |
|                 | verify                   | ✅             | ✅                   |
|                 | derive\_sr25519\_key     | ✅             | ✅                   |
|                 | get\_public\_key         | ✅             | ✅                   |
| Volatile Cache  | cache\_set               | ✅             | ✅                   |
|                 | cache\_set\_expire       | ✅             | ✅                   |
|                 | cache\_get               | ✅             | ❌                   |
|                 | cache\_remove            | ✅             | ✅                   |
| Misc            | log                      | ✅             | ✅                   |
|                 | is\_running\_in\_command | ✅             | ✅                   |

Refer to our [Phat Hello World](https://github.com/Phala-Network/phat-hello/blob/master/lib.rs) contract to see how you can import these functions to your contract.
