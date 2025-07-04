---
icon: desktop
---

# Local Development Guide

Dstack enables running containerized applications in Trusted Execution Environments (TEE). For development purposes, you can use our TEE simulator to develop and test your applications locally without TEE hardware. This guide covers setting up the simulator and using our SDKs to interact with TEE functionalities.

Refer to the [**Hardware Requirements**](hardware-requirements.md) for release.

## Prerequisites

- Rust toolchain (for building the simulator)
- Git
- One of the following development environments:
    - Node.js 16+ (for JavaScript SDK)
    - Python 3.7+ (for Python SDK)
    - Go 1.16+ (for Go SDK)
    - Rust 1.70+ (for Rust SDK)

## Simulator

The latest TEE simulator is available in [dstack](https://github.com/Dstack-TEE/dstack/tree/master/sdk/simulator) code repository. Use the following commands to build it:

### Build Simulator

```bash
# Install rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Clone the repository
git clone https://github.com/Dstack-TEE/dstack.git

# Build the simulator
cd dstack/sdk/simulator
./build.sh

# Run the simulator
./dstack-simulator

# The simulator will create the following socket files:
#   tappd.sock   // Legacy TEE service interface (recommended)
#   dstack.sock  // New TEE service interface (in development)
#   external.sock
#   guest.sock
```

To use the simulator with any SDK, set the following environment variable with the absolute path:

```bash
export DSTACK_SIMULATOR_ENDPOINT=/path/to/tappd.sock
```

### Verifying Simulator Setup

After starting the simulator, verify the setup by checking:

1. The socket files exist in the simulator directory:
```bash
ls *.sock
```

2. The environment variable is set correctly:
```bash
echo $DSTACK_SIMULATOR_ENDPOINT
```

## Dstack API

The Dstack API provides the basic abstraction of the TEE functionalities. In general, it provides the following functions:

- **Get Key**: Generate a cryptographic key from the specified key path and returns it along with its certificate chain.
- **Get TDX Quote**: Generate a TDX quote with report data. This can be further verified in our [TEE Attestation Explorer](https://proof.t16z.com/) to prove your application and data are in TEE.
- **Get TDX Information**: Retrieve worker information, one example response is like
    ```json
    {
        "app_id": "<hex-encoded-app-id>",
        "instance_id": "<hex-encoded-instance-id>",
        "app_cert": "<certificate-string>",
        "tcb_info": "<tcb-info-string>",
        "app_name": "my-app",
        "public_logs": true,
        "public_sysinfo": true,
        "device_id": "<hex-encoded-device-id>",
        "mr_aggregated": "<hex-encoded-mr-aggregated>",
        "os_image_hash": "<hex-encoded-os-image-hash>",
        "key_provider_info": "<key-provider-info-string>",
        "compose_hash": "<hex-encoded-compose-hash>"
    }
    ```

The `tappd.sock` is the current TEE RPC API. For more detailed documents, check the [README](https://github.com/Dstack-TEE/dstack/blob/master/sdk/curl/api-tappd.md) file.

> Dstack API is now undergoing an upgrade from the legacy `tappd.sock` to the new `dstack.sock`. `tappd.sock` is still recommended until the full upgrade is done.

## Programming Language Support

### JavaScript

Check the latest version in [dstack](https://github.com/Dstack-TEE/dstack/tree/master/sdk/js) code repository.

#### Installation

```bash
npm install @phala/dstack-sdk
```

#### Basic Usage

```js
import { TappdClient } from '@phala/dstack-sdk';

const client = new TappdClient();

// Check if service is reachable (500ms timeout, never throws)
const isReachable = await client.isReachable();
if (!isReachable) {
  console.log('Tappd service is not available');
  return;
}

// Get the information of the Base Image.
await client.info();

// Derive a key with optional path and subject
const keyResult = await client.deriveKey('<unique-id>');
console.log(keyResult.key); // X.509 private key in PEM format
console.log(keyResult.certificate_chain); // Certificate chain
const keyBytes = keyResult.asUint8Array(); // Get key as Uint8Array

// Generate TDX quote
const quoteResult = await client.tdxQuote('some-data', 'sha256');
console.log(quoteResult.quote); // TDX quote in hex format
console.log(quoteResult.event_log); // Event log
const rtmrs = quoteResult.replayRtmrs(); // Replay RTMRs
```

### Python

Check the latest version in [dstack](https://github.com/Dstack-TEE/dstack/tree/master/sdk/python) code repository.

#### Installation

```bash
pip install dstack-sdk
```

#### Basic Usage

```python
from dstack_sdk import TappdClient, AsyncTappdClient

# Synchronous client
client = TappdClient()

# Caution: You don't need to do this most of the time.
http_client = TappdClient('http://localhost:8000')

# Asynchronous client
async_client = AsyncTappdClient()

# Get the information of the Base Image.
info = client.info()  # or await async_client.info()
print(info.app_id)  # Application ID
print(info.tcb_info.mrtd)  # Access TCB info directly
print(info.tcb_info.event_log[0].event)  # Access event log entries

# Derive a key with optional path and subject
key_result = client.derive_key('<unique-id>')  # or await async_client.derive_key('<unique-id>')
print(key_result.key)  # X.509 private key in PEM format
print(key_result.certificate_chain)  # Certificate chain
key_bytes = key_result.toBytes()  # Get key as bytes

# Generate TDX quote
quote_result = client.tdx_quote('some-data', 'sha256')  # or await async_client.tdx_quote('some-data', 'sha256')
print(quote_result.quote)  # TDX quote in hex format
print(quote_result.event_log)  # Event log
rtmrs = quote_result.replay_rtmrs()  # Replay RTMRs
```

### Golang

Check the latest version in [dstack](https://github.com/Dstack-TEE/dstack/tree/master/sdk/go) code repository.

#### Installation

```bash
go get github.com/Dstack-TEE/dstack/sdk/go
```

#### Basic Usage

```go
package main

import (
	"context"
	"fmt"
	"log/slog"

	"github.com/Dstack-TEE/dstack/sdk/go/dstack"
)

func main() {
	client := dstack.NewDstackClient(
		// dstack.WithEndpoint("http://localhost"),
		// dstack.WithLogger(slog.Default()),
	)

	// Get information about the dstack client instance
	info, err := client.Info(context.Background())
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(info.AppID)  // Application ID
	fmt.Println(info.TcbInfo.Mrtd)  // Access TCB info directly
	fmt.Println(info.TcbInfo.EventLog[0].Event)  // Access event log entries

	path := "/test"
	purpose := "test" // or leave empty

	// Derive a key with optional path and purpose
	deriveKeyResp, err := client.GetKey(context.Background(), path, purpose)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(deriveKeyResp.Key)

	// Generate TDX quote
	tdxQuoteResp, err := client.GetQuote(context.Background(), []byte("test"))
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(tdxQuoteResp.Quote)  // 0x0000000000000000000 ...

	rtmrs, err := tdxQuoteResp.ReplayRTMRs()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(rtmrs)  // map[0:00000000000000000 ...
}
```

#### Rust

Check the latest version in [dstack](https://github.com/Dstack-TEE/dstack/tree/master/sdk/rust) code repository.

#### Installation

```toml
[dependencies]
dstack-rust = { git = "https://github.com/Dstack-TEE/dstack.git", package = "dstack-rust" }
```

#### Basic Usage

```rust
use dstack_sdk::DstackClient;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = DstackClient::new(None); // Uses env var or default to Unix socket

    // Get system info
    let info = client.info().await?;
    println!("Instance ID: {}", info.instance_id);

    // Derive a key
    let key_resp = client.get_key(Some("my-app".to_string()), None).await?;
    println!("Key: {}", key_resp.key);
    println!("Signature Chain: {:?}", key_resp.signature_chain);

    // Generate TDX quote
    let quote_resp = client.get_quote(b"test-data".to_vec()).await?;
    println!("Quote: {}", quote_resp.quote);
    let rtmrs = quote_resp.replay_rtmrs()?;
    println!("Replayed RTMRs: {:?}", rtmrs);

    // Emit an event
    client.emit_event("BootComplete".to_string(), b"payload-data".to_vec()).await?;

    Ok(())
}
```