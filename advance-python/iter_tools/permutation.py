# itertools : permutations - returns all possible ordering of an input
from itertools import permutations
a=[1,2,3]
perm = permutations(a)
print(list(perm))

''' we have different orderings
[(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)] 
'''
# we can also specify the length of the permutations as a second argument
# if you want to have shorted permutations with length 2, give it the argument 2

perm2 = permutations(a, 2)
print(list(perm2))

''' different orderings with length 2
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)] 
'''

