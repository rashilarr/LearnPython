# to print sorted use print_set(sorted(a))

# how many times run you will get same order

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(sorted(a))
    print_set(sorted(b))

def print_set(o):
    print('{', end='')
    for x in o: print(x, end='')
    print('}')

if __name__ == '__main__' : main()
