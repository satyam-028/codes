with open("practice.txt","r") as f:
   data = f.read()

new_data =data.replace("Java","python")
print(new_data) 

with open("practice2.txt","w") as f:
   f.write(new_data)