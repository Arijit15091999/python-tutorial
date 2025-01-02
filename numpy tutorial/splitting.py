import numpy as np
# horizontal
arr1 = np.array([
    [1, 2],
    [3, 4]
    ])

arr2 = np.array([
    [5, 6],
    [7, 8]
    ])

# print(np.hstack((arr1, arr2)))

# vertical

# print(np.vstack((arr1, arr2)))


# Splitting

# hsplit

result = np.hstack((arr1, arr2))

print(np.hsplit(result, 2))

# vertical splitting

result = np.vstack((arr1, arr2))

print(np.vsplit(result, 2))