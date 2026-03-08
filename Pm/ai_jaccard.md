# ai_jaccard.md
# Day 9 PM – Part D: AI-Augmented Task

---

## Step 1 — Exact Prompt Used

> "Write a Python function that calculates the Jaccard similarity between two sets of strings. Explain what Jaccard similarity is and where it is used in industry."

---

## Step 2 — AI-Generated Output

```python
def jaccard_similarity(set_a, set_b):
    intersection = set_a & set_b
    union = set_a | set_b
    if len(union) == 0:
        return 0
    return len(intersection) / len(union)

# Example
set_a = {'python', 'java', 'sql'}
set_b = {'python', 'sql', 'docker', 'aws'}
print(jaccard_similarity(set_a, set_b))
```

**AI's explanation:**
Jaccard similarity measures how similar two sets are. The formula is:

`J(A, B) = |A ∩ B| / |A ∪ B|`

It returns a value between 0 (no overlap) and 1 (identical sets).

---

## Step 3 — Testing the AI Code

```python
set_a = {'python', 'java', 'sql'}
set_b = {'python', 'sql', 'docker', 'aws'}
print(jaccard_similarity(set_a, set_b))
# intersection = {'python', 'sql'} → size 2
# union = {'python', 'java', 'sql', 'docker', 'aws'} → size 5
# Expected: 2/5 = 0.4
# Output: 0.4  ✅ Correct
```

### Validation Checklist

| Check | Result |
|---|---|
| Formula correct? | ✅ `|A ∩ B| / |A ∪ B|` — correct |
| Empty set handled? | ✅ Returns 0 when union is empty |
| Both empty sets? | ✅ `0/0` avoided via the guard clause |
| One empty, one not? | ✅ Returns 0 (no overlap, union = the non-empty set) |
| Identical sets? | ✅ Returns 1.0 |
| No overlap at all? | ✅ Returns 0.0 |

The AI-generated code is **correct and handles edge cases well**.

---

## Step 4 — Improved Version

```python
def jaccard_similarity(set_a: set, set_b: set) -> float:
    """
    Calculate Jaccard similarity between two sets.

    Formula: J(A, B) = |A ∩ B| / |A ∪ B|
    Returns a float in [0.0, 1.0]:
        0.0  → completely disjoint sets
        1.0  → identical sets

    Args:
        set_a: first set of elements
        set_b: second set of elements

    Returns:
        Jaccard similarity score (float)
    """
    # Accept lists/tuples and auto-convert for convenience
    set_a = set(set_a)
    set_b = set(set_b)

    intersection = set_a & set_b
    union = set_a | set_b

    if not union:          # both sets empty → define similarity as 1.0 (identical)
        return 1.0

    return round(len(intersection) / len(union), 4)


# ── Tests ──
print(jaccard_similarity({'python','java','sql'}, {'python','sql','docker','aws'}))
# → 0.4  ✅

print(jaccard_similarity({'a','b','c'}, {'a','b','c'}))
# → 1.0  ✅ identical

print(jaccard_similarity({'a','b'}, {'c','d'}))
# → 0.0  ✅ no overlap

print(jaccard_similarity(set(), set()))
# → 1.0  ✅ two empty sets are identical by definition

print(jaccard_similarity(set(), {'a','b'}))
# → 0.0  ✅ nothing in common
```

### Improvement Over AI Version

| Aspect | AI Version | Improved Version |
|---|---|---|
| Type hints | ❌ None | ✅ `set_a: set, set_b: set → float` |
| Docstring | ❌ None | ✅ Full docstring with formula |
| Auto-converts lists | ❌ Crashes on list input | ✅ `set(set_a)` handles lists/tuples |
| Both empty sets | Returns 0 (debatable) | Returns 1.0 (mathematically consistent) |
| Result precision | Raw float | `round(..., 4)` for clean output |

---

## Industry Applications of Jaccard Similarity

**Recommendation Systems:** Platforms like Amazon and Netflix use Jaccard
similarity to compare users' purchase or viewing histories (treated as sets of
items). Users with high Jaccard similarity are considered similar, so products
one user liked can be recommended to the other.

**NLP & Document Similarity:** Documents are represented as sets of words or
n-grams, and Jaccard similarity scores how much vocabulary they share. This
powers near-duplicate detection in search engines and content deduplication
pipelines.

**Plagiarism Detection:** Tools like Turnitin break texts into shingles (short
overlapping word sequences represented as sets) and compute Jaccard similarity
against a database. A high score indicates likely copied content.

**Bioinformatics:** Jaccard similarity is used to compare gene sets, protein
interaction networks, and biological pathway memberships — measuring how much
two biological entities share common features.
