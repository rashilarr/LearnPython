# itertools : combinations - this function makes all possible combinations
# with a specified length
from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2) # second arg - length, mandatary
print(list(comb))

''' we have all combinations here
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
note that we dont have repetition in combination there is no combinations like
(2,1),(3,1),(3,2),(4,1),(4,2),(4,3) 

if you want the repetition you can use the combinations with replacement function '''
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))
''' we have all the combinations with 1 and 1 itself, then goes on
[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
'''
