import numpy as np

array_zero = np.zeros(10)
array_one = np.ones(10)
array_range = np.arange(start=10, stop=51)
array_even_range = np.arange(start=10, stop=51, step=2)
matrix_identity = np.identity(3)
random_number = np.random.uniform(0, 1)
matrix_simple = np.arange(start=0, stop=1, step=0.111111111)


print('zeros:', array_zero)
print('ones:', array_one)
print('range:', array_range)
print('evens:', array_even_range)
print('identity:', matrix_identity)
print('random:', random_number)
print('matrix:', matrix_simple)
