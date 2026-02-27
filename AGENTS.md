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
│   ├── blueprint.md              # Project blueprint
│   ├── evaluation-framework.md    # Skill evaluation framework
│   ├── quality-assurance.md       # QA guidelines
│   ├── skill-schema.md           # Skill JSON schema
│   ├── skill-template.md         # Skill template
│   ├── skill-telemetry-schema.json # Telemetry schema
│   ├── ui-ux-engineer.md         # UI/UX engineer memory
│   ├── ai-agent-engineer.md      # AI agent engineer notes
│   ├── backend-engineer.md       # Backend engineer notes
│   ├── DX-engineer.md            # DX engineer notes
│   ├── frontend-engineer.md      # Frontend engineer notes
│   ├── platform-engineer.md      # Platform engineer notes
│   ├── security-engineer.md      # Security engineer notes
│   ├── technical-writer.md       # Technical writer notes
│   ├── user-story-engineer.md    # User story engineer notes
│   ├── Product-Architect.md      # Product architect notes
│   ├── Growth-Innovation-Strategist.md # Growth strategy notes
│   └── RnD.md                    # Research & Development notes
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
│       ├── doc-test/
│       ├── figma/
│       ├── figma-implement-design/
│       ├── gh-address-comments/
│       ├── gh-fix-ci/
│       ├── growth-innovation-strategist/
│       ├── imagegen/
│       ├── jupyter-notebook/
│       ├── linear/
│       ├── netlify-deploy/
│       ├── notion-knowledge-capture/
│       ├── notion-meeting-intelligence/
│       ├── notion-research-documentation/
│       ├── notion-spec-to-implementation/
│       ├── openai-docs/
│       ├── pdf/
│       ├── playwright/
│       ├── render-deploy/
│       ├── screenshot/
│       ├── security-best-practices/
│       ├── security-ownership-map/
│       ├── security-threat-model/
│       ├── sentry/
│       ├── sora/
│       ├── speech/
│       ├── spreadsheet/
│       ├── transcribe/
│       ├── vercel-deploy/
│       └── yeet/
├── README.md
└── contributing.md
```

## Skills Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md           # Skill definition with frontmatter (required)
├── skill.json         # Metadata for discovery and versioning (required)
├── LICENSE.txt        # License file (required)
├── agents/            # Agent-specific instructions
│   └── openai.yaml    # Codex agent configuration
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
