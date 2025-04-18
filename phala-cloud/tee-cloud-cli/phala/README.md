# phala

## Base Command: `phala`

#### Syntax

```
phala [options] [command]
```

### Description

The `phala` base command is used to interact with Phala Cloud and manage your deployments from the command line interface.

```bash
Phala Cloud CLI - Manage your Phala Cloud Deployments

Options:
  -V, --version   output the version number
  -h, --help      display help for command

Commands:
  auth            Authenticate with Phala Cloud
  cvms            Manage Phala Confidential Virtual Machines (CVMs)
  docker          Login to Docker Hub and manage Docker images
  simulator       TEE simulator commands
  help [command]  display help for command
```

### Examples

*   Display help:

    ```bash
    phala --help
    ```
*   Check version:

    ```bash
    phala --version
    ```
*   Display help for subcommand

    ```bash
    phala help auth
    ```

