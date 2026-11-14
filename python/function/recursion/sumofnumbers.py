def sum_number(n):
    if n == 0:
        return 0
    return sum_number(n-1) + n
    
sum = sum_number(10)
print(sum)