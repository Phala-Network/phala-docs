# Hardware Requirements

## General Khala Hardware Requirements <a href="#general-khala-hardware-requirements" id="general-khala-hardware-requirements"></a>

A system can potentially mine Phala if it meets these general requirements:

| CPU                      | System       | Memory        | Storage |
| ------------------------ | ------------ | ------------- | ------- |
| SGX-compatible Processor |              |               |         |
| SGX-compatible BIOS      | Ubuntu 20.04 | ≥ 2G per core | ≥ 1T    |
| ≥ 2 cores                |              |               |         |

### Requirements Checklist <a href="#requirements-checklist" id="requirements-checklist"></a>

* An [Intel® SGX](https://www.intel.com/content/www/us/en/architecture-and-technology/software-guard-extensions.html) compatible processor.
  * [Lookup your CPU](broken-reference) and see if it is compatible.
  * [How to find new Intel® SGX processors](broken-reference) if mine is not compatible.
* A motherboard and BIOS that supports [Intel® SGX](https://www.intel.com/content/www/us/en/architecture-and-technology/software-guard-extensions.html) to run the [Trusted Execution Environment (TEE)](https://murdoch.is/talks/rhul14tee.pdf) is required.
  * [Check BIOS compatability](broken-reference).
* A Solid-state drive (SSD) storage device
  * Storing your blockchain data on a mechanical HDD will result in extremely slow synchronization speeds. At a minimum a 1TB SSD drive is recommended.
    * Refer to [issue #554](https://github.com/Phala-Network/phala-blockchain/issues/554) for more info.
* Have a supported version of Ubuntu (18.04, 20.04, 21.04) installed and booted from it.
  * See [Supported OS requirements](broken-reference).
* You require $$S_{min}=k \sqrt{P}$$ tokens to stake when starting your worker.
  * As an example an [Intel® Core™ i7-8700 CPU @ 3.20GHz](https://ark.intel.com/content/www/us/en/ark/products/126686/intel-core-i78700-processor-12m-cache-up-to-4-60-ghz.html) had a `P` value (worker/ worker score) between `1400` and `1700` during testing.
  * Feel free to use our [spreadsheet](broken-reference) (coming soon) containing the formulas from the PHA tokenomics section to estimate your required minimum tokens to stake.
  * Alternatively, you may also use a [pool and delegate](https://app.phala.network/delegate/). There is a guide here on how to delegate.

> Alternatively, you can test mining through renting hardware.

## Check Your CPU <a href="#check-your-cpu" id="check-your-cpu"></a>

> Currently, only [Intel® SGX](https://www.intel.com/content/www/us/en/architecture-and-technology/software-guard-extensions.html) is supported, hence an [Intel® SGX compatible CPU](https://www.intel.com/content/www/us/en/support/articles/000028173/processors.html) is a requirement.

### 1. Lookup Your Processor <a href="#1-lookup-your-processor" id="1-lookup-your-processor"></a>

**Windows**

<details>

<summary>See how to lookup your CPU on Windows</summary>

`Start` > ⚙️`Settings` > 🎛️`Control Panel`

Note that you require a [supported Linux OS](broken-reference) to run a Phala worker.

On Windows, head over to ‘Control Panel/Settings,’ or right-click on the Start icon and select ‘System.’

</details>

**Linux**

<details>

<summary>See how to lookup your CPU's model on Linux</summary>

* **With a GUI**

`Settings` > `About`

On Ubuntu, click in the upper-right corner, pick ‘Settings,’ select ‘About,’ and look for ‘Processor.’

<img src="../../.gitbook/assets/linux_settings.png" alt="" data-size="original">

(Navigating to ‘Settings’ on a Desktop GUI to look up CPU specs)

* **Without GUI**

In case you do not have a GUI, enter the following command into your shell and look for your CPU’s ‘Model name:’

```
lscpu
```

![](../../.gitbook/assets/CPU\_Linux\_check.gif)

(Looking up the CPU model with the `lscpu` command in the Linux shell)

</details>

### 2. Confirm the CPU Supports Intel® SGX <a href="#2-confirm-the-cpu-supports-intel-sgx" id="2-confirm-the-cpu-supports-intel-sgx"></a>

> Once you know your CPU’s model name:
>
> * Lookup your Processor’s Intel® SGX compatability in the [Intel® product specifications (ARK)](https://ark.intel.com/content/www/us/en/ark.html#@Processors)

On the [Intel® product specifications (ARK)](https://ark.intel.com/content/www/us/en/ark.html#@Processors) website, you will find information about your CPU’s Intel® SGX compatibility. In addition, under the ‘Security & Reliability’ section, it will mention if your CPU is compatible or not. Below is an example of the [Intel® Core™ i7-8700 CPU @ 3.20GHz](https://ark.intel.com/content/www/us/en/ark/products/126686/intel-core-i78700-processor-12m-cache-up-to-4-60-ghz.html), a screenshot taken from the Intel® product specifications (ARK).

<figure><img src="../../.gitbook/assets/SGX_comptible_ARK.png" alt=""><figcaption><p>(This image shows a CPU that supports Intel® SGX.)</p></figcaption></figure>

ℹ️ If you do not have an Intel® SGX compatible CPU yet, you may use the [advanced search](https://ark.intel.com/content/www/us/en/ark/search/featurefilter.html?productType=873&2\_SoftwareGuardExtensions=Yes%20with%20Intel%C2%AE%20ME&3\_CoreCount-Min=8&2\_StatusCodeText=4) option at the Intel® website to find your next processor. In general terms, the newer the processor is and the more cores it has, the greater the compatibility and the worker rating.

## Check Your BIOS <a href="#check-your-bios" id="check-your-bios"></a>

> A motherboard supporting Intel® SGX and the BIOS settings listed below is required.

### 1. Boot into BIOS <a href="#1-boot-into-bios" id="1-boot-into-bios"></a>

> Refer to these resources to ‘boot into BIOS mode’ from [Microsoft©](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/boot-to-uefi-mode-or-legacy-bios-mode?view=windows-11) or [wikiHow](https://www.wikihow.com/Enter-BIOS).

Look for instructions to boot into your BIOS on the screen immediately after a cold boot; this varies by manufacturer.

### 2. Disable Secure Boot <a href="#2-disable-secure-boot" id="2-disable-secure-boot"></a>

> In the BIOS settings go to: `Security` > `Secure Boot` and set it to `Disabled`
>
> * The terms in the BIOS menu may differ depending on your motherboard manufacturer.

### 3. Use UEFI Boot <a href="#3-use-uefi-boot" id="3-use-uefi-boot"></a>

> In the BIOS menu under `Boot` > `Boot Mode` set it to `UEFI`.
>
> * Refer to [‘boot into UEFI mode’](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/boot-to-uefi-mode-or-legacy-bios-mode?view=windows-11) for additional information.

### 4. Save & Reboot <a href="#4-save--reboot" id="4-save--reboot"></a>

> Do not forget to save your BIOS settings.
>
> * Reboot your machine after the settings are saved.

### 5. Enable Intel® SGX Extensions <a href="#5-enable-intel-sgx-extensions" id="5-enable-intel-sgx-extensions"></a>

> Go to `Security` > `Intel® SGX` (The exact name may vary by manufacturer), set it to `Enabled`.
>
> > <details>
> >
> > <summary>Expand for critical additional information ℹ️</summary>
> >
> > * Note: If you only see the Intel® `SGX: Software Controlled` or similar, you need to run the [Intel® Software Guard Extensions Software Enabling Application for Linux](https://github.com/intel/sgx-software-enable) after booting into your Ubuntu OS. Before executing the script, refer to the [Supported Operating Systems](broken-reference) section.
> > * Phala also provides a prebuilt binary [here](https://github.com/Phala-Network/sgx-tools/releases/tag/0.1). You can download and execute it with the following commands:
> >
> > ```
> > wget https://github.com/Phala-Network/sgx-tools/releases/download/0.1/sgx_enable
> > chmod +x sgx_enable
> > sudo ./sgx_enable
> > ```
> >
> > </details>

## Supported Operating Systems <a href="#supported-operating-systems" id="supported-operating-systems"></a>

Ubuntu is recommended. You need to be able to boot your computer into a supported version of Ubuntu to mine. The following OS versions of Ubuntu have been reported to be compatible to mine.

> More information on how to [install Ubuntu Desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).
>
> * If you have no GUI or physicall access to the machine, you may want to use SSH.
>   * [SSH crash course](https://youtu.be/hQWRp-FdTpc?t=40) expaining what SSH is and how to use it, may be a usefull resource.
>   * [Linux Fundamentals](https://academy.hackthebox.com/course/preview/linux-fundamentals) provides an overview of Linux and how to use the shell.\
>

{% tabs %}
{% tab title="Ubuntu 20.04" %}
#### Ubuntu 20.04 <a href="#ubuntu-2004" id="ubuntu-2004"></a>

Using a Linux kernel version of `5.8.0-xxx` is recommended for Ubuntu 20.04.

To find your Linux kernel version type:

```
hostnamectl | grep Kernel
```

Get the Linux Kernel utilities for Ubuntu 20.04.

```
git clone https://github.com/mtompkins/linux-kernel-utilities.git
```

```
cd linux-kernel-utilities/
chmod +x *.sh
```

To see a list of available Kernel versions for your machine, execute the following command:

```
./compile_linux_kernel.sh
```

It is recommended to follow the instructions and select to install Ubuntu 20.04 Kernel version 5.8.
{% endtab %}

{% tab title="Ubuntu 21.10" %}
Ubuntu 21.10

For Ubuntu 21.10 we recommend kernel version `5.13.0-xxx`.

To find your Linux kernel version type:

```
hostnamectl | grep Kernel
```

Some packages do not come natively installed. It is therefore recommended to install the most crucial ones now as instructed below.

**DCAP Driver for Intel® SGX**

First, install Rust with [rustup](https://rustup.rs/). This is needed to install the driver.

To install rustup:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Follow the instructions in the script.

> Do not forget to execute `source $HOME/.cargo/env` for the installation to work.

After successfully installing Rust, you need to install Rust nightly with the following command:

```
rustup default nightly
```

To install the Foranix EDP target through executing:

```
rustup target add x86_64-fortanix-unknown-sgx --toolchain nightly
```

Now you are ready to Install the Intel® SGX driver.

```
echo "deb https://download.fortanix.com/linux/apt xenial main" | sudo tee -a /etc/apt/sources.list.d/fortanix.list >/dev/null
curl -sSL "https://download.fortanix.com/linux/apt/fortanix.gpg" | sudo -E apt-key add -
sudo apt-get update
sudo apt-get install intel-sgx-dkms
```

Follow the instructions in the installation script. You may need to reboot after successful completion.

You are now ready to proceed to the next section.
{% endtab %}
{% endtabs %}

👇 If you have any issues feel free to reach out to the community. 👇
