#----------- Decorators ----------

# A decorator is a form of metaprogramming and it can be described as a special type of function
# that returns a wrapper function

# uses @ as syntax

def f1(f):
    def f2():
        print('this is before f function call')
        f()
        print('this is after f function call')
        
    return f2

@f1
def f3():
    print('this is f3')

f3()
