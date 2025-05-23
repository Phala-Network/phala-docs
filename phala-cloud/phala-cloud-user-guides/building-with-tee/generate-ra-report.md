# Generate Remote Attestation

The cloud will generate a default RA report for your application when it is bootstrapped. You can view this report on the dashboard under the **Attestation** tab and verify it by clicking the **Check** **Attestation** button.

<figure><img src="../../../.gitbook/assets/cloud-cert-chain.png" alt="cert-chain"><figcaption></figcaption></figure>

There are two steps needed to generate a new RA report, rather than using the default one, which allows you to prove the execution of your code.

### Config docker compose file

This Docker Compose file spins up a Jupyter Notebook environment, and importantly, it's configured the `volumes` to connect to the Dstack API by mounting its socket file (`/var/run/tappd.sock`) into the container. This allows the Jupyter Notebook running inside the TEE to interact with the Dstack service like generate a remote attestation, get a TLS key, or generate a key for chains like ETH (`ECDSA, K256 curve`) or SOL (`ed25519`).

For development convenience, this setup grants sudo privileges inside the container (`environment`), runs the Jupyter server with root user permissions (`user`), and starts the notebook with token-based authentication using the `TOKEN` environment variable (`command`).

```yaml
version: '3'
services:
  jupyter:
    image: quay.io/jupyter/base-notebook
    ports:
      - 8080:8888
    volumes:
      - /var/run/tappd.sock:/var/run/tappd.sock
    environment:
      - GRANT_SUDO=yes
    user: root
    command: "start-notebook.sh --NotebookApp.token=${TOKEN}"
```

### Generate RA report inside your application code

In your application, you can generate the RA report using the [Dstack SDK](https://www.npmjs.com/package/@phala/dstack-sdk?activeTab=readme), which supports Python, JS, and Go. The `user-data` argument allows you to attach your own data to the RA report.

```javascript
import { TappdClient } from '@phala/dstack-sdk';

const client = new TappdClient();

// Show the information of the Base Image.
await client.info();

// Get a TDX quote for the given custom data and hash algorithm.
const quoteResult = await client.tdxQuote('user-data', 'sha256');
console.log(quoteResult.quote); // TDX quote in hex format
console.log(quoteResult.event_log); // Event log
const rtmrs = quoteResult.replayRtmrs(); // Replay RTMRs
```

You can implement the above code in your application as an public API that anyone can call to generate a new RA report.

### Conclusion

In practice, this is a method to bind the RA report to your application. For example, you can generate a key pair and set the public key as the `user-data`. This way, anyone can verify the execution of your application by extract the public key from the RA report and checking the signature with the public key.
