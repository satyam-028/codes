list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def list_even(l):
    elist = []
    for x in l:
        if x%2==0:
           elist.append(x)

    return elist

print(list_even(list))