import numpy as np
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication (the important one)
print(A @ B)                      # same as np.matmul(A, B)

# Transpose
print(A.T)

# Inverse
print(np.linalg.inv(A))

# Determinant
print(np.linalg.det(A))           # you'll use this Wednesday

# Eigenvalues + eigenvectors
print(np.linalg.eig(A))           # you'll use this Sunday

#rotation of matrix
# Rotation matrix (90 degrees)
theta = np.pi / 2
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])

v = np.array([1, 0])
print(R @ v)                      # rotates the vector