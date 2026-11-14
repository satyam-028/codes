items = input("Enter a words : ")
data = items.split("-")
print(data)
 
for n in items:
    print("-".join(sorted(items)))
    break





# items = [n for n in input().split("-")]
# items.sort()
