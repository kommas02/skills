---
name: workflow-helper
description: Helps manage GitHub Actions workflows and CI/CD pipelines
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: ci/cd
---

## What I do

I help manage GitHub Actions workflows and CI/CD pipelines:

- Analyze workflow files
- Understand job dependencies
- Check for common issues
- Help debug workflow failures
- Suggest improvements

## When to use me

Use this when working with:
- GitHub Actions workflows
- CI/CD pipeline configuration
- Automation scripts
- GitHub API integrations

## Workflow Structure

This repository uses a multi-stage workflow:

```yaml
Stage 1: Architect    - Strategy & Triage
Stage 2: Specialists  - Domain-specific work  
Stage 3: Fixer         - Repository maintenance
Stage 4: PR-Handler    - Merge handling
```

## Common Tasks

### Debug Workflow Failures
1. Check workflow file syntax
2. Review job dependencies
3. Examine logs for errors
4. Verify secrets are set
5. Check permission settings

### Improve Workflows
- Add caching for dependencies
- Optimize job parallelization
- Add better error handling
- Implement retry logic
- Add notification hooks

## Environment Variables

Common secrets needed:
- `GH_TOKEN` - GitHub token
- `GEMINI_API_KEY` - For AI agents
- `IFLOW_API_KEY` - Optional
- `CLOUDFLARE_*` - Optional

## Examples

Analyzing a workflow failure:
1. Read the workflow file
2. Identify the failing job
3. Check job dependencies
4. Review recent commits
5. Examine logs for clues

## Best Practices

- Keep workflows modular
- Use meaningful job names
- Add timeout-minutes
- Implement proper concurrency
- Use caching wisely
- Document complex logic
