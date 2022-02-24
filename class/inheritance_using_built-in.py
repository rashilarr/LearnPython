# Im inheriting from str and it does not have a capital first letter. This is a built-in class, built-in to python and that's our standard string class
# Im inheriting from that an im overwritting the string representation method, to instead of returning the string itself, to return a slice of the string where the step goes backwards
# and so this will reverse the string. so this is a type of a string that every time i print it will print backwards.

class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__' : main()


# Class inheritance is very powerful to do it and you can inherit and extend and even as in this case change built-in classes or classes that you define yourself
# Class inheritance is a vital part of object-oriented programming and in python
