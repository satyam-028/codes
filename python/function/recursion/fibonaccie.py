def fibo(n):
    if(n==1 or n==2) :
         return 1 
    else:
        return fibo(n-1) + fibo(n-2) 

print(fibo(3))
print(fibo(4))
print(fibo(11))
print(fibo(10))
print(fibo(6))
print(fibo(5))



 

# def show(n):
#     if n==0:
#         return 
#     print(n)
#     show(n-1)
#     # print("end")

# show(5)