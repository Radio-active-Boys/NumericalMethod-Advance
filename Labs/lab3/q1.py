import numpy as np

def lu_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        U[i, i] = 1

    for i in range(n):
        L[i, 0] = matrix[i, 0]

    for j in range(1, n):
        U[0, j] = matrix[0, j] / L[0, 0]

    for j in range(1, n):
        for i in range(j, n):
            L[i, j] = matrix[i, j]
            for k in range(j):
                L[i, j] -= L[i, k] * U[k, j]

        for i in range(j + 1, n):
            U[j, i] = matrix[j, i]
            for k in range(j):
                U[j, i] -= L[j, k] * U[k, i]
            U[j, i] /= L[j, j]

    L[n - 1, n - 1] = matrix[n - 1, n - 1]
    for k in range(n - 1):
        L[n - 1, n - 1] -= L[n - 1, k] * U[k, n - 1]

    return L, U

# Example matrix
A = np.array([[4.0, 3.0, 3.0],
              [6.0, 6.0, 1.0],
              [3.0, 1.0, 3.0]])

# Perform LU decomposition
L, U = lu_decomposition(A)

# Print L and U matrices
print("L matrix:")
print(L)
print("U matrix:")
print(U)
