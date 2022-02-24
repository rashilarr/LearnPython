# Exceptions
# if the statement is syntactically correct and it may cause error during executionthis is called as exceptional error
# there are several different error clauses

#1. Type Error
    # trying to add a number and a string will raise a type error
#a = 5 + '10'

#2. Import Error
    # when im trying to import some module and it could not found then this will raise import error

#import somemodule

#3. Name Error
    # when i try to assign a variable that is not defined already, it will raise name error 
'''
a = 5
b = c
'''

#4. file not found error
    # when i try to open a file that is not found, it will raise file not found error
#f = open('somefile.txt')

#5. value error
    # this error will occur when the values of argument are of same type but it may be inapropriate value
'''
a = [1,2,3]
a.remove(4)
'''
#6. Index Error
    # this error will occur when you try to access the large number of index that is not yet used
'''
a = [1,2,3]
print(a[4])
'''

#7. key error
    # when i access the key that is available
'''
my_dict = {'name':'max'}
my_dict['age']
'''

