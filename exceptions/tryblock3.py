

# ----- Exceptions-------

''' Exceptions are a powerful runtime error reporting mechanism commonly used in onject - oriented systems '''

def main():
    try:
        x = 5/3
    except ValueError:
        print('I caught a ValueError')
    except ZeroDivisionError:
        print('Don\'t divide by zero')
    else:
        print('Good job!')
        print(x)

if __name__ == '__main__':main()


''' Else block is executed when you have no errors '''
