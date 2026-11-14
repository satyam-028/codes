count = 0
with open("pratice3.txt","r") as f:
    data = f.read()
    print(data)
    
    num = data.split(",")  
    for x in num:
      if int(x)%2 == 0:
        count += 1

print(count)