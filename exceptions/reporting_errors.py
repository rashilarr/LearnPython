# ------- Reporting Errors -----------
''' Exceptions are an excellent way to report run time errors.
    You can generate your own exceptions for error reporting in your code, and this is considered best practice '''

def main():
    for i in inclusive_range(1,2,3,1):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator

    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__' : main()

''' intialize parameters block :
    while checking the arguments: if no of arguments < 1 --> raising the error
    if no of args is > 3 --> raising the error 
    try giving without args and with many args > 3
    '''
