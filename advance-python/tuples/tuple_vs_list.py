
''' Tuple is more efficient sometimes compared to list especially when working with the large data and tuple is immutable '''

import sys
mylist = [0,1,2,'hello',True]
mytuple = (0,1,2,'hello',True)
print(sys.getsizeof(mylist),"bytes")
print(sys.getsizeof(mytuple),"bytes")


''' List size is larger than tuple even with the same elements 4
tuple is more efficient than list
tuple is easy to iterate and create '''

import timeit
print(timeit.timeit(stmt='[0,1,2,3,4,5]', number=1000000))
print(timeit.timeit(stmt='(0,1,2,3,4,5)', number=1000000))

''' comparing the time for creating 1 million times of clearing the given list and tuple
Tuple took less time to create 1 millions tuple '''
