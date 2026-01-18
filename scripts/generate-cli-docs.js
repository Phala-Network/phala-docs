#!/usr/bin/env node

/**
 * CLI Documentation Generator for Phala Cloud CLI
 *
 * Generates MDX documentation files from `phala --help` output.
 * Run: node scripts/generate-cli-docs.js
 */

const { execSync } = require("child_process");
const fs = require("fs");
const path = require("path");

// Configuration - use process.cwd() for portability
const ROOT_DIR = process.cwd();
const OUTPUT_DIR = path.join(
  ROOT_DIR,
  "phala-cloud/references/phala-cloud-cli/phala"
);
const DOCS_JSON_PATH = path.join(ROOT_DIR, "docs.json");

// Commands to skip (deprecated or internal)
const SKIP_COMMANDS = new Set(["help", "completion"]);

// Files to preserve (manually edited, not auto-generated)
// These files won't be overwritten but will still be included in docs.json
const PRESERVE_FILES = new Set(["overview"]);

// Commands that are deprecated but should redirect to new commands
const DEPRECATED_REDIRECTS = {
  auth: "Use `phala login`, `phala logout`, and `phala status` instead.",
};

/**
 * Execute a command and return its output
 */
function runCommand(args) {
  try {
    const command = `npx phala ${args.join(" ")} --help 2>&1`;
    return execSync(command, { encoding: "utf-8", timeout: 30000 });
  } catch (error) {
    if (error.stdout) {
      return error.stdout;
    }
    console.error(`Failed to run: phala ${args.join(" ")} --help`);
    return "";
  }
}

/**
 * Parse the help output into a structured Command object
 */
