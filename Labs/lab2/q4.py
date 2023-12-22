import numpy as np

def solve_upper_triangular(U, b):
    n = len(U)
    x = np.zeros(n)
    
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    
    return x

def gaussian_elimination(A, b):
    n = len(A)
    augmented_matrix = np.column_stack((A, b))

    for i in range(n):
        # Partial pivoting
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    x = solve_upper_triangular(augmented_matrix[:, :-1], augmented_matrix[:, -1])
    return x

# Example system of linear equations
A = np.array([[2.0, 1.0, -1.0],
              [1.0, 3.0, 2.0],
              [3.0, 2.0, -3.0]])
b = np.array([8.0, 9.0, 3.0])

# Perform Gaussian elimination
solution = gaussian_elimination(A, b)
print("Solution:", solution)
