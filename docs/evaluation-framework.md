# Skill Evaluation Framework

## Overview

This document describes the evaluation framework for assessing skill quality, accuracy, and effectiveness.

## Motivation

Currently, only 4 out of 31 skills have evaluation data (notion-* skills). This framework provides a standardized way to:
- Test skill quality
- Verify skill accuracy
- Measure skill effectiveness
- Ensure consistent skill development

## Evaluation Directory Structure

Each skill can include an optional `evaluation/` directory with the following structure:

```
skill-name/
├── evaluation/
│   ├── cases/
│   │   ├── case_001.json
│   │   ├── case_002.json
│   │   └── ...
│   └── config.json
```

## Evaluation Case Schema

Each evaluation case is a JSON file with the following structure:

```json
{
  "id": "case_001",
  "name": "Basic skill invocation",
  "description": "Test that the skill triggers correctly for basic usage",
  "input": {
    "prompt": "Create a new skill for handling JSON files",
    "context": {}
  },
  "expected_output": {
    "triggers_skill": true,
    "skill_name": "skill-creator",
    "contains_keywords": ["skill", "create", "JSON"]
  },
  "metrics": {
    "trigger_accuracy": 1.0,
    "relevance_score": 0.9
  },
  "tags": ["basic", "trigger"]
}
```

### Schema Fields

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier for the case |
| name | string | Human-readable name |
| description | string | What this case tests |
| input | object | Input prompt and context |
| input.prompt | string | The user prompt to test |
| input.context | object | Additional context variables |
| expected_output | object | Expected behavior/response |
| expected_output.triggers_skill | boolean | Should this prompt trigger the skill? |
| expected_output.skill_name | string | Expected skill to trigger (if any) |
| expected_output.contains_keywords | array | Keywords that should appear in response |
| metrics | object | Performance metrics |
| metrics.trigger_accuracy | float | 0.0-1.0 score for trigger prediction |
| metrics.relevance_score | float | 0.0-1.0 score for response relevance |
| tags | array | Categorization tags |

## Evaluation Config

The `config.json` file provides skill-level configuration:

```json
{
  "skill_name": "skill-creator",
  "min_required_cases": 2,
  "evaluation_mode": "automated", 
  "run_on_ci": true
}
```

### Config Fields

| Field | Type | Description |
|-------|------|-------------|
| skill_name | string | Name of the skill being evaluated |
| min_required_cases | integer | Minimum number of evaluation cases required |
| evaluation_mode | string | "automated", "manual", or "hybrid" |
| run_on_ci | boolean | Whether to run evaluations in CI |

## Evaluation Runner

The evaluation runner script (`scripts/evaluate_skill.py`) can be used to run evaluations locally or in CI.

### Usage

```bash
# Evaluate a specific skill
python scripts/evaluate_skill.py skills/skill-name

# Evaluate all skills with evaluation directories
python scripts/evaluate_skill.py --all

# Run with verbose output
python scripts/evaluate_skill.py skills/skill-name --verbose

# Output results to JSON
python scripts/evaluate_skill.py skills/skill-name --output results.json
```

### Exit Codes

- 0: All evaluations passed
- 1: One or more evaluations failed
- 2: Evaluation framework error

## CI Integration

The evaluation framework integrates with the existing `validate-skills.yml` workflow to check for evaluation presence:

```yaml
- name: Check evaluation presence
  run: |
    for skill_dir in skills/*/; do
      skill_name=$(basename "$skill_dir")
      eval_dir="$skill_dir/evaluation"
      if [ -d "$eval_dir" ]; then
        case_count=$(find "$eval_dir/cases" -name "*.json" | wc -l)
        if [ "$case_count" -lt 2 ]; then
          echo "ERROR: $skill_name has only $case_count evaluation cases (min: 2)"
          exit 1
        fi
      fi
    done
```

## Adding Evaluations to a Skill

To add evaluations to a skill:

1. Create the `evaluation/` directory
2. Add at least 2 evaluation case files in `evaluation/cases/`
3. Create `evaluation/config.json` with skill configuration

Example:

```bash
mkdir -p skills/my-skill/evaluation/cases
# Add case files...
# Add config.json...
```

## Best Practices

1. **Minimum Cases**: Each skill should have at least 2 evaluation cases
2. **Diverse Coverage**: Include cases covering:
   - Basic/trivial inputs
   - Edge cases
   - Error conditions
   - Common use patterns
3. **Realistic Prompts**: Use prompts that reflect actual user behavior
4. **Clear Metrics**: Define measurable metrics for each case
5. **Regular Updates**: Keep evaluations updated as skills evolve

## Future Enhancements

- Automated LLM-based evaluation
- Human feedback integration
- A/B testing support
- Performance benchmarking
- Cross-skill compatibility testing
