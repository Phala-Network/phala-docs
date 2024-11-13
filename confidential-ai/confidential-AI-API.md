# 💎 Confidential AI API

## Overview

1. When the service start, it will generate a signing key in TEE.
2. You can get the CPU and GPU attestation to verify the service is running in Confidential VM with NVIDIA H100 in TEE mode.
3. The attestation includes the public key of the signing key to prove the key is generated in TEE.
4. All the inference results contain signature with the signing key.
5. You can use the public key to verify all the inference results is generated in TEE.

## Endpoint

https://inference-api.phala.network/

## Attestation & Public Key

### Request

`GET https://inference-api.phala.network/v1/attestation/report`

### Sample Response

```
{
  "signing_address": "...",
  "nvidia_payload": "...",
  "intel_quote": "..."
}
```

### Verify the Attestation

* Verify GPU Attestation

You can copy the value of `nvidia_payload` as the whole payload as followed to verify:

```
curl -X POST https://nras.attestation.nvidia.com/v3/attest/gpu \
 -H "accept: application/json" \
 -H "content-type: application/json" \
 -d '__COPY_FROM_ABOVE__'
```

<figure><img src="../.gitbook/assets/nvidia-gpu-attestation-v3.png" alt=""><figcaption></figcaption></figure>

* Verify TDX Quote

Theoretically, you can verify the Intel TDX quote with the value of `intel_quote` at anywhere that provide TDX quote verification service. The screenshot below is an example of how to verify the Intel TDX quote with the [Automata's on-chain attestation smart contract](https://explorer.ata.network/address/0xE26E11B257856B0bEBc4C759aaBDdea72B64351F/contract/65536\_2/readContract#F6). For Automata example, just need to convert the returned base64 encoded quote to hex format (take Node for example).

```sh
console.log('Quote bytes:', '0x' + Buffer.from(intel_quote, 'base64').toString('hex'));

// Use on-chain smart contract function `verifyAndAttestOnChain` https://explorer.ata.network/address/0xE26E11B257856B0bEBc4C759aaBDdea72B64351F/contract/65536_2/readContract#F6
// to verify with the printed quote bytes above.
```

<figure><img src="../.gitbook/assets/automata-attestation.png" alt=""><figcaption></figcaption></figure>

## Chat API

OpenAI-compatible API. See: https://platform.openai.com/docs/api-reference/chat

### Request

Endpoint: `POST https://inference-api.phala.network/v1/chat/completions` `model` in the request body: currently we only support:

* `meta-llama/meta-llama-3.1-8b-instruct`
* `google/gemma-2-9b-it`
* `microsoft/phi-3-mini-4k-instruct`

### Sample Request

```bash
curl -X 'POST' \
  'https://inference-api.phala.network/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
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
  "model": "meta-llama/meta-llama-3.1-8b-instruct"
}'
```

That sha256 of the request body is `bcf152411970b14faab35a76d559b4188b78c24ced0048d0edcd320bf47bff0a`

(note: in this example, there is no new line in the end of request)

### Sample Response

```bash
data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"role":"assistant"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":"I"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":"'m"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" an"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" AI"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" model"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" known"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" as"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" L"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":"lama"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":"."},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" L"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":"lama"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" stands"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" for"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" \""},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":"Large"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" Language"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" Model"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" Meta"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":" AI"},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":".\""},"logprobs":null,"finish_reason":null}]}

data: {"id":"chat-7ee2a39468ce48d7b2284783f21782b0","object":"chat.completion.chunk","created":1728887353,"model":"meta-llama/meta-llama-3.1-8b-instruct","choices":[{"index":0,"delta":{"content":""},"logprobs":null,"finish_reason":"stop","stop_reason":null}]}

data: [DONE]

```

The sha256sum of response body is `2e704942816901eaf435945fd01d76346e5dd283d5f8a2391e525e8f9a9ef36e`

(note: in this example, there are two new line  in the end of response)

## Signature

By default, you can query another API with the value of `id` in the response in 5 minutes. With this way, you can have maximum compatible with OpenAPI with your existing code.

### Request

`GET https://inference-api.phala.network/v1/signature/{request_id}`

For example, the response in the previous section, the `id` is `chat-7ee2a39468ce48d7b2284783f21782b0`:

`GET https://inference-api.phala.network/v1/signature/chat-7ee2a39468ce48d7b2284783f21782b0`

### Response

* Text: the message you may want to verify. It is joined by the sha256 of the HTTP request body, and of the HTTP response body, separated by a colon `:`.
* Signature.

### Sample Response

```
{
  "text": "bcf152411970b14faab35a76d559b4188b78c24ced0048d0edcd320bf47bff0a:2e704942816901eaf435945fd01d76346e5dd283d5f8a2391e525e8f9a9ef36e",
  "signature": "9277f6a8a65e155c57c6738abdfd13d324d38e834b80c4dc6df5a45c6e7ec10505299edffb36ed0639529b8d96488238019e8fe240369a9344993809845cf2151c"
}
```

We can see that the `text` is `bcf152411970b14faab35a76d559b4188b78c24ced0048d0edcd320bf47bff0a:2e704942816901eaf435945fd01d76346e5dd283d5f8a2391e525e8f9a9ef36e`

Exactly match the value we calculated in the sample in previous section.

### Limitation

Since the resource limitation, the signature will be kept in the memory for 5 minutes since the response is generated.

## Verify Signature

Go to https://etherscan.io/verifiedSignatures, click `Verify Signature`:

* Address: You can get the address from the attestation API. The address should be same if the service did not restarted.
* Message: see the Response of the Signature section. You can also calculate the sha256 by yourselves.

```
bcf152411970b14faab35a76d559b4188b78c24ced0048d0edcd320bf47bff0a:2e704942816901eaf435945fd01d76346e5dd283d5f8a2391e525e8f9a9ef36e
```

* Signature Hash: See the Signature section.
