# Run a Local Testnet With Docker

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

Run a local testnet with [`docker` support](https://docs.docker.com/desktop/). All you need to do to get a local testnet started is run:

{% hint style="danger" %}
Running the local testnet may return an error if port **`8000`** is already in use.
{% endhint %}

```shell
npm run dev
```

**Make a Request to Your Local Build**

```shell
# GET request
curl http://127.0.0.1:8000/local
# GET request with URL queries
curl http://127.0.0.1:8000/local?query1=one&query2=two
# POST request
curl http://127.0.0.1:8000/local -X POST -H 'content-type: application/json' -d '{"foo": "bar"}'
```

**Add Secrets to Your Local Build**

```shell
curl http://127.0.0.1:8000/vaults -H 'Content-Type: application/json' -d '{"cid": "local", "data": {"secretKey":"secretValue"}}'
```

**Check The Logs of Your Local Build**

```shell
curl 'http://127.0.0.1:8000/logs/all/local'
```
