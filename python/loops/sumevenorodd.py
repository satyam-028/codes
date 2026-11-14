n = int(input("Enter a number : "))

sum_even = 0
sum_odd = 0
ctr = 1

for i in range(n):

        if i%2==0:
           sum_even += ctr
           ctr += 1
        else:
           sum_odd += ctr
           ctr += 1


print("The sum of even number is : ",  sum_odd)
print("The sum of odd number is : ",  sum_even)



