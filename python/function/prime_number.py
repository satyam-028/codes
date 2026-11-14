def prime_number(n):
    for x in range(2, n):
        if x%2!=0:
            print("this is not a prime number ") 
            break
    if n == 1:
        print("This is nither be prime or composite : ")
    elif n == 2:
        print("This is prime number : ")
    
    return 
print(prime_number(9))