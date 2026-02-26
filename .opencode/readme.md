# OpenCode Configuration

This repository uses OpenCode for AI agent task execution and management.

## Overview

This is the official OpenAI Skills repository - a collection of AI agent skills that can be discovered and used by Codex and other AI agents to perform specific tasks in a repeatable way.

## Documentation

- [OpenCode Official Docs](https://opencode.ai/docs)
- [SDK Documentation](https://opencode.ai/docs/sdk)
- [Agents Configuration](https://opencode.ai/docs/agents/)
- [Skills Configuration](https://opencode.ai/docs/skills/)
- [LSP Servers](https://opencode.ai/docs/lsp/)
- [Custom Tools](https://opencode.ai/docs/custom-tools/)
- [Plugins](https://opencode.ai/docs/plugins/)

## OpenCode Zen (Free Models)

OpenCode Zen is a curated list of tested and verified models provided by the OpenCode team. It includes free models:

| Model | Input | Output |
|-------|-------|--------|
| MiniMax M2.5 Free | Free | Free |
| Big Pickle | Free | Free |

- [OpenCode Zen Documentation](https://opencode.ai/docs/zen/)

This repository is configured to use the free `opencode/minimax-m2.5-free` model by default.

## Installation

### Install OpenCode

```bash
curl -fsSL https://opencode.ai/install | bash
```

Or using npm:

```bash
npm install -g opencode-ai
```

Or using Bun:

```bash
bun install -g opencode-ai
```

Or using pnpm:

```bash
pnpm install -g opencode-ai
```

Or using Yarn:

```bash
yarn global add opencode-ai
```

### Verify Installation

```bash
opencode --version
```

### Initialize

Run the following command in your project:

```bash
opencode
/init
```

This will analyze your project and create an `AGENTS.md` file.

## Configuration

### opencode.json

The main configuration file is at `.opencode/opencode.json`. It configures:

- **Model**: Default model is `opencode/minimax-m2.5-free` (free tier)
- **Permissions**: Skill loading permissions
- **Agents**: Custom agent configurations

Example configuration:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "opencode/minimax-m2.5-free",
  "permission": {
    "skill": {
      "*": "allow",
      "experimental-*": "ask"
    }
  },
  "agent": {
    "plan": {
      "model": "opencode/minimax-m2.5-free"
    },
    "build": {
      "model": "opencode/minimax-m2.5-free"
    },
    "explore": {
      "model": "opencode/minimax-m2.5-free"
    }
  }
}
```

### Agents

Custom agents can be defined in `.opencode/agents/`. Agents can be configured as:

- **Primary agents**: Main assistants for development work
- **Subagents**: Specialized assistants invoked via @mentions

Example agent definition (`.opencode/agents/example.md`):

```markdown
---
description: Example agent for specific tasks
mode: subagent
model: opencode/minimax-m2.5-free
tools:
  write: true
  edit: true
  bash: false
---
You are a specialized agent for example tasks.
```

See [Agents Documentation](https://opencode.ai/docs/agents/) for details.

### Skills

Skills are defined in `.opencode/skills/` following the [Agent Skills](https://opencode.ai/docs/skills/) specification.

Each skill follows this structure:

```
skill-name/
├── SKILL.md           # Skill definition (required)
├── LICENSE.txt        # License (required)
├── agents/            # Agent-specific instructions
├── assets/            # Static assets
└── scripts/           # Helper scripts
```

SKILL.md must include frontmatter with:

- `name` (required): Skill identifier
- `description` (required): What the skill does
- `license` (optional): License name
- `compatibility` (optional): Compatible platforms

## Directory Structure

```
.opencode/
├── opencode.json    # Main configuration
├── readme.md        # This file
├── agents/          # Custom agent definitions
│   ├── ai-agent-engineer.md
│   ├── skill-qa.md
│   └── dx-engineer.md
└── skills/          # Custom skill definitions
    └── repo-manager/
        ├── SKILL.md
        └── LICENSE.txt
```

## GitHub Workflow

This repository uses OpenCode in its GitHub Actions workflow (see `.github/workflows/main.yml`) to:

1. **Architect Stage**: Analyze repository state and create issues
2. **Specialists Stage**: Execute domain-specific improvements
3. **Fixer Stage**: Improve repository efficiency and configuration
4. **PR Handler Stage**: Merge qualified pull requests

## Usage

### Ask Questions

```bash
How is authentication handled in @src/auth.ts
```

### Add Features

1. Press **Tab** to enter Plan mode
2. Describe the feature you want
3. Press **Tab** to switch to Build mode
4. Ask to implement the changes

### Make Changes

```bash
Add authentication to the /settings route.
```

### Undo Changes

```bash
/undo
```

### Share Sessions

```bash
/share
```

## Customize

- [Themes](https://opencode.ai/docs/themes)
- [Keybinds](https://opencode.ai/docs/keybinds)
- [Formatters](https://opencode.ai/docs/formatters)
- [Commands](https://opencode.ai/docs/commands)

## License

Individual skills have their own licenses found in their respective `LICENSE.txt` files.
