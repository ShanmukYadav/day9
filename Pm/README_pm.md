# 📘 Day 9 · PM — Tuples & Sets Deep Dive
**Submission Date:** 08-03-2026 | **Due:** 23:00  
**Topic:** Tuple creation, unpacking, named tuples, set operations, frozenset, O(1) lookup  
**Folder:** `/week2/day9/Pm/`

---

## 📁 File Structure

```
week2/day9/Pm/
├── product_analytics.py    # Part A — E-Commerce Analytics Tool
├── frozenset_bundles.py    # Part B — Bundle Discount System
├── interview_answers.md    # Part C — Interview Questions
├── ai_jaccard.md           # Part D — AI-Augmented Task
└── README.md
```

---

## 🧠 Part A — Product Analytics Tool (`product_analytics.py`)

A shopping behaviour analysis tool built with named tuples and sets.

### Data Model
```python
from collections import namedtuple
Product = namedtuple("Product", ["id", "name", "category", "price"])
```
- 16 products across 4 categories: **Electronics, Clothing, Books, Home**
- 5 customer carts modelled as sets of `Product` named tuples

### Functions Implemented

| Function | Description | Set Operation Used |
|---|---|---|
| `bestsellers()` | Products in ALL carts | `intersection` |
| `catalog_reach()` | Products in ANY cart | `union` |
| `exclusive_purchases(cart, others)` | Products only one customer bought | `difference` (`-`) |
| `recommend_products(cart, all_carts)` | Suggest what others bought | `difference` |
| `category_summary()` | Map category → set of product names | set comprehension |

### How to Run
```bash
python product_analytics.py
```

---

## 🚀 Part B — Frozenset Bundle Discount System (`frozenset_bundles.py`)

Demonstrates why `frozenset` is needed as dictionary keys for bundle combinations.

### Bundle Discount Table
| Bundle | Discount |
|---|---|
| Electronics + Books | 10% |
| Clothing + Home | 15% |
| Electronics + Clothing | 8% |
| Books + Home | 12% |
| All 4 categories | 20% |

### Key Concept
```python
# set cannot be a dict key → TypeError
# frozenset CAN be a dict key → works perfectly
bundle_discounts = {
    frozenset({"Electronics", "Books"}): 10,
    ...
}
```

### Includes
- `check_bundle_discount(cart_categories)` — finds all applicable deals
- `timeit` benchmark comparing `set` vs `frozenset` creation (100,000 iterations)
- Detailed comment block explaining frozenset vs set

### How to Run
```bash
python frozenset_bundles.py
```

---

## 💼 Part C — Interview Ready (`interview_answers.md`)

### Q1 — Tuple Immutability Trap
```python
t = ([1, 2], [3, 4])
t[0][0] = 99   # Does this work?
```
✅ It works — tuples are shallowly immutable. The tuple's slot still points to the same list object; the list's contents were mutated, not the tuple's references.

### Q2 — Duplicate Detection (O(n), sets only)
```python
find_duplicates([1, 2, 3, 2, 4, 3, 5])  →  {2, 3}
```
Uses a `seen` set and a `duplicates` set — single pass, O(1) lookups, O(n) total.

### Q3 — Debug: `unique_to_each`
**Bug:** Used one-way `set(a) - set(b)` instead of symmetric difference.  
**Fix:** `set(a) ^ set(b)` or `set(a).symmetric_difference(set(b))`
```python
unique_to_each([1,2,3], [3,4,5])  →  [1, 2, 4, 5]  ✅
```

---

## 🤖 Part D — AI-Augmented Task (`ai_jaccard.md`)

**Prompt used:**
> "Write a Python function that calculates the Jaccard similarity between two sets of strings. Explain what Jaccard similarity is and where it is used in industry."

### Formula
```
J(A, B) = |A ∩ B| / |A ∪ B|     →  range: [0.0, 1.0]
```

### AI Code Assessment
- ✅ Formula correct
- ✅ Empty set edge case handled
- ❌ No type hints or docstring
- ❌ Crashes if passed lists instead of sets
- ❌ Defines `similarity(∅, ∅) = 0` — improved to `1.0`

### Industry Use Cases
Recommendation systems, NLP document similarity, plagiarism detection, bioinformatics gene-set comparison.

---

## ✅ Concepts Demonstrated

- `namedtuple` from `collections`
- Set operations: `intersection`, `union`, `difference`, `symmetric_difference`
- Set comprehensions
- `frozenset` as dictionary key
- Tuple immutability (shallow) trap
- O(1) set membership lookup
- `timeit` for performance benchmarking
