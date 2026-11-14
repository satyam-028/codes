def max_number(x,y,z):
    if x > y:
        return x
    elif y > z:
        return y
    else:
        return z
    

result = max_number(3,4,-5)
print(result)