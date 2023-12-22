import math

def exponential_series(y):
    tol = 1e-12
    x = abs(y) if y < 0 else y
    sum = 1.0
    term = 1.0

    for i in range(1, 1001):
        term = term * x / float(i)
        sum += term

        if abs(sum - (sum - term)) / abs(sum + term) <= tol:
            if y < 0:
                result = 1.0 / sum
            else:
                result = sum

            return result, i

y_values = [1, 5, 10, 100]

for y in y_values:
    result, iterations = exponential_series(y)
    print(f"e^({y}) ≈ {result} after {iterations} iterations")
