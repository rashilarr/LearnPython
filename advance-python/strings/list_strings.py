# List and Strings

# to convert the strings to a list
# here to convert my strings into list with each word as an element
print('----To convert string into list----')
str = 'how are you doing'
list = str.split()
print(list)

''' split()
   * default limitor or argument is space " "
   * if you want to split with other specification, pass it as an argument
'''

str1 = 'how,are,you,doing'
list1 = str1.split(",")
print(list1)
list2 = str1.split(" ") # if it does not finds it, list is created with single element 
print(list2)  

print('----To convert back to a string----')
print(list1)
newstr = ''.join(list1) # syntax is empty string.join(string name)
print(newstr)

''''syntax:  ''.join(listname)
This will concatenate all the element of the list together as a string
if we need to put a space then add space in empty string
'''
newstr1 = ' '.join(list1)
print(newstr1)

