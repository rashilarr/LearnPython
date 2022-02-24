# ----- Exceptions-------

''' Exceptions are a powerful runtime error reporting mechanism commonly used in onject - oriented systems '''

import sys

def main():
    try:
        x = 5/0
    except ValueError:
        print('I caught a ValueError')
    except:
        print(f'Unknown Error: {sys.exc_info()[1]}')
    else:
        print('Good job!')
        print(x)

if __name__ == '__main__':main()

''' you can get to know the type of error by using import sys, which has a lot of constants in it, that will help me to understand things like this'''
