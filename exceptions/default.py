# ----- Exceptions-------

''' Exceptions are a powerful runtime error reporting mechanism commonly used in onject - oriented systems '''

def main():
    try:
        x = 5/0
    except ValueError:
        print('I caught a ValueError')
    except:
        print('Unknown Error')
    else:
        print('Good job!')
        print(x)

if __name__ == '__main__':main()

''' If i am excepting error and don't know what it is, you can have a default except that does not know which error it is, then the except is block gets printed '''
