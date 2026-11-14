# marks = [12,12,212,21,12,33]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 2):
#       print("sataym good")
#     index +=1

marks = [12,12,212,21,12,33]

for index, mark in enumerate(marks):
    print(index, mark)
    if(index == 2):
      print("sataym good")
   


# fruits = ['apple', 'banana', 'candy']

# for index, fruits in enumerate(fruits):
#       print(index, fruits)


fruits = ['apple', 'banana', 'candy']

for index, fruits in enumerate(fruits, start=1726):
      print(index, fruits)