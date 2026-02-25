# Technical-Writer Domain

This document serves as the long-time memory for the Technical-Writer agent domain.

## Overview

The Technical-Writer domain focuses on documentation improvements, creating and maintaining architectural documentation, and ensuring consistent documentation standards across the repository.

## Completed Tasks

### Issue #2: Create docs/blueprint.md as architectural constitution
- **Status**: Completed
- **PR**: #12
- **Summary**: Created comprehensive architectural constitution documenting:
  - Repository structure and skill categories (.system, .curated, .experimental)
  - Skill manifest with all 30 curated skills
  - Required files per skill (SKILL.md, LICENSE.txt, agents/openai.yaml)
  - Naming conventions (references/ not reference/)
  - Quality standards
  - Contribution guidelines

## Known Issues (Related to Technical-Writer)

1. **Issue #3**: Standardize directory naming (reference/ vs references/)
   - 4 skills use singular "reference/" instead of "references/"
   - This is documented in blueprint.md for future resolution

2. **Issue #4**: Standardize license file (NOTICE.txt vs LICENSE.txt)
   - playwright skill uses NOTICE.txt while others use LICENSE.txt
   - This is documented in blueprint.md for future resolution

## Workflow

1. **INIT Phase**: Check for existing PRs with "technical-writer" label or open issues
2. **PLAN Phase**: Analyze the task and create implementation plan
3. **IMPLEMENT Phase**: Make small, atomic changes
4. **VERIFY Phase**: Verify changes are correct
5. **SELF-REFLECTION Phase**: Document learnings and update this file
6. **DELIVER Phase**: Create PR with proper labels and linked issues

## Best Practices

- Keep documentation atomic and focused
- Use clear, concise language
- Include code examples where helpful
- Link related documentation
- Follow existing documentation patterns
