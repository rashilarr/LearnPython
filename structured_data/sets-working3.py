# Mostly if you are using sets, you are going to be checking the membership of the set and using them as sets 
# not as list
# if you want an ordered list, you will use a list or a string

# I can check for the members that are in set a but in set b by using the minus operator

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a-b)    # that's the members of set a that are not also in set b
                      

def print_set(o):
    print('{', end='')
    for x in o: print(x, end='')
    print('}')

if __name__ == '__main__' : main()
