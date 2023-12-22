import numpy as np

# Function to define the system of nonlinear equations
def system_equations(x, k):
    k1, k2, k3, k4 = k
    f1 = -x[0] + 10 + 2 * (-k1 * x[0] - k2 * x[0]**1.5 + k3 * x[2]**2)
    f2 = -x[1] + 2 * (2 * k1 * x[0] - k4 * x[1]**2)
    f3 = -x[2] + 2 * (k2 * x[0]**1.5 - k4 * x[1]**2 - k3 * x[2]**2)
    f4 = -x[3] + 2 * (k4 * x[1]**2)
    return np.array([f1, f2, f3, f4])

# Function to compute the Jacobian matrix
def jacobian(x, k):
    k1, k2, k3, k4 = k
    J = np.zeros((4, 4), dtype=float)
    J[0, 0] = -1.0 - 2 * k1 - 3 * k2 * (x[0]**0.5)
    J[0, 1] = 0
    J[0, 2] = 4 * k3 * x[2]
    J[0, 3] = 0
    J[1, 0] = 4 * k1 * x[0] - 3 * k4 * (x[1]**2)
    J[1, 1] = -1.0 - 4 * k4 * x[1]
    J[1, 2] = 0
    J[1, 3] = 0
    J[2, 0] = 3 * k2 * (x[0]**0.5)
    J[2, 1] = -4 * k4 * x[1]
    J[2, 2] = -1.0 - 4 * k3 * x[2]
    J[2, 3] = 0
    J[3, 0] = 0
    J[3, 1] = 4 * k4 * x[1]
    J[3, 2] = 0
    J[3, 3] = -1.0
    return J

# Newton-Raphson method to solve the equations
def newton_raphson_solver(x, k, tol=1e-4, max_iter=100):
    residuals = []
    
    for i in range(max_iter):
        f = system_equations(x, k)
        J = jacobian(x, k)
        dx = np.linalg.solve(J, -f)
        x = x + dx
        residual = np.max(np.abs(f))
        residuals.append(residual)
        
        if residual < tol:
            return x, residuals
    
    return x, residuals

# Set the parameters
k = [1.0, 0.2, 0.05, 0.4]

# Initial guess
x0 = np.array([1.0, 1.0, 1.0, 1.0])

# Solve the system
converged_x, residuals = newton_raphson_solver(x0, k)

# Print the converged values of x1, x2, x3, and x4
x1, x2, x3, x4 = converged_x
print("Converged Values:")
print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)
print("x4 =", x4)

# Print the residuals at the end of each iteration
print("Residuals at the end of each iteration:")
for i, residual in enumerate(residuals):
    print(f"Iteration {i+1}: Residual = {residual:.4e}")
