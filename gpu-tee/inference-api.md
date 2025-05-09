# 🔐 GPU TEE Inference API

Phala Cloud provides LLM inference API by connecting to Redpill. By navigating to **Dashboard**->**GPU TEE API** page, you will see details.

## Enable API Service

In order to use the API, **user needs to deposit at least $5 in advance to enable a Redpill account** if your balance is not sufficient. You can head to **Dashboard**->**Billing** page then click **Deposit** button to top-up with your bank card or crypto wallet.

<figure><img src="../.gitbook/assets/gpu-tee-api.png" alt=""><figcaption></figcaption></figure>

## Generate API Key

At the bottom of the page, click the **Enable** button to connect your Cloud account with a Redpill account, and then click the button **Create New API Key**. Copy the key to use when you interact with Redpill API.

<figure><img src="../.gitbook/assets/gpu-tee-api-generate-key.png" alt=""><figcaption></figcaption></figure>

[Redpill](https://red-pill.ai/) is a models marketplace that supports private AI inference. It currently supports two models that are running in GPU TEE, you can view them in the models page by clicking the `GPU TEE` checkbox:

* [**DeepSeek: R1 Distill 70B**](https://red-pill.ai/models/phala/deepseek-r1-70b)
* [**Meta: Llama 3.3 70B Instruct**](https://red-pill.ai/models/phala/llama-3.3-70b-instruct)

<figure><img src="../.gitbook/assets/models-in-tee.png" alt=""><figcaption></figcaption></figure>

## Chat With Private AI

We provide OpenAI-compatible API for you to send chat requests to the LLM running inside TEE, where you just need to use the API endpoint `https://api.red-pill.ai/v1/chat/completions`. A simple request could be like:

```sh
curl -X 'POST' \
  'https://api.red-pill.ai/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <The API Key you generated previously>' \
  -d '{
  "messages": [
    {
      "content": "You are a helpful assistant.",
      "role": "system"
    },
    {
      "content": "What is your model name?",
      "role": "user"
    }
  ],
  "stream": true,
  "model": "phala/deepseek-r1-70b"
}'
```

**Sample Response**

```sh
...

data: {"id":"chatcmpl-0cdf7629fcfa4135bbdb9936e737e95c","object":"chat.completion.chunk","created":1740415146,"model":"/mnt/models/deepseek-r1-70b/deepseek-r1-70b.guff","choices":[{"index":0,"delta":{"content":""},"logprobs":null,"finish_reason":"stop","stop_reason":128001}]}

data: [DONE]
```

## Get TEE Attestation Report

You can verify if the LLM is running in GPU TEE. This can be done by verifying its attestation report. To get the attestation report of the LLM inference, you can do this by sending a POST request to the Redpill API endpoint like below:

```sh
curl 'https://api.red-pill.ai/v1/attestation/report?model=phala/deepseek-r1-70b' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <The API Key you generated previously>'
```

The response will be like:

```sh
{
  "signing_address": "...",
  "nvidia_payload": "...",
  "intel_quote": "...",
  "all_attestations": [
    {
      "signing_address": "...",
      "nvidia_payload": "...",
      "intel_quote": "..."
    }
  ]
}
```

The `signing_address` is the account address generated inside TEE that will be used to sign the chat message later.

The `all_attestations` is the list of all the attestations of all GPU nodes since we add more TEE nodes to serve the inference requests. You can utilize the `signing_address` from the `all_attestations` to select the appropriate TEE node for verifying its integrity.

## Verify Attestation Report

### Verify GPU Attestation Report

You can copy the value of nvidia\_payload as the whole payload as followed to verify:

```sh
curl -X POST https://nras.attestation.nvidia.com/v3/attest/gpu \
 -H "accept: application/json" \
 -H "content-type: application/json" \
 -d "<NVIDIA_PAYLOAD_FROM_ABOVE>"
```

### Verify TDX Attestation Report

You can verify the Intel TDX Attestation Report, aka quote with the value of `intel_quote` at [TEE Attestation Explorer](https://proof.t16z.com/).

The `signing_address` is the account address generated inside TEE that will be used to sign the chat response. You can go to https://etherscan.io/verifiedSignatures, click Verify Signature, and paste the `signing_address` and message response to verify it.

`nvidia_payload` and `intel_quote` are the attestation report from NVIDIA TEE and Intel TEE respectively. You can use them to verify the integrity of the TEE. See Verify the Attestation for more details.

> Note: The trust chain works as follows: when you verify the attestation report, you trust the model provider (Redpill) and the TEE providers (NVIDIA and Intel). You then trust the open-source, reproducible code by verifying the source code [here](https://github.com/nearai/private-ml-sdk). Finally, you trust the cryptographic key derived inside the TEE. This is why we only need to verify the signature of the message during chat.

## Verify Chat Signature

If you chat with the LLM, the response will contain an `id` which you can use to get the chat Signature later.

**Sample Request**

```sh
curl -X 'POST' \
  'https://api.red-pill.ai/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <REDPILL_API_KEY>' \
  -d '{
  "messages": [
    {
      "content": "You are a helpful assistant.",
      "role": "system"
    },
    {
      "content": "What is your model name?",
      "role": "user"
    }
  ],
  "stream": true,
  "model": "phala/deepseek-r1-70b"
}'
```

That sha256 of the request body is **e5542b0757e0b9d05bfa4a15da7bac97a03bd35d21b648ec492152708e795ff9**

(note: in this example, there is no new line in the end of request)

**Simple Response**

```
...

data: {"id":"chatcmpl-0cdf7629fcfa4135bbdb9936e737e95c","object":"chat.completion.chunk","created":1740415146,"model":"/mnt/models/deepseek-r1-70b/deepseek-r1-70b.guff","choices":[{"index":0,"delta":{"content":""},"logprobs":null,"finish_reason":"stop","stop_reason":128001}]}

data: [DONE]
```

The sha256sum of response body is 7a97926adb2044fd598b392eee98ad8f7c39ea3a47747ca968ef755bbf57c211

(note: in this example, there are two new line in the end of response)

The `id` is calculated by sha256sum(sha256sum(request\_body) + sha256sum(response\_body)).

### Request Chat Signature

By default, you can query another API with the value of id in the response in 30 minutes.

Request\
GET `https://api.red-pill.ai/v1/signature/{request_id}?model={model_id}&signing_algo=ecdsa`

For example, the response in the previous section, the id is `chatcmpl-0cdf7629fcfa4135bbdb9936e737e95c`:

**Response**

```sh
{
  "text": "e5542b0757e0b9d05bfa4a15da7bac97a03bd35d21b648ec492152708e795ff9:7a97926adb2044fd598b392eee98ad8f7c39ea3a47747ca968ef755bbf57c211",
  "signature": "faf0316a4860fd3d412cb5851b55687edc31f5600b4667502cf32112e1ad533b5d6420beb1fd7002334a46d897e11347837675bc01982485e00549091b06f8a81b",
  "signing_algo": "ecdsa"
}
```

* text: the message you may want to verify. It is joined by the sha256 of the HTTP request body, and of the HTTP response body, separated by a colon :.
* signature: the signature data.
* signing\_algo: The cryptographic scheme that the signer private key generated.

Exactly match the value we calculated in the sample in previous section.

**Limitation**

Since the resource limitation, the signature will be kept in the memory for 5 minutes since the response is generated.

### Verify Signature on etherscan

Go to https://etherscan.io/verifiedSignatures, click Verify Signature:

* Address: You can get the address from the attestation API. The address should be same if the service did not restart.
* Message: see the Response of the Signature section. You can also calculate the sha256 by yourself.
* Signature Hash: See the Signature section.

<figure><img src="../.gitbook/assets/gpu-tee-api-verify-signature.png" alt=""><figcaption></figcaption></figure>
