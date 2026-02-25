# Example: Refine Existing Story

## Scenario

You find this vague story in the backlog:

> "Improve search functionality"

## Step 1: Analyze the Problem

Issues with current story:
- User role is unclear
- "Improve" is subjective
- No acceptance criteria
- No scope

## Step 2: Ask Clarifying Questions

Before rewriting, ask the user:
1. Who is doing the searching?
2. What specifically should improve?
3. What does success look like?

User answers:
- "Our customers need to find products faster"
- "Currently search is slow and doesn't filter well"
- "Should work like Amazon - fast with filters"

## Step 3: Rewrite Using Template

### Original:
> "Improve search functionality"

### Refined:
```
As a shopping customer,
I want to filter search results by category, price range, and rating,
so that I can quickly find products that meet my needs.
```

## Step 4: Add Acceptance Criteria

### ❌ Vague criteria
- Search is better
- Faster results

### ✅ Measurable criteria
- [ ] Category filter dropdown appears on search results page
- [ ] Price range slider allows $0-$1000 range
- [ ] Minimum rating filter shows 1-5 stars
- [ ] Multiple filters can be combined
- [ ] Results update within 300ms of filter change
- [ ] Active filters display as removable tags
- [ ] "No results" shows suggestions when filters are too strict

## Step 5: Estimate

This involves:
- Database query optimization
- New filter UI components
- API endpoints for filtering
- Caching strategy

**Original estimate: Unknown**
**New estimate: 8 points** (large, needs breakdown)

## Step 6: Note This Is Still Large

Actually, this is an epic. Break into:

1. **Basic filters (3 pts):** Category, price range
2. **Rating filter (2 pts):** Star rating
3. **Performance (5 pts):** Optimization

Or use the parallel filter approach in acceptance criteria.

## Result Summary

| Aspect | Before | After |
|--------|--------|-------|
| Role | Vague | Shopping customer |
| Goal | "Improve search" | Filter by category, price, rating |
| Benefit | None stated | Find products quickly |
| Criteria | None | 7 measurable items |
| Points | Unknown | 8 (epic-sized) |

## Linear Update Example

```python
linear:update_issue(
  issueId="PROD-123",
  title="Search filtering by category, price, rating",
  description="""## User Story
As a shopping customer,
I want to filter search results by category, price range, and rating,
so that I can quickly find products that meet my needs.

## Acceptance Criteria
- [ ] Category filter dropdown appears on search results page
- [ ] Price range slider allows $0-$1000 range
- [ ] Minimum rating filter shows 1-5 stars
- [ ] Multiple filters can be combined
- [ ] Results update within 300ms of filter change
- [ ] Active filters display as removable tags
- [ ] "No results" shows suggestions when filters are too strict

## Notes
Blocked by: Search infrastructure (PROD-100)
Epic: Search improvements (PROD-900)""",
  estimate=8
)
```
