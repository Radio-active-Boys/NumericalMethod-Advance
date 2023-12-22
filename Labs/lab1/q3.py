import math

def equation(Theta, alphaL):
    return alphaL - (Theta - (math.sin(2 * Theta)) / 2) / math.pi

def bisection(alphaL):
    Theta1 = 0
    Theta2 = math.pi
    xp, xn = (Theta1, Theta2) if equation(Theta1, alphaL) < 0 else (Theta2, Theta1)

    eps = 1e-6
    Itermax = 1000

    for II in range(1, Itermax):
        xr = (xn + xp) / 2.0
        yr = equation(xr, alphaL)
        print(f"Iteration {II}: xr = {xr}, yr = {yr}")

        if abs(yr) <= eps:
            hlbyD = (1 - math.cos(xr)) / 2
            alphalC = (xr - (math.sin(2 * xr)) / 2) / math.pi
            print(f"Root found: hl/D = {hlbyD}, alphalC = {alphalC}")
            return hlbyD, alphalC

        if yr < 0:
            xn = xr
        else:
            xp = xr

    print("Root not found within the maximum number of iterations.")
    return None, None

# Case (a) 20% of the cross-sectional area is occupied by liquid
alphaL_a = 0.2
hD_a, alphalC_a = bisection(alphaL_a)
print(f"Case (a): h/D = {hD_a}, alphalC = {alphalC_a}")

# Case (b) 40% of the cross-sectional area is occupied by liquid
alphaL_b = 0.4
hD_b, alphalC_b = bisection(alphaL_b)
print(f"Case (b): h/D = {hD_b}, alphalC = {alphalC_b}")

# Case (c) 60% of the cross-sectional area is occupied by liquid
alphaL_c = 0.6
hD_c, alphalC_c = bisection(alphaL_c)
print(f"Case (c): h/D = {hD_c}, alphalC = {alphalC_c}")

# Case (d) 80% of the cross-sectional area is occupied by liquid
alphaL_d = 0.8
hD_d, alphalC_d = bisection(alphaL_d)
print(f"Case (d): h/D = {hD_d}, alphalC = {alphalC_d}")
