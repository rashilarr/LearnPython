
# Function Arguments

# Function arguments are fairly straight forward
# if i want to pass an argument to kitten()

def main():
    kitten(5,6)

def kitten(a, b, c=0): # if you dont give enough arg, it will assume last arg is not given
    print('Meow')      # you can assign here in fun def also like this c =0
    print(a,b,c)

if __name__ == '__main__' : main()
