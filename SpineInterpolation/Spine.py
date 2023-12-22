import numpy as np

def thomas(N, AA, RHS):
    # Tridiagonal solver using Thomas algorithm
    SOL = np.zeros(N)
    for i in range(1, N):
        factor = AA[i][0] / AA[i - 1][1]
        AA[i][1] -= factor * AA[i - 1][2]
        RHS[i] -= factor * RHS[i - 1]

    SOL[-1] = RHS[-1] / AA[-1][1]
    for i in range(N - 2, -1, -1):
        SOL[i] = (RHS[i] - AA[i][2] * SOL[i + 1]) / AA[i][1]

    return SOL

def main():
    # Read data from input file
    with open('spline.inp', 'r') as file:
        N = int(file.readline())
        data = [list(map(float, line.split())) for line in file]

    x = [item[0] for item in data]
    y = [item[1] for item in data]

    # Read the value of x where you need the interpolated value
    xx = float(input('Enter the value of x where you need the value: '))

    # Initialize derivatives and coefficients
    fdprim = [0.0] * N
    a = np.zeros((N - 2, 3))
    b = np.zeros(N - 2)
    z = np.zeros(N - 2)

    # Generate coefficients for tridiagonal matrix (step-1)
    for i in range(1, N - 1):
        if i == 1:
            a[i - 1][0] = 0.0
        else:
            a[i - 1][0] = (x[i] - x[i - 1]) / 6.0
        a[i - 1][1] = (2.0 * (x[i + 1] - x[i - 1])) / 6.0
        if i == N - 2:
            a[i - 1][2] = 0.0
        else:
            a[i - 1][2] = (x[i + 1] - x[i]) / 6.0
        b[i - 1] = ((y[i + 1] - y[i]) / (x[i + 1] - x[i])) + ((y[i - 1] - y[i]) / (x[i] - x[i - 1]))

    # Solve for n-2 derivatives
    z = thomas(N - 2, a, b)

    # Copy derivatives to fdprim
    for i in range(1, N - 1):
        fdprim[i] = z[i - 1]

    # Output the values of fdprim
    print('fdprim(i)s:')
    print(fdprim[1:N-1])

    # Check the interval where xx is lying (step-2)
    ii = 0
    for i in range(1, N):
        if x[i] >= xx:
            ii = i
            break

    # Interpolation (step-3)
    Ai = (x[ii] - xx) / (x[ii] - x[ii - 1])
    Bi = (xx - x[ii - 1]) / (x[ii] - x[ii - 1])
    term1 = fdprim[ii - 1] * (Ai**3 - Ai) * (x[ii] - x[ii - 1])**2 / 6.0
    term2 = fdprim[ii] * (Bi**3 - Bi) * (x[ii] - x[ii - 1])**2 / 6.0
    term3 = Ai * y[ii - 1]
    term4 = Bi * y[ii]
    yy = term1 + term2 + term3 + term4

    # Output the interpolated value
    print('The value of y =', yy)

if __name__ == '__main__':
    main()
