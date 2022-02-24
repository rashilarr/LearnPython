
# Function Arguments

# Function arguments are fairly straight forward
# if i want to pass multiple arguments to kitten()

def main():
    kitten(5,6,7)  # if i dont pass enough args or smaller no of args in func call than are expected
                   # here in the fuction def, then we will get error
                   #  kitten(5,6)
def kitten(a,b,c): #  def kitten(a,b,c) Type error: kitten() missing 1 required postional arg : 'c'
    print('Meow')
    print(a,b,c)

if __name__ == '__main__' : main()
