# User-Story-Engineer Domain

## Overview
The User-Story-Engineer domain focuses on documentation clarity, user story quality, and product usability improvements within the Agent Skills repository.

## Responsibilities
- Ensuring skill documentation is clear, consistent, and user-friendly
- Creating and maintaining user stories for skill improvements
- Improving README and contributing documentation
- Quality checking skill descriptions and metadata
- Identifying documentation gaps and opportunities

## Focus Areas

### Documentation Quality
- SKILL.md files should have consistent frontmatter (name, description)
- Description should be actionable and clear
- Each skill should have clear usage instructions

### User Story Development
- Create issues with proper format (Problem Statement, Root Cause, Proposed Solution, Acceptance Criteria)
- Ensure acceptance criteria are measurable and testable
- Link issues to specific skills or system components

### Readability Improvements
- README.md should be comprehensive but concise
- Contributing guidelines should be clear for external contributors
- Create domain-specific documentation when needed

## Key Metrics
- All skills should have complete SKILL.md with frontmatter
- README coverage of all skill categories
- Issue quality score (proper format, measurable criteria)

## Related Domains
- Technical-Writer: Blueprint and architectural documentation
- DX-Engineer: Developer experience and tooling
- Product-Architect: System architecture and skill schema
- Quality-Assurance: Evaluation frameworks and testing

## User Story Templates

### Issue Template

Use this format when creating issues:

```markdown
**Problem Statement:** [What is the issue? Why does it matter?]

**Root Cause:** [What's causing the problem?]

**Proposed Solution:** [How should it be fixed?]

**Acceptance Criteria:**
- [ ] Criterion 1 (measurable)
- [ ] Criterion 2 (measurable)

**Definition of Done:**
- [ ] Code updated
- [ ] Tests added/updated
- [ ] Documentation updated

**Impact Surface:** [Architecture | Security | Performance | UX | DevEx]
**Priority:** [High | Medium | Low]
**Owner Agent:** [Domain name]
```

### Acceptance Criteria Best Practices

- **Specific:** Clearly describe what should happen
- **Measurable:** Include quantifiable metrics where possible
- **Testable:** Can be verified through manual or automated testing
- **Independent:** Each criterion can be evaluated separately
- **Realistic:** Achievable with available resources

### Example: Good vs Bad Acceptance Criteria

| Bad | Good |
|-----|------|
| "Improve documentation" | "Add Troubleshooting section to all skills missing it" |
| "Fix bugs" | "Resolve #95: Add agents/ directory to growth-innovation-strategist skill" |
| "Make it faster" | "Reduce CI build time by 30% (measured via GitHub Actions logs)" |

---

## Recent Work

### 2026-02-26
- **Issue #86**: Improved contributing.md with skill creation guidance
  - Added "Creating Skills" section with quick start guide
  - Documented required directory structure and SKILL.md requirements
  - Added resources section linking to skill-template.md and system skills
  - PR #87: https://github.com/kommas02/skills/pull/87

### 2026-02-27 (Proactive Scan)
- **Proactive Scan**: Verified all skills have required files (SKILL.md, LICENSE.txt)
  - ✅ 32 curated skills: all have SKILL.md and LICENSE.txt
  - ✅ 2 system skills: all have SKILL.md and LICENSE.txt
  - ✅ All SKILL.md files have proper frontmatter (name, description)
  - ✅ All descriptions start with action verbs (best practice verified)
  - ✅ README.md comprehensive with installation instructions
  - ✅ contributing.md has skill creation guidance
- **Documentation Fix**: Found and documented missing `scripts/evaluate_skill.py` references
  - Issue #96 and #52 verified as resolved (files/folders now exist)
  - Found `evaluate_skill.py` referenced in docs but not implemented (part of QA issue #21)
  - Added notes in docs/evaluation-framework.md and docs/quality-assurance.md indicating the script is planned
  - This prevents user confusion while QA implements the evaluation runner

### 2026-02-27 (Proactive Improvement)
- **Documentation Enhancement**: Added User Story Templates section to docs/user-story-engineer.md
  - Added issue template with Problem Statement, Root Cause, Proposed Solution, Acceptance Criteria
  - Added Acceptance Criteria Best Practices (Specific, Measurable, Testable, Independent, Realistic)
  - Added Good vs Bad Acceptance Criteria examples table
  - This helps contributors create better issues with measurable criteria

