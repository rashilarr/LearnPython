# collections: Counters, namedtuple, OrderedDict, defaultdict, deque

'''the collections modules implements special container data types and provides alternatives with some aditional functionality compared to the general built-in containers like dictionaries, list or tuples'''

''' Counters : counters is a container that stores the elements as dictionary keys and the counts as dictionary values
'''
from collections import Counter
a = 'aaaaabbbbccccccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.items()) # view the items : key value pairs
print(my_counter.keys())  # to get the keys, gives us iterable over the keys
print(my_counter.values()) # give us values

# to print the one most common elements, if 2 elements has same count, it will take first one
print(my_counter.most_common(1)) 
print(my_counter.most_common(2)) # to print the two most common elements

''' this will return the list of tuples of counter values
    [('c',7),('a',5)] 
    if you need to access the most common element 
    then, my_counter.most_common(1)[0][0]
    index [0][0] means, first [0] --> ('c',7)
                        [0][0] --> 'c'
'''
print(my_counter.most_common(1)[0][0]) # prints c

print('to print all the elements from counter as list')
print(list(my_counter.elements()))  # it is iterable

