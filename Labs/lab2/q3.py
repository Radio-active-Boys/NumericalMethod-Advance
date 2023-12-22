import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    augmented_matrix = np.column_stack((A, b))

    for i in range(n):
        # Partial pivoting: Find the pivot row with the maximum absolute value in the current column
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented_matrix[k, i]) > abs(augmented_matrix[max_row, i]):
                max_row = k

        # Swap the current row with the pivot row
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        # Elimination
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    # Back-substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] / augmented_matrix[i, i]
        for j in range(i + 1, n):
            x[i] -= augmented_matrix[i, j] * x[j] / augmented_matrix[i, i]

    return x

# Example usage:
A = np.array([[3.0, -1.0, 2.0],
              [1.0,2.0, 3.0],
              [2.0, -2.0, -1.0]])
b = np.array([12.0, 11.0, 2.0])

solution = gaussian_elimination(A, b)
print("Solution:", solution)
