student = {
    "name" : "satyam sharam",
    "subjects" : {
        "phy" : 95,
        "chem" : 32,
        "maths" : 54
    }
}

# print(student)

# print(student["subjects"])

# print(student["subjects"]["chem"])
# print(student["subjects"]["phy"])
# print(student["subjects"]["maths"])


## -> same methods 

print(student.keys())

print(student.values())

print(student.items())

print(student.get('name'))

print(student.get('name2'))

print(len(student))

## -> convert into lists
 
print(list(student.keys()))

print(len(list(student.keys())))

pairs = list(student.items())
print(pairs[0])