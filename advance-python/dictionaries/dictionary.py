# Dictionary : key-value pairs, unordered, mutable
mydict = {'name':'Max','age':'28','city':'New York'}
print(mydict)

# another way - using dict function to create a dictionary
mydict2 = dict(name='Mary',age='27',city='Boston')
print(mydict2)

# To access the values
value1 = mydict['name']
print(value1)
value2 = mydict['age']
print(value2)
value3 = mydict['city']
print(value3)
# if we try to access the value that is not preset in our dictionary, key error will appear

# Dictionary is mutable, so you can add or change items after its creation
mydict['email'] = 'max@xyz.com'
print(mydict)

#if we change it again, it will overwrite it
mydict['email'] = 'coolmax@xyz.com'
print(mydict)

# options to Delete items

# del statement
del mydict['name']
print(mydict)

# Pop method
mydict.pop('age')
print(mydict)

# popitem() method
# it removes the last pair
mydict.popitem()
print(mydict)

# when you want to check the key is inside the dictionary
# 1. if in statement
if 'city' in mydict:
    print(mydict['city'])
else:
    print('No')

#2. try except statement
try:
    print(mydict['city'])
except:
    print('Error')



