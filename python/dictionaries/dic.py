dic = {
    "satyam": "smart boy",
    "handsome": "kon ha satyam"
}

print(dic["handsome"])


info = {'name':"satyam sharma", 'age':18, 'college name':"sunder deeep college"}
print(info)
print(info['name'])
print(info.get('name'))
print(info.get('name1'))

print(info.keys())
print(info.values())
print(info.items())


for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

for key in info:
    print(key,info[key])