Matrix Multiplication — why (i,j) comes from row i of A and column j of B

The algebraic answer:
result[i][j] = sum of A[i][k] * B[k][j] for all k

But the geometric answer is more useful.

In 3B1B terms, a matrix is a transformation between spaces.
Each COLUMN of a matrix is a basis vector — where that dimension lands after the transform.

When you compute A @ B:
- B transforms a vector first (its columns are the new basis vectors)
- A then transforms the result (its columns are another set of basis vectors)
- The composition only makes sense if B's output dimension == A's input dimension
  → which is why cols_A must equal rows_B

Why row i of A, column j of B specifically?
- Column j of B tells you where the j-th basis vector lands after B's transform
- Row i of A is the i-th component of A's output space
- Their dot product gives you the i-th component of where B's j-th basis vector
  ends up after BOTH transforms — which is exactly result[i][j]

This is why a 1x2 matrix fed into a 2x2 rotation fails geometrically:
- 1x2 outputs a scalar (1D)
- The rotation lives in 2D input space
- There's no basis to rotate — the dimensions don't connect

Nonsquare matrices aren't broken — they're intentional dimension changes.
A 2x3 matrix maps 3D → 2D (projects down).
The rule cols_A == rows_B is just the geometry forcing your hand.

Timing result (50x50, 100 runs averaged):
Pure Python: 8.64 ms
NumPy:       0.01 ms
Speedup:     862x

Why: NumPy calls BLAS (Basic Linear Algebra Subprograms) —
Fortran/C routines, vectorized, parallelized at CPU level.
Same math, completely different execution.
This gap grows with matrix size.