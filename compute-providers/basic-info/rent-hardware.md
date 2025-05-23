# Rent Hardware

## Worker on Vultr <a href="#khala-worker-on-vultr" id="khala-worker-on-vultr"></a>

> This guide will show you how to set up your worker on the `VULTR Bare Metal Simplified™ Intel E-2288G` Instance. For mining on your own hardware check our guide [here](requirements-in-phala-khala.md).

## Before Getting Started <a href="#before-getting-started" id="before-getting-started"></a>

1. Sign up on[Vultr](https://vultr.com/).
2. Enter your [billing information](https://my.vultr.com/billing/).
3. Request to [increase your limit](https://my.vultr.com/billing/#billinglimits) may be required.

> Increasing the credit depends on the cloud provider’s support’s response time.

## Deploy Instance <a href="#deploy-instance" id="deploy-instance"></a>

After successfully signing up and increasing your credit limit, it is time to pick the correct instance.

* Go to [Deploy](https://my.vultr.com/deploy/)
  * Select ‘Bare Metal’
  * Pick an available location geographically closest to you.
  * Select `Intel E-2288G`
  * Choose the 64 bit OS Ubuntu 21.10 x64
  * Leave any remaining options as default.
  * Add a meaningful ‘Server Hostname & Label’
  * You are ready to hit ‘Deploy Now’
  * Wait for 5-15 minutes: Get a cup of coffee ☕ until your instance is ready

## Instance Settings <a href="#instance-settings" id="instance-settings"></a>

Once your new instance is displayed as ‘Running,’ there are currently no additional steps required to adjust the machine’s BIOS. The instance works out of the box.

> _Optional:_ To optimize the worker’s score, you can reboot the instance, head over to the console, and enter the BIOS with F11, to adjust the BIOS settings mentioned in this [guide](requirements-in-phala-khala.md#os-requirements).

You can get the correct drivers from our guide here under the Ubuntu 21.10 tab.

Once the drivers are installed, you may now turn your instance into a Phala worker.\
👉 [Get mining scripts](https://docs.phala.network/compute-providers/run-workers-on-phala/solo-worker-deployment)
