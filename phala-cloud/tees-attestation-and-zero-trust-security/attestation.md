# Attestation

## Introduction

Remote Attestation (RA) is a critical security mechanism in Trusted Execution Environments (TEEs) like Intel TDX. It allows a remote verifier to confirm that an application is running inside a genuine, secure TEE with the expected configuration and code. This guide explains the key fields in TEE attestation reports, with a specific focus on Intel TDX attestation as used by Phala Cloud.

Let’s get into it!

## Attestation Report Overview

An attestation report (or "quote") is a cryptographically signed document containing evidence about the TEE environment, including hardware measurements, runtime measurements, and application-specific data. The Attestation Key sealed by the manufactory in the Quoting Enclave will be used to sign the quote when received request from Challenger. When the remote Challenger receives this report, it can validate that the environment meets expected security properties before trusting it with sensitive data or operations.

<figure><img src="https://img0.phala.world/files/1cf0317e-04a1-8025-945f-ce263a7b96e3.jpg" alt=""><figcaption></figcaption></figure>

Source: [https://www.intel.com/content/www/us/en/developer/tools/software-guard-extensions/attestation-services.html](https://www.intel.com/content/www/us/en/developer/tools/software-guard-extensions/attestation-services.html)

### Key Fields in a TDX Attestation Report

Here is an example report generated on Phala Cloud:

```bash
{
      "tee_tcb_svn": "06010300000000000000000000000000",
      "mr_seam": "5b38e33a6487958b72c3c12a938eaa5e3fd4510c51aeeab58c7d5ecee41d7c436489d6c8e4f92f160b7cad34207b00c1",
      "mr_signer_seam": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "seam_attributes": "0000000000000000",
      "td_attributes": "0000001000000000",
      "xfam": "e702060000000000",
      "mr_td": "c68518a0ebb42136c12b2275164f8c72f25fa9a34392228687ed6e9caeb9c0f1dbd895e9cf475121c029dc47e70e91fd",
      "mr_config_id": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "mr_owner": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "mr_owner_config": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "rt_mr0": "85e0855a6384fa1c8a6ab36d0dcbfaa11a5753e5a070c08218ae5fe872fcb86967fd2449c29e22e59dc9fec998cb6547",
      "rt_mr1": "9b43f9f34a64bc7191352585be0da1774a1499e698ba77cbf6184547d53d1770d6524c1cfa00b86352f273fc272a8cfe",
      "rt_mr2": "7cc2dadd5849bad220ab122c4fbf25a74dc91cc12702447d3b5cac0f49b2b139994f5cd936b293e5f0f14dea4262d668",
      "rt_mr3": "2c482b5b34f6902293bc203696f407241bfa319d2410a04c604d1021888d6028bf4bd280ff859ee270a0429aac5f0d82",
      "report_data": "afab9790acb13c4c651c1933a22b5f0663ef22927120dd08cc8291d7e0912d8b1c36eb75cf661a64735042f8e81bbe42cb9ab310ca95bf8d36c44cb8835c901f"
}
```

You can check those information at the **CVM Dashboard→Attestation** page.

<figure><img src="https://img0.phala.world/files/1cf0317e-04a1-80f6-822d-ddfca969efb5.jpg" alt=""><figcaption></figcaption></figure>

Now, let’s dive into each field and learn what it represents.

### Hardware Identity and Security Fields

#### `tee_tcb_svn`

The Trusted Computing Base Security Version Number.

* **Meaning**: This represents the security patch level and version information for the TEE hardware components
* **Verification Use**: Crucial for ensuring the platform has the latest security patches against known vulnerabilities.

#### `MRSEAM` (Measurement of TDX-Module)

The cryptographic measurement of the SEAM (Secure Arbitration Mode) firmware.

* **Meaning**: A hash representing the identity and integrity of the TDX module firmware.
* **Verification Use**: Verifies that the TDX firmware hasn't been tampered with and is a known, trusted version.

#### `MRTD` (Measurement Register for Trust Domain)

A cryptographic measurement of the initial TD memory contents and configuration.

* **Meaning**: Captures the initial state of the TD (Trust Domain) when it was created. Measurement of TDVF.
* **Verification Use**: Ensures the TD was initialized with expected memory contents and configuration.

### Runtime Measurement Fields

#### `RTMR0`, `RTMR1`, `RTMR2` (Runtime Measurement Registers)

Registers that contain hash chains of measurements of components loaded during boot.

* **Meaning**: Each register measures a different aspect of the boot process:
*
  * `RTMR0`: Measurement of virtual hardware environment
  * `RTMR1`: Measurement of Linux kernel
  * `RTMR2`: Measurement of kernel cmdline and initrd
* **Verification Use**: Verifies that the expected boot components were loaded, ensuring the integrity of the boot chain.

#### `RTMR3` (Application-specific Measurement Register)

In dstack's implementation, RTMR3 is dedicated to application-specific measurements.

* **Meaning**: Measurements of application components including app-id, compose-hash, instance-id, and key-provider.
* **Verification Use**: Can be used to confirm the application running in the TEE has the expected code and configuration.

### Additional TEE Configuration Fields

#### `seamattributes`

Attributes of the SEAM (Secure Arbitration Mode).

* **Meaning**: Configuration flags for the SEAM firmware.
* **Verification Use**: Always zeros for TDX-module.

#### `tdattributes`

Attributes of the Trust Domain.

* **Meaning**: Configuration flags for the TD (Trust Domain).
* **Verification Use**: Verifies the TD has the expected security settings.

#### `xfam` (eXtended Feature Activation Mask)

Controls which extended features are enabled in the TDX environment.

* **Meaning**: Specifies which extended CPU features are accessible to the TD.
* **Verification Use**: Ensures the TD has access to the expected CPU features while maintaining security boundaries.

#### Application-specific Fields

#### `reportData`

User-specified data that gets included in the quote.

* **Meaning**: A 64-byte field that applications can fill with custom data (such as nonces, challenge responses, or application state hashes).
* **Verification Use**: Binds application-specific data to the hardware attestation, allowing for challenge-response protocols or linking to application state.

#### `mrconfig`, `mrowner`, and `mrownerconfig`

Configuration and ownership information.

* **Example Values**: (Usually all zeros for dstack)
* **Meaning**: These fields can contain configuration data for more complex attestation scenarios.
* **Verification Use**: Generally not used in basic attestation but may be important in advanced scenarios.

### RTMR3 Event Chain: How Application Components Are Measured

In dstack's implementation, application components are measured and stored in RTMR3 through a hash chain mechanism:

* **Component Measurement**: Each application component (compose-hash, instance-id, key-provider) is individually hashed.
* **Event Creation**: Measurement events are created with key-value pairs (e.g., "app-id": "your-app-123").
* **Event Hashing**: Each event is hashed (e.g., Event0 → Hash(0x11111)).
* **RTMR3 Extension**: The hash chain is extended using the formula:

```
RTMR3_new = SHA384(RTMR3_old || SHA384(event))
```

* **Verification**: The final RTMR3 value can be verified against a known-good value to ensure the application components haven't been modified.

When you deployed your application on Phala Cloud, you can verify the RTMR3 with the data shown in dashboard attestation page. You can do it with a community tool called [rtmr3-calculator](https://rtmr3-calculator.vercel.app/).

<figure><img src="https://img0.phala.world/files/1cf0317e-04a1-802e-9b07-eca33e760a18.jpg" alt=""><figcaption></figcaption></figure>

_The source code of the rtmr3-calculator:_ [_https://github.com/propeller-heads/rtmr3-calculator_](https://github.com/propeller-heads/rtmr3-calculator)

## Verification Process

When verifying an attestation report, follow these steps:

1. **Verify Signature**: Ensure the attestation report is properly signed by a valid TEE certificate.
2. **Verify Certificate Chain**: Validate the entire certificate chain back to a trusted root.
3. **Check Hardware Identity**: Verify MRSEAM, and TCB values match known-good values.
4. **Verify System Measurements**: Ensure MRTD, RTMR0-2 values match your security policy.
5. **Verify Application Measurements**: Check that RTMR3 contains the expected hash of your application components.
6. **Verify ReportData**: If you used a challenge-response mechanism, verify the reportData contains the expected response.

### Common Verification Targets

In a typical attestation verification flow, you'll check:

{% stepper %}
{% step %}
**Hardware Integrity**: Ensuring genuine, up-to-date, and properly configured TEE hardware.

* Fields: `tee_tcb_svn` (or **tcbStatus**, **advisoryIds**), `MRSEAM`
{% endstep %}

{% step %}
**System Integrity**: Verifying the System running in the TEE.

* Fields: `MRTD`, `RTMR0`, `RTMR1`, `RTMR2`
{% endstep %}

{% step %}
**Application Integrity**: Verifying the application running in the TEE is the expected one.

* Fields: `RTMR3`
{% endstep %}

{% step %}
**Identity Authentication**: Confirming the TEE has the expected identity for secure communication.

* This often involves TLS certificates, blockchain wallet addresses, or other identity proofs embedded in `reportData`
{% endstep %}
{% endstepper %}

### dstack-Specific Verification

When working with dstack TEE deployments, pay special attention to:

1. **app-id Verification**: This field is relevant when the CVM is deployed with KMS, which generates application keys based on the app-id.
2. **compose-hash Verification**: The manifest hash of the currently executing application. This determines the application code executing within the TEE.
3. **key-provider Verification**: Indicates who distributed the keys for the App. The key is used to encrypt the root filesystem of the CVM. Therefore, it’s important to verify this field.
4. **reportData**: TLS certificates, blockchain wallet addresses, and social proofs like Twitter handles can be verified through the reportData field.

Check more instructions [here](https://github.com/Dstack-TEE/dstack/blob/master/attestation.md) on how Dstack attestation work.

### Conclusion

Understanding attestation reports is crucial for developers working with TEE environments. By correctly interpreting these fields, you can verify that your application is running in a genuine, secure environment with the expected configuration and code.

For more detailed information on Intel TDX attestation, refer to the Intel TDX Module documentation. For dstack-specific attestation flows, consult the dstack documentation and GitHub repository at [https://github.com/dstack-TEE/dstack](https://github.com/dstack-TEE/dstack).

Example of verification: [https://github.com/Dstack-TEE/dstack-examples/pull/16/files#diff-a37816fef898fbd92c747eefa6ed85ede031a8bcd3288295976c6772ffd69fcc](https://github.com/Dstack-TEE/dstack-examples/pull/16/files#diff-a37816fef898fbd92c747eefa6ed85ede031a8bcd3288295976c6772ffd69fcc)
