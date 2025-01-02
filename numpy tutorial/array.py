import numpy as np

# array slicing

# x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(x[0: , 1:4])

# np array containt zero and ones
x = np.zeros(4, dtype = int)
print(x)
print(x.dtype)

x = np.ones(4)
print(x)
print(x.dtype)

# np arrau with range
x = np.arange(4)
print(x)

x = np.arange(2, 9, 2)
print(x)

# line space

# x = np.linspace(start, end, num = ?)
x = np.linspace(0, 10, num = 5)
print(x)