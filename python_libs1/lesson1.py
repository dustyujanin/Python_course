import numpy as np

a = np.array([[1,6],
               [2,8],
               [3,11],
               [3,10],
               [1,7]])
a_mean = a.mean(axis=0)
print(a)
print(a_mean)

a_centered = a - a_mean
print(a_centered)

a_centered_sp = np.dot(a_centered[:,0],a_centered[:,1])
print(a_centered_sp)

a_final = a_centered_sp/(a.shape[0]-1)
print(a_final)

print(np.cov(a.transpose())[0][1])