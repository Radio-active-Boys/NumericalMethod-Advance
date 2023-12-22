import numpy as np
from scipy.interpolate import CubicSpline

# Data
x_data = np.array([0.261799, 0.523599, 0.785398, 1.047198, 1.308997, 1.570796, 1.832596, 2.094395, 2.356194, 2.617994, 2.879793, 3.141593])
f_data = np.array([0.258819, 0.5, 0.707107, 0.866025, 0.965926, 1, 0.965926, 0.866025, 0.707107, 0.5, 0.258819, -3.2E-16])

# Create a cubic spline interpolator
spline = CubicSpline(x_data, f_data)

# Values of x for prediction
x_values = [1, 1.5, 2, 2.5, 3]

# Predict f(x) for x_values
f_values = spline(x_values)

# Print the results
for x, f in zip(x_values, f_values):
    print(f"f({x}) = {f:.6f}")
