fun = lambda x: x*fun(x-1) if x>1 else 1
print(fun(4))