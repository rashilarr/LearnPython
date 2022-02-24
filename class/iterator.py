# ---------------- Iterator -------------
# An iterator is a class that provides a sequence of items, generally used in a loop. 

# This is an iterator class implementation of the inclusive range application, its functionally identical to the generator from the 
#fucntions chapter


class inclusive_range:
    def __init__(self, *args):       # This is our constructor 
        numargs = len(args)          # a constructor sets up all the variables and checks the arguments
        self._start = 0              
        self._step = 1
                                      # checks how many arguments we have,
        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')      
        elif numargs == 1:
            self._stop = args[0]      # if it is one argument then it is stop
        elif numargs == 2:                 
            (self._start, self._stop) = args  # if two: then start and stop
        elif numargs == 3:
            (self._start, self._stop, self._step) = args                   # if three: start, stop and step
        else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

        self._next = self._start

    def __iter__(self):    # we have special iterator method
        return self        # simply identifies this object as an iterator obj

    def __next__(self):   # next function which is iterator itself
        if self._next > self._stop:  # constuct like, for loop is going to look for this
            raise StopIteration      # next function in order to treat this as an iterator
        else:                        # and in order to use it for iteration
            _r = self._next
            self._next += self._step
            return _r

def main():
    for n in inclusive_range(25):
        print(n, end=' ')
    print()

if __name__ == '__main__' : main()
