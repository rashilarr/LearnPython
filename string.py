# string data type

x = 'seven'     # In python there is no difference between single quotes and double quotes
y = "seven"
z = '''

seven            

'''              # you can make multi line string using triple single quotes or triple double quotes
a = """


seven


"""

b = "seven".upper()                     # string is an object
c = "seven".capitalize()            

d = 'seven {} {}'.format(8,9)           
e = 'seven {1} {0}'.format(8,9)  # here format arguments are postional arguments so output will be - seven 9 8


f = 'seven "{1:<9}" "{0:>9}" '.format(8,9)  # you can use double quotes inside single quotes and vice versa 
                                            # {1:<9} - left indent 9 spaces and {0:>9} - right indent 9 spaces

print('e is {}'.format(e))

print('f is {}'.format(f))


print('d is {}'.format(d))
print('e is {}'.format(e))

print('x is {}'.format(x))
print('y is {}'.format(y))
print('z is {}'.format(z))
print('a is {}'.format(a))
print('b is {}'.format(b))
print('c is {}'.format(c))



print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))


