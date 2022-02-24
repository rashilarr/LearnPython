# some more useful methods 

mystr = '       Hello World        '
print(mystr)   # printed with space

# .strip() method - removes with space
mystr.strip
print(mystr)  # printed with space
mystr = mystr.strip()
print(mystr)
# this .strip() method does not change the original string because strings are immutable 
# so, again assign it yo mystr to do the change

# To change the string to upper case
mystr1 = "Hello Akshara"
print(mystr1.upper())

# To change the string to lower case
print(mystr1.lower())

print('----startswith----')
# To check the char or substring in starting position of the string - stringname.startswith('char/substring')
print(mystr1.startswith('H'))     # returns true 
print(mystr1.startswith('Hello')) # returns true 
print(mystr1.startswith('Akshara')) # returns false
print(mystr1.startswith('o')) # returns false 

print('----endswith----')

# To check the char or substring in end position of the string - stringname.endswith('char/substring')
print(mystr1.endswith('Akshara'))  # returns true
print(mystr1.endswith('a'))      # returns true
print(mystr1.endswith('Hello'))      # returns false

print('----find index----')
# To find the index of the char or substring - stringname.find('char/substring') will return the index of char/substring
print(mystr1.find('o'))     # returns 4, the first index that finds with 'o'
print(mystr1.find('World')) # returns -1, if it does not find the char/substring, returns -1
print(mystr1.find('Akshara')) # returns 6 
print(mystr1.find('l'))     # returns 2, the first index that finds with letter 'l'
print(mystr1.find('lo'))    # reutrns 3

print('----count----')
# To find the count of char or substring
print(mystr1.count('l')) # returns 2 
print(mystr1.count('a')) # returns 2
print(mystr1.count('h')) # returns 1
print(mystr1.count('k')) # returns 1

print('----replace----')
# To replace the char/substring in the string
print(mystr1.replace('Akshara' , 'Universe'))
print(mystr1.replace('Aksssshara' , 'Universe')) # if it does not find, it will print original

