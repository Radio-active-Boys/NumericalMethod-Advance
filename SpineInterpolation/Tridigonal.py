def thomas_algorithm(N, a, b, c, d):
    # Forward elimination (Upper Triangulation)
    for i in range(1, N):
        factor = a[i] / b[i - 1]
        b[i] -= factor * c[i - 1]
        d[i] -= factor * d[i - 1]

    # Back substitution
    x = [0] * N
    x[-1] = d[-1] / b[-1]
    for i in range(N - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

    return x

# Example usage
N = 4
a = [0, 1, 1, 0]  # Sub-diagonal
b = [1, -2, -2, 1]  # Diagonal
c = [0, 1, 1, 0]  # Super-diagonal
d = [0, 0, 0, 1]  # Right-hand side

x = thomas_algorithm(N, a, b, c, d)
print("Solution:", x)
