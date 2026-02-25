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
