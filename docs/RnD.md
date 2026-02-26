# RnD Documentation

## Session 2026-02-25

### Review Status
- PR #8 (Standardize directory naming): ✅ Up to date, CLEAN, mergeable, reviewed and commented

### Issue #17 - CI Wrong Branch Trigger
- **Problem**: Workflow triggers on `main` instead of `opencode` (default branch)
- **Fix**: Change line 6 in `.github/workflows/main.yml`: `main` → `opencode`
- **Status**: FIXED in current session - PR created with the fix

## Active Improvements

### 2026-02-25
- **Skill structure validation in CI**: Added validation workflow `.github/workflows/skill-validation.yml` that checks:
  - Each skill has a `SKILL.md` file
  - Each skill has a `LICENSE.txt` file
  - `SKILL.md` has required frontmatter (`name` and `description`)
  - All 30 existing skills pass validation

- **Standardize directory naming**: Renamed `reference/` to `references/` in 4 skills (notion-spec-to-implementation, notion-meeting-intelligence, notion-research-documentation, notion-knowledge-capture) to match the majority convention.

## Notes
- Default branch: `opencode`
- Skills are stored in `.system/` and `.curated/` directories
