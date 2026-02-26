# OpenCode Configuration

This repository uses OpenCode for AI agent task execution and management.

## Overview

This is the official OpenAI Skills repository - a collection of AI agent skills that can be discovered and used by Codex and other AI agents to perform specific tasks.

## Documentation

- [OpenCode Official Docs](https://opencode.ai/docs)
- [SDK Documentation](https://opencode.ai/docs/sdk)
- [Agents Configuration](https://opencode.ai/docs/agents/)
- [Skills Configuration](https://opencode.ai/docs/skills/)
- [LSP Servers](https://opencode.ai/docs/lsp/)
- [Custom Tools](https://opencode.ai/docs/custom-tools/)
- [Plugins](https://opencode.ai/docs/plugins/)

## OpenCode Zen (Free Models)

OpenCode provides free models through OpenCode Zen:
- [OpenCode Zen Documentation](https://opencode.ai/docs/zen/)

This repository is configured to use the free `opencode/minimax-m2.5-free` model by default.

## Configuration

### opencode.json

The main configuration file is at `.opencode/opencode.json`. It configures:

- **Model**: Default model is `opencode/minimax-m2.5-free` (free tier)
- **Permissions**: Skill loading permissions
- **Agents**: Custom agent configurations

### Agents

Custom agents can be defined in `.opencode/agents/`. See [Agents Documentation](https://opencode.ai/docs/agents/) for details.

### Skills

Skills are defined in `.opencode/skills/` following the [Agent Skills](https://opencode.ai/docs/skills/) specification.

## Directory Structure

```
.opencode/
├── opencode.json    # Main configuration
├── agents/          # Custom agent definitions
├── skills/          # Custom skill definitions
└── readme.md        # This file
```

## GitHub Workflow

This repository uses OpenCode in its GitHub Actions workflow (see `.github/workflows/main.yml`) to:

1. Analyze repository state
2. Plan improvements
3. Implement changes
4. Verify and test
5. Create pull requests

## Getting Started

1. Install OpenCode: `curl -fsSL https://opencode.ai/install | bash`
2. Run OpenCode: `opencode`
3. Initialize: `/init`

## License

Individual skills have their own licenses found in their respective `LICENSE.txt` files.
