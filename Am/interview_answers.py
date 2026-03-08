# interview_answers.py
# Day 9 AM – Part C: Interview Ready

import copy

# ══════════════════════════════════════════════════════════════════
# Q1 — Shallow Copy vs Deep Copy
# ══════════════════════════════════════════════════════════════════
"""
SHALLOW COPY
------------
A shallow copy creates a new list object, but the elements inside are
still references to the same objects as in the original list.

• For a flat (1D) list, shallow copy is fine — integers/strings are
  immutable, so changing them in the copy doesn't affect the original.
• For a NESTED list, the inner lists are shared between original and copy.
  Mutating an inner list through the copy also mutates the original.

DEEP COPY
---------
A deep copy creates a completely independent new object, recursively
copying every element — including all nested structures.
No references are shared with the original.

WHY SHALLOW COPY FAILS WITH NESTED LISTS
-----------------------------------------
"""

print("=" * 55)
print("  Q1 – Shallow vs Deep Copy Demo")
print("=" * 55)

original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# --- Shallow copy ---
shallow = copy.copy(original)       # same as original[:]  or  list(original)
shallow[0][0] = 99                  # mutate inner list through shallow copy

print("\n  After shallow[0][0] = 99 :")
print(f"    original : {original}")   # ← original[0][0] is ALSO 99  ❌
print(f"    shallow  : {shallow}")

# reset
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# --- Deep copy ---
deep = copy.deepcopy(original)
deep[0][0] = 99                     # mutate inner list through deep copy

print("\n  After deep[0][0] = 99 :")
print(f"    original : {original}")   # ← original[0][0] stays 1  ✅
print(f"    deep     : {deep}")

"""
WHEN TO USE DEEP COPY
----------------------
• When you have nested lists / objects and need a completely independent copy.
• When passing mutable structures to functions and you don't want side effects.
• When implementing undo/redo history in applications.

SUMMARY TABLE
┌───────────────┬──────────────────────────┬───────────────────────────┐
│               │ Shallow Copy             │ Deep Copy                 │
├───────────────┼──────────────────────────┼───────────────────────────┤
│ Flat list     │ Safe ✅                  │ Safe ✅                   │
│ Nested list   │ Inner lists shared ❌    │ Fully independent ✅      │
│ Speed         │ Faster                   │ Slower                    │
│ Module needed │ copy.copy()              │ copy.deepcopy()           │
└───────────────┴──────────────────────────┴───────────────────────────┘
"""


# ══════════════════════════════════════════════════════════════════
# Q2 — List Rotation
# ══════════════════════════════════════════════════════════════════
def rotate_list(lst: list, k: int) -> list:
    """
    Rotate a list to the right by k positions using slicing.
    Handles k > len(lst) with modulo.

    Example:
        rotate_list([1, 2, 3, 4, 5], 2)  →  [4, 5, 1, 2, 3]
    
    Logic:
        k = k % n  prevents unnecessary full rotations
        split = n - k  is the pivot index
        result = lst[split:] + lst[:split]
    """
    if not lst:
        return []
    n = len(lst)
    k = k % n           # handle k > len(lst)
    split = n - k
    return lst[split:] + lst[:split]


print("\n" + "=" * 55)
print("  Q2 – List Rotation Tests")
print("=" * 55)
print(f"  rotate_list([1,2,3,4,5], 2)   → {rotate_list([1,2,3,4,5], 2)}")   # [4,5,1,2,3]
print(f"  rotate_list([1,2,3,4,5], 7)   → {rotate_list([1,2,3,4,5], 7)}")   # k%5=2 → [4,5,1,2,3]
print(f"  rotate_list([1,2,3,4,5], 0)   → {rotate_list([1,2,3,4,5], 0)}")   # no rotation
print(f"  rotate_list([10], 5)           → {rotate_list([10], 5)}")           # single element
print(f"  rotate_list([], 3)             → {rotate_list([], 3)}")             # empty list


# ══════════════════════════════════════════════════════════════════
# Q3 — Debug Problem
# ══════════════════════════════════════════════════════════════════
print("\n" + "=" * 55)
print("  Q3 – Debug Problem")
print("=" * 55)

"""
BUGGY CODE:
-----------
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    for num in nums:
        if num % 2 == 0:
            nums.remove(num)
    print(nums)
    # Actual (wrong) output: [1, 3, 5, 7, 6, 8]  or similar

WHY THE BUG HAPPENS:
--------------------
When you iterate over a list and modify it at the same time, Python's
internal index pointer gets confused.

Step-by-step with [2, 4, 6, 8]:
  Index 0 → num=2 (even) → remove(2) → list becomes [4,6,8]
  Index 1 → num=6 (Python skipped index 0 which is now 4!) → remove(6) → [4,8]
  Index 2 → out of range → loop ends
  Result: [4, 8]  ← 4 and 8 were never checked!

Root cause: removing elements shifts all subsequent indices left by 1,
but the loop counter keeps incrementing → elements are skipped.

This is especially visible with a list of all-even numbers like [2,4,6,8].
Expected output: []  but you get [4, 8].

CORRECT SOLUTION 1 – List Comprehension (Recommended):
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums = [n for n in nums if n % 2 != 0]
print(f"\n  Solution 1 (comprehension) : {nums}")  # [1,3,5,7]

"""
CORRECT SOLUTION 2 – Iterate over a copy:
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8]
for num in nums[:]:            # nums[:] creates a shallow copy to iterate over
    if num % 2 == 0:
        nums.remove(num)
print(f"  Solution 2 (copy loop)     : {nums}")   # [1,3,5,7]

"""
CORRECT SOLUTION 3 – filter():
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums = list(filter(lambda n: n % 2 != 0, nums))
print(f"  Solution 3 (filter)        : {nums}")   # [1,3,5,7]

# Demonstrate the bug clearly with all-even list
nums_bug = [2, 4, 6, 8]
for num in nums_bug:
    if num % 2 == 0:
        nums_bug.remove(num)
print(f"\n  Bug demo with [2,4,6,8]    : {nums_bug}")  # Shows [4,8] — wrong!
