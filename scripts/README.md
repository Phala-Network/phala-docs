# Documentation Generation Scripts

## CLI Reference Generator

Generates MDX documentation files from `phala --help` output. This ensures the CLI reference documentation stays in sync with the actual CLI.

### Usage

From the repository root:

```bash
node scripts/generate-cli-docs.js
```

### What it does

1. Runs `npx phala --help` to discover all CLI commands
2. For each command, runs `npx phala <command> --help` to get detailed information
3. Parses the help output to extract:
   - Command description and usage syntax
   - Options with their flags and descriptions
   - Subcommands with status indicators (Deprecated, Unstable)
   - Command examples
   - Arguments and pass-through options
4. Generates MDX files in `phala-cloud/references/phala-cloud-cli/phala/`
5. Updates `docs.json` navigation with the correct page order

### Output files

The script generates/updates these files (except `overview.mdx` which is preserved):

- `phala-cloud/references/phala-cloud-cli/phala/overview.mdx` - Main CLI reference
- `phala-cloud/references/phala-cloud-cli/phala/login.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/logout.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/status.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/deploy.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/cvms.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/ssh.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/cp.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/docker.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/simulator.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/nodes.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/config.mdx`
- `phala-cloud/references/phala-cloud-cli/phala/auth.mdx` (deprecated)

### Preserved files

Some files are manually edited and won't be overwritten by the script:

- `overview.mdx` - Contains the polished CLI manual with installation, quick start, and workflow examples

To add a file to the preserve list, edit `PRESERVE_FILES` in `generate-cli-docs.js`.

### When to run

Run this script when:

- The Phala CLI is updated with new commands or options
- Command descriptions or examples change
- You want to ensure docs match the current CLI version

### Requirements

- Node.js
- `phala` CLI (installed via `npx phala`)
