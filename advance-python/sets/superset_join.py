# super set and join method

setA = {1,2,3,4,5,6}
setB = {1,2,3}

# setA is subset of setB : Means setB has all the elements of setA

print(setA.issubset(setB))
print(setB.issubset(setA))

# super set is opposite of subset
# super set returns true : if first set contains all the elements of second set
print('super set')
print(setA.issuperset(setB))
print(setB.issuperset(setA))

# we can calculate disjoint
# disjoint returns true if two sets have a null intersection
print(setA.isdisjoint(setB))

setC = {7,8}
print(setA.isdisjoint(setC))
