import numpy as np

depletion_matrix = np.array([[+7, +1, +1, +4, -3],
                             [+0, +3, +2, +0, +5],
                             [+7, +1, +5, +3, -1],
                             [+0, +3, +2, +2, +4],
                             [+0, +6, +4, +0, +11]])
print(depletion_matrix)

num_dens = np.array([[8], [-6], [4], [-3], [-11]])

v = np.array([[0], [0], [0], [0], [0]])

num_rows = 5

has_lower_triangular = True

# Tarjan
#for k in range(1,num_rows):
#    print(k)
#    print(depletion_matrix)
#    for j in range(0,num_rows):
#        if depletion_matrix[j][k] != 0:
#            v[j] = depletion_matrix[j][k]
#    for j in range(0,num_rows):
#        if depletion_matrix[k][j] != 0:
#            if k > j:
#                num_dens[k] = num_dens[k] + num_dens[j] * depletion_matrix[j][k] / (1 - depletion_matrix[j][j])
#                for i in range(0,num_rows):
#                    if depletion_matrix[j][i] != 0:
#                        if i > j:
#                            v[i] = v[i] + depletion_matrix[i][j] * depletion_matrix[j][k] / (1 - depletion_matrix[j][j])
#    for j in range(0,num_rows):
#        if depletion_matrix[k][j] != 0:
#            depletion_matrix[j][k] = v[j]

# Maria
#for i in range(0, num_rows):
#    print(i)
#    print(depletion_matrix)
#    for j in range(0, num_rows):
#        if depletion_matrix[i][j] != 0:
#            v[j] = depletion_matrix[i][j]
#        else:
#            v[j] = 0
#    for j in range(0, num_rows):
#        if depletion_matrix[i][j] != 0:
#            if i > j:
#                num_dens[i] = num_dens[i] - num_dens[j] * depletion_matrix[i][j] / depletion_matrix[j][j]
#                for k in range(0, num_rows):
#                    if depletion_matrix[j][k] != 0:
#                        v[k] = v[k] - depletion_matrix[i][j] * depletion_matrix[j][k] / depletion_matrix[j][j]
#    for j in range(0, num_rows):
#        if depletion_matrix[i][j] != 0:
#            depletion_matrix[i][j] = v[j]

print(1 / 2)

run = True
while run:
    for j in range(0, num_rows):
        for k in range(0, num_rows):
            if k > j:
                print(depletion_matrix)
                if depletion_matrix[j][j] == 1:
                    check_rows = True
                    row_number = 0
                    while check_rows:
                        old_non_zeroes = num_rows
                        for m in range(0, num_rows):
                            if m != j and depletion_matrix[m][j] != 0:
                                for n in range(0, num_rows):
                                    non_zeroes = 0
                                    if depletion_matrix[m][n] != 0:
                                        non_zeroes += 1
                                if non_zeroes < old_non_zeroes:
                                    row_number = m
                                    old_non_zeroes = non_zeroes
                        check_rows = False
                    for i in range(0, num_rows):
                        depletion_matrix[j][i] += depletion_matrix[row_number][i]
                    num_dens[j] += num_dens[row_number]
                    continue
                else:
                    num_dens[k] = num_dens[k] + num_dens[j] * depletion_matrix[j][k] / (1 - depletion_matrix[j][j])
                    for i in range(0, num_rows):
                        if i > j:
                            depletion_matrix[i][k] = depletion_matrix[i][k] + depletion_matrix[i][j] * depletion_matrix[j][k] / (1 - depletion_matrix[j][j])
    has_lower_triangular = False
    for m in range(0, num_rows):
        for n in range(0, num_rows):
            if m > n and depletion_matrix[m][n] != 0:
                has_lower_triangular = True
    run = has_lower_triangular

print(depletion_matrix)
