# frozen set method- immutable version of set
# you cannot change it after its creation
# syntax is frozenset(arg) , arg - iterable like list

a = frozenset([1,2,3,4,5])
print(a)

# if we try to modify this, we will get an error
#a.add(6)
#print(a)

# .remove and .update will not work with this, but union, intersection will work

b = frozenset([2,6,8,10])
c = a.union(b)
print(c)

d = a.intersection(b)
print(d)