function parseHelpOutput(output, commandPath) {
  const lines = output.split("\n");

  const command = {
    name: commandPath[commandPath.length - 1] || "phala",
    description: "",
    usage: "",
    options: [],
    subcommands: [],
    examples: [],
    arguments: [],
    passThrough: null,
    deprecated: false,
    unstable: false,
  };

  let section = "";
  let currentExample = "";

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmedLine = line.trim();

    // Parse usage line
    if (trimmedLine.startsWith("Usage:")) {
      command.usage = trimmedLine.replace("Usage:", "").trim();
      continue;
    }

    // Parse description (line after usage, before sections)
    if (
      command.usage &&
      !command.description &&
      trimmedLine &&
      !trimmedLine.endsWith(":") &&
      !trimmedLine.startsWith("-") &&
      !trimmedLine.startsWith("<") &&
      section === ""
    ) {
      command.description = trimmedLine;
      // Check for deprecated/unstable markers
      if (command.description.includes("[DEPRECATED]")) {
        command.deprecated = true;
        command.description = command.description
          .replace("[DEPRECATED]", "")
          .trim();
      }
      if (command.description.includes("[UNSTABLE]")) {
        command.unstable = true;
        command.description = command.description
          .replace("[UNSTABLE]", "")
          .trim();
      }
      continue;
    }

    // Detect section headers
    if (trimmedLine === "Available commands:") {
      section = "commands";
      continue;
    }
    if (
      trimmedLine === "Options:" ||
      trimmedLine === "Global options:" ||
      trimmedLine === "Global Options:"
    ) {
      section = "options";
      continue;
    }
    if (trimmedLine === "Arguments:") {
      section = "arguments";
      continue;
    }
    if (trimmedLine === "Examples:") {
      section = "examples";
      continue;
    }
    if (trimmedLine.startsWith("Pass-through")) {
      section = "passthrough";
      command.passThrough = "";
      continue;
    }

    // Parse sections
    if (section === "commands" && trimmedLine) {
      // Format: "  command-name    Description [DEPRECATED]"
      const match = trimmedLine.match(
        /^(\S+)\s+(.+?)(?:\s+\[(DEPRECATED|UNSTABLE)\])?(?:\s+\[(DEPRECATED|UNSTABLE)\])?$/
      );
      if (match) {
        const subCmd = {
          name: match[1],
          description: match[2].trim(),
          deprecated: false,
          unstable: false,
        };
        if (
          trimmedLine.includes("[DEPRECATED]") ||
          match[3] === "DEPRECATED" ||
          match[4] === "DEPRECATED"
        ) {
          subCmd.deprecated = true;
        }
        if (
          trimmedLine.includes("[UNSTABLE]") ||
          match[3] === "UNSTABLE" ||
          match[4] === "UNSTABLE"
        ) {
          subCmd.unstable = true;
        }
        command.subcommands.push(subCmd);
      }
    }

    if (section === "options" && trimmedLine) {
      // Format variations:
      // "  -h, --help              Description"
      // "  --api-token TOKEN, --api-key TOKENAPI token used for authentication"
      // "  --cvm-id <value>        Description"
      // "  -n, --name <value>      Description"
      // "  -t, --instance-type <value>Instance type..." (no space between <value> and description)

      // Look for pattern: flags (with optional value placeholder) followed by 2+ spaces then description
      let optMatch = trimmedLine.match(/^(-[^\s]+(?:[\s,]+(?:<[^>]+>|\w+|--[^\s]+))*)\s{2,}(.+)$/);

      // Fallback: handle cases where description immediately follows <value> with no space
      // e.g., "-t, --instance-type <value>Instance type..."
      if (!optMatch) {
        optMatch = trimmedLine.match(/^(-[^\s]+(?:,\s*-[^\s]+)?(?:\s+<[^>]+>)?)([A-Z].*)$/);
      }

      if (optMatch) {
        let flags = optMatch[1].trim();
        let description = optMatch[2].trim();
        let defaultValue;

        // Clean up flags - keep only the flag parts, move <value> to description context
        // For display, format as: --flag <value>
        const flagParts = flags.split(/,\s*/);
        const cleanFlags = flagParts.map(part => {
          // Handle cases like "--cvm-id <value>" or "--api-token TOKEN"
          return part.trim();
        }).join(", ");

        // Extract default value if present
        const defaultMatch = description.match(/\(default:\s*([^)]+)\)/);
        if (defaultMatch) {
          defaultValue = defaultMatch[1];
        }

        command.options.push({
          flags: cleanFlags,
          description,
          defaultValue,
        });
      }
    }

    if (section === "arguments" && trimmedLine) {
      // Format: "  <arg-name>?     Description"
      if (trimmedLine.startsWith("<") || trimmedLine.match(/^\S+\s+/)) {
        command.arguments.push(trimmedLine);
      }
    }

    if (section === "examples") {
      if (trimmedLine.startsWith("#")) {
        // Comment line, start new example
        if (currentExample) {
          command.examples.push(currentExample.trim());
        }
        currentExample = trimmedLine + "\n";
      } else if (trimmedLine.startsWith("phala ")) {
        currentExample += trimmedLine + "\n";
      } else if (trimmedLine && currentExample) {
        currentExample += trimmedLine + "\n";
      }
    }

    if (section === "passthrough") {
      command.passThrough += line + "\n";
    }
  }

  // Add last example
  if (currentExample) {
    command.examples.push(currentExample.trim());
  }

  return command;
}

/**
 * Generate MDX content for a command
 */
