import numpy as np
n,m = map(int,input().split())
A = np.array([input().split() for _ in range(n)],int)
v = np.sum(A, axis = 0)
print(np.prod(v))