import numpy as np

v1 = np.array([2, 3])      # 2D vector
v2 = np.array([1, -1])

print(v1 + v2)                    # array([3, 2])

print(2 * v1)                     # array([4, 6])

print(np.dot(v1, v2))             # 2*1 + 3*(-1) = -1

print(np.linalg.norm(v1))         # sqrt(4+9) = 3.6