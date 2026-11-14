# a = 50
# b = 3

# print("The value of ",a," + ",b," is : ",a+b)
# print("The value of ",a," + ",b," is : ",int(a) + int (b))
# print("The value of ",a," - ",b," is : ",a-b)
# print("The value of ",a," * ",b," is : ",a*b)
# print("The value of ",a," / ",b," is : ",a/b)  

# string = "15"
# number = 7
# string_number = int(string)

# sum  = number + string_number
# print("the sum of both the number is:",sum)




x = int(input("fcdj"))
n1 = 0
n2 = 1
print("Fibonacci Series:", n1, n2, end=" ")

for i in range(2,x):
    sum = n1 + n2
    n1 = n2 
    n2 = sum
    print(sum, end= " ")

print()

# num = 10
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")

# print()