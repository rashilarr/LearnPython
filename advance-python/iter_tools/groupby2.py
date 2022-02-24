# itertools: groupby

from itertools import groupby

# this is a list - we have diff dictionaries contains name and age 

persons = [{ 'name' : 'Tim', 'age':25 },{'name':'Dan','age':25 },{'name':'Lisa','age':27}, {'name':'claire','age':28}]

# we want to group by a person's age
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print( key, list(value))


