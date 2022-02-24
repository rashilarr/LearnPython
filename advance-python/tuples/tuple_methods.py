# some of the methods used in tuple
mytuple = ('a','p','p','l','e')

# len() method: to get the no of elements inside a tuple
print(len(mytuple))

#if you want to count of the elements inside the tuple
print(mytuple.count('p'))
print(mytuple.count('l'))
print(mytuple.count('o')) # not an element of the tuple
print()

# you find the index of the element
print(mytuple.index('p')) # returns the first occurance of p i.e 1
print(mytuple.index('a'))
print(mytuple.index('l'))
print(mytuple.index('e'))

