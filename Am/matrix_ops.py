# matrix_ops.py
# Day 9 AM – Part B: Matrix Operations using Lists

# ─────────────────────────────────────────────
# 1. Matrix Addition
# ─────────────────────────────────────────────
def matrix_add(A: list, B: list) -> list:
    """
    Return element-wise sum of two matrices.
    Raises ValueError if dimensions don't match.
    """
    if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
        raise ValueError("Matrix dimensions must match for addition.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


# ─────────────────────────────────────────────
# 2. Matrix Transpose
# ─────────────────────────────────────────────
def matrix_transpose(matrix: list) -> list:
    """
    Return the transpose of a matrix using nested list comprehension.
    zip(*matrix) groups columns together.
    """
    return [list(row) for row in zip(*matrix)]


# ─────────────────────────────────────────────
# 3. Matrix Multiplication
# ─────────────────────────────────────────────
def matrix_multiply(A: list, B: list) -> list:
    """
    Return the dot-product multiplication of two matrices.
    Handles dimension mismatch gracefully.
    A: m×n   B: n×p  → Result: m×p
    """
    cols_A = len(A[0])
    rows_B = len(B)
    if cols_A != rows_B:
        raise ValueError(
            f"Cannot multiply: columns of A ({cols_A}) ≠ rows of B ({rows_B})."
        )
    return [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)]
        for row_a in A
    ]


# ─────────────────────────────────────────────
# Helper: pretty-print a matrix
# ─────────────────────────────────────────────
def print_matrix(matrix: list, label: str = "") -> None:
    if label:
        print(f"\n  {label}:")
    for row in matrix:
        print("  ", row)


# ─────────────────────────────────────────────
# Tests
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 45)
    print("  Matrix Operations – Test Suite")
    print("=" * 45)

    # ── Test 1: 2×2 matrices ──
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    print("\n  ── 2×2 Matrices ──")
    print_matrix(a, "A")
    print_matrix(b, "B")

    result_add  = matrix_add(a, b)
    result_T    = matrix_transpose(a)
    result_mul  = matrix_multiply(a, b)

    print_matrix(result_add, "A + B  (expected [[6,8],[10,12]])")
    print_matrix(result_T,   "Transpose of A  (expected [[1,3],[2,4]])")
    print_matrix(result_mul, "A × B  (expected [[19,22],[43,50]])")

    # ── Test 2: 3×3 matrices ──
    c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    d = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    print("\n  ── 3×3 Matrices ──")
    print_matrix(c, "C")
    print_matrix(d, "D")
    print_matrix(matrix_add(c, d),       "C + D")
    print_matrix(matrix_transpose(c),    "Transpose of C")
    print_matrix(matrix_multiply(c, d),  "C × D")

    # ── Test 3: Dimension mismatch ──
    print("\n  ── Dimension Mismatch Test ──")
    try:
        matrix_multiply([[1, 2]], [[1, 2]])   # 1×2 × 1×2 → should fail
    except ValueError as e:
        print(f"  ✅  Caught expected error: {e}")
