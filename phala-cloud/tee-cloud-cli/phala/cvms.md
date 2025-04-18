# cvms

## Command: cvms

#### Syntax

```
phala cvms [options] [command]
```

### Description

The `phala cvms`  command is used to manage the CVMs deployed to a user's account in Phala Cloud. These include fetching information about the deployments, deploying new CVMs, and managing the CVMs from the command line.

```bash
Usage: phala cvms [options] [command]

Manage Phala Confidential Virtual Machines (CVMs)

Options:
  -h, --help                      display help for command

Commands:
  attestation [options] [app-id]  Get attestation information for a CVM
  create [options]                Create a new CVM
  delete [options] [app-id]       Delete a CVM
  get [options] [app-id]          Get details of a CVM
  list|ls [options]               List all CVMs
  start [app-id]                  Start a stopped CVM
  stop [app-id]                   Stop a running CVM
  resize [options] [app-id]       Resize resources for a CVM
  restart [app-id]                Restart a CVM
  upgrade [options] [app-id]      Upgrade a CVM to a new version
  help [command]                  display help for command
```

### Examples

* Display help

```bash
phala cvms --help
```

* Create a new CVM

```bash
# without env file
phala cvms create
# with env file
phala cvms create -e <path-to-env-file>
```

<details>

<summary>Example Output</summary>

```bash
✔ Enter a name for the CVM: suh
✔ Enter the path to your Docker Compose file: examples/timelock-nts/docker-compose.yml
✓ Deleted DSTACK_SIMULATOR_ENDPOINT from current process
✔ Do you want to skip environment variable prompt? Yes
ℹ Skipping environment variable prompt
✔ Enter number of vCPUs (default: 2): 2
✔ Enter memory in MB (default: 4096): 4096
✔ Enter disk size in GB (default: 40): 40
⟳ Getting public key from CVM... ✓
⟳ Encrypting environment variables... ✓
⟳ Creating CVM... ✓
✓ CVM created successfully
ℹ CVM ID: 2936
ℹ Name: suh
ℹ Status: creating
ℹ App ID: 00c6b8e73822fc86f64f2335d6812081d5ba2beb
ℹ App URL: https://cloud.phala.network/dashboard/cvms/app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
ℹ 
ℹ Your CVM is being created. You can check its status with:
ℹ phala cvms get app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

</details>

* Get a CVM's Information

```bash
phala cvms get app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

<details>

<summary>Example Output</summary>

```bash
⟳ Fetching available CVMs... ✓
✔ Select a CVM: suh (00c6b8e73822fc86f64f2335d6812081d5ba2beb) - Status: running
⟳ Fetching CVM with App ID app_00c6b8e73822fc86f64f2335d6812081d5ba2beb... ✓

╭──────────────┬────────────────────────────────────────────────────────────────────────────────────────────╮
├──────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ Name         │ suh                                                                                        │
├──────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ App ID       │ app_00c6b8e73822fc86f64f2335d6812081d5ba2beb                                               │
├──────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ Status       │ running                                                                                    │
├──────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ VCPU         │ 1                                                                                          │
├──────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ Memory       │ 1024 MB                                                                                    │
├──────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ Disk Size    │ 10 GB                                                                                      │
├──────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ Dstack Image │ dstack-0.3.5                                                                               │
├──────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ App URL      │ https://cloud.phala.network/dashboard/cvms/app_00c6b8e73822fc86f64f2335d6812081d5ba2beb    │
╰──────────────┴────────────────────────────────────────────────────────────────────────────────────────────╯
```

</details>

* List all CVMs

```bash
phala cvms ls
```

<details>

<summary>Example Output</summary>

```bash
⟳ Fetching CVMs... ✓
╭───────────────┬────────────────────────────────────────────────────────────────────────────────────────────╮
├───────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ Name          │ suh                                                                                        │
├───────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ App ID        │ app_00c6b8e73822fc86f64f2335d6812081d5ba2beb                                               │
├───────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ Status        │ running                                                                                    │
├───────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ Node Info URL │ https://36a6d736e7ebe09b090a345239ed527b372f1a87-8090.dstack-prod5.phala.network:443       │
├───────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ App URL       │ https://cloud.phala.network/dashboard/cvms/app_00c6b8e73822fc86f64f2335d6812081d5ba2beb    │
╰───────────────┴────────────────────────────────────────────────────────────────────────────────────────────╯

✓ Found 1 CVMs

ℹ Go to https://cloud.phala.network/dashboard/ to view your CVMs
```

</details>

* Fetch. an Attestation of a CVM

```bash
phala cvms attestation app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

<details>

<summary>Example Output</summary>

```bash
✓ CVM with App ID app_5592440286f5947743f58975a8335459d6fee5cd detected
⟳ Fetching attestation information for CVM app_5592440286f5947743f58975a8335459d6fee5cd...... ✓
✓ Attestation Summary:
╭───────────────┬───────────────╮
├───────────────┼───────────────┤
│ Status        │ Online        │
├───────────────┼───────────────┤
│ Public Access │ Enabled       │
├───────────────┼───────────────┤
│ Error         │ None          │
├───────────────┼───────────────┤
│ Certificates  │ 2 found       │
╰───────────────┴───────────────╯

