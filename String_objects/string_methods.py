#-------- Common strings Methods ----------
# The python string object has no of useful methods
# String is immutable, it cannot be changed, so when you use one of the transformation methods, the return string is a different object


print('Hello World' .upper()) # all upercase
print('Hello World' .lower()) # all to lowercase 
print('Hello World' .capitalize()) # makes first letter to capital
print('Hello World' .title()) # capitalizes first letter of every word 
print('Hello World' .swapcase()) # swap the case of every letter, lower as uppper & upper as lower

print('Hello World' .casefold()) # makes everything to lowercase

# s1 and s2 are two objects lets check the id
s1 = 'Hello World'
s2 = s1.upper()
print(id(s1))
print(id(s2))

#you can cancatenate two strings using + operator
a1 = 'Akshara'
a2 = 'Ayyallu Karthick Kumaran'
print(a1+' '+a2)

# string concatenation can be done like this also
a3 = 'Rashila' ' Ragupathi Ravichandran'
print(a3)
