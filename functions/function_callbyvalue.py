# call by value and call by reference

def main():
    a = 5                     # integer is immutable
    print(id(a))
    kitten(a)                 # here function is call by value
    print(f'a in main is {a}') # you are not sending the reference of variable

def kitten(x):       
    print(x)
    print(id(x))   # same id as a in main
    x = 3
    print(x)       # different id because the function call makes copy of variable 
    print(id(x))   # different id is printed

if __name__ == '__main__' : main()
