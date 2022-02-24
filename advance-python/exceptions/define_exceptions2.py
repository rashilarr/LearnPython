
# Define our own exceptions
# can define own error classes by sub classing from the base exception class

class ValueTooHighError(Exception):  # as a base class, using Exception class
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)


# using try and except block to catch the error

