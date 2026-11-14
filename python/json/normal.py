book = {}

book['tom'] = {
    "name" : "tom",
    "address" : " juyg",
    "phone" :  76789345343553
}

book['saa'] = {
    "name" : "tsas",
    "address" : " sjaksja",
    "phone" : 645458
}

import json
s = json.dumps(book)
print(s)

m = book['tom']['phone']
print(m)

book = json.loads(s)
print(book)

for person in book:
    print(book[person])