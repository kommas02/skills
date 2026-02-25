# Product-Architect Domain Memory

## Overview
The Product-Architect domain focuses on:
- Product design decisions
- System architecture
- Feature specifications
- Metadata schemas
- API designs
- Quality standards

## Completed Work

### Issue #20: Skill Metadata Schema (skill.json)
**Status**: Implemented

**Changes**:
1. Created `docs/skill-schema.md` - JSON Schema definition for skill metadata
2. Created `scripts/migrate-skill-json.js` - Migration script to generate skill.json for existing skills
3. Created `scripts/validate-skill-json.js` - Validation script for CI
4. Created `.github/workflows/skill-json-validate.yml` - CI workflow for validation
5. Created `docs/blueprint.md` - Updated architectural constitution with skill.json requirements
6. Generated skill.json for all 32 existing skills

**Schema Fields**:
- `name`: kebab-case identifier
- `version`: semver
- `description`: 10-200 chars
- `category`: .system | .curated | .experimental
- `author`: object with name, email, url
- `capabilities`: array of strings
- `dependencies`: array of skill names
- `tags`: array of keywords
- `license`: license identifier
- `homepage`: documentation URL
- `repository`: source URL

## Future Work

### Potential Improvements
1. **Skill Discovery API** - Build an API to query skills by tags/capabilities
2. **Dependency Resolution** - Implement skill dependency resolution system
3. **Version Migration** - Add version upgrade scripts for skill.json schema changes

### Related Issues
- #20: Create skill metadata schema (COMPLETED)
- #21: Add skill evaluation framework (QA domain)
- #30: Add skill quality telemetry (Growth-Innovation-Strategist domain)

## Standards

### skill.json Requirements
- All skills MUST have valid skill.json
- Description length: 10-200 characters
- Version must follow semver
- Category must be one of: .system, .curated, .experimental

### CI Validation
- `skill-json-validate.yml` runs on push to main/opencode and PRs affecting skills/
- Validation script uses JSON Schema draft-07
