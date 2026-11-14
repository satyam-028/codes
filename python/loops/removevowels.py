i = input("enter a statement : ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = " "

for x in range(len(i)):
    if i[x] not in vowels:
        result = result + i[x]    

print("\nAfter removing vowels : ",result)       