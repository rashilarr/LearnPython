# I can look for only the members that are in both 

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    
    print_set(a&b)

def print_set(o):
    print('{', end='')
    for x in o: print(x, end='')
    print('}')

if __name__ == '__main__' : main()

# so like the other collection in python members of a set can be any type
# in this case i found that the strings were convinient way to get a bunch of data into them easily 
# so we can look at the intersections of the sets.
