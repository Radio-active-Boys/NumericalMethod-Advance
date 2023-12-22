import numpy as np

Tin = 0.0
Tmax = 42.0
Dee = 5.0
Theta = 0.5
Tright = 0.0
Tleft = 0.0
Alpha = 0.01
El = 1.0
Nodes = 11
delx = El / (Nodes - 1)
delt = Dee * delx * delx / Alpha

def initialize_grid():
    x = np.linspace(0.0, El, Nodes)
    return x

x = initialize_grid()

pi = np.pi

T0 = np.zeros(Nodes + 2)
for i in range(1, Nodes + 1):
    T0[i] = np.sin(pi * x[i - 1])

tt = Tin + delt

AA = np.zeros((Nodes, 3))
C = np.zeros(Nodes)
T = np.zeros(Nodes)

# Computation of tridiagonal coefficients for internal nodes
for I in range(1, Nodes - 1):
    AA[I, 0] = -Theta * Dee
    AA[I, 2] = AA[I, 0]
    AA[I, 1] = 1.0 - AA[I, 0] - AA[I, 2]
    C[I] = (1.0 - Theta) * Dee * T0[I + 1] + (1.0 - 2.0 * (1 - Theta) * Dee) * T0[I] + (1.0 - Theta) * Dee * T0[I - 1]

# Treatment of boundary nodes
AA[0, 1] = 1.0
AA[0, 2] = 0.0
C[0] = 0.0
AA[Nodes - 1, 0] = 0.0
AA[Nodes - 1, 1] = 1.0
C[Nodes - 1] = 0.0

# Computation of temperatures
for I in range(Nodes):
    T[I] = T0[I + 1]

while tt <= Tmax:
    # Update T0 with current T
    T0[1:Nodes + 1] = T

    # Perform Thomas algorithm to solve the tridiagonal system
    for i in range(1, Nodes):
        m = AA[i, 0] / AA[i - 1, 1]
        AA[i, 1] -= m * AA[i - 1, 2]
        C[i] -= m * C[i - 1]

    T[Nodes - 1] = C[Nodes - 1] / AA[Nodes - 1, 1]

    for i in range(Nodes - 2, -1, -1):
        T[i] = (C[i] - AA[i, 2] * T[i + 1]) / AA[i, 1]

    # Update time
    tt = tt + delt

    # Compute the analytical solution
    T_ana = np.exp(-Alpha * pi * pi * tt) * np.sin(pi * x)
    print(np.column_stack((x, T, T_ana)))
d