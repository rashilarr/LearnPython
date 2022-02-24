
# Function Arguments

# Function arguments are fairly straight forward
# if i want to pass an argument to kitten()

# -------------Non-default arguments and default arguments----------------

def main():
    kitten(5,8)

def kitten(a, b=1, c=0,d): # prints 5,1,0 here b=1 and c=0 are default argument, a is without default
    print('Meow')        # any arguments with default must be given after non default
    print(a,b,c,d)    # Error : type error non default argument follows default argument        

if __name__ == '__main__' : main()
