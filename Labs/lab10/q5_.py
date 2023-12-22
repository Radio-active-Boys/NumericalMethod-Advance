import numpy as np

def solve_diffusion_equation(Theta, D, Tmax):
    Tin = 0.0
    Dee = 2.0
    Tleft = 0.0
    Alpha = 0.01
    el = 1.0
    Nodes = 11
    delx = el / (Nodes - 1)
    delt = Dee * delx * delx / Alpha

    # Grid Generation
    x = np.linspace(0, el, Nodes)

    # Temperature Initialization
    pi = np.pi
    T0 = np.sin(pi * x)
    tt = Tin + delt

    while tt <= Tmax:
        # Computation of Tridiagonal Coefficients for Internal Nodes
        AA = np.zeros((Nodes, 3))
        T = np.zeros(Nodes)
        for i in range(1, Nodes - 1):
            AA[i, 0] = -Theta * Dee
            AA[i, 2] = 1 - Theta * Dee
            AA[i, 1] = -AA[i, 0] - AA[i, 2]
            T[i] = (1 - Theta) * Dee * T0[i + 1] + (1 - 2 * (1 - Theta) * Dee) * T0[i] + (1 - Theta) * Dee * T0[i - 1]

        # Treatment of Boundary Nodes
        AA[0, 2] = 1.0
        T[0] = Tleft
        AA[Nodes - 1, 2] = 1.0
        T[Nodes - 1] = Tright

        # Computation of Temperatures
        T = np.linalg.solve(AA, T)

        # Computation of Analytical Solution
        T_ana = np.exp(-Alpha * np.pi ** 2 * tt) * np.sin(np.pi * x)

        # Print values
        print("Time t =", tt)
        for i in range(Nodes):
            print("x =", x[i], "Numerical Solution =", T[i], "Analytical Solution =", T_ana[i])

        tt += delt

if __name__ == "__main__":
    # Scenario 1: Theta = 0.5, D = 2.0
    solve_diffusion_equation(Theta=0.5, D=2.0, Tmax=40.0)
