# Backend Engineer Domain

## Repository: skills

## Issues Fixed

### 1. Workflow Trigger Branch Mismatch
- **File**: `.github/workflows/main.yml`
- **Issue**: Workflow triggered on `main` branch but default branch is `opencode`
- **Status**: PENDING - requires GitHub App `workflows` permission to push
- **Impact**: Workflows will now properly trigger on default branch pushes

### 2. Default Ref in Install Script
- **File**: `skills/.system/skill-installer/scripts/install-skill-from-github.py`
- **Issue**: DEFAULT_REF was set to `main` but default branch is `opencode`
- **Fix**: Changed DEFAULT_REF to `opencode`
- **Impact**: Scripts will use correct default branch

### 3. Default Ref in List Script
- **File**: `skills/.system/skill-installer/scripts/list-skills.py`
- **Issue**: DEFAULT_REF was set to `main` but default branch is `opencode`
- **Fix**: Changed DEFAULT_REF to `opencode`
- **Impact**: Scripts will use correct default branch

## Key Observations

1. The repository uses "opencode" as default branch, not "main"
2. All references to default branch in code and configs should be consistent
3. Python scripts and CI/CD configurations need to stay synchronized with repository branch structure

## Action Items

- [ ] **Workflow file fix**: Requires GitHub App with `workflows` permission to push changes to `.github/workflows/main.yml` (change `main` to `opencode` on line 6)
- [ ] Consider creating a centralized config for default branch name
- [ ] Audit other scripts that may reference "main" branch
- [ ] Add validation to check branch consistency in CI

## Permission Notes

GitHub App tokens (like those used by CI) require explicit `workflows` permission to modify workflow files. Current token lacks this permission, preventing automated workflow file updates.

## Last Updated

2026-02-25
