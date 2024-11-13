# Start From Scratch

This tutorial will step you through setting up a project from scratch with Dstack SDK. The following have a couple ways to get started with

* Create a next.js application written in JavaScript
* Build a Python backend application

{% hint style="info" %}
### Before You Start

Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) or [OrbStack](https://orbstack.dev/) started before you begin.
{% endhint %}

{% tabs %}
{% tab title="next.js" %}
## Installation

For this example, we will be starting from scratch and will need to generate a new project. For simplicity, I will use a template for a next.js docker app.

```bash
npx create-next-app --example with-docker nextjs-docker
```

This should create a new project called `nextjs-docker` in the current working directory. Now let's add the `@phala/dstack-sdk` to the project along with `viem` and `dotenv` to get our project compatible with the TEE simulator.

```
npm install @phala/dstack-sdk viem dotenv
```

## Make Calls to Dstack SDK Functions

Now that we have the packages installed, we can begin to configure our existing project to make calls to the `deriveKey(path, data)` and `tdxQuote(data)`functions in the Dstack SDK.

### Edit Dockerfile

First lets make 1 small change to the `Dockerfile` and add the line to line 66 in the file.

```docker
ENV DSTACK_SIMULATOR_ENDPOINT="http://host.docker.internal:8090"
```

Next, lets create the API calls for both of the functions.

### Create API Calls

Create 2 new files called `derivekey.js` `tdxquote.js` in the `pages/api/` folder.

```bash
touch ./pages/api/derivekey.js
touch ./pages/api/tdxquote.js
```

You should now have 2 empty files in the directory, and run `ls ./pages/api` to verify the files were created.

```bash
ls pages/api 
total 24
drwxr-xr-x  5 hashwarlock  staff   160B Nov  7 14:51 .
drwxr-xr-x  5 hashwarlock  staff   160B Nov  7 14:47 ..
-rw-r--r--@ 1 hashwarlock  staff   892B Nov  7 15:01 derivekey.js
-rw-r--r--  1 hashwarlock  staff   169B Nov  7 14:00 hello.js
-rw-r--r--@ 1 hashwarlock  staff   604B Nov  7 15:05 tdxquote.js
```

Now that the API calls are created, let's implement the `api/derivekey` function first. We can copy and paste the following code snippet to generate a random ECDSA Keypair.

```typescript
// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import {TappdClient} from '@phala/dstack-sdk'
import { privateKeyToAccount } from 'viem/accounts'
import {keccak256} from "viem";
import 'dotenv/config'

export const dynamic = 'force-dynamic'

const endpoint = process.env.DSTACK_SIMULATOR_ENDPOINT || 'http://localhost:8090'

export default async function hello(req, res) {
    // Get the Tappd client
    const client = new TappdClient(endpoint)
    const randomNumString = Math.random().toString();
    // Call the deriveKey function and pass random data as parameters
    const randomDeriveKey = await client.deriveKey(randomNumString, randomNumString);
    // Hash the derivedKey uint8Array value
    const keccakPrivateKey = keccak256(randomDeriveKey.asUint8Array());
    // Get the private key account from the derived key hash
    const account = privateKeyToAccount(keccakPrivateKey);
    // Return derived key pair
    res.status(200).json({account: account.address, privateKey: keccakPrivateKey});
}
```

Let's move to implementing the `api/tdxquote` API call with the following snippet of code.

```typescript
// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import {TappdClient} from '@phala/dstack-sdk'
import 'dotenv/config'

export const dynamic = 'force-dynamic'

const endpoint = process.env.DSTACK_SIMULATOR_ENDPOINT || 'http://localhost:8090'

export default async function hello(req, res) {
    // Get Tappd client
    const client = new TappdClient(endpoint)
    const randomNumString = Math.random().toString();
    // Generate Remote Attestation Quote based on a random string of data
    const getRemoteAttestation = await client.tdxQuote(randomNumString);
    // Return Remote Attestation result
    res.status(200).json({ getRemoteAttestation });
}
```

Now that these API calls are done, we can start with the fun of testing this locally.

## Testing Locally

With the basic implementation done, let's do a quick test to see if the code works by building the docker image and testing locally.&#x20;

```bash
docker build -t my-nextjs-app:latest .
```

Now that the docker image is built, let's start testing against the TEE Simulator. First we must pull the latest TEE Simulator in docker, and run it with the following commands.

```bash
docker pull phalanetwork/tappd-simulator:latest
docker run --rm -p 8090:8090 phalanetwork/tappd-simulator:latest
```

With the simulator up and running, we can now start our docker app to test out the functionality.

```bash
docker run --rm -p 3000:3000 my-nextjs-app:latest
```

Now we can go to `http://localhost:3000` and see our deployed application.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### Call the APIs

We can test to see if our functions work by calling the API calls with

* http://localhost:3000/api/derivekey
* http://localhost:3000/api/tdxquote

We should see the results similar to the following screenshots.

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption><p>/api/derivekey</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption><p>/api/tdxquote</p></figcaption></figure>
{% endtab %}

{% tab title="backend" %}
For the python example, we will take an existing tutorial from Docker docs [https://docs.docker.com/guides/python/containerize/](https://docs.docker.com/guides/python/containerize/) and add Dstack SDK to the project to make calls to the TEE SDK functions.

## Installation

First step is to clone the python application repo.

```bash
git clone https://github.com/estebanx64/python-docker-example.git
```

Now that we have cloned a python repo, let's add the `Dockerfile` with the following contents.

```docker
# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Switch to the non-privileged user to run the application.
USER appuser

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 3000

# Dstack simulator endpoint for local deployments
ENV DSTACK_SIMULATOR_ENDPOINT="http://host.docker.internal:8090"

# Run the application.
CMD python3 -m uvicorn app:app --host=0.0.0.0 --port=3000
```

You can also add a `.dockerignore` file with the following contents.

```ignore
# Include any files or directories that you don't want to be copied to your
# container here (e.g., local build artifacts, temporary files, etc.).
#
# For more help, visit the .dockerignore file reference guide at
# https://docs.docker.com/go/build-context-dockerignore/

**/.DS_Store
**/__pycache__
**/.venv
**/.classpath
**/.dockerignore
**/.env
**/.git
**/.gitignore
**/.project
**/.settings
**/.toolstarget
**/.vs
**/.vscode
**/*.*proj.user
**/*.dbmdl
**/*.jfm
**/bin
**/charts
**/docker-compose*
**/compose.y*ml
**/Dockerfile*
**/node_modules
**/npm-debug.log
**/obj
**/secrets.dev.yaml
**/values.dev.yaml
LICENSE
README.md
```

Now that we have the `Dockerfile` built, let's add the [Python Dstack SDK](https://pypi.org/project/dstack-sdk/) to our python project in `requirements.txt`

```
dstack-sdk==0.1.2
asyncio>=3.4.3
fastapi==0.111.0
```

## Make Calls to Dstack SDK Functions&#x20;

Let's make 2 new API call within the `app.py` file for `derivekey` and `tdxquote`.

```python
import os
from dstack_sdk import AsyncTappdClient, DeriveKeyResponse, TdxQuoteResponse
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "The World! Call /derivekey or /tdxquote"}

@app.get("/derivekey")
async def derivekey():
    client = AsyncTappdClient()
    deriveKey = await client.derive_key('/', 'test')
    assert isinstance(deriveKey, DeriveKeyResponse)
    asBytes = deriveKey.toBytes()
    assert isinstance(asBytes, bytes)
    limitedSize = deriveKey.toBytes(32)
    return {"deriveKey": asBytes.hex(), "derive_32bytes": limitedSize.hex()}
    
@app.get("/tdxquote")
async def tdxquote():
    client = AsyncTappdClient()
    tdxQuote = await client.tdx_quote('test')
    assert isinstance(tdxQuote, TdxQuoteResponse)
    return {"tdxQuote": tdxQuote}
```

Now that these API calls are done, we can start with the fun of testing this locally.

## Testing Locally

With the basic implementation done, let's do a quick test to see if the code works by building the docker image and testing locally.&#x20;

```bash
docker build -t my-python-app:latest .
```

Now that the docker image is built, let's start testing against the TEE Simulator. First we must pull the latest TEE Simulator in docker, and run it with the following commands.

```bash
docker pull phalanetwork/tappd-simulator:latest
docker run --rm -p 8090:8090 phalanetwork/tappd-simulator:latest
```

With the simulator up and running, we can now start our docker app to test out the functionality.

```bash
docker run --rm -p 3000:3000 my-nextjs-app:latest
```

Now we can go to `http://localhost:3000` and see our deployed application.

<figure><img src="../../.gitbook/assets/Screenshot 2024-11-07 at 19.44.10.png" alt=""><figcaption></figcaption></figure>

### Call the APIs

We can test to see if our functions work by calling the API calls with

* http://localhost:3000/api/derivekey
* http://localhost:3000/api/tdxquote

We should see the results similar to the following screenshots.

<figure><img src="../../.gitbook/assets/Screenshot 2024-11-07 at 19.44.26.png" alt=""><figcaption><p>/derivekey</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Screenshot 2024-11-07 at 19.44.41.png" alt=""><figcaption><p>/tdxquote</p></figcaption></figure>
{% endtab %}
{% endtabs %}

## Conclusion

Now you have the skills to start building on the Dstack SDK from scratch. Checkout the other tutorials where we start from a template or integrate the SDK into an existing project. For more info on how to setup your project to be deployed on the real TEE hardware, reach out to the Phala Team for more information.
