# Example: Epic to Stories

## Scenario

User says: "Build a complete shopping cart experience"

This is too large for one story. Let's break it into an epic with multiple stories.

## Step 1: Identify the Epic

**Epic Title:** Shopping Cart Experience
**Description:** Complete cart functionality including view, edit, checkout flow

## Step 2: Break into Stories

Using the **User Journey** strategy:

### Story 1: View Cart
```
As a shopper,
I want to view items in my cart,
so that I can see what I've added before checkout.
```
- [ ] Cart icon shows item count
- [ ] Clicking cart shows items list
- [ ] Each item shows name, quantity, price
- [ ] Subtotal displays correctly
- [ ] Empty cart shows helpful message

**Estimate: 3 points**

### Story 2: Update Quantities
```
As a shopper,
I want to change item quantities in my cart,
so that I can adjust my order before checkout.
```
- [ ] Quantity input is editable
- [ ] +/- buttons work
- [ ] Changing quantity updates subtotal
- [ ] Minimum quantity is 1
- [ ] Maximum quantity is 99

**Estimate: 2 points**

### Story 3: Remove Items
```
As a shopper,
I want to remove items from my cart,
so that I can remove things I no longer want.
```
- [ ] Remove button appears for each item
- [ ] Clicking removes item
- [ ] Confirmation not required (can undo)
- [ ] Subtotal updates after removal
- [ ] Empty cart state shows when last item removed

**Estimate: 1 point**

### Story 4: Cart Persistence
```
As a shopper,
I want my cart items to persist across sessions,
so that I can come back later and still have my items.
```
- [ ] Items saved to database
- [ ] Items restore on login
- [ ] Guest cart persists 30 days
- [ ] Merge guest cart on login

**Estimate: 5 points**

### Story 5: Checkout Button
```
As a shopper,
I want a clear checkout button,
so that I can proceed to complete my purchase.
```
- [ ] Checkout button is prominent
- [ ] Button disabled when cart empty
- [ ] Button leads to checkout flow
- [ ] Shows order total on button (optional)

**Estimate: 1 point**

## Step 3: Create Epic in Linear

```python
linear:create_issue(
  title="Shopping Cart Experience (Epic)",
  description="Complete cart functionality for the e-commerce platform",
  labels=["epic"],
  # No estimate - will sum children
)
```

## Step 4: Create Child Stories

```python
# For each story, include parentId
linear:create_issue(
  title="View cart items",
  description="...",
  labels=["user-story"],
  parentId="CART-1",  # Parent epic ID
  estimate=3
)
```

## Total Estimate

3 + 2 + 1 + 5 + 1 = **12 points** (fits in 1-2 sprints)

## Validation

- [x] Each story delivers value independently
- [x] Stories can be completed in 1 sprint
- [x] No hard dependencies (all can be parallelized except Story 1 should come first)
- [x] Each has clear acceptance criteria
- [x] Total fits sprint capacity
