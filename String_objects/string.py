#--------- String Objects --------
''' strings are the first class objects in python 3
    This is different than many languages
    It is even a little bit diff than python2, even though strings were obj in python 2, they where not fully first class objects and the string interface is for more consistent now '''

print('Hello World.'.upper())
print('Hello World.'.swapcase()) # swap the case from upper to lower and viceversa
print('Hello World.{}'.format(42*7)) # string formatting is commonly done like this

''' triple quoted strings that are unique in python
    this is usually done with double quotes and works for single quotes also.
    you can type in different lines 
    you can include space '''

print("""
        Hello,
        World.

        {}

        """.format(42*7))

# all of these applies to string as a variable, assign to s, still works as same
s = 'Hello World. {}'
print(s.format(42*7))

# you can sub-class strings in python

class MyString(str):
    def __str__(self):
        return self[::-1]  # prints string reverse

c = MyString('Hello World')
print(c)
