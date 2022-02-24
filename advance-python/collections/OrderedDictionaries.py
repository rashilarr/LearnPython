# collections : OrderedDict

from collections import OrderedDict

''' OrderedDict is like a regular dictionary but they remember the order that the items were inserted
    They are become less important now since the built in dictionary class has also the ability to remember the order since python 3.7
    If you use older version of python, this is the way to use the dictionary that remembers the order'''
# create ordered dictionary
ordered_dict = OrderedDict()
# now append the key value pairs like the normal dictionary
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
ordered_dict['a']=1
print(ordered_dict)
# prints the key value pairs in order which is inserted

