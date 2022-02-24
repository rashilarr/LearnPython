
# I can find the members that are in set a or set b or both by using the vertical bar operator 
# that's all of the members that are in one or both of the sets

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a|b)

def print_set(o):
    print('{', end='')
    for x in o: print(x, end='')
    print('}')

if __name__ == '__main__' : main()
