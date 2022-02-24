
mytuple = 'Max',28,'Boston'

name,age,city = mytuple  # the no of elements in left side must match the no of ele in tuples
print(name)
print(age)
print(city)

# we can unpack multiple elements using *

num = (0,1,2,3,4)

i1, *i2, i3 = num

print(i1) # first element 0
print(i3) # list [1,2,3]
print(i2)  # last element 4

''' Tuple is more efficient sometimes compared to list especially when working with the large data and tuple is immutable '''
