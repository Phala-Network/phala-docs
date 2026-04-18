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
  "phala-cloud/phala-cloud-cli"
);
const DOCS_JSON_PATH = path.join(ROOT_DIR, "docs.json");

// Commands to skip (deprecated or internal)
const SKIP_COMMANDS = new Set(["help", "completion"]);

// Files to preserve (manually edited, not auto-generated)
// These files won't be overwritten but will still be included in docs.json
const PRESERVE_FILES = new Set(["overview", "link"]);

// Commands that are deprecated but should redirect to new commands
const DEPRECATED_REDIRECTS = {
  auth: "Use `phala login`, `phala logout`, and `phala status` instead.",
};

/**
 * Execute a command and return its output
 */
function runCommand(args) {
  // Try global `phala` first, fall back to `npx phala`
  const binaries = ["phala", "npx phala"];
  for (const bin of binaries) {
    try {
      const command = `${bin} ${args.join(" ")} --help 2>&1`;
      return execSync(command, { encoding: "utf-8", timeout: 30000 });
    } catch (error) {
      if (error.stdout) {
        return error.stdout;
      }
    }
  }
  console.error(`Failed to run: phala ${args.join(" ")} --help`);
  return "";
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
    optionGroups: {}, // { groupName: [option, ...] }
    subcommands: [],
    examples: [],
    arguments: [],
    passThrough: null,
    deprecated: false,
    unstable: false,
  };

  let section = "";
  let currentOptionGroup = "";
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
    // Match both "Available commands:" and grouped headers like "Deploy:", "Manage:", etc.
    if (trimmedLine === "Available commands:" || trimmedLine === "Subcommands:") {
      section = "commands";
      continue;
    }
    if (
      section !== "options" &&
      section !== "arguments" &&
      section !== "examples" &&
      section !== "passthrough" &&
      /^[A-Z][a-zA-Z /]+:$/.test(trimmedLine) &&
      !trimmedLine.startsWith("Usage:") &&
      !trimmedLine.startsWith("Options:") &&
      !trimmedLine.startsWith("Global") &&
      !trimmedLine.startsWith("Arguments:") &&
      !trimmedLine.startsWith("Examples:") &&
      !trimmedLine.startsWith("Pass-through")
    ) {
      // "Help topics:" lists bundled help topics (e.g., `phala help envs`),
      // not real commands — skip the whole section.
      if (trimmedLine === "Help topics:") {
        section = "helpTopics";
        continue;
      }
      // Command group header (e.g., "Deploy:", "Manage:", "CVM operations:")
      section = "commands";
      continue;
    }
    if (
      trimmedLine === "Options:" ||
      trimmedLine === "Global options:" ||
      trimmedLine === "Global Options:" ||
      trimmedLine === "Basic options:" ||
      trimmedLine === "Basic Options:" ||
      trimmedLine === "Advanced options:" ||
      trimmedLine === "Advanced Options:" ||
      trimmedLine === "Deprecated options:" ||
      trimmedLine === "Deprecated Options:"
    ) {
      section = "options";
      // Map help group names to MDX section names
      if (trimmedLine.toLowerCase().startsWith("global")) {
        currentOptionGroup = "Global Options";
      } else if (trimmedLine.toLowerCase().startsWith("advanced")) {
        currentOptionGroup = "Advanced Options";
      } else if (trimmedLine.toLowerCase().startsWith("deprecated")) {
        currentOptionGroup = "Deprecated Options";
      } else if (trimmedLine.toLowerCase().startsWith("basic")) {
        currentOptionGroup = "Options";
      } else {
        currentOptionGroup = "Options";
      }
      if (!command.optionGroups[currentOptionGroup]) {
        command.optionGroups[currentOptionGroup] = [];
      }
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
      // Subcommand entries are always indented. Lines at column 0
      // (e.g. trailing prose like `Use "phala help <topic>" to read a topic.`)
      // are not commands.
      if (!/^\s{2,}/.test(line)) {
        continue;
      }
      // Format: "  command-name    Description [DEPRECATED]"
      // Also handles "  command (alias)    Description" by stripping the
      // "(alias)" marker from the description after matching.
      const match = trimmedLine.match(
        /^(\S+)\s+(.+?)(?:\s+\[(DEPRECATED|UNSTABLE)\])?(?:\s+\[(DEPRECATED|UNSTABLE)\])?$/
      );
      if (match) {
        let description = match[2].trim();
        // Strip leading alias markers like "(list)" from descriptions
        description = description.replace(/^\([^)]+\)\s+/, "");
        const subCmd = {
          name: match[1],
          description,
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

        const opt = {
          flags: cleanFlags,
          description,
          defaultValue,
        };
        command.options.push(opt);
        if (currentOptionGroup && command.optionGroups[currentOptionGroup]) {
          command.optionGroups[currentOptionGroup].push(opt);
        }
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

function h(level) {
  return "#".repeat(level);
}

/**
 * Render the body of a command (without frontmatter) at a given heading level.
 */
function renderCommandBody(command, commandPath, level) {
  const fullCommand = ["phala", ...commandPath.slice(1)].join(" ");
  let mdx = "";

  // Command header
  if (commandPath.length > 1) {
    mdx += `${h(level)} Command: \`${fullCommand}\`\n\n`;
  } else {
    mdx += `${h(level)} Base Command: \`phala\`\n\n`;
  }

  // Syntax
  mdx += `${h(level + 1)} Syntax\n\n`;
  mdx += "```\n";
  mdx += command.usage + "\n";
  mdx += "```\n\n";

  // Description
  mdx += `${h(level + 1)} Description\n\n`;
  mdx += `${command.description}\n\n`;

  // Arguments
  if (command.arguments.length > 0) {
    mdx += `${h(level + 1)} Arguments\n\n`;
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

  // Options tables (grouped)
  if (command.options.length > 0) {
    const groupNames = Object.keys(command.optionGroups);
    const hasNonGlobalGroups = groupNames.some(g => g !== "Global Options");

    if (hasNonGlobalGroups) {
      // Render groups in order: Options, Advanced Options, Deprecated Options, Global Options
      const groupOrder = ["Options", "Advanced Options", "Deprecated Options", "Global Options"];
      for (const groupName of groupOrder) {
        const groupOpts = command.optionGroups[groupName];
        if (groupOpts && groupOpts.length > 0) {
          mdx += `${h(level + 1)} ${groupName}\n\n`;
          mdx += `| Option | Description |\n`;
          mdx += `| ------ | ----------- |\n`;
          for (const opt of groupOpts) {
            mdx += `| \`${opt.flags}\` | ${escapeForTable(opt.description)} |\n`;
          }
          mdx += "\n";
        }
      }
    } else {
      // Only global options — just render as "Global Options"
      const globalOpts = command.optionGroups["Global Options"];
      if (globalOpts && globalOpts.length > 0) {
        mdx += `${h(level + 1)} Global Options\n\n`;
        mdx += `| Option | Description |\n`;
        mdx += `| ------ | ----------- |\n`;
        for (const opt of globalOpts) {
          mdx += `| \`${opt.flags}\` | ${escapeForTable(opt.description)} |\n`;
        }
        mdx += "\n";
      }
    }
  }

  // Pass-through section
  if (command.passThrough) {
    mdx += `${h(level + 1)} Pass-through Arguments\n\n`;
    mdx += command.passThrough
      .split("\n")
      .map((line) => line.trim())
      .filter((line) => line)
      .join("\n\n");
    mdx += "\n\n";
  }

  // Examples
  if (command.examples.length > 0) {
    mdx += `${h(level + 1)} Examples\n\n`;
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
    mdx += `${h(level + 1)} Examples\n\n`;
    mdx += `* Display help:\n\n`;
    mdx += "```bash\n";
    mdx += `${fullCommand} --help\n`;
    mdx += "```\n";
  }

  return mdx;
}

/**
 * Generate MDX content for a command
 */
function generateMdx(command, commandPath, isStandalone = false) {
  let title;
  if (commandPath.length > 2) {
    // Subcommand — use "parent sub" form so sidebar matches CLI invocation
    title = commandPath.slice(1).join(" ");
  } else if (commandPath.length > 1) {
    // Parent/top-level command
    title = commandPath[commandPath.length - 1];
  } else {
    title = "Overview";
  }

  // Add deprecation marker to title
  if (command.deprecated) {
    title += " (Deprecated)";
  }

  const hasSubcommands = command.subcommands && command.subcommands.length > 0;
  const hiddenAttr = !isStandalone && hasSubcommands ? "\nhidden: true" : "";

  let mdx = `---
title: "${escapeForYaml(title)}"
description: "${escapeForYaml(command.description || `Reference for the ${["phala", ...commandPath.slice(1)].join(" ")} command`)}"${hiddenAttr}
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

  // Heading level: standalone pages use ##, parent pages use ###
  const level = isStandalone ? 2 : 3;
  mdx += renderCommandBody(command, commandPath, level);

  // Subcommands summary table — only on parent pages
  if (!isStandalone && command.subcommands.length > 0) {
    const activeSubcommands = command.subcommands.filter(sub => !sub.deprecated);
    const deprecatedSubcommands = command.subcommands.filter(sub => sub.deprecated);

    if (activeSubcommands.length > 0) {
      mdx += `### Subcommands\n\n`;
      mdx += `| Command | Description |\n`;
      mdx += `| ------- | ----------- |\n`;
      for (const sub of activeSubcommands) {
        mdx += `| \`${sub.name}\` | ${escapeForTable(sub.description)} |\n`;
      }
      mdx += "\n";
    }

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
      cmd.subcommandDetails = [];
      for (const nestedSub of cmd.subcommands) {
        if (SKIP_COMMANDS.has(nestedSub.name)) continue;
        const nestedOutput = runCommand([subCmd.name, nestedSub.name]);
        const nestedCmd = parseHelpOutput(nestedOutput, ["phala", subCmd.name, nestedSub.name]);
        if (nestedSub.deprecated) nestedCmd.deprecated = true;
        if (nestedSub.unstable) nestedCmd.unstable = true;
        cmd.subcommandDetails.push(nestedCmd);
      }
    }
  }

  return commands;
}

