list = (8, 2, 0, 3, 7)
# items = 0

def list_sum(list):
    total = 1
    for x in list:
        total += x
        # total *= x
    return total

print(list_sum(list))