# ----------------- Keyword Argument------------
# Keyword arguments are like list arguments that are dictionaries instead of tuples

# This allows your function to have a variable number of named arguments

# ** ---> used for keyword argument

# kwargs --> traditional name for keyword arguments


def main():
    kitten( Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(f'kitten {k} says {kwargs[k]}')
    else: print('Meow')

if __name__ == '__main__' : main()
