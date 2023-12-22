import numpy as np

# Define the data points (x, f(x))
data = np.array([[0, 1], [1, 2], [2, 9], [3, 28], [4, 65], [5, 126]])

# Number of data points
n = data.shape[0]

# Define the polynomial order (cubic)
m = 3

# Initialize the matrix A and vector b for the least squares equation
A = np.zeros((n, m + 1))
b = np.zeros(n)

# Populate the A matrix and b vector
for i in range(n):
    x_i = data[i, 0]
    f_x_i = data[i, 1]
    for j in range(m + 1):
        A[i, j] = x_i ** j
    b[i] = f_x_i

# Solve the least squares system of equations
coefficients = np.linalg.lstsq(A, b, rcond=None)[0]

# Extract the coefficients for the cubic polynomial
a, b, c, d = coefficients

# Print the coefficients
print(f'Coefficients of the cubic polynomial:')
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')
print(f'd: {d}')
