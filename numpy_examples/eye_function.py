"""
Continuing from numpy basics to cover some more numpy functions
"""
import numpy as np


eye = np.eye(4)
print('Identity matrix : ', eye)

# Working with random numbers in numpy
random_matrix = np.random.rand(3, 4)
print('Random matrix : ', random_matrix)

# Choosing random numbers from standard normal distribution
normal = np.random.randn(10)
print('Normal distribution : ', normal)

# Returning random numbers
n = np.random.randint(1, 100, 10)
print('N : ', n)
print('Max number : ', n.max())
print('Max number index: ', n.argmax())

# Reshaping method
rand_matrix = np.random.randint(1, 100, 25)
rand_matrix = rand_matrix.reshape(5, 5)
print('Reshaped matrix : ', rand_matrix)
print('Shape is : ', rand_matrix.shape)
print('Datatype : ', rand_matrix.dtype)
print('Sum of matrix : ', rand_matrix.sum())
print('Sum of matrix cols : ', rand_matrix.sum(axis=1))
print('Sum of matrix rows : ', rand_matrix.sum(axis=0))


