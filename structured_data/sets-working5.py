
# I can look for the exclusive or using the caret operator. so that's a or b but not both
    
def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    
    print_set(a^b)

def print_set(o):
    print('{', end='')
    for x in o: print(x, end='')
    print('}')

if __name__ == '__main__' : main()
