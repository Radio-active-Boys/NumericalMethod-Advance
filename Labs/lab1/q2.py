eps = 1.0
for i in range(1, 1001):
    if (1.0 + eps) > 1.0:
        small = eps
        eps = eps / 2.0
    else:
        print('small =', small, 'No of Terms =', i)
        break

