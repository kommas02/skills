# Skills Registry

This file provides a centralized registry of all available skills in this repository.

## Curated Skills

| Skill | Description |
|-------|-------------|
| [cloudflare-deploy](./.curated/cloudflare-deploy/SKILL.md) | Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. |
| [develop-web-game](./.curated/develop-web-game/SKILL.md) | Build and iterate on web games (HTML/JS) with Playwright-based testing loop. |
| [doc](./.curated/doc/SKILL.md) | Read, create, or edit .docx documents with formatting fidelity. |
| [figma-implement-design](./.curated/figma-implement-design/SKILL.md) | Translate Figma nodes into production-ready code with visual fidelity. |
| [figma](./.curated/figma/SKILL.md) | Fetch design context from Figma using MCP server. |
| [gh-address-comments](./.curated/gh-address-comments/SKILL.md) | Help address review/issue comments on GitHub PRs. |
| [gh-fix-ci](./.curated/gh-fix-ci/SKILL.md) | Debug or fix failing GitHub PR checks in Actions. |
| [imagegen](./.curated/imagegen/SKILL.md) | Generate or edit images via OpenAI Image API. |
| [jupyter-notebook](./.curated/jupyter-notebook/SKILL.md) | Create, scaffold, or edit Jupyter notebooks. |
| [linear](./.curated/linear/SKILL.md) | Manage issues, projects & workflows in Linear. |
| [netlify-deploy](./.curated/netlify-deploy/SKILL.md) | Deploy web projects to Netlify. |
| [notion-knowledge-capture](./.curated/notion-knowledge-capture/SKILL.md) | Capture conversations into structured Notion pages. |
| [notion-meeting-intelligence](./.curated/notion-meeting-intelligence/SKILL.md) | Prepare meeting materials with Notion context. |
| [notion-research-documentation](./.curated/notion-research-documentation/SKILL.md) | Research across Notion and synthesize documentation. |
| [notion-spec-to-implementation](./.curated/notion-spec-to-implementation/SKILL.md) | Turn Notion specs into implementation plans. |
| [openai-docs](./.curated/openai-docs/SKILL.md) | Access up-to-date OpenAI product documentation. |
| [pdf](./.curated/pdf/SKILL.md) | Read, create, or review PDF files. |
| [playwright](./.curated/playwright/SKILL.md) | Automate real browsers from terminal. |
| [render-deploy](./.curated/render-deploy/SKILL.md) | Deploy applications to Render. |
| [screenshot](./.curated/screenshot/SKILL.md) | Capture desktop or system screenshots. |
| [security-best-practices](./.curated/security-best-practices/SKILL.md) | Security best-practice reviews and suggestions. |
| [security-ownership-map](./.curated/security-ownership-map/SKILL.md) | Build security ownership topology from git. |
| [security-threat-model](./.curated/security-threat-model/SKILL.md) | Repository-grounded threat modeling. |
| [sentry](./.curated/sentry/SKILL.md) | Inspect Sentry issues and production errors. |
| [sora](./.curated/sora/SKILL.md) | Generate, remix, or download Sora videos. |
| [speech](./.curated/speech/SKILL.md) | Text-to-speech narration and voiceover. |
| [spreadsheet](./.curated/spreadsheet/SKILL.md) | Create, edit, analyze spreadsheets. |
| [transcribe](./.curated/transcribe/SKILL.md) | Transcribe audio files with diarization. |
| [vercel-deploy](./.curated/vercel-deploy/SKILL.md) | Deploy applications to Vercel. |
| [yeet](./.curated/yeet/SKILL.md) | Stage, commit, push, and open GitHub PR in one flow. |

## System Skills

| Skill | Description |
|-------|-------------|
| [skill-creator](./.system/skill-creator/SKILL.md) | Guide for creating effective skills. |
| [skill-installer](./.system/skill-installer/SKILL.md) | Install Codex skills from curated list or GitHub. |

## Registry Format

This registry is automatically generated from SKILL.md frontmatter. Each skill should include:

```yaml
---
name: <skill-name>
description: <one-line-description>
---
```

- **name**: Unique identifier for the skill (kebab-case)
- **description**: One-line description of what the skill does (used for discovery)

## Adding New Skills

1. Create skill directory under `skills/.curated/` or `skills/.system/`
2. Add `SKILL.md` with required frontmatter (name, description)
3. Update this registry (auto-generation coming soon)
