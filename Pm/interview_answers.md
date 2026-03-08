# interview_answers.md
# Day 9 PM – Part C: Interview Ready

---

## Q1 — Tuple Immutability Trap

**Question:** Given `t = ([1, 2], [3, 4])`, can we run `t[0][0] = 99`?

### Answer: Yes, it works — and that is the trap.

```python
t = ([1, 2], [3, 4])
t[0][0] = 99
print(t)   # ([99, 2], [3, 4])  ← it changed!
```

### Why it works

A tuple's immutability means you **cannot reassign its references** — i.e., you
cannot make `t[0]` point to a different object. But `t[0]` itself is a **list**,
which is mutable. Mutating the list's contents does not rebind the tuple's
reference, so Python allows it.

```
t  ──►  [ ref_0, ref_1 ]   ← tuple (immutable: these refs cannot change)
          │        │
          ▼        ▼
       [1, 2]   [3, 4]     ← lists (mutable: their contents CAN change)
```

- `t[0] = something_else` → ❌ **TypeError**: tuple does not support item assignment
- `t[0][0] = 99`          → ✅ Allowed — mutating the list, not the tuple

### What this reveals about tuple immutability

Tuple immutability is **shallow** — it protects the identity of its elements
(which object each slot points to), not the internal state of those objects.
If a tuple holds mutable objects (lists, dicts, custom objects), those objects
can still be mutated freely. True deep immutability requires using immutable
types (e.g., nested tuples, frozensets) as elements.

---

## Q2 — Duplicate Detection

**Task:** Find elements appearing more than once. O(n), set operations only.

```python
def find_duplicates(lst: list) -> set:
    """
    Return a set of elements that appear more than once.
    O(n) time | O(n) space
    Uses only set operations — no Counter, no nested loops.
    """
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:        # O(1) lookup
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates


# Tests
print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))   # {2, 3}
print(find_duplicates([1, 1, 1, 1]))             # {1}
print(find_duplicates([1, 2, 3]))                # set()  — no duplicates
print(find_duplicates([]))                       # set()  — empty list
```

### Why O(n)?
- Single pass through the list: **O(n)**
- `item in seen` is a hash set lookup: **O(1)**
- Total: **O(n)** — no nested loops, no Counter

---

## Q3 — Debug Problem

**Buggy code:**
```python
def unique_to_each(a, b):
    result = set(a) - set(b)
    return list(result)

unique_to_each([1, 2, 3], [3, 4, 5])
# Expected: [1, 2, 4, 5]
# Actual:   [1, 2]
```

### Why the bug happens

`set(a) - set(b)` computes the **one-way difference** — elements in `a` that
are NOT in `b`. This returns `{1, 2}`, completely ignoring `4` and `5` which
are unique to `b`.

The question asks for the **symmetric difference** — elements that are in
either set, but NOT in both.

```
set(a) = {1, 2, 3}
set(b) = {3, 4, 5}

set(a) - set(b)             = {1, 2}       ← one-way, misses 4 and 5
set(a).symmetric_difference(set(b)) = {1, 2, 4, 5}  ← correct
```

### Fixed Function

```python
def unique_to_each(a: list, b: list) -> list:
    """
    Return elements that are unique to EITHER list (not in both).
    Uses symmetric difference: A △ B = (A - B) ∪ (B - A)
    """
    return list(set(a).symmetric_difference(set(b)))   # or: set(a) ^ set(b)


# Test
print(unique_to_each([1, 2, 3], [3, 4, 5]))   # [1, 2, 4, 5]  ✅
print(unique_to_each([1, 2], [1, 2]))          # []            ✅  all shared
print(unique_to_each([], [1, 2]))              # [1, 2]        ✅  edge case
```

The `^` operator is shorthand for symmetric difference:
```python
set(a) ^ set(b)   # equivalent and more concise
```
