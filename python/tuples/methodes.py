countries = ('india', 'spain', 'pok', 'england', 'germany')
temp = list(countries)
temp.append("russia")     # add new item
temp.pop(3)               # remove item
temp[2] ='finland'        # change item
countries = tuple(temp)
print(countries)




# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5 )

# print (tup1[0]) 
# print (tup2[1:5]) 


tup =(20,)
print(tup,type(tup))