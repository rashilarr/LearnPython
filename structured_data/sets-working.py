# ------------------- sets ---------------
# Python has datatype for sets
# A set is like a list that does not allow duplicate elements

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a) # prints in different order each time
    print_set(b)

def print_set(o):
    print('{', end='')
    for x in o: print(x, end='')
    print('}')

if __name__ == '__main__' : main()
