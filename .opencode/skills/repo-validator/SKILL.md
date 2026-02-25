---
name: repo-validator
description: Validates repository structure, configuration files, and OpenCode setup
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: ci/cd
---

## What I do

I validate the repository structure and configuration to ensure everything is properly set up:

- Check .opencode directory exists and has required files
- Validate agent YAML frontmatter
- Verify skill SKILL.md files have correct format
- Check for common configuration issues
- Validate GitHub workflow files

## When to use me

Use this when you need to:
- Verify repository is properly configured
- Check that OpenCode can run without errors
- Validate skill and agent definitions
- Audit repository structure
- Prepare for CI/CD runs

## Validation Checks

### Required Files
- `.opencode/readme.md` - Main documentation
- `.opencode/agents/` - Agent directory (can be empty)

### Optional but Recommended
- `.opencode/skills/*/SKILL.md` - Skill definitions
- Agent markdown files with valid frontmatter

### Common Issues to Check
1. YAML frontmatter syntax errors
2. Missing required fields (name, description)
3. Invalid skill names (must match pattern: `^[a-z0-9]+(-[a-z0-9]+)*$`)
4. Missing SKILL.md files in skill directories

## How to Run

```bash
# Check directory structure
ls -la .opencode/

# Validate a specific agent
# Agent files should have valid YAML frontmatter

# Run opencode to verify it works
opencode --version
```

## Examples

Validating the entire .opencode setup:
1. List all files in .opencode/
2. Check each agent file for valid frontmatter
3. Verify skills have SKILL.md files
4. Run opencode --version to confirm it works
