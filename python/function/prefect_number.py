def  prefect_number(n):
    sum = 0
    for i in range(1 ,n):
        if n%i==0:
           sum += i
    if sum == n:       
      print("This is prefect number") 
    else:
       print("Not Prefect number")
 
print(prefect_number(8128))