---
name: <skill-name>
description: <brief one-line description of what the skill does and when to use it>
---

# <Skill Display Name>

<2-3 sentence overview explaining what this skill accomplishes and its primary use cases.>

## When to Use This Skill

Use this skill when the user asks to:
- <specific user request 1>
- <specific user request 2>
- <specific user request 3>

Do NOT use this skill when:
- < scenarios where this skill is inappropriate >

## Prerequisites

- <prerequisite 1 (e.g., API key, tool installation)>
- <prerequisite 2>
- <any sandbox/permission requirements>

## Quick Start

```bash
<quick start command or steps>
```

## Usage

### Basic Usage

<step-by-step instructions for basic usage>

### Advanced Usage

<additional options, configurations, or advanced scenarios>

## Examples

### Example 1: <Example Title>

<brief description>

```bash
<command or code>
```

### Example 2: <Example Title>

<brief description>

```bash
<command or code>
```

## Configuration

| Option | Description | Default |
|--------|-------------|---------|
| <option> | <description> | <default> |

## References

- `<references/reference-name/>` - <description>
- `<references/another-reference/>` - <description>

## Scripts

- `<scripts/script-name>` - <description of what the script does>
- `<scripts/another-script>` - <description>

## Assets

- `<assets/asset-name>` - <description>

## Troubleshooting

### Issue: <Common Issue 1>

**Symptom:** <what the user sees>

**Solution:** <how to fix it>

### Issue: <Common Issue 2>

**Symptom:** <what the user sees>

**Solution:** <how to fix it>

---

# Section Requirements

This document defines the required, recommended, and optional sections for skills in this repository.

## REQUIRED Sections

These sections MUST be present in every skill:

1. **Frontmatter (`---`)**
   - `name`: Unique skill identifier (kebab-case)
   - `description`: One-line description for skill selection

2. **Skill Title**: H1 heading with display name

3. **Description**: 2-3 sentence overview

4. **When to Use This Skill**: Clear guidance on when to invoke the skill

## RECOMMENDED Sections

These sections should be included unless not applicable:

1. **Prerequisites**: Required setup, tools, or permissions
2. **Quick Start**: Minimal commands to get started
3. **Usage**: Detailed usage instructions
4. **Examples**: Concrete usage examples
5. **References/**: Subdirectory with detailed reference docs
6. **Scripts/**: Automation scripts (if applicable)
7. **Assets/**: Static assets (if applicable)

## OPTIONAL Sections

Include these when relevant:

1. **Configuration**: Table of configurable options
2. **Troubleshooting**: Common issues and solutions
3. **Evaluations**: Quality assessment data
4. **Benchmarks**: Performance metrics
