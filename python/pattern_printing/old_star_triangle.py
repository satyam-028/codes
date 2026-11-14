n = int(input("Enter a number : "))

x = 1

for i in range(1,n+1):
    for j in range(1,x+1):
        print("*",end=" ")
    x = x + 2
    print()

