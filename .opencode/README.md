# OpenCode Configuration

This directory contains OpenCode configuration for the Agent Skills repository.

## Structure

```
.opencode/
├── agents/           # Agent definitions (markdown)
│   ├── ai-agent-engineer.md
│   └── dx-engineer.md
├── commands/         # Custom commands (if needed)
├── plugins/          # Custom plugins (if needed)
└── skills/          # Additional skills (if needed)
```

## Configuration Files

- `opencode.json` - Main configuration file in project root
  - Model configuration
  - Agent definitions
  - Skills paths

## Available Agents

Defined in `opencode.json`:

- `rnd` - Research and Development
- `product-architect` - Product Architecture
- `ai-agent-engineer` - AI Agent Engineering
- `backend-engineer` - Backend Development
- `frontend-engineer` - Frontend Development
- `ui-ux-engineer` - UI/UX Design
- `platform-engineer` - Platform/DevOps
- `security-engineer` - Security
- `quality-assurance` - QA/Testing
- `dx-engineer` - Developer Experience
- `technical-writer` - Documentation
- `user-story-engineer` - Requirements
- `growth-innovation-strategist` - Growth/Innovation

## Skills

Skills are located in:
- `skills/.system/` - System skills (auto-installed)
- `skills/.curated/` - Curated skills

## Usage

Run OpenCode with specific agent:
```bash
opencode run --agent ai-agent-engineer "Your task"
```

Run with specific model:
```bash
opencode run --model opencode/minimax-m2.5-free "Your task"
```

## Skill Versioning

Skills use semantic versioning (semver) in the SKILL.md frontmatter:

```yaml
---
name: my-skill
description: Skill description
version: 1.0.0
---
```

### Version Format

- **MAJOR** (1.0.0 → 2.0.0): Breaking changes to skill behavior or API
- **MINOR** (1.0.0 → 1.1.0): New features, backward compatible
- **PATCH** (1.0.0 → 1.0.1): Bug fixes, backward compatible

### Auto-Generated Index

The `skills/index.json` is automatically generated and contains:
- All skills with their metadata
- Version information
- Category (.system or .curated)
- License type

The index is updated automatically via GitHub Actions when:
- SKILL.md files change
- LICENSE.txt files change

To regenerate manually:
```bash
python scripts/generate_skill_index.py
```