function generateMdx(command, commandPath) {
  const fullCommand = ["phala", ...commandPath.slice(1)].join(" ");
  let title =
    commandPath.length > 1
      ? commandPath[commandPath.length - 1]
      : "Overview";

  // Add deprecation marker to title
  if (command.deprecated) {
    title += " (Deprecated)";
  }

  let mdx = `---
title: "${title}"
description: "${escapeForYaml(command.description || `Reference for the ${fullCommand} command`)}"
---

`;

  // Add deprecation notice
  if (command.deprecated) {
    mdx += `<Warning>
This command is deprecated. ${DEPRECATED_REDIRECTS[command.name] || "See the newer alternatives."}
</Warning>

`;
  }

  // Add unstable notice
  if (command.unstable) {
    mdx += `<Note>
This command is marked as unstable and may change in future releases.
</Note>

`;
  }

  // Command header
  if (commandPath.length > 1) {
    mdx += `## Command: \`${fullCommand}\`\n\n`;
  } else {
    mdx += `## Base Command: \`phala\`\n\n`;
  }

  // Syntax
  mdx += `### Syntax\n\n`;
  mdx += "```\n";
  mdx += command.usage + "\n";
  mdx += "```\n\n";

  // Description
  mdx += `### Description\n\n`;
  mdx += `${command.description}\n\n`;

  // Arguments
  if (command.arguments.length > 0) {
    mdx += `### Arguments\n\n`;
    mdx += `| Argument | Description |\n`;
    mdx += `| -------- | ----------- |\n`;
    for (const arg of command.arguments) {
      const parts = arg.match(/^(\S+)\s+(.*)$/);
      if (parts) {
        mdx += `| \`${parts[1]}\` | ${parts[2]} |\n`;
      } else {
        mdx += `| \`${arg}\` | - |\n`;
      }
    }
    mdx += "\n";
  }

  // Options table
  if (command.options.length > 0) {
    mdx += `### Options\n\n`;
    mdx += `| Option | Description |\n`;
    mdx += `| ------ | ----------- |\n`;
    for (const opt of command.options) {
      const desc = opt.description;
      mdx += `| \`${opt.flags}\` | ${escapeForTable(desc)} |\n`;
    }
    mdx += "\n";
  }

  // Subcommands tables (separate active from deprecated)
  if (command.subcommands.length > 0) {
    const activeSubcommands = command.subcommands.filter(sub => !sub.deprecated);
    const deprecatedSubcommands = command.subcommands.filter(sub => sub.deprecated);

    // Active subcommands
    if (activeSubcommands.length > 0) {
      mdx += `### Subcommands\n\n`;
      mdx += `| Command | Description |\n`;
      mdx += `| ------- | ----------- |\n`;
      for (const sub of activeSubcommands) {
        mdx += `| \`${sub.name}\` | ${escapeForTable(sub.description)} |\n`;
      }
      mdx += "\n";
    }

    // Deprecated subcommands
    if (deprecatedSubcommands.length > 0) {
      mdx += `### Deprecated Subcommands\n\n`;
      mdx += `| Command | Description |\n`;
      mdx += `| ------- | ----------- |\n`;
      for (const sub of deprecatedSubcommands) {
        mdx += `| \`${sub.name}\` | ${escapeForTable(sub.description)} |\n`;
      }
      mdx += "\n";
    }
  }

  // Pass-through section
  if (command.passThrough) {
    mdx += `### Pass-through Arguments\n\n`;
    mdx += command.passThrough
      .split("\n")
      .map((line) => line.trim())
      .filter((line) => line)
      .join("\n\n");
    mdx += "\n\n";
  }

  // Examples
  if (command.examples.length > 0) {
    mdx += `### Examples\n\n`;
    for (const example of command.examples) {
      const lines = example.split("\n");
      for (const line of lines) {
        if (line.startsWith("#")) {
          // Comment becomes description
          mdx += `${line.replace("#", "*").trim()}\n\n`;
        } else if (line.startsWith("phala ")) {
          mdx += "```bash\n";
          mdx += line + "\n";
          mdx += "```\n\n";
        }
      }
    }
  } else {
    // Default examples
    mdx += `### Examples\n\n`;
    mdx += `* Display help:\n\n`;
    mdx += "```bash\n";
    mdx += `${fullCommand} --help\n`;
    mdx += "```\n";
  }

  // Replace placeholder domains with realistic Phala examples
  // TODO: Remove this workaround once CLI is fixed upstream
  // See: https://github.com/Phala-Network/phala-cloud/issues/139
  mdx = mdx.replace(/dstack-gateway\.example\.com/g, "dstack-prod5.phala.network");

  return mdx;
}

/**
 * Escape special characters for YAML frontmatter
 */
