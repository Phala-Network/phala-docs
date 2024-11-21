# 🥷 AI Agent Contract

This section will dive into the technical specifications of the AI Agent Contract's execution. All content will focus on the off-chain components that allow for developers to host their Agent scripts or general purpose JS programs on Phala Network as a serverless backend.&#x20;

## Phala's WASM Runtime (Wapo)

The AI Agent Contract is served through Phala's gateway (https://wapo-testnet.phala.network/ipfs/\<cid>) and executes in a TEE compute node on Phala Network. Phala enables the execution of JS programs through a custom built WASM runtime called Wapo.&#x20;

<figure><img src="../../.gitbook/assets/AI-Agent-Contract-Execution.png" alt=""><figcaption></figcaption></figure>

**Wapo** is a **poll-based** async WebAssembly runtime that provides extended networking support for guest WASM applications. It originated as a module called SideVM in Phala PRuntime, now independent, and the execution engine has been switched from `wasmer` to `wasmtime`.

### Why Wapo?

Wapo is mainly designed as the next version of the AI Agent Contract execution engine. However, it can be used as a general-purpose WebAssembly runtime with networking support. The AI Agent Contract execution engine today is based on Substrate's pallet-contracts, which is not flexible enough and also has many limitations. Here is the table of comparison between 2.x and 3.0:

| <p><br></p>             | **AI Agent Contract 2.0**                | **AI Agent Contract 3.0**          |
| ----------------------- | ---------------------------------------- | ---------------------------------- |
| **Program Type**        | WebAssembly                              | WebAssembly                        |
| **VM Engine**           | wasmi                                    | wasmtime (faster)                  |
| **Incoming Networking** | Query RPC                                | Query RPC or Listening on TCP port |
| **Outgoing Networking** | HTTP requests (with time and size limit) | Arbitrary TCP connections          |
| **Execution mode**      | Transaction/query-based, 10s limit       | Long-running or query-based, no tx |
| **App Memory**          | 4MB for ink / 16 MB for JS               | Up to 4GB due to wasm32 limit      |

With the enhancements with Wapo, Phala has taken the next steps to port the QuickJS implementation to execute in Wapo runtime called WapoJS.

## WapoJS

WapoJS is an upgrade from the previous JS runtime called SideVM QuickJS. With this upgrade, developers can push the boundaries with their general-purpose JS programs with a faster response time vs the previous implementation.

| Feature                    | SideVM QuickJS                                                                                     | WapoJS                                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **VM Memory**              | 16MB                                                                                               | 100MB (default) Up to 4GB                                                                          |
| **Maximum Execution Time** | 60 seconds (default) to unlimited                                                                  | 60 seconds (default) to unlimited                                                                  |
| **HTTP Request API**       | Asynchronous [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch\_API/Using\_Fetch) API | Asynchronous [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch\_API/Using\_Fetch) API |
| **Websockets**             | Not Supported                                                                                      | Supported (not enabled, yet)                                                                       |
| **Concurrent Requests**    | Fully supported                                                                                    | Fully supported                                                                                    |
| **Execution Speed**        | Fast                                                                                               | Faster                                                                                             |
| **SCALE codec API**        | Sidevm.SCALE                                                                                       | Wapo.SCALE                                                                                         |
| **Max Code Size**          | 500KB                                                                                              | Unlimited (Could be limited by streaming receiving from `fetch` + AbortController)                 |
| **Limited CPU Burst**      | CPU time between async calls is limited. e.g. Too complex for-loop may hit the burst limit.        | CPU time between async calls is limited. e.g. Too complex for-loop may hit the burst limit.        |

For more information or inquries about increasing some resource limits, reach out the Phala Network team on [discord](https://discord.gg/phala-network).
