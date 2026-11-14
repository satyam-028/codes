n = int(input("Enter a number : "))

for i in range(n):
    print(' ' * (n - i - 1), end='')
    print('*' * (2 * i + 1))

for i in range(n):
    for j in range(i):
        print(" ",end="")
    
    for k in range(0,2*(n - i) - 1):
        print("*",end="")
    
    print()