✓ Certificate #1 (End Entity):
╭─────────────────────┬─────────────────────────────────────────────────────────────────────╮
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Subject             │ 5592440286f5947743f58975a8335459d6fee5cd.phala                      │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Issuer              │ Phala KMS CA (Phala Network)                                        │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Serial Number       │ 1d651ceb77d826a547444fa140fd5ef2aa57a76e                            │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Validity            │ 12/31/1974, 6:00:00 PM to 3/14/2026, 2:03:35 PM                     │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Fingerprint         │ 0a69a723d5bd53a429626009ed99ed2e369062591ccba4ed62a4df5ff95122f8    │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Signature Algorithm │ ecdsa-with-SHA256                                                   │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Is CA               │ Yes                                                                 │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Position in Chain   │ 0                                                                   │
╰─────────────────────┴─────────────────────────────────────────────────────────────────────╯

✓ Certificate #2 (CA):
╭─────────────────────┬─────────────────────────────────────────────────────────────────────╮
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Subject             │ Phala KMS CA (Phala Network)                                        │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Issuer              │ Phala KMS CA (Phala Network)                                        │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Serial Number       │ 43a1a79f8766c24aa2274de642b481f9ada4438                             │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Validity            │ 12/31/1974, 6:00:00 PM to 12/31/4095, 6:00:00 PM                    │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Fingerprint         │ 68246c57488458f40e589c09ee348c0b823c3cb36599fff93d18a9a9699d1179    │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Signature Algorithm │ ecdsa-with-SHA256                                                   │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Is CA               │ Yes                                                                 │
├─────────────────────┼─────────────────────────────────────────────────────────────────────┤
│ Position in Chain   │ 1                                                                   │
╰─────────────────────┴─────────────────────────────────────────────────────────────────────╯

✓ Trusted Computing Base (TCB) Information:
╭───────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────╮
├───────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Mrtd              │ c68518a0ebb42136c12b2275164f8c72f25fa9a34392228687ed6e9caeb9c0f1dbd895e9cf475121c029dc47e70e91fd    │
├───────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Rootfs Hash       │ 7458d2859b90c071be1f8af3adf4285b764d0c9d08a442be98ff96bb6b160a019db5fbd74edde26095bb659db7a27ab2    │
├───────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Rtmr0             │ 79207fa707c5bbf697d579bbd44c2ba14f8565d528aff0de407c58fd34815b67a35cfbb0a0d996b1c7b911a2c8ae806c    │
├───────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Rtmr1             │ 4a7db64a609c77e85f603c23e9a9fd03bfd9e6b52ce527f774a598e66d58386026cea79b2aea13b81a0b70cfacdec0ca    │
├───────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Rtmr2             │ 8a4fe048fea22663152ef128853caa5c033cbe66baf32ba1ff7f6b1afc1624c279f50a4cbc522a735ca6f69551e61ef2    │
├───────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Rtmr3             │ 7b59d1740c489a43ed83b6cc7480edf987a3188b5b19166b2a971018e13304b80406bad2a9ec804d091a764a0ba3d3af    │
├───────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Event Log Entries │ 25 entries                                                                                          │
╰───────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────╯

✓ Event Log (Showing entries to reproduce RTMR3):
╭──────────────┬─────┬───────────┬──────────────────────────────────────────────────────────────────╮
│ Event        │ IMR │ Type      │ Payload                                                          │
├──────────────┼─────┼───────────┼──────────────────────────────────────────────────────────────────┤
│ rootfs-hash  │ 3   │ 134217729 │ 2ec914e7be46b48eb4184959cafc524b9c08583a22cacccaa3c66a3938ca03c1 │
│ app-id       │ 3   │ 134217729 │ 5592440286f5947743f58975a8335459d6fee5cd                         │
│ compose-hash │ 3   │ 134217729 │ 5592440286f5947743f58975a8335459d6fee5cd9dbcd97a20cf85a58b1bdf82 │
│ ca-cert-hash │ 3   │ 134217729 │ d2d9c7c29e3f18e69cba87438cef21eea084c2110858230cd39c5decc629a958 │
│ instance-id  │ 3   │ 134217729 │ 19b555ea772e0d56ebaf75091193ecf4ba603f04                         │
╰──────────────┴─────┴───────────┴──────────────────────────────────────────────────────────────────╯
Total: 5 rows
ℹ To see all full attestation data, use --json

✓ To reproduce RTMR3, use the tool at https://rtmr3-calculator.vercel.app/
```

</details>

* Start a CVM

```bash
phala cvms start app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

<details>

<summary>Example Output</summary>

