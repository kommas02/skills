# User Story Template

## Standard Format

```
As a [user role],
I want to [goal/feature],
so that [benefit/value].
```

## Full Template

```markdown
## Title
[Short, action-oriented title - max 50 chars]

## User Story
As a [user role],
I want to [goal/feature],
so that [benefit/value].

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Story Points
[1/2/3/5/8/13]

## Priority
[Urgent/High/Medium/Low]

## Dependencies
- Depends on: [Issue # or story]
- Blocked by: [Issue # or story]

## Notes
[Any additional context, links to specs, technical notes]
```

## Example: Complete

```markdown
## Title
Export search results to CSV

## User Story
As a marketing analyst,
I want to export search results to CSV,
so that I can analyze data in Excel and share with stakeholders.

## Acceptance Criteria
- [ ] Export button appears on search results page
- [ ] Clicking export downloads a CSV file
- [ ] CSV includes all visible columns
- [ ] File downloads within 5 seconds for up to 1000 rows
- [ ] Empty search shows "No results to export" message

## Story Points
3

## Priority
Medium

## Dependencies
- Depends on: Search functionality (complete)

## Notes
- See API spec: /docs/search-export.md
- Need to handle special characters in CSV
```

## Quick Copy-Paste Version

```
**As a** [user role]
**I want to** [goal]
**so that** [benefit]

**AC:**
- [ ] 
- [ ] 

**Points:** [X]
**Priority:** [X]
```
