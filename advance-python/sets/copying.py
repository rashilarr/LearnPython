# copying two sets
setA = {1,2,3,4,5,6}

# first method
setB = setA
print('setB',setB)
print('id of setA',id(setA))
print('id of setB',id(setB))

# if we modify the copy, the original is also modified
setB.add(7)
print('setB',setB)
print('setA',setA)

#second method - actual copy using copy() method
setC = setA.copy()
print('setc',setC)
print('setA',setA)

print('id of setA', id(setA)) 
print('id of setc', id(setC)) 

setC.add(8)
print('setC', setC)
print('setA', setA)

# third method - use the set() method - also actual copy method
setD = set(setA)
print('setA',setA)
print('setD',setD)
setD.add(9)
print('setA',setA)
print('setD',setD)


