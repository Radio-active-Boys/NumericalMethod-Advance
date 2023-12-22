import numpy as np

# Define the function y = a + b * x + c * x^2
def true_function(x, a, b, c):
    return a + b * x + c * x**2

# Construct a table of y values
N = 6  # Number of data points
a = 1.0
b = 2.0
c = 3.0
x_values = np.linspace(0, 1, N)
y_values = true_function(x_values, a, b, c)

# Read the value of x for interpolation
xx = float(input("Input the value of x where you need the value: "))

# Find the appropriate interval for interpolation
ii = 0
for i in range(1, N):
    if x_values[i] >= xx:
        ii = i
        break

if ii == 0 or ii == 1:
    print("x is out of range.")
else:
    if ii == 2:
        yy = y_values[ii-1:ii+2]
        xx = x_values[ii-1:ii+2]
    else:
        yy = y_values[ii-2:ii+1]
        xx = x_values[ii-2:ii+1]

    # Lagrange interpolation
    yyy = 0.0
    for i in range(3):
        prod = yy[i]
        for j in range(3):
            if i != j:
                prod *= (xx[3] - xx[j]) / (xx[i] - xx[j])
        yyy += prod

    print("The estimated value of y =", yyy)

# Calculate the actual values for comparison
actual_values = true_function(xx, a, b, c)
print("The actual values for comparison:")
for i, x in enumerate(xx):
    print(f"x = {x}, Actual y = {actual_values[i]}")