/**
 * Generate MDX files for all commands and their subcommands
 */
function generateMdxFiles(commands) {
  const generatedFiles = [];
  const subcommandGroups = [];

  // Ensure output directory exists
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Generate parent command pages
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

  // Generate standalone subcommand pages
  for (const [name, command] of commands) {
    if (command.subcommandDetails && command.subcommandDetails.length > 0) {
      const subDir = path.join(OUTPUT_DIR, name);
      if (!fs.existsSync(subDir)) {
        fs.mkdirSync(subDir, { recursive: true });
      }

      const subPages = [];
      for (const sub of command.subcommandDetails) {
        if (SKIP_COMMANDS.has(sub.name)) continue;
        const subFile = path.join(subDir, `${sub.name}.mdx`);
        const subMdx = generateMdx(sub, ["phala", name, sub.name], true);
        fs.writeFileSync(subFile, subMdx);
        console.log(`Generated: ${subFile}`);
        subPages.push(sub.name);
      }

      if (subPages.length > 0) {
        subcommandGroups.push({ parent: name, pages: subPages });
      }
    }
  }

  return { generatedFiles, subcommandGroups };
}

/**
 * Update docs.json with new CLI pages and subcommand groups
 */
function updateDocsJson({ generatedFiles, subcommandGroups }) {
  const docsJson = JSON.parse(fs.readFileSync(DOCS_JSON_PATH, "utf-8"));

  // Build a set of parent commands that have subcommands
  const parentsWithSubcommands = new Set(subcommandGroups.map((g) => g.parent));

  // Build a map of parent path -> nested group for subcommands.
  // Entries are plain strings — the sidebar label comes from each MDX's
  // frontmatter `title`, which the generator sets to "parent sub".
  const subcommandMap = new Map();
  for (const { parent, pages } of subcommandGroups) {
    const groupPages = [`/phala-cloud/phala-cloud-cli/${parent}`];
    for (const sub of pages) {
      groupPages.push(`/phala-cloud/phala-cloud-cli/${parent}/${sub}`);
    }
    subcommandMap.set(parent, {
      group: parent,
      pages: groupPages,
    });
  }

  // Wrap a string path into a subcommand group if applicable.
  // For existing parent commands (like cvms, profiles), this turns the
  // flat string into the nested group. For new commands, same thing.
  function wrapIfNeeded(nameOrPath) {
    const name = typeof nameOrPath === "string"
      ? nameOrPath.replace("/phala-cloud/phala-cloud-cli/", "")
      : nameOrPath;
    if (subcommandMap.has(name)) {
      return subcommandMap.get(name);
    }
    return nameOrPath;
  }

  // Recursively process a pages array. Two jobs:
  //  - Replace a parent command's flat path with its subcommand group (only
  //    at the outermost level where the parent appears as a sibling of other
  //    commands — not inside its own already-wrapped group).
  //  - Recurse into existing groups to normalize legacy `{page, title}`
  //    objects back to plain strings (Mintlify `pages` entries must be a
  //    string or a nested `{group, pages}` — no other shapes are valid; the
  //    sidebar label comes from each MDX's frontmatter `title`).
  //
  // `insideGroup` is set while recursing into a group with that name; inside
  // it we must NOT re-wrap `/phala-cloud/phala-cloud-cli/<insideGroup>` into
  // another nested group, which would compound on each run.
  function processPages(pages, insideGroup = null) {
    if (!Array.isArray(pages)) return pages;
    const result = [];
    for (const page of pages) {
      if (typeof page === "string") {
        const name = page.replace("/phala-cloud/phala-cloud-cli/", "");
        if (name !== insideGroup && subcommandMap.has(name)) {
          result.push(subcommandMap.get(name));
        } else {
          result.push(page);
        }
      } else if (typeof page === "object" && page !== null && Array.isArray(page.pages)) {
        // If this group corresponds to a freshly-built subcommand group,
        // replace it outright so we emit a clean, flat list of strings.
        if (page.group && subcommandMap.has(page.group)) {
          result.push(subcommandMap.get(page.group));
        } else {
          result.push({ ...page, pages: processPages(page.pages, page.group || insideGroup) });
        }
      } else if (typeof page === "object" && page !== null && typeof page.page === "string") {
        result.push(page.page);
      } else {
        result.push(page);
      }
    }
    return result;
  }

  // Find and update the CLI Reference group in docs.json
  function findAndUpdateCliGroup(obj) {
    if (Array.isArray(obj)) {
      for (const item of obj) {
        if (typeof item === "object" && item !== null) {
          if (findAndUpdateCliGroup(item)) return true;
        }
      }
    } else if (typeof obj === "object" && obj !== null) {
      if (obj.group === "Phala Cloud CLI") {
        const pages = obj.pages;
        const isGrouped = pages.some((p) => typeof p === "object" && p.group);

        if (isGrouped) {
          // Collect existing leaf paths (strings and {page} objects)
          const existingPaths = new Set();
          const groupMap = {};
          function collectPaths(items) {
            for (const p of items) {
              if (typeof p === "string") {
                existingPaths.add(p);
              } else if (p.page) {
                existingPaths.add(p.page);
              } else if (p.group && Array.isArray(p.pages)) {
                groupMap[p.group] = p;
                collectPaths(p.pages);
              }
            }
          }
          collectPaths(pages);

          // Add any new parent commands
          generatedFiles.forEach((name) => {
            const pagePath = `/phala-cloud/phala-cloud-cli/${name}`;
            if (existingPaths.has(pagePath)) return;
            existingPaths.add(pagePath);

            if (name === "instances") {
              const manage = groupMap["Manage"];
              if (manage) {
                const idx = manage.pages.indexOf("/phala-cloud/phala-cloud-cli/apps");
                if (idx !== -1) {
                  manage.pages.splice(idx + 1, 0, pagePath);
                } else {
                  manage.pages.push(pagePath);
                }
              }
            } else {
              const firstGroupIndex = pages.findIndex((p) => typeof p === "object");
              if (firstGroupIndex !== -1) {
                pages.splice(firstGroupIndex, 0, pagePath);
              } else {
                pages.push(pagePath);
              }
            }
          });

          // Replace string paths with subcommand groups in one pass
          obj.pages = processPages(pages);
        } else {
          // Flat list fallback — reconstruct as flat strings
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
            "auth",
          ];
          const sortedNames = generatedFiles.sort((a, b) => {
            const aIndex = commandOrder.indexOf(a);
            const bIndex = commandOrder.indexOf(b);
            if (aIndex === -1 && bIndex === -1) return a.localeCompare(b);
            if (aIndex === -1) return 1;
            if (bIndex === -1) return -1;
            return aIndex - bIndex;
          });
          obj.pages = sortedNames.map(
            (name) => `/phala-cloud/phala-cloud-cli/${name}`
          );
        }
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
  const { generatedFiles, subcommandGroups } = generateMdxFiles(commands);
  const totalFiles = generatedFiles.length + subcommandGroups.reduce((sum, g) => sum + g.pages.length, 0);
  console.log(`\nGenerated ${totalFiles} MDX files (${generatedFiles.length} parents, ${subcommandGroups.length} subcommand groups)\n`);

  // Update docs.json
  updateDocsJson({ generatedFiles, subcommandGroups });

  console.log("\nDone! Run 'npx mintlify dev' to preview the documentation.");
}

main();
