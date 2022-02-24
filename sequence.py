# sequence typesy

# Python provides buit in sequence types including 'List', 'Tuples' and 'Dictinaries'

#--------List--------
# List is created with square brackets

x = [1,2,3,4,5]

for i in x:
    print(' i is {}'.format(i))

# List is mutable sequence, I can reassign the value after the value have assigned 

x[2] = 42
for i in x:
    print(' i is {}'.format(i))


#-------Tuple--------
# Tuple is created with paranthesis


y = (1,2,3,4,5)

for i in y:
    print('i is {}'.format(i))

# Tuple is not mutable, you cannot reassign the values

y[2]=42         # type error: tuple obj does not support item assignment

for i in y:
    print('i is {}'.format(i))

