# Acceptance Criteria Guide

Acceptance criteria define when a user story is complete. They must be measurable, independent, and testable.

## Format Options

### Given-When-Then (Gherkin)

```
Given [precondition]
When [action]
Then [expected outcome]
```

Example:
```
Given I am logged in as a standard user
When I navigate to the settings page
Then I should see only the options available to my role
And I should not see admin-only settings
```

### Checklist Format

```
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
```

Example:
```
- [ ] User can enter a search query in the search box
- [ ] Search results appear within 500ms of pressing Enter
- [ ] Results are ranked by relevance
- [ ] Empty search shows helpful message
- [ ] Special characters are handled gracefully
```

## Quality Checklist

- [ ] Each criterion can be verified as passed/failed
- [ ] Criteria are independent (don't depend on each other)
- [ ] Criteria are small enough to test in one session
- [ ] Technical implementation details are NOT in criteria
- [ ] Criteria focus on user-observable behavior
- [ ] All edge cases are covered (empty state, errors, etc.)

## Common Mistakes

### ❌ Too vague
"User can search effectively"

### ✅ Measurable
"User can search by product name, SKU, or category and see results within 500ms"

### ❌ Implementation-focused
"Add Elasticsearch index for product search"

### ✅ User-observable
"Search results display relevant products matching the query"

## Happy Path vs Edge Cases

Include both:

**Happy Path:**
```
Given valid credentials
When user logs in
Then dashboard loads within 3 seconds
```

**Edge Cases:**
```
Given invalid credentials
When user attempts login
Then error message displays
And user remains on login page
And login attempt is logged
```
