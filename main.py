import numpy as np
from numpy import random as rd

a = np.array([1, 2, 3, 2, 1])
b = np.array([1, 2, 3, 4, 5])
w = np.array([5, 4, 3, 2, 1])
t = np.array([[9, 8, 7, 6, 5], [4, 3, 2, 1, 0]])
h = [True, True, True, False, False]
c = a[h]
n = rd.randint(50, size=4)
e = rd.randint(50, size=(2, 2))
m = rd.choice(w, p=[0.1, 0.2, 0.3, 0.4, 0], size=10)
s = rd.choice(b, p=[0.1, 0.2, 0.3, 0.4, 0], size=(2, 5))
p = np.searchsorted(b, 3)
d = np.searchsorted(w, 3, side='right')
u = np.where(a == 1)
l = rd.rand()
r = rd.rand(4)
f = rd.rand(2, 2)
x = np.add(b, w)
y = []
print(p)
print(d)
print(np.sort(a))
print(np.sort(t))
print(u)
print(c)
print(n)
print(e)
print(l)
print(r)
print(f)
print(m)
print(s)
print(x)
for i, j in zip(b, w):
    y.append(i + j)
print(y)
