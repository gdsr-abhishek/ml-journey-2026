def apply_transformation(matrix, vector):
    transformed_matrix=[]
    i=0
    j=0
    for i in range(len(matrix)):
        sum = 0 
        for j in range(len(matrix[i])):
            sum +=matrix[i][j] * vector[j]
        transformed_matrix.append(sum)
    return transformed_matrix

    return
import numpy as np

A = np.array([[0, -1], [1, 0]])  # 90-degree rotation
v = np.array([1, 0])

your_result = apply_transformation([[0,-1],[1,0]], [1,0])
numpy_result = (A @ v).tolist()

print(your_result == numpy_result)  # should be True