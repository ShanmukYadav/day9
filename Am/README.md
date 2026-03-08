# 📘 Day 9 · AM — Lists Deep Dive
**Submission Date:** 08-03-2026 | **Due:** 23:00  
**Topic:** List creation, indexing, slicing, list methods, list comprehensions, shallow vs deep copy  
**Folder:** `/week2/day9/Am/`

---

## 📁 File Structure

```
week2/day9/Am/
├── student_system.py     # Part A — Student Management System
├── matrix_ops.py         # Part B — Matrix Operations
├── interview_answers.py  # Part C — Interview Ready
├── ai_pair_sum.md        # Part D — AI-Augmented Task
└── README.md
```

---

## 🧠 Part A — Student Management System (`student_system.py`)

A CLI-based Student Management System backed by a list of lists.

### Data Structure
```python
records = [
    ["Aman",   "Math",      88],
    ["Priya",  "Physics",   91],
    ...  # 12 students across Math, Physics, Chemistry
]
```

### Functions Implemented

| Function | Description | Key Concept Used |
|---|---|---|
| `add_student(name, subject, marks)` | Adds a record, prevents duplicates | `append` |
| `get_toppers(subject)` | Returns top 3 by marks | `sorted(..., key=lambda)` + slicing |
| `class_average(subject)` | Returns average marks for a subject | list comprehension |
| `above_average_students()` | Returns students above overall average | comprehension + nested logic |
| `remove_student(name)` | Removes all records of a student | safe filter comprehension |
| `save_to_file()` | Saves all records to `students.txt` | file I/O |

### How to Run
```bash
python student_system.py
```
Use the numbered menu (1–6) to interact. Records are saved to `students.txt` on exit.

---

## 🚀 Part B — Matrix Operations (`matrix_ops.py`)

Implements core matrix operations using nested lists.

### Functions

| Function | Description |
|---|---|
| `matrix_add(A, B)` | Element-wise sum of two matrices |
| `matrix_transpose(matrix)` | Transpose using `zip(*matrix)` |
| `matrix_multiply(A, B)` | Dot-product multiplication with dimension check |

### Sample Output
```
matrix_add([[1,2],[3,4]], [[5,6],[7,8]])      → [[6,8],[10,12]]
matrix_transpose([[1,2],[3,4]])               → [[1,3],[2,4]]
matrix_multiply([[1,2],[3,4]], [[5,6],[7,8]]) → [[19,22],[43,50]]
```

### How to Run
```bash
python matrix_ops.py
```

---

## 💼 Part C — Interview Ready (`interview_answers.py`)

### Q1 — Shallow vs Deep Copy
- Demonstrates with a nested list example
- Shows why `copy.copy()` fails for nested structures
- Explains when `copy.deepcopy()` is required

### Q2 — List Rotation
```python
rotate_list([1, 2, 3, 4, 5], 2)  →  [4, 5, 1, 2, 3]
```
Uses slicing with `k % n` to handle `k > len(lst)`.

### Q3 — Debug Problem
Identifies the bug in modifying a list while iterating over it, demonstrates the failure case with `[2,4,6,8]`, and provides 3 correct solutions using list comprehension, copy-loop, and `filter()`.

### How to Run
```bash
python interview_answers.py
```

---

## 🤖 Part D — AI-Augmented Task (`ai_pair_sum.md`)

**Prompt used:**
> "Write a Python function that finds all pairs in a list that sum to a target number using list comprehensions."

### What Was Found & Fixed

| Issue | AI Version | Improved Version |
|---|---|---|
| Duplicate pairs | ❌ Returns `(1,1)` three times for `[1,1,1]` | ✅ Returns `(1,1)` once |
| Order sensitivity | ❌ `(1,5)` and `(5,1)` treated differently | ✅ Normalized via `sorted()` |
| Performance | O(n²) | Also includes O(n) set-based solution |

---

## ✅ Concepts Demonstrated

- `append`, `pop`, `sorted`, `remove` (safe usage)
- List comprehensions (flat and nested)
- List slicing
- Shallow copy vs deep copy (`copy` module)
- File I/O (`open`, `write`)
- Lambda functions as sort keys
- Modifying lists safely during iteration