```bash
⟳ Fetching available CVMs... ✓
✔ Select a CVM: suh (00c6b8e73822fc86f64f2335d6812081d5ba2beb) - Status: stopped
⟳ Starting CVM with App ID app_00c6b8e73822fc86f64f2335d6812081d5ba2beb... ✓

╭────────────┬─────────────────────────────────────────────────╮
├────────────┼─────────────────────────────────────────────────┤
│ CVM ID     │ 2936                                            │
├────────────┼─────────────────────────────────────────────────┤
│ Name       │ suh                                             │
├────────────┼─────────────────────────────────────────────────┤
│ Status     │ starting                                        │
├────────────┼─────────────────────────────────────────────────┤
│ App ID     │ app_00c6b8e73822fc86f64f2335d6812081d5ba2beb    │
╰────────────┴─────────────────────────────────────────────────╯

✓ Your CVM is being started. You can check the dashboard for more details:
https://cloud.phala.network/dashboard/cvms/app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

</details>

* Stop a CVM

```bash
phala cvms stop app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

<details>

<summary>Example Output</summary>

```bash
⟳ Fetching available CVMs... ✓
✔ Select a CVM: suh (00c6b8e73822fc86f64f2335d6812081d5ba2beb) - Status: running
⟳ Stopping CVM with App ID app_00c6b8e73822fc86f64f2335d6812081d5ba2beb... ✓
╭────────────┬─────────────────────────────────────────────────╮
├────────────┼─────────────────────────────────────────────────┤
│ CVM ID     │ 2936                                            │
├────────────┼─────────────────────────────────────────────────┤
│ Name       │ suh                                             │
├────────────┼─────────────────────────────────────────────────┤
│ Status     │ stopped                                         │
├────────────┼─────────────────────────────────────────────────┤
│ App ID     │ app_00c6b8e73822fc86f64f2335d6812081d5ba2beb    │
╰────────────┴─────────────────────────────────────────────────╯

✓ Your CVM is being stopped. You can check the dashboard for more details:
https://cloud.phala.network/dashboard/cvms/app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

</details>

* Delete a CVM

```bash
phala cvms delete app_5592440286f5947743f58975a8335459d6fee5cd
```

<details>

<summary>Example Output</summary>

```bash
⟳ Fetching available CVMs... ✓
✔ Select a CVM: hell (5592440286f5947743f58975a8335459d6fee5cd) - Status: running
✔ Are you sure you want to delete CVM with App ID app_5592440286f5947743f58975a8335459d6fee5cd? This action cannot be undone. Yes
⟳ Deleting CVM app_5592440286f5947743f58975a8335459d6fee5cd... ✓
✓ CVM app_5592440286f5947743f58975a8335459d6fee5cd deleted successfully
```

</details>

* Resize a CVM

```bash
phala cvms resize app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

<details>

<summary>Example Output</summary>

```bash
⟳ Fetching available CVMs... ✓
✔ Select a CVM: suh (00c6b8e73822fc86f64f2335d6812081d5ba2beb) - Status: running
✔ Enter number of vCPUs: 1
✔ Enter memory in MB: 1024
✔ Enter disk size in GB: 10
✔ Allow restart of the CVM if needed for resizing? Yes
╭───────────────┬───────────────────────╮
├───────────────┼───────────────────────┤
│ VCPUs         │ 2 -> 1                │
├───────────────┼───────────────────────┤
│ Memory        │ 4096 MB -> 1024 MB    │
├───────────────┼───────────────────────┤
│ Disk Size     │ 40 GB -> 10 GB        │
├───────────────┼───────────────────────┤
│ Allow Restart │ Yes                   │
╰───────────────┴───────────────────────╯
✔ Are you sure you want to resize CVM app_00c6b8e73822fc86f64f2335d6812081d5ba2beb with the following changes:
 Yes

✓ Your CVM is being resized. You can check the dashboard for more details:
https://cloud.phala.network/dashboard/cvms/app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

</details>

* Restart a CVM

```bash
phala cvms restart app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

<details>

<summary>Example Output</summary>

```bash
⟳ Fetching available CVMs... ✓
✔ Select a CVM: suh (00c6b8e73822fc86f64f2335d6812081d5ba2beb) - Status: stopped
⟳ Fetching current configuration for CVM app_00c6b8e73822fc86f64f2335d6812081d5ba2beb... ✓
✔ Enter the path to your Docker Compose file: examples/timelock-nts/docker-compose.yml
✓ Deleted DSTACK_SIMULATOR_ENDPOINT from current process
⟳ Upgrading CVM app_00c6b8e73822fc86f64f2335d6812081d5ba2beb... ✓
ℹ Details: Accepted

✓ Your CVM is being upgraded. You can check the dashboard for more details:
https://cloud.phala.network/dashboard/cvms/app_00c6b8e73822fc86f64f2335d6812081d5ba2beb
```

</details>
