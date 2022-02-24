# itertools : infinite iterators
# count function, cycle function and repeat function

from itertools import count, cycle, repeat

# count function is simple
for i in count(10):
    print(i)       # this will make infinite loop starting from 10
    if i == 15:    # this will stop at 15
        break

# cycle function - this will cycle infinite through a iterable
a = [1,2,3]
for j in cycle(a):
    print(j)       # this will print 1,2,3 and cycle again goes infinite
    if j == 3:
        break

# repeat function - infinite loop of given value
# second argument - stop arg, how many times the value should be repeated
for k in repeat(1, 4):
    print(k)       # this will print 1 infinite times

