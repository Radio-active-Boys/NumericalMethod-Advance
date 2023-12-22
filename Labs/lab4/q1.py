import numpy as np

def newton_raphson_solver(combined_f, initial_guess, tol=1e-6, max_iter=100):
    x = np.array(initial_guess, dtype=float)
    iter_count = 0
    
    while iter_count < max_iter:
        y = combined_f(x)
        J = compute_jacobian(combined_f, x)
        dx = np.linalg.solve(J, -y)
        x = x + dx
        
        if np.max(np.abs(dx)) < tol:
            return x
        
        iter_count += 1
    
    raise Exception("Newton-Raphson did not converge")

def compute_jacobian(f, x, epsilon=1e-7):
    n = len(x)
    m = len(f(x))
    J = np.zeros((m, n), dtype=float)
    
    for i in range(m):
        for j in range(n):
            x_plus_dx = np.array(x, dtype=float)
            x_plus_dx[j] += epsilon
            J[i, j] = (f(x_plus_dx)[i] - f(x)[i]) / epsilon
    
    return J

# Example usage:
def combined_f(x):
    f1 = x[0]**2 + x[1]**2 - 4
    f2 = x[0] - x[1] - 1
    return np.array([f1, f2])

initial_guess = [1.0, 2.0]
solution = newton_raphson_solver(combined_f, initial_guess)
print("Solution:", solution)
