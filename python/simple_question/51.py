# l = []
# def convert(b):
#     if(b==0):
#         return 1
#     dig=b%2
#     l.append(dig)
#     convert(b//2)

# convert(6)
# l.reverse()
# for i in l:
#     print(i,end="")



import numpy as np

arr = np.array([2,4,3])
arr1 = np.array([5,6,4])

arr4 = arr[::-1]
ar = arr1[::-1]

carry = 0

total_sum = arr4 + ar + carry

total = total_sum //10
print(total_sum)

