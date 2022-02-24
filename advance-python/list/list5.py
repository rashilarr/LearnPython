
l1 = [1,2,3,4]
l2 = l1
l3 = l1.copy()
l4 = l1
l1[0] = [5]
print(l1,l2,l3,l4)
print(id(l1))
print(id(l2))
print(id(l3))
print(id(l4))
