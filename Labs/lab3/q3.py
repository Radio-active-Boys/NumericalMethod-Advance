import numpy as np

def thomas_algorithm(n, aa, rhs):
    # Ensure aa is a NumPy array
    aa = np.array(aa, dtype=float)
    rhs = np.array(rhs, dtype=float)

    # Forward elimination
    for i in range(1, n):
        aa[i, 2] /= aa[i, 1]
        aa[i, 1] -= aa[i, 2] * aa[i-1, 3]
        rhs[i] -= aa[i, 2] * rhs[i-1]

    # Back substitution
    solution = np.zeros(n, dtype=float)
    solution[-1] = rhs[-1] / aa[-1, 1]

    for i in range(n - 2, -1, -1):
        solution[i] = (rhs[i] - aa[i, 3] * solution[i+1]) / aa[i, 1]

    return solution

# Example usage
n = 4  # Number of equations
aa = np.array([[0, 1, 0], [1, -2, 1], [0, 1, -2], [0, 0, 1]], dtype=float)
rhs = np.array([0, 0, 0, 1], dtype=float)

solution = thomas_algorithm(n, aa, rhs)
print("Solution x:", solution)
