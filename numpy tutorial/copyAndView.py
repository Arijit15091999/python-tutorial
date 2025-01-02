import numpy as np

a = np.arange(6)
a2 = a.copy()
a2[0] = 42

print(a)
print(a2)


a = np.arange(6)
a2 = a.view()[2 : 4]
a2[0] = 42

print(a)
print(a2)
