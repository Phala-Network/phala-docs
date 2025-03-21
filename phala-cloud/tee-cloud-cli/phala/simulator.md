# simulator

## Command: simulator

#### Syntax

```
phala simulator [options] [command]
```

### Description

The `phala simulator`  command is used to launch a local TEE Simulator for testing locally against your local development to simulate how your application will be able to call the TEE functions like remote attestation or key generation with the KMS.

```bash
Usage: phala simulator [options] [command]

TEE simulator commands

Options:
  -h, --help       display help for command

Commands:
  start [options]  Start the TEE simulator
  stop [options]   Stop the TEE simulator
  help [command]   display help for command
```

### Examples

* Display help

```bash
phala simulator --help
```

* Start the TEE Simulator

```bash
# default uses docker
phala simulator start --port 8090
# run on the native host machine
phala simulator start --type native
```

<details>

<summary>Example Output</summary>

simulator running docker

```bash
ℹ Running TEE simulator with image phalanetwork/tappd-simulator:latest
ℹ Pulling latest simulator image...
ℹ Starting simulator in background...
✓ TEE simulator running successfully. Container ID: d8b4f2fe9392b99b4fd44837f26a09508523200025eb3b125e06f27b4cd736b3
ℹ 

Useful commands:
ℹ - View logs: docker logs -f d8b4f2fe9392b99b4fd44837f26a09508523200025eb3b125e06f27b4cd736b3
ℹ - Stop simulator: docker stop d8b4f2fe9392b99b4fd44837f26a09508523200025eb3b125e06f27b4cd736b3

✓ Setting DSTACK_SIMULATOR_ENDPOINT=http://localhost:8090 for current process
```

simulator running natively on host machine

```bash
ℹ Simulator logs will be written to: /Users/hashwarlock/.phala-cloud/logs/tappd-simulator.log
ℹ Starting simulator with: ./tappd-simulator -l unix:/tmp/tappd.sock
✓ Simulator is running in the background
✓ TEE simulator started successfully
✓ Setting DSTACK_SIMULATOR_ENDPOINT=unix:///tmp/tappd.sock for current process
```

</details>

* Get a CVM's Information

```bash
# default uses docker
phala simulator stop --port 8090
# stop on the native host machine
phala simulator stop --type native
```

<details>

<summary>Example Output</summary>

simulator running docker

```bash
⟳ Stopping TEE simulator...... ✓ Deleted DSTACK_SIMULATOR_ENDPOINT from current process
✓: TEE simulator stopped successfully
```

simulator running natively on host machine

```bash
ℹ Stopping simulator...
✓ Simulator stopped successfully
✓ Deleted DSTACK_SIMULATOR_ENDPOINT from current process
```

</details>
