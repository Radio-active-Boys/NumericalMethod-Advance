import math

def f(v, R, a, b, p, T):
    return p - (R * T / (v - b) - a / (math.sqrt(T) * (v + b)))

def newton_method(T):
    eps = 1e-8
    itermax = 50
    print('Input T(C):')
    T = float(input())
    T = T + 273.15  # Convert to Kelvin
    tcrit = 647.25
    pcrit = 220.89e5
    R = 8314 / 18.015  # Universal gas constant / molar mass of water
    p = 100000.0
    Omega = 1.0
    a = 0.42748 * R ** 2 * tcrit ** 2.5 / pcrit
    b = 0.08664 * R * tcrit / pcrit
    x1 = R * T / p
    x2 = 1.00001 * x1
    y1 = f(x1, R, a, b, p, T)
    y2 = f(x2, R, a, b, p, T)
    em = (y2 - y1) / (0.00001 * x1)
    
    for Iter in range(1, itermax):
        xnew = x1 - Omega * (y1 / em)
        err = f(xnew, R, a, b, p, T)
        delxn = abs((xnew - x1) / xnew)
        print(f'vnew = {xnew}, err = {err}, iter = {Iter}')
        
        if abs(err) < eps and abs(delxn) < eps:
            print(f'Root found after {Iter} iterations')
            return xnew
        
        em = (f(1.00001 * xnew, R, a, b, p, T) - err) / (0.00001 * xnew)
        x1 = xnew
        y1 = err
    
    print('Iterations did not converge')
    return None

# Calculate specific volumes at temperatures from 100°C to 300°C in steps of 50°C
for temp_C in range(100, 350, 50):
    specific_volume = newton_method(temp_C)
    print(f'Temperature: {temp_C}°C, Specific Volume: {specific_volume}')
