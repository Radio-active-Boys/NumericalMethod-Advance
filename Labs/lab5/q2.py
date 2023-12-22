import numpy as np

# Define your data points (x, f(x))
data = np.array([
    [0.261799, 0.258819],
    [0.523599, 0.5],
    [0.785398, 0.707107],
    [1.047198, 0.866025],
    [1.308997, 0.965926],
    [1.570796, 1],
    [1.832596, 0.965926],
    [2.094395, 0.866025],
    [2.356194, 0.707107],
    [2.617994, 0.5],
    [2.879793, 0.258819],
    [3.141593, -3.2E-16]
])

# Separate x and f(x) values
x = data[:, 0]
fx = data[:, 1]

# Function to perform cubic spline interpolation
def cubic_spline_interpolation(x, fx, x_interpolate):
    n = len(x)
    a = fx.copy()
    h = np.diff(x)
    alpha = np.zeros(n)
    l = np.ones(n)
    mu = np.zeros(n)
    z = np.zeros(n)

    for i in range(1, n - 1):
        alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    c = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    for i in range(n - 1):
        if x_interpolate >= x[i] and x_interpolate <= x[i + 1]:
            dx = x_interpolate - x[i]
            interpolated_fx = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
            return interpolated_fx

# Specify the x values for prediction
x_values_to_predict = [1, 1.5, 2, 2.5, 3]

# Predict f(x) for the specified x values
for x_value in x_values_to_predict:
    fx_predicted = cubic_spline_interpolation(x, fx, x_value)
    print(f'x = {x_value:.2f}, f(x) ≈ {fx_predicted:.6f}')
