import matplotlib.pyplot as plt
import numpy as np

random_matrix = np.random.randint(10, size=20)
matrix_from_array = np.arange(0,12).reshape((4, 3))

def	pure_range(n):
	return np.arange(start=0, stop=1+1/(n-1), step=1/(n-1))

big_matrix = np.arange(0,120).reshape((10, 12))
sub_matrix = big_matrix[0:4,8:12]

print(random_matrix)
print(matrix_from_array)
print(pure_range(5).shape)
print(big_matrix)
print(sub_matrix)
