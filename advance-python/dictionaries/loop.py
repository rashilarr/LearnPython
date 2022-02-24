
mydict = {'name':'Max', 'age':'28','city':'New York'}
print(mydict)

# loops through dictionary and prints key
for key in mydict:
    print(key)

# you can also use mydict.keys() method
for key in mydict.keys():
    print(key)

# you can do for values also
for value in mydict.values():
    print(value)

# to get both key and value
for key, value in mydict.items():
    print(key,value)


