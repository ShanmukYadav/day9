# ai_pair_sum.md
# Day 9 AM – Part D: AI-Augmented Task

---

## Step 1 — Exact Prompt Used

> "Write a Python function that finds all pairs in a list that sum to a target number using list comprehensions."

---

## Step 2 — AI-Generated Code

```python
def find_pairs(lst, target):
    return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i+1, len(lst)) if lst[i] + lst[j] == target]
```

---

## Step 3 — Testing the AI Code

```python
print(find_pairs([1, 2, 3, 4, 5], 6))
# Output: [(1, 5), (2, 4)]  ✅  Correct

print(find_pairs([1, 1, 1], 2))
# Output: [(1, 1), (1, 1), (1, 1)]  ❌  Duplicate pairs!
```

### Issues Found

| Issue | Description |
|---|---|
| ❌ Duplicate pairs | `[1, 1, 1]` with target 2 returns 3 identical pairs `(1,1)` |
| ❌ No handling for duplicate values | Every index combination is treated as unique even if values are the same |
| ⚠️ Performance | O(n²) time — nested loop over all index pairs |

---

## Step 4 — Improved Version

```python
def find_pairs_improved(lst: list, target: int) -> list:
    """
    Find all UNIQUE pairs that sum to target.
    - Avoids duplicate pairs using a seen set
    - Handles lists with repeated values correctly
    - Time: O(n²)  |  Space: O(n)
    """
    seen_pairs = set()
    result = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pair = tuple(sorted((lst[i], lst[j])))   # normalize order
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    result.append(pair)

    return result


# Tests
print(find_pairs_improved([1, 2, 3, 4, 5], 6))   # [(1, 5), (2, 4)]  ✅
print(find_pairs_improved([1, 1, 1], 2))           # [(1, 1)]          ✅  only one pair
print(find_pairs_improved([3, 3, 3, 3], 6))        # [(3, 3)]          ✅
print(find_pairs_improved([], 5))                  # []                ✅
print(find_pairs_improved([5], 5))                 # []                ✅  need 2 elements
```

---

## Improvements Explained

### 1. Deduplicate Pairs with a `seen` Set
The AI version returns all index combinations, so `[1,1,1]` yields 3 identical
`(1,1)` pairs. The fix: normalize each pair to a sorted tuple and track it in a
`seen_pairs` set. If the same value-pair has already been recorded, skip it.

### 2. Normalize Pair Order
`tuple(sorted((a, b)))` ensures `(1, 5)` and `(5, 1)` are treated as the same
pair, regardless of which element appeared first in the list.

### 3. Edge Cases Handled
- Empty list → returns `[]`
- Single-element list → returns `[]` (can't form a pair)
- All-duplicate list like `[3,3,3,3]` → returns `[(3,3)]` once, not 6 times

---

## O(n) Solution Using Sets

For large lists, the nested loop approach is O(n²). An O(n) solution uses a
complement-lookup via a hash set:

```python
def find_pairs_on(lst: list, target: int) -> list:
    """
    O(n) solution using a seen-set for complement lookup.
    Limitation: doesn't distinguish between indices (value-based dedup only).
    """
    seen = set()
    result = set()

    for num in lst:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            result.add(pair)
        seen.add(num)

    return list(result)


# Tests
print(find_pairs_on([1, 2, 3, 4, 5], 6))   # {(1,5), (2,4)}  ✅
print(find_pairs_on([1, 1, 1], 2))           # {(1,1)}         ✅
```

### Why O(n)?
- Each element is visited **once**.
- `complement in seen` is an O(1) hash-set lookup.
- Total time: **O(n)** vs O(n²) for the nested loop.

### Trade-off
The O(n) version works on **values**, not indices, so it naturally deduplicates
by value. However, if you need the actual indices of each pair (not just values),
the O(n²) improved version with `seen_pairs` is more appropriate.

---

## Summary

| Version | Time | Handles Duplicates | Notes |
|---|---|---|---|
| AI original | O(n²) | ❌ | Returns duplicate pairs |
| Improved (index loop) | O(n²) | ✅ | Correct dedup via sorted tuple set |
| O(n) set solution | O(n) | ✅ | Best for large inputs, value-based |
