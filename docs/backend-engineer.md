# Backend Engineer Domain

## Repository: skills

## Issues Fixed

### 1. Workflow Trigger Branch Mismatch
- **File**: `.github/workflows/main.yml`
- **Issue**: Workflow triggered on `main` branch but default branch is `opencode`
- **Status**: ✅ READY - Manual application required
- **Fix**: Changed line 6 from `- main` to `- opencode`
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
- **Status**: ✅ READY - Manual application required
- **Fix**: Remove 4 occurrences of `API_KEY: ${{ secrets.GEMINI_API_KEY }}` from all jobs
- **Impact**: Removes security confusion from redundant secret mapping

## Key Observations

1. The repository uses "opencode" as default branch, not "main"
2. All references to default branch in code and configs should be consistent
3. Python scripts and CI/CD configurations need to stay synchronized with repository branch structure
4. GitHub App tokens (like those used in CI) cannot modify workflow files without explicit `workflows` permission
5. Any push involving `.github/workflows/` files is rejected when using GITHUB_TOKEN without workflow permission

## Action Items

- [x] **Workflow trigger fix**: Ready for manual application
- [x] **Duplicate API_KEY fix**: Ready for manual application
- [ ] Consider creating a centralized config for default branch name
- [ ] Audit other scripts that may reference "main" branch
- [ ] Add validation to check branch consistency in CI

## Pending Fix Ready for Manual Application

Both workflow fixes are ready but blocked by GitHub App permission restriction.

### Exact Diff
```diff
--- a/.github/workflows/main.yml
+++ b/.github/workflows/main.yml
@@ -3,7 +3,7 @@ name: parallel
 on:
   push:
     branches:
-      - main
+      - opencode
   schedule:
     - cron: "0 */4 * * *"
   workflow_dispatch:
@@ -34,7 +34,6 @@ jobs:
       CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
       CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
       GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
-      API_KEY: ${{ secrets.GEMINI_API_KEY }}

     steps:
       - uses: actions/checkout@v4
@@ -269,7 +268,6 @@ jobs:
           CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
           CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
           GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
-          API_KEY: ${{ secrets.GEMINI_API_KEY }}
         run: |
           echo "🚀 Specialist ${{ matrix.role }} executing"
@@ -345,7 +343,6 @@ jobs:
           CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
           CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
           GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
-          API_KEY: ${{ secrets.GEMINI_API_KEY }}
         run: |
           opencode run /ulw-loop "
@@ -411,7 +408,6 @@ jobs:
           CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
           CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
           GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
-          API_KEY: ${{ secrets.GEMINI_API_KEY }}
         run: |
           opencode run /ulw-loop "
```

## Solution Options

1. **Manual Application**: Apply the diff above manually (repo owner)
2. **Add Workflow Permission**: Grant `workflows` permission to the GitHub App
3. **Use Personal Token**: Use a personal access token with proper permissions

## Permission Notes

GitHub App tokens (like those used by CI) require explicit `workflows` permission to modify workflow files. Current token lacks this permission, preventing automated workflow file updates. This is a security feature - workflow file changes require user-level access or explicit app permissions.

## Attempted Fixes

- **2026-02-27**: Both fixes applied locally, YAML validated. Push rejected due to GitHub App permission restriction.
- **2026-02-27**: Both fixes applied and PR created (#107)
- **2026-02-26**: Attempted to apply fixes directly but push was rejected due to GitHub App permission restrictions on workflow files

## Last Updated

2026-02-27
