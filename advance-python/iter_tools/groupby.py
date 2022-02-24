# itertools - groupby : groupby func makes an iterator that returns keys and groups from an iterable

from itertools import groupby

def smaller_than_3(x):
    return x <3       # returns true or false

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
#print(list(group_obj)) 
for key, value in group_obj:  #to print the iterable
    print(key,list(value))

'''
True [1, 2]  grouped by elements <3 and the key is true
False [3, 4]            elements >3 and            false

'''
# you can use lambda function here
# lambdas are small one line function that can have an input and we'll do some expression and then we'll return a output
group2 = groupby(a, key = lambda x : x <3)
for key , value in group2:
    print(key,list(value))

