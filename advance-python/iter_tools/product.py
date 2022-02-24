# itertools : Product
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b) #product commute a cartisian product of input iterables
print(list(prod)) # prod is itertool object, to see the elements convert it to list

''' cartisian product of a and b is 
    (1,3) (1,4) (2,3) (2,4)
    elements of a is combined individually with elements of b
'''

# we can also define no of repetitions 
c = [3]
prod2 = product(a,c, repeat=2)
print(list(prod2))


