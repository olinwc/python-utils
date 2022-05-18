import numpy as np
from scipy import linalg

depletion_matrix = np.mat('[-2,0,0,0;2,-4,0,0;0,3,-1,0;0,1,0,-1]')

print(depletion_matrix)

init_densities = np.mat('[1;0;0;0]')

print(init_densities)

t = 1.0

print((linalg.expm(depletion_matrix * t)) * init_densities)

depletion_matrix_2 = np.mat('[-2,0,0,0;2,-4,0,0;0,3,-1,0;0,1,0,-1]')

init_densities_2 = np.mat('[1;0;0;0]')

print(depletion_matrix_2)

print(init_densities_2)

print((linalg.expm(depletion_matrix_2 * t)))

print((linalg.expm(depletion_matrix_2 * t)) * init_densities_2)
