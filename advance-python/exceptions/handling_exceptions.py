# Handling exceptions
# you can catch exceptions with try except block
'''
try :
     a = 5/0
except:
    print('an error happend')
'''
# you can also catch the type of exceptions
'''
try:
    a = 5/0
except Exception as e:
    print(e)   # prints zero division error
'''

# its good practise to specify the type of exception error you want to catch
'''
try:
    a = 5/1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
'''
# you can also have else clause in try except block
# you can also have finally clause - used for clean up operations
try:
    a = 5/1
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:  
    print('Everything is fine')
finally:
    print('cleaning up')

