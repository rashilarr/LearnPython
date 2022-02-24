# To access the characters inside the string
mystr = "Hello World"
print(mystr)

char = mystr[0] # to access first char, index is 0
print('first char:',char)

#for i in mystr:
#    print(i, end = ' ')

# we can use negative index 
# index -1 will give the last char
char1 = mystr[-1]
print('last char:',char1)
# index -2 is second last
char2 = mystr[-2]
print('second last char:',char2)

# if i want to change the char, i cannot do because strings are immutable, it cannot be change after its creation
char[0] = 'h' # try to change the first char, type error will appear
