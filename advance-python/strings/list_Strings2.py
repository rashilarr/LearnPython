# List and strings continuation...

from timeit import default_timer as timer

list = ['a'] * 6  # This will create a list with 6 elements of 'a'
print(list) 


# creating an empty string then convert it to string
# bad coading style

start = timer()
print('bad style')
str = ''
for i in list:    # strings are immutable
    str += i      # here new string is created and assigned to that 
stop = timer()
print(stop - start)
print(str)        # very expensive


print('good style')
# good coading style
# using join method

start = timer()
mystr = ''.join(list)
stop = timer()                  # faster than bad method
print(stop - start)
print(mystr)
