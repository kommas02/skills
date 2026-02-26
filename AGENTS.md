# Agent Guidelines

## Repository Purpose

This is the official **OpenAI Skills** repository - a collection of AI agent capabilities (skills) that can be discovered and used by Codex and other AI agents to perform specific tasks in a repeatable way.

## Project Structure

```
.
├── .github/workflows/     # CI/CD workflows using OpenCode
├── .opencode/             # OpenCode configuration
│   ├── opencode.json      # Main configuration
│   ├── agents/            # Custom agent definitions
│   ├── skills/            # Custom skill definitions
│   └── readme.md          # OpenCode documentation
├── docs/                  # Documentation
│   ├── evaluation-framework.md
│   ├── quality-assurance.md
│   └── ui-ux-engineer.md
├── scripts/               # Utility scripts
│   └── evaluate_skill.py
├── skills/                 # Agent skills
│   ├── .system/           # System skills (auto-installed in Codex)
│   │   ├── skill-creator/
│   │   └── skill-installer/
│   └── .curated/          # Curated skills
│       ├── cloudflare-deploy/
│       ├── develop-web-game/
│       ├── doc/
│       ├── figma/
│       ├── figma-implement-design/
│       ├── gh-address-comments/
│       ├── gh-fix-ci/
│       ├── imagegen/
│       ├── jupyter-notebook/
│       ├── linear/
│       ├── netlify-deploy/
│       ├── notion-knowledge-capture/
│       ├── notion-meeting-intelligence/
│       ├── notion-research-documentation/
│       ├── notion-spec-to-implementation/
│       ├── openai-docs/
│       └── pdf/
├── README.md
└── contributing.md
```

## Skills Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md           # Skill definition (required)
├── LICENSE.txt        # License (required)
├── agents/            # Agent-specific instructions
├── assets/            # Static assets
└── scripts/           # Helper scripts
```

## Key Conventions

1. **Skill Naming**: lowercase alphanumeric with single hyphen separators
2. **Frontmatter**: SKILL.md must include `name` and `description` fields
3. **Licensing**: Each skill must have a LICENSE.txt file
4. **System Skills**: Located in `skills/.system/` - auto-installed in Codex
5. **Curated Skills**: Located in `skills/.curated/` - can be installed via `$skill-installer`

## For AI Agents

When working in this repository:

- Focus on improving skills, documentation, and CI/CD workflows
- Follow the issue/PRODUCT workflow defined in contributing.md
- Be mindful of security (see security@openai.com for vulnerabilities)
- Use the evaluation framework in docs/ for skill quality assessment

## Model Configuration

This repository uses OpenCode's free tier:
- Default model: `opencode/minimax-m2.5-free`
- See `.opencode/opencode.json` for full configuration