function escapeForYaml(str) {
  return str.replace(/"/g, '\\"').replace(/\n/g, " ");
}

/**
 * Escape special characters for markdown tables
 */
function escapeForTable(str) {
  return str.replace(/\|/g, "\\|").replace(/\n/g, " ");
}

/**
 * Get all commands recursively
 */
function getAllCommands() {
  const commands = new Map();

  // Get root command
  const rootOutput = runCommand([]);
  const rootCommand = parseHelpOutput(rootOutput, ["phala"]);
  commands.set("overview", rootCommand);

  console.log(`Found ${rootCommand.subcommands.length} top-level commands`);

  // Get each top-level command
  for (const subCmd of rootCommand.subcommands) {
    if (SKIP_COMMANDS.has(subCmd.name)) {
      console.log(`  Skipping: ${subCmd.name}`);
      continue;
    }

    console.log(`  Processing: ${subCmd.name}`);
    const cmdOutput = runCommand([subCmd.name]);
    const cmd = parseHelpOutput(cmdOutput, ["phala", subCmd.name]);

    // Inherit deprecated/unstable status from parent's subcommand info
    if (subCmd.deprecated) cmd.deprecated = true;
    if (subCmd.unstable) cmd.unstable = true;

    commands.set(subCmd.name, cmd);

    // Get subcommands for this command (for reference in the same page)
    if (cmd.subcommands.length > 0) {
      console.log(`    Found ${cmd.subcommands.length} subcommands`);
    }
  }

  return commands;
}

/**
 * Generate MDX files for all commands
 */
function generateMdxFiles(commands) {
  const generatedFiles = [];

  // Ensure output directory exists
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  for (const [name, command] of commands) {
    const filename = `${name}.mdx`;
    const filepath = path.join(OUTPUT_DIR, filename);

    // Skip preserved files (manually edited)
    if (PRESERVE_FILES.has(name)) {
      console.log(`Preserved: ${filepath} (manually edited)`);
      generatedFiles.push(name);
      continue;
    }

    const commandPath = name === "overview" ? ["phala"] : ["phala", name];
    const mdxContent = generateMdx(command, commandPath);
    fs.writeFileSync(filepath, mdxContent);
    console.log(`Generated: ${filepath}`);
    generatedFiles.push(name);
  }

  return generatedFiles;
}

/**
 * Update docs.json with new CLI pages
 */
function updateDocsJson(commandNames) {
  const docsJson = JSON.parse(fs.readFileSync(DOCS_JSON_PATH, "utf-8"));

  // Define the order of commands
  const commandOrder = [
    "overview",
    "login",
    "logout",
    "status",
    "deploy",
    "cvms",
    "ssh",
    "cp",
    "docker",
    "simulator",
    "nodes",
    "config",
    "auth", // deprecated, at the end
  ];

  // Sort command names by the defined order
  const sortedNames = commandNames.sort((a, b) => {
    const aIndex = commandOrder.indexOf(a);
    const bIndex = commandOrder.indexOf(b);
    if (aIndex === -1 && bIndex === -1) return a.localeCompare(b);
    if (aIndex === -1) return 1;
    if (bIndex === -1) return -1;
    return aIndex - bIndex;
  });

  // Build the new pages array
  const cliPages = sortedNames.map(
    (name) => `/phala-cloud/references/phala-cloud-cli/phala/${name}`
  );

  // Find and update the CLI Reference group in docs.json
  function findAndUpdateCliGroup(obj) {
    if (Array.isArray(obj)) {
      for (const item of obj) {
        if (typeof item === "object" && item !== null) {
          if (findAndUpdateCliGroup(item)) return true;
        }
      }
    } else if (typeof obj === "object" && obj !== null) {
      if (obj.group === "CLI Reference") {
        obj.pages = cliPages;
        return true;
      }
      for (const key of Object.keys(obj)) {
        const value = obj[key];
        if (typeof value === "object" && value !== null) {
          if (findAndUpdateCliGroup(value)) return true;
        }
      }
    }
    return false;
  }

  if (findAndUpdateCliGroup(docsJson)) {
    fs.writeFileSync(DOCS_JSON_PATH, JSON.stringify(docsJson, null, 2) + "\n");
    console.log(`Updated: ${DOCS_JSON_PATH}`);
  } else {
    console.error("Could not find CLI Reference group in docs.json");
  }
}

/**
 * Main function
 */
function main() {
  console.log("Generating CLI documentation from phala --help...\n");

  // Get all commands
  const commands = getAllCommands();
  console.log(`\nTotal commands found: ${commands.size}\n`);

  // Generate MDX files
  const generatedFiles = generateMdxFiles(commands);
  console.log(`\nGenerated ${generatedFiles.length} MDX files\n`);

  // Update docs.json
  updateDocsJson(generatedFiles);

  console.log("\nDone! Run 'npx mintlify dev' to preview the documentation.");
}

main();
