n = int(input("Enter a number : "))

for i in range(n):
    for j in range(n):
        a = n/2 + 1
        if (j==a or i==a):
          print("*",end="")
        else:
          print(" ",end="")

    print()