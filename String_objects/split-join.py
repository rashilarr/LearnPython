#----------- Spliting and Joining ---------
# Python allows you to easily split and join strings based on seperator characters.

s = 'This is a long string with a bunch of words in it.'
print(s)

# 1. i can easily split this string into a list
print(s.split())
''' The result is a list with each element as a seperate word from the string. so what python has done here is folded on all spaces and then split the string on the spaces and loaded up a list with each of the individual words. ''' 

#2. i can add as many spaces and even add new line using triple quotes, the result is as same as above 

y = '''This is a          long     string 
with a bunch of words in it.
'''
print(y.split())

#3. i can split on the letter i instead
print(s.split('i'))  
''' leaves all space instead it's splitting on the letter i and so removes the i and splits on i, and then loads up the list with the seperated parts of the string that were seperated on the i '''

#4. spliting into list and joining the list with seperator colon
x = 'This is a long string with a bunch of words in it.'
l = x.split()     # we are making the list 
x2 = ':'.join(l)  # we are joining the elements of list with seperator :
print(x2)
x3 = ' -- '.join(l) # with seperator --
print(x3)

''' so spliting and joining strings is a common operation. Python object model makes it relatively simple to do '''

