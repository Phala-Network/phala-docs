# auth

## Command: `auth`

#### Syntax

```
phala auth [options] [command]
```

### Description

The `phala auth`  command is used to authenticate a user's API key to manage their Phala Cloud account.

```bash
Usage: phala auth [options] [command]

Authenticate with Phala Cloud

Options:
  -h, --help        display help for command

Commands:
  login [api-key]   Set the API key for authentication
  logout            Remove the stored API key
  status [options]  Check authentication status
  help [command]    display help for command
```

### Examples

* Display help

```bash
phala auth --help
```

* Login to Phala Cloud with API Key

```bash
phala auth login <your-api-key>
```

* Login to Phala Cloud with user prompt

```bash
phala auth login
? Enter your API key: › *********************
```

* Get Status of Login

```bash
phala auth status
```

<details>

<summary>Example Output</summary>

```bash
⟳ Checking authentication status... ✓

✓ Authenticated as bitsbender
╭────────────┬─────────────────────────────────╮
├────────────┼─────────────────────────────────┤
│ Username   │ bitsbender                      │
├────────────┼─────────────────────────────────┤
│ Email      │ hashwarlock@protonmail.com      │
├────────────┼─────────────────────────────────┤
│ Role       │ user                            │
├────────────┼─────────────────────────────────┤
│ Team       │ bitsbender's projects (free)    │
├────────────┼─────────────────────────────────┤
│ Credits    │ $400                            │
╰────────────┴─────────────────────────────────╯
```

</details>

* Logout of Phala Cloud

```bash
phala auth logout
```
