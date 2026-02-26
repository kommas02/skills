# Backend Engineer Domain

## Repository: skills

## Issues Fixed

### 1. Workflow Trigger Branch Mismatch
- **File**: `.github/workflows/main.yml`
- **Issue**: Workflow triggered on `main` branch but default branch is `opencode`
- **Status**: NEEDS MANUAL FIX - cannot push workflow changes due to GitHub App permission restriction
- **Fix Required**: Change line 6 from `- main` to `- opencode`
- **Exact diff**:
```diff
on:
  push:
    branches:
-      - main
+      - opencode
```
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

### 4. Duplicate API_KEY Environment Variable
- **File**: `.github/workflows/main.yml`
- **Issue**: Redundant `API_KEY` env var mapping to same secret as `GEMINI_API_KEY`
- **Status**: NEEDS MANUAL FIX - cannot push workflow changes due to GitHub App permission restriction
- **Fix Required**: Remove 4 occurrences of `API_KEY: ${{ secrets.GEMINI_API_KEY }}` from the workflow file
- **Exact diff** (apply to all jobs: architect, specialists, Fixer, PR-Handler):
```diff
          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
-          API_KEY: ${{ secrets.GEMINI_API_KEY }}
```
- **Impact**: Removes security confusion from redundant secret mapping

## Key Observations

1. The repository uses "opencode" as default branch, not "main"
2. All references to default branch in code and configs should be consistent
3. Python scripts and CI/CD configurations need to stay synchronized with repository branch structure
4. GitHub App tokens (like those used in CI) cannot modify workflow files without explicit `workflows` permission
5. Any push involving `.github/workflows/` files is rejected when using GITHUB_TOKEN without workflow permission

## Action Items

- [ ] **Workflow trigger fix**: Manual change required - change `main` to `opencode` on line 6 of main.yml
- [ ] **Duplicate API_KEY fix**: Manual change required - remove redundant API_KEY environment variable
- [ ] Consider creating a centralized config for default branch name
- [ ] Audit other scripts that may reference "main" branch
- [ ] Add validation to check branch consistency in CI

## Permission Notes

GitHub App tokens (like those used by CI) require explicit `workflows` permission to modify workflow files. Current token lacks this permission, preventing automated workflow file updates. This is a security feature - workflow file changes require user-level access or explicit app permissions.

## Attempted Fixes

- **2026-02-26**: Attempted to apply fixes directly but push was rejected due to GitHub App permission restrictions on workflow files
- The exact diffs are now provided above for manual application

## Last Updated

2026-02-26

## Linked PRs

- PR #104: docs: update backend-engineer.md with findings
