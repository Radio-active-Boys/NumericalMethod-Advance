def back_substitution(U, b):
    n = len(U)
    x = [0] * n  # Initialize the solution vector with zeros

    for i in range(n - 1, -1, -1):
        if U[i][i] == 0:
            raise ValueError("Matrix is singular or has zero pivot")

        x[i] = b[i] / U[i][i]  # Calculate the solution for the current variable

        for j in range(i - 1, -1, -1):
            b[j] -= U[j][i] * x[i]  # Update the right-hand side vector

    return x

# Example usage:
U = [[1,-1,2],[0,1,2],[0,0,-1]]
b = [-8,-2,-20]
solution = back_substitution(U, b)
print("Solution:", solution)
