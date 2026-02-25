# Story Point Estimation Guide

Story points represent the relative complexity and effort required to complete a user story, not the time.

## Fibonacci Sequence

Use Fibonacci numbers: 1, 2, 3, 5, 8, 13, 21

The increasing gaps reflect increasing uncertainty in larger items.

## Point Definitions

| Points | Description | Examples |
|--------|-------------|----------|
| 1 | Trivial, no unknowns | Fix typo, add button text, simple CSS change |
| 2 | Small, straightforward | Simple form validation, basic API endpoint |
| 3 | Moderate complexity | Standard CRUD operation, multi-field form |
| 5 | Complex, some unknowns | Third-party integration, data migration |
| 8 | Very large, needs breakdown | Complex workflow, multiple systems |
| 13 | Epic, must split | System-wide feature, major refactor |

## Estimation Factors

Consider these when estimating:

1. **Complexity** — How many components involved?
2. **Unknowns** — Any unclear requirements or technical challenges?
3. **Effort** — How much work (not time)?
4. **Risk** — What could go wrong?

## Reference Stories

Compare new stories to completed ones:

**1-point stories:**
- "Change button color"
- "Fix typo in error message"
- "Add placeholder text"

**3-point stories:**
- "Add login form with validation"
- "Create user profile page"
- "Implement search filter"

**5-point stories:**
- "Integrate payment gateway"
- "Build export to CSV feature"
- "Implement password reset flow"

## Planning Poker Guidelines

- Discuss the story first
- Ask clarifying questions
- Consider edge cases
- Vote simultaneously (avoid anchoring)
- Discuss outliers
- Re-vote if needed

## Quick Estimation Heuristics

- Is it similar to something we've done? → Same points
- Does it require research? → Add 1-2 points
- Does it touch multiple systems? → Add points
- Is the requirement clear? → Standard estimate
- Is the requirement vague? → Add points for uncertainty
