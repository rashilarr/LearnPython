# copying a list
list_org = ['Banana', 'cherry', 'apple']

# now i want to create a copy
list_cpy = list_org

print(list_cpy)
print(id(list_org))
print(id(list_cpy))

# if i modify the copy, it will also modify the original list
list_cpy.append('lemon')
print(list_cpy)
print(list_org)

# if you want to create actual copy, then use copy method
newlist = list_org.copy()
print(id(list_org))
print(id(newlist))

newlist.append('raspberry')
print(list_org)
print(newlist)

# we can also do with the list function, give org list as argument
newlist2 = list(list_org)
print(newlist2)
print(id(list_org))
print(id(newlist2))

# third option for copying
newlist3 = list_org[:] # slicing indicates all the elements
print(newlist3)

# list comprehension
# fast way to create a newlist from the existing list in one line
a = [1,2,3,4,5,6]

# we want a list with squared numbers of numbers in list a
b = [i*i for i in a]
# syntax is expression--> i*i then for loop over the list--> a
print(a)
print(b)


