#------------ Formatting String -------
# Python has rich formatting capabilities

x = 42
print('the number is {}'.format(x))  

#{} is place holder the format method specifies the values for the place holder

# if you have two values and while printing use two place holder & format(a,b) 
a = 10 
b = 20
print('the numbers are {} {}'.format(a,b))

# you can name the variables like this

print('the numbers are {aa} {bb}'.format(aa = a, bb = b))

# you can change the place like this

print('the numbers are {bb} {aa}'.format(aa=a,bb=b))

# you can use the positional arguments, say {1} {0} the postional args starts with zero

print('the numbers are {1} {0}'.format(a,b)) #reversing them again
print('the numbers are {0} {1}'.format(a,b)) 

#this allows me to repeat a value like this

print('the numbers are {0} {1} {0}'.format(a,b))

# you can also add formatting instructions, formatting instructions are preceded by a colon, eg {0: } {1: } 
# <5 --> left justified by 5 spaces
# >5 --> right justified by 5 spaces

print('the values are {0:<5} {1:>5}'.format(a,b))

# i can add a leading zero
print('the values are {0:<5} {1:>05}'.format(a,b))

# i can add sign if i want to
print('the values are {0:<5} {1:+}' .format(a,b))

# i can use sign in combination with positional args and leading zeros
print('the values are {0:<5} {1:+05}'.format(a,b)) #sign takes up 1 of the 5 positions

# using one value
y = 42 * 747 * 1000
print('the value is {}'.format(y)) # the value is big number

# if i want to format with comma for big numbers use this
print('the value is {:,}'.format(y)) # i will get comma for thousands seperation

# if i want to use period instead of commas in european method
print('the value is {:,}'.format(y).replace(',','.'))

#you can also specify a fixed number of decimal places with the letter f
print('the value is {:f}'.format(y)) # defaults to that many places
print('the value is {:.3f}'.format(y)) # point three gives me three places right to the decimal point

# you can specify different bases
z = 42
print('the value is {:x}'.format(z)) # hexadecimal
print('the vaue is {:o}'.format(z))  # octal
print('the vaue is {:b}'.format(z))  # binary

'''begining with python version 3.6 you may now use F strings for formatting, so instead of whole format thing here, it looks like that, put the letter f or F infront of string then i use the variable name where you could otherwise use the positional arg with the format method'''
print(f'the value is {z}')

# if i want to do some formatting, i can say .3F
print(f'the value is {z:.3F}') # it will give me 3 decimal places

# all the formatting method showed above all work with this method as well, in fact the F string is simply a short cut for the format method






