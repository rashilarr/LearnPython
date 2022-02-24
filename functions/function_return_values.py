# ---------------- Return values -------------

# In python, ther is no distinction between a function and a procedure.
# All functions return a value

def main():
    x = kitten()                # if there is no return statement or empty return statement
    y = kitten1()                            # then the function returns none
    z = kitten2()  
    a = kitten3()
    print(type(x),x)
    print(type(y),y)
    print(type(z),z)
    print(type(a),a)

def kitten():
    print('meow')

def kitten1():
    return 42         # if we return a number then function returns it 

def kitten2():
    return [42,43,44]
def kitten3():
    return dict(x =1,y=2,z=3)

if __name__ == '__main__' : main()
