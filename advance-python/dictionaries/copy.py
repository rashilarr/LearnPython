
mydict = {'name':'Max', 'age':'28','city':'New York'}
print(mydict)

# different ways for copy
#first one
mydict_cpy = mydict
print(mydict_cpy)

print(id(mydict))
print(id(mydict_cpy))

# if we modify the copy one, it will also modifies the original one
mydict_cpy['email'] = 'max@xyz.com'
print(mydict_cpy)
print(mydict)

#second one
# if you want to do actual copy, then use the built-in copy function
mydict_new = mydict.copy()
print(mydict_new)

print(id(mydict))
print(id(mydict_new))

print('printing actual copy')
mydict_new['zip code'] = '95391'
print(mydict_new)
print(mydict)

# third one
# using the dict function with the original dictionary
mydict_3 = dict(mydict)
print('mydict_3')
print(mydict_3)

print(id(mydict))
print(id(mydict_3))

