# collections : defaultdict

from collections import defaultdict

''' defaultdict similar to regular dictionary, only difference is it contains default value if the key has not been set yet '''
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
print(d['a']) # to access the values
print(d['b'])
print(d['c']) # try to access the value of key does not exist , it gives us default value of integer

d1 = defaultdict(float)
d1['a'] = 1
d1['b'] = 2
print(d1)
print(d1['a']) # to access the values
print(d1['b'])
print(d1['c']) # this does not exist, so give you the default value of float 

d2 = defaultdict(list)
d2['a']=1
d2['b']=2
print(d2)
print(d2['c']) # default value of list is empty list, with normal dictionary this will raise a key error


