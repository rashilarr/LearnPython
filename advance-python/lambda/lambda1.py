# lambda arguments : expression
# lambda function is a small one line anonymous function that is defined without a name and syntax looks like about line
# first is lambda key word, then arguments then ':' then expression
''' lambda arguments : expression
first it will create a function with the arguments and then performs expression and returns the result
'''
add10 = lambda x : x+10   # add10 is the function with argument x
print(add10(5))

# this lambda function is same as function below
def add10_func(x):
    return x + 10
print(add10_func(5))

''' both functions do the same thing but lambda function is much shorter and only in one line
'''
''' Lambda function has three functions
     1. map function
     2. filter function
     3. reduce function - needs to be imported for python 3
 
     map function and filter function can be achieved by using list comprehension
'''


