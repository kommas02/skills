---
name: user-story-engineer
description: Create, refine, and manage user stories from requirements. Use when the user wants to turn feature requests, PRD notes, or vague ideas into actionable, well-structured user stories with acceptance criteria.
metadata:
  short-description: Create and manage user stories from requirements
---

# User Story Engineer

Transform requirements, feature requests, and PRD notes into actionable user stories with clear acceptance criteria, story points, and proper tracking.

## Quick start

1. Gather requirements from the user or source document
2. Identify the user role, goal, and benefit for each story
3. Write the user story using the standard format
4. Define acceptance criteria with measurable conditions
5. Estimate story points using Fibonacci sequence
6. Create issues in Linear with `linear:create_issue`

## Workflow

### Step 0: Confirm the source

- If the user provides requirements → proceed to Step 1
- If they mention a spec/PRD → fetch it first (use `Notion:notion-fetch` or read the document)
- If they mention Linear issues → use `linear:list_issues` to see existing items
- Ask clarifying questions if requirements are vague or incomplete

### Step 1: Identify the user role

Determine who will benefit from this feature:
- Internal user (team member, admin, support staff)
- External customer (end user, partner, visitor)
- System/automated actor

### Step 2: Define the goal (I want to...)

Articulate what the user wants to accomplish. Make it specific and actionable:
- Instead of "better search" → "find products by multiple filters simultaneously"
- Instead of "improve onboarding" → "complete account setup in under 2 minutes"

### Step 3: Define the benefit (so that...)

Explain why this matters:
- "so that I can quickly find relevant products without scrolling through everything"
- "so that new users feel confident using the platform immediately"

### Step 4: Write acceptance criteria

Use the Given-When-Then format or checklist format. Each criterion must be:
- Measurable (can verify it passed/failed)
- Independent (doesn't depend on other criteria)
- Small (can be tested in a single session)

See `reference/acceptance-criteria-guide.md` for patterns.

### Step 5: Estimate story points

Use Fibonacci sequence (1, 2, 3, 5, 8, 13):
- 1: Trivial, no unknowns
- 2: Small, straightforward
- 3: Moderate, some complexity
- 5: Large, significant complexity or unknowns
- 8: Very large, needs breakdown
- 13: Epic, should be split

See `reference/story-point-estimation.md` for guidance.

### Step 6: Create issues in tracker

Use Linear MCP to create issues:
- Title: Short action-oriented summary
- Description: User story format + acceptance criteria
- Labels: `user-story`, relevant feature label
- Estimate: Story points
- Priority: Urgent/High/Medium/Low

## Handling Epics

When a feature is too large for a single sprint:

1. Break into theme-level chunks (epics)
2. Each epic becomes a parent issue in Linear
3. Stories become child issues linked to the epic
4. Use `linear:create_issue` with `parentId` for nesting

See `reference/epic-breaking-guide.md` for detailed patterns.

## Story Refinement Workflow

For existing vague stories:

1. Read the current description
2. Identify missing parts: role unclear? goal vague? benefit missing?
3. Ask the user clarifying questions
4. Rewrite using the template
5. Verify acceptance criteria are testable

## References

- `reference/acceptance-criteria-guide.md` — Writing measurable acceptance criteria
- `reference/story-point-estimation.md` — Fibonacci-based estimation guide
- `reference/epic-breaking-guide.md` — Breaking large features into stories
- `reference/user-story-template.md` — Copy-paste template

## Examples

- `examples/simple-feature-story.md` — Basic user story creation
- `examples/epic-to-stories.md` — Breaking an epic into multiple stories
- `examples/refine-existing-story.md` — Improving unclear stories
