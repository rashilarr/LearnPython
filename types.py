

x = 7
y = 7.0
z = '7.0'
a = True
b = None
print('x is {}'.format(x))
print('y is {}'.format(y))
print('z is {}'.format(z))
print('b is {}'.format(b))
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

print('')


# -----------Type() and id()----------
# In python, everything is an object, so a type is same as a class

# using tuple elements
c = (1,2,3,4,5)
print('c is {}'.format(c))
print(type(c))   # shows Tuple type

print("")

# using more data tpes in typle 
d = (1,'two',3.0,[4,'four'],5)
print('d is {}'.format(d))
print (type(d)) #shows tuple type

# inspect element in my structure and type of elements
print(type(d[1])) # shows str type since d[1] = 'two'
print(f'{d[1]}')

# creating two objects of same content
d = (1,'two',3.0,[4,'four'],5)
e = (1,'two',3.0,[4,'four'],5)
print('d is {}'.format(d))
print('e is {}'.format(e))
print(type(d))     # shows tuple
print(type(e))     # shows tuple
print ('')

# to print id of d and e 
print(id(d))
print(id(e))     # you will get two different unique numbers, d and e are two diff objects
                 # id function returns a unique identifier for each object
print('')
# to print id of d sub zero
print(id(d[0]))
print(id(e[0]))  # you will get same numbers as id
                 # here d[0] = 1 and e[0] = 1
                 # no need to create two object for same literal value 1 so same id

if d[0] is e[0]:
    print ("yep") # her d[0] = 1 and e[0] =1
else:
    print ("nope")

if d is e:
    print ("yep") 
else:
    print ("nope") # d and e are two different objects even though they have same values


# if you want to know a particular object is tuple

if type(d)=='tuple':     # this will not help it will show wrong ans
    print("yes")         # use a special function called 'isinstance()'
else:
    print("no")

# using isinstance

if isinstance(d, tuple):   # shows tuple
    print("tuple")
elif isinstance(d, list):
    print("list")
else:
    print("no")


f = [1,2,3,4,5]
if isinstance(f, tuple):   # shows list
    print("tuple")
elif isinstance(f, list):
    print("list")
else:
    print("no")

