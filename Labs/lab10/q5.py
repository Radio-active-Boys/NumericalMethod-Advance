import numpy as np
import matplotlib.pyplot as plt

# Parameters
Tin = 0.0
Tmax = 40.0

d = 1/(20**(0.5))
Alpha = 0.01
L = 1.0
Nodes = 11
delx = L / (Nodes - 1)


# Function to perform the diffusion calculation
def solve_diffusion(theta, delt, nodes, d):
    x = np.linspace(0, L, nodes)
    T = np.sin(np.pi * x)  # Initialize temperature at t = 0

    for t in np.arange(0, Tmax, delt):
        T_new = np.copy(T)
        for i in range(1, nodes - 1):
            T_new[i] = T[i] + theta * d * (T[i + 1] - 2 * T[i] + T[i - 1]) + (1 - theta) * d * T[i]
        T = T_new

    return T


Theta_values = [1.0]
t_values = [40.0]
D = 2.0
# Plot the results
for theta in Theta_values:
    for t in t_values:
        delt = D * delx**2 / Alpha
        nodes = Nodes
        T = solve_diffusion(theta, delt, nodes, D)
        print(T)
        
        plt.figure()
        plt.plot(np.linspace(0, L, nodes), T, label=f'Theta = {theta}')
        plt.title(f'Diffusion Equation at t = {t} (Theta = {theta})')
        plt.xlabel('Position (x)')
        plt.ylabel('Temperature (T)')
        plt.legend()
        plt.grid(True)
        plt.show()
