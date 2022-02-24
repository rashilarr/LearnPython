#------------------- Argument Lists--------------
# python functions allows variable length, arg lists like the variadic args in c and other languages

# *args ---> This is the variable length argument list, we can treat it like sequence of list 
#            its actually a tuple

def main():
    kitten('meow','grrr','purr')

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow')

if __name__ == '__main__' : main()
