# Define our own exceptions
# can define own error classes by sub classing from the base exception class

class ValueTooHighError(Exception):  # as a base class, using Exception class
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(4)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message,e.value)


# using try and except block to catch the error
