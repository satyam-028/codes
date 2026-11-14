from functools import reduce
A = lambda y, z: y+z/0
x = lambda x: reduce(A, range(4,x+1))
print(x(4))
print(x(5))
