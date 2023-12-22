def f1(x):
    return x**2 - 2*x + 1

def f2(x):
    return x**2 - 3*x + 2

def newton_method(f, df, x0, tolerance=1e-12):
    x = x0
    iterations = 0
    x_values = [x]
    e_values = [abs(x - 1)]
    f_values = [f(x)]

    while abs(f(x)) >= tolerance:
        x = x - f(x) / df(x)
        iterations += 1
        x_values.append(x)
        e_values.append(abs(x - 1))
        f_values.append(f(x))

    return x_values, e_values, f_values, iterations

x0 = 1.1

# Case (a) f(x) = x^2 - 2x + 1
def df1(x):
    return 2*x - 2

x_values1, e_values1, f_values1, iterations1 = newton_method(f1, df1, x0)

print("Case (a): f(x) = x^2 - 2x + 1")
for i, (x, e, f) in enumerate(zip(x_values1, e_values1, f_values1)):
    print(f"Iteration {i}: x = {x}, e = {e}, f(x) = {f}")

print(f"Number of iterations for convergence (Case a): {iterations1}")

# Case (b) f(x) = x^2 - 3x + 2
def df2(x):
    return 2*x - 3

x_values2, e_values2, f_values2, iterations2 = newton_method(f2, df2, x0)

print("\nCase (b): f(x) = x^2 - 3x + 2")
for i, (x, e, f) in enumerate(zip(x_values2, e_values2, f_values2)):
    print(f"Iteration {i}: x = {x}, e = {e}, f(x) = {f}")

print(f"Number of iterations for convergence (Case b): {iterations2}")
