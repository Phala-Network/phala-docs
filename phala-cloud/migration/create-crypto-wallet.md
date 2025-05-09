# Create Crypto Wallet

You can derive a deterministic key using the [Dstack SDK](https://www.npmjs.com/package/@phala/dstack-sdk?activeTab=readme) inside Docker. Under the hood, the `TappdClient` derives the key from the application root key.

```javascript
import { TappdClient } from '@phala/dstack-sdk';

const keyResult = await client.deriveKey('<unique-id>'); // Same unique-id will get same key
console.log(keyResult.key); // X.509 private key in PEM format
console.log(keyResult.certificate_chain); // Certificate chain
const keyBytes = keyResult.asUint8Array(); // Get key as Uint8Array
```

## Derive wallet using viem

DStack SDK provides a helper function to derive a [viem](https://viem.sh) compatible wallet.

```javascript
import { toViemAccount } from '@phala/dstack-sdk/viem';

const keyResult = await client.deriveKey('<unique-id>'); // Same unique-id will get same key
const account = toViemAccount(keyResult);
// Use the account with viem operations
```

## Derive Solana Wallet

If you want to derive a Solana wallet, you can use the following code that derive a Solana wallet based on [Solana Web3.js](https://solana-labs.github.io/solana-web3.js/).

```javascript
import { toKeypair } from '@phala/dstack-sdk/solana';

const keyResult = await client.deriveKey('<unique-id>'); // Same unique-id will get same key
const keypair = toKeypair(keyResult);
```
