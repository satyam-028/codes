dict = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3',
    'key4': 'val4',
    'key5': 'val5'
}

# vals = dict.values()
# vals = dict.items()
vals = dict.fromkeys(dict.values())
print(vals)