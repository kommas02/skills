# AI Agent Engineer - Long-term Memory

## Domain
Skills infrastructure, validation, quality assurance, and automation for the Agent Skills repository.

## Current Work (Feb 2026)

### Issue #5: Add test coverage for skill validation

**Status**: Implemented

**Approach**:
1. Created `package.json` with test scripts
2. Created `test/skills.test.js` with validation logic

**Validation Rules**:
- Required files: `SKILL.md`, `LICENSE.txt`
- Required frontmatter in SKILL.md: `name`, `description`, `metadata`

**Findings**:
- 8 skills pass validation (2 system skills, 6 curated)
- 24 curated skills are missing the `metadata` field in frontmatter

**Test Execution**:
```bash
npm test
```

**Future Improvements**:
- Add validation for scripts/ directory structure
- Add validation for agents/ directory structure  
- Add validation for references/ format
- Add validation for asset file types
- Create separate issue to fix the 24 skills missing metadata

## Notes
- Skills are located in `skills/.system/` and `skills/.curated/`
- Each skill must have SKILL.md with YAML frontmatter
- The test currently fails because it detects real issues in existing skills
- For CI purposes, consider making this a lint-style check that reports but doesn't fail
