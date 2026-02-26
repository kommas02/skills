# RnD Documentation

## Session 2026-02-26 (continued)

### Issue #97 - Skill Dependency Resolution System - COMPLETED
- **Problem**: Skills operate independently with no mechanism to declare dependencies
- **Solution**: Added dependency resolution to skill-installer
- **Implementation**:
  - Added `_load_skill_json()` function to parse skill.json
  - Added `_get_dependencies()` to extract dependencies array
  - Added `_detect_circular_dependencies()` for circular dependency detection (FIXED algorithm bug)
  - Added `_resolve_dependencies()` for topological sort of dependencies
  - Modified main() to resolve and install skills in dependency order
- **Files Changed**: 
  - `skills/.system/skill-installer/scripts/install-skill-from-github.py`
  - `skills/.system/skill-installer/SKILL.md` (documentation update)
  - `docs/skill-schema.md` - Enhanced dependency field documentation
- **New Test Asset**: Created `skills/.curated/doc-test` skill with dependency on `doc` skill

### Bug Fix: Circular Dependency Detection
- **Issue**: Original algorithm used `rec_stack.copy()` which lost path tracking
- **Fix**: Changed to track path as list with proper backtracking (pop on return)
- **Result**: Now correctly detects cycles including self-loops

## Session 2026-02-26

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
