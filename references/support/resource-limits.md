# Resource Limits

{% hint style="danger" %}
**WARNING**

This section is no longer recommended for deploying on Phala. To build and deploy securely and efficiently, please use the fully managed [Phala Cloud](https://cloud.phala.network) platform instead. Check out the doc on how to [get started](../../cloud/getting-started/getting-started.md).
{% endhint %}

## Resource Limits <a href="#resource-limits" id="resource-limits"></a>

| Item                               | Description                                                                      | (LEGACY) ink | SideVM                            |
| ---------------------------------- | -------------------------------------------------------------------------------- | ------------ | --------------------------------- |
| Maximum code size                  | The maximum size of the compiled contract code that can be deployed              | 2 megabytes  | 32 megabytes                      |
| Maximum ingress requests           | The maximum number of simultaneous query requests processed by a single worker   | 8 by default | unlimited                         |
| Request fulfillment timeout        | The maximum duration of an in-flight query request                               | 10 seconds   | unlimited                         |
| Maximum request size               | The maximum size of a incoming request (this includes all arguments)             | 1 megabytes  | unlimited, streaming is supported |
| Maximum returned value size        | The maximum size of the response of a query                                      | 1 megabytes  | unlimited, streaming is supported |
| Maximum query execution time       | The maximum amount of time that a single query can execute                       | 10 seconds   | N/A (continuously running)        |
| Maximum memory allocated           | The maximum amount of memory allocated to your contract during execution         | 4 megabytes  | 16 MB                             |
| HTTP - Maximum concurrent requests | The maximum number of HTTP requests that your source code can make               | 5            | unlimited                         |
| HTTP - Request timeout             | The duration of an HTTP request before timeout                                   | 10 seconds   | unlimited                         |
| HTTP - Maximum request length      | The maximum size of an HTTP request, including the request body and HTTP headers | 16 kilobytes | unlimited                         |
| HTTP - Maximum response length     | The maximum size of an HTTP response                                             | 16 kilobytes | unlimited                         |
