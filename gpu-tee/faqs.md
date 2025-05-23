# ❓ FAQs

## What is the relationship between dstack Private ML SDK, and what's the vllm-proxy doing there?

The Private ML SDK leverages the TEE features provided by Intel and NVIDIA GPUs to support running any GPU workload as a Docker container in a GPU TEE. In the Private ML SDK, dstack is a framework that can run Docker containers, while vllm-proxy is a specific container within it. The vllm-proxy container operates as a server that forwards requests to a vllm container (hosting a large language model) and generates quotes to attach to responses. This separation allows vllm to remain unmodified and compatible with its latest versions.

## Do I need CUDA or NVIDIA drivers on the host for Private ML SDK with GPU support?

No, CUDA and NVIDIA drivers are not required on the host for the Private ML SDK with GPU support. The host should not have NVIDIA drivers installed to avoid conflicts with TDX and VFIO passthrough. Drivers (e.g., 550.54.15) and CUDA (e.g., 12.4) are loaded inside the guest CVM via Docker containers (e.g., kvin/cuda-notebook). The vllm and vllm-proxy services also run entirely within the TEE guest, not on the host.

## Is CUDA directly accessible in Phala GPU TEE?

Yes, CUDA works in the GPU TEE environment. By default, you don’t need to install it on the host environment when using private-ml-sdk to create a CVM. If you want to use CUDA in your CVM, you can install it manually inside the CVM. You can refer to our benchmark analysis with Succinct, where the SP1 VM also involves CUDA.

## Can I run my app in a docker container with access to GPU TEE under Intel TDX? Is this similar to Google Cloud's Confidential Space?

Yes, you can build your application into a docker image and prepare a docker-compose file. The SDK will create a TDX-based virtual machine to launch your application. However, unlike Google Cloud's Confidential Space, which uses virtual machines, dstack and private-ml-sdk require a bare-metal environment.

## Is dstack-based including private-ml-sdk’s CVM running on bare metal or a hypervisor?

DStack is launched on a bare-metal environment. However, for CVMs created by dstack, a hypervisor (qemu) is used to launch the VM with TDX enabled.
