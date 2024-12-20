# FAQ

This page is dedicated to troubleshooting issues found when building on the AI Agent Contract.

#### 1. Why does my code fail to run a local testnet when executing the commands `npm run start` and `npm run dev`?

For these commands to work, you must have Docker installed on your machine. Check out the [Docker Docs](https://docs.docker.com/) or try installing [Docker Desktop](https://docs.docker.com/desktop/).

#### 2. How do I query my local AI Agent Contract build when running a local testnet?

To interact with your local AI Agent Conract build through a local testnet, you will use the following `curl` commands:

<pre class="language-sh"><code class="lang-sh"><strong># GET request
</strong><strong>curl http://127.0.0.1:8000/local
</strong><strong># GET request with URL queries
</strong>curl http://127.0.0.1:8000/local?query1=one&#x26;query2=two
# POST request
curl http://127.0.0.1:8000/local -X POST -H 'content-type: application/json' -d '{"foo": "bar"}'
</code></pre>

#### 3. How do I add secrets to my AI Agent Contract build when running a local testnet?

Execute the following command to add your secrets. Make sure to set the `cid` key to value `local.`

```sh
curl http://127.0.0.1:8000/vaults -H 'Content-Type: application/json' -d '{"cid": "local", "data": {"secretKey":"secretValue"}}' 
```

#### 4. How do I check the logs of my local testnet?

Logs can be checked by running the following `curl` command:

```sh
curl 'http://127.0.0.1:8000/logs/all/local'
```

You should see your logs outputted in your terminal like below.

```sh
2024-09-14T03:22:05.542Z [82570760-98d3-4dda-9f82-eb69a3a5e79a] [REPORT] END Request: Duration: 222ms
2024-09-14T03:22:05.542Z [82570760-98d3-4dda-9f82-eb69a3a5e79a] [INFO] 'Type: , Data: '
2024-09-14T03:22:05.542Z [82570760-98d3-4dda-9f82-eb69a3a5e79a] [INFO] { secretSalt: 'LOCAL_TEST' }
2024-09-14T03:22:05.542Z [82570760-98d3-4dda-9f82-eb69a3a5e79a] [REPORT] START Request: GET https://127.0.0.1:8000/local?key=2a769684f518edfe
```

For further assistance, refer to the documentation or reach out to the support team.
