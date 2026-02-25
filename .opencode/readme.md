# OpenCode Configuration

This repository contains OpenCode configuration for managing the Agent Skills repository.

## Overview

This `.opencode/` directory provides:
- Custom agents for repository management
- Skills for AI-assisted development
- Documentation and reference materials

## Directory Structure

```
.opencode/
├── readme.md          # This file
├── agents/            # Custom agent definitions
│   └── *.md          # Agent configuration files
└── skills/           # OpenCode skills
    └── */SKILL.md    # Skill definitions
```

## Resources

### Installation & Setup
- [OpenCode Installation Guide](https://opencode.ai/docs)
- [oh-my-opencode Installation](https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/refs/heads/master/docs/guide/installation.md)

### Documentation
- [OpenCode Docs](https://opencode.ai/docs)
- [SDK Documentation](https://opencode.ai/docs/sdk)
- [Agents Documentation](https://opencode.ai/docs/agents/)
- [Skills Documentation](https://opencode.ai/docs/skills/)
- [LSP Servers](https://opencode.ai/docs/lsp/)
- [Custom Tools](https://opencode.ai/docs/custom-tools/)
- [Plugins](https://opencode.ai/docs/plugins/)

### Free Models
- [OpenCode Zen](https://opencode.ai/docs/zen/) - Free models for OpenCode

## Available Agents

See `.opencode/agents/` directory for custom agent configurations.

## Available Skills

See `.opencode/skills/` directory for skill definitions.

## Usage

### Running OpenCode

```bash
opencode
```

### Initialize for a project

```bash
opencode /init
```

### Using Skills

Agents can discover and use skills from:
- `.opencode/skills/<name>/SKILL.md` (project-local)
- `~/.config/opencode/skills/<name>/SKILL.md` (global)

### Using Agents

Custom agents can be invoked via:
- `@agentname` mention in conversation
- Task tool for subagents

## Configuration

OpenCode reads configuration from:
1. Project `.opencode/` directory
2. Global `~/.config/opencode/` directory

## Notes

This repository is primarily for OpenAI Codex skills. The `.opencode/` configuration enhances AI agent integration and productivity when working with this repository.
