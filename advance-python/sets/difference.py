# To calculate difference

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

print('setA', setA)
print('setB', setB)


# the difference will return a set with all elements from the first set that are not in the second set
print('difference setA and setB')
diff = setA.difference(setB)
print(diff)

print('differnce setB and setA')
diff2 = setB.difference(setA)
print(diff2)

# second method : symmetric difference : returns all the elements in setA & setB but not the elements present in both sets
print('symmetric difference')
sdiff = setA.symmetric_difference(setB)
print(sdiff)

sdiff2 = setB.symmetric_difference(setA)
print(sdiff2)

# These will not modify setA and setB, it will return new set
print('setA', setA)
print('setB', setB)

# To modify the sets
#setA.update(setB)
#print(setA)

# intersection update method
#setA.intersection_update(setB)
#print(setA)

# difference_update method
#setA.difference_update(setB)
#print(setA) 

# symmetric difference update method
setA.symmetric_difference_update(setB)
print(setA)


