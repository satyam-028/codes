string = "The quick Brow Fox"

def count_case(s):
    d = {"Upper case": 0, "Lower case ": 0}
    for c in s:
        if c.isupper():
            d["Upper case"] += 1
    
        if c.islower():
            d["Lower case "] += 1
        
        else:
            pass
    
    print('The orgianl string : ',s)
    print('The upper case string : ',d["Upper case"])
    print('The lowwer case string : ',d["Lower case "])
    
    return 

print(count_case(string))

