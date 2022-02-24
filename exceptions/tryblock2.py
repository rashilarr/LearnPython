

# ----- Exceptions-------

''' Exceptions are a powerful runtime error reporting mechanism commonly used in onject - oriented systems '''

def main():
    try:
        x = 5/0
    except ValueError:
        print('I caught a ValueError')
    except ZeroDivisionError:
        print('don\'t divide by zero')   # you can include ' using \

if __name__ == '__main__':main()

''' By capturing the error , i can handle it intelligently.
    My execution continues since i caught the error if we don't catch the error then it actually stops the execution of my script
    you can catch different type error in the same try block 
    there are no of possible errors like zero division error '''
