def f(x):
    return x**2 - 2.2*x + 1.2

def fixed_point_iteration(x0, omega, tolerance=1e-5, max_iterations=50):
    x = x0
    for i in range(max_iterations):
        if abs(f(x)) < tolerance:
            print(f"Root is {x}, iterations = {i}")
            return x
        if abs(x) > 1e10:  # Check for divergence
            print("Divergence detected.")
            return None
        x = x + omega * f(x)
        print(f"Iteration {i}: x = {x}")
    print("Iterations exceeded.")
    return None

# (a) Initial guess x = 1.10, omega = 1.00
x_a = 1.10
omega_a = 1.00
result_a = fixed_point_iteration(x_a, omega_a)

# (b) Initial guess x = 0.90, omega = 1.00
x_b = 0.90
omega_b = 1.00
result_b = fixed_point_iteration(x_b, omega_b)

# (c) Initial guess x = 1.10, omega = 1.80
x_c = 1.10
omega_c = 1.80
result_c = fixed_point_iteration(x_c, omega_c)

# (d) Initial guess x = 0.90, omega = 1.80
x_d = 0.90
omega_d = 1.80
result_d = fixed_point_iteration(x_d, omega_d)

# (e) Initial guess x = 1.21, omega = 1.0
x_e = 1.21
omega_e = 1.0
result_e = fixed_point_iteration(x_e, omega_e)

# (f) Initial guess x = 1.21, omega = 1.6
x_f = 1.21
omega_f = 1.6
result_f = fixed_point_iteration(x_f, omega_f)

# (g) Initial guess x = 1.21, omega = -1.6
x_g = 1.21
omega_g = -1.6
result_g = fixed_point_iteration(x_g, omega_g)
