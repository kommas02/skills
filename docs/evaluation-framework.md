# Skill Evaluation Framework

## Overview

This document defines the evaluation framework for ensuring skill quality, accuracy, and effectiveness. Every skill in the repository should have at least 2 evaluation cases to verify it works correctly across different scenarios.

## Directory Structure

Each skill can optionally include an `evaluations/` directory with the following structure:

```
skills/.curated/my-skill/
├── SKILL.md
├── evaluations/
│   ├── config.json          # Evaluation configuration
│   ├── case-1.json          # First evaluation case
│   ├── case-2.json          # Second evaluation case
│   └── README.md           # Evaluation documentation (optional)
```

## Evaluation File Format

### Case JSON Schema

Each evaluation case should be a JSON file with the following structure:

```json
{
  "name": "Case Name",
  "skills": ["skill-name"],
  "query": "Input query or prompt to test",
  "expected_behavior": [
    "Step 1: Expected action",
    "Step 2: Expected action"
  ],
  "success_criteria": [
    "Specific, measurable criterion 1",
    "Specific, measurable criterion 2"
  ]
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Descriptive name for the evaluation case |
| `skills` | Yes | Array of skill names this case tests |
| `query` | Yes | The input prompt/query to test the skill |
| `expected_behavior` | Yes | Ordered list of expected actions the skill should take |
| `success_criteria` | Yes | Measurable criteria for determining success |

## config.json Schema

```json
{
  "skill_name": "my-skill",
  "description": "What this skill does",
  "min_cases_required": 2,
  "evaluation_model": "sonnet",
  "tested_models": ["haiku", "sonnet", "opus"]
}
```

## Minimum Requirements

- **At least 2 evaluation cases per skill** (required)
- Each case should test different scenarios:
  - Basic/happy path
  - Edge case or error handling
  - Complex scenario (if applicable)

## Writing Good Evaluation Cases

### Success Criteria Guidelines

**Good** (specific, measurable):
- "Uses Notion:notion-search before fetching page"
- "Creates implementation plan with 3 phases"
- "Each task has acceptance criteria in checklist format"
- "Searches for spec page using feature name"

**Bad** (vague, untestable):
- "Creates good implementation plan"
- "Tasks are well-structured"
- "Breaks down spec appropriately"

### Query Examples

Include realistic queries that users would actually ask:
- "Create an implementation plan for the User Authentication spec"
- "Set up CI/CD pipeline for my React app"
- "Fix the failing tests in the authentication module"

### Expected Behavior

List each step the skill should take in order:
1. Search for the spec page
2. Fetch the spec content
3. Parse requirements
4. Create implementation phases
5. Link back to original spec

## Running Evaluations

> **Note**: The evaluation runner script (`scripts/evaluate_skill.py`) is planned as part of issue #21 and is not yet implemented. For now, evaluations can be run manually using the case JSON files in each skill's `evaluations/` directory.

### Local Testing (Manual)

```bash
# Manually run evaluation cases by reading the case JSON files
# and executing them against the skill
```

### CI Validation

The `validate-skills.yml` workflow checks for:
- Presence of `evaluations/` directory
- At least 2 JSON case files per skill
- Valid JSON syntax
- Required fields in each case

## Example: notion-spec-to-implementation

See `skills/.curated/notion-spec-to-implementation/evaluations/` for a complete example with:
- `basic-spec-implementation.json` - Tests creating implementation plans
- `spec-to-tasks.json` - Tests creating tasks from specs
- `README.md` - Documentation of evaluation approach

## Best Practices

1. **Test different complexity levels**: Simple, medium, and complex scenarios
2. **Include edge cases**: Error handling, ambiguous inputs, missing data
3. **Be specific**: Success criteria should be objectively measurable
4. **Keep queries realistic**: Mirror actual user queries
5. **Update regularly**: Add cases for bugs found in production

## Integration with Quality Assurance

The evaluation framework integrates with QA processes:

- **Pre-commit**: Validate evaluation files exist
- **CI/CD**: Run evaluation checks on PRs
- **Release**: Verify all skills have minimum evaluations
- **Monitoring**: Track evaluation pass rates over time

## Related Documentation

- [Quality Assurance](quality-assurance.md) - General QA practices
- [SKILL.md Frontmatter](quality-assurance.md#skillmd-frontmatter-format) - Skill metadata requirements
