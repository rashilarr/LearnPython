# Rasing an exception using keyword raise
'''
x = -5
if x < 0:
    raise Exception('x should be positive') 
'''
# second way using assert statement 
# syntax is assert(conditon), 'message'
# assert statement will through an assertion error if your assertion is not true 

x = -5
assert(x>=0), 'x is not positive' # if the condition is true, your code is fine



