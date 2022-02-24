# function call by reference

def main():
    x = [5]   # list is mutable
    print(id(x))
    kitten(x)
    print(f"value of x in main is {x}")  # value of x becomes 3 after function call

def kitten(a):
    print(a)  
    print(id(a))
    a[0] = 3        # x is list of one element so a[0]=3 is accessing reference
    print(a)        # 3 is printed
    print(id(a))    # same id of x 

if __name__ == '__main__' : main()

