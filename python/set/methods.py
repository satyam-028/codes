set1 = {1, 2, 3, 4,}
set2 = {1, 2, 6, 7, 5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.isdisjoint(set2)) ## give true or false value in set
print(set1, set2)


set = {1, 2, 3, 4, 6, 5}
set2 = {6, 7, 5}
print(set.issuperset(set2))
set3 = {6, 4, 5}
print(set.issuperset(set3))

print(set3.issubset(set))

set.remove(1)
print(set)
