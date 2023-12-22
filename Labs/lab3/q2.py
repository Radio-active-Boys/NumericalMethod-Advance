import numpy as np

# Define the matrix A and the right-hand side vector b
A = np.array([[3, -1, 2],
              [1, 2, 3],
              [2, -2, 1]])
b = np.array([12, 11, 2])

# Perform LU decomposition
n = A.shape[0]
L = np.zeros((n, n))
U = np.zeros((n, n))

for i in range(n):
    # U matrix
    U[i, i:] = A[i, i:]
    L[i:, i] = A[i:, i] / U[i, i]

    for j in range(i + 1, n):
        L[j, i] = A[j, i] - np.dot(L[j, :i], U[:i, i])
        U[i, j] = (A[i, j] - np.dot(L[i, :i], U[:i, j])) / L[i, i]

# Solve Ly = b using forward substitution
y = np.zeros(n)
for i in range(n):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

# Solve Ux = y using backward substitution
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

print("Solution x:", x)
