import time
import numpy as np
def matmul(A,B):
    assert len(A[0]) == len(B) , f"Incompatible A @ B since column of A: {len(A[0])} != row of B: {len(B)}"
    rows_A, cols_A, cols_B = len(A), len(A[0]), len(B[0])
    result = [[0]*cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

size = 50
A_big = [[1]*size for _ in range(size)]
B_big = [[1]*size for _ in range(size)]
A_np = np.ones((size, size))
B_np = np.ones((size, size))

start = time.time()
for _ in range(100):
    matmul(A_big, B_big)
pure_python = (time.time() - start) / 100

start = time.time()
for _ in range(100):
    np.matmul(A_np, B_np)
numpy_time = (time.time() - start) / 100

print(f"Pure Python: {pure_python*1000:.2f} ms")
print(f"NumPy:       {numpy_time*1000:.4f} ms")
print(f"Speedup:     {pure_python/numpy_time:.0f}x")