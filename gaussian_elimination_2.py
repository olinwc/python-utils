import numpy as np

A = np.array([[+7.0, +1.0, +1.0, +4.0, -3.0],
              [+0.0, +3.0, +2.0, +0.0, +5.0],
              [+7.0, +1.0, +5.0, +3.0, -1.0],
              [+0.0, +3.0, +2.0, +2.0, +4.0],
              [+0.0, +6.0, +4.0, +0.0, +11.0]])
print(A)

num_dens = np.array([[8.0], [-6.0], [4.0], [-3.0], [-11.0]])

v = np.array([[0.0], [0.0], [0.0], [0.0], [0.0]])

num_rows = 5

for i in range(0, num_rows):
    for j in range(0, num_rows):
        if i > j and A[i][j] != 0:
            num_dens[i] = num_dens[i] - num_dens[j] * A[i][j] / A[j][j]
            for k in range(0, num_rows):
                v[k] = A[i][k] - A[j][k] * A[i][j] / A[j][j]
            for k in range(0, num_rows):
                A[i][k] = v[k]
                v[k] = 0.0

print(A)
print(num_dens)
