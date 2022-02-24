# concatinate two string with + operator
greetings = "Hello"
name = "Tom"
sentence = greetings + " " + name
print(sentence)

# we can iterate our string with for in loop
for i in greetings:
    print(i)

for x in name:
    print(x)

# To check the char or substring inside the string, we can do with if in statements
if 'e' in greetings:      # checks for char 'e'
    print('yes')
else:
    print('no')

if 'ell' in greetings:     # checks for substring 'ell'
    print('yes')
else:
    print('no')


