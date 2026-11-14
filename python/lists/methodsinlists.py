l = [11, 22, 3, 3, 5, 7, 8]
print(l)


# method 1

l.append(9)
print(l)


# method 

l.sort()
l.sort(reverse=False)
l.sort(reverse=True)
print(l)


# method 3

l.reverse()
print(l)


# method 4

print(l.index(3))


# method 5

print(l.count(3))


# method 6

print(l.copy())


# method 7

l.insert(0,44)
print(l)


# method 8

m = [222,3333,66,77]
k = l + m
print(k)
l.extend(m)
print(l)