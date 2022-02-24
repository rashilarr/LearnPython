# An instance of a class is called an object.
# Object is created by calling the class itself as if it were a function

class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name
    
    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('Print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".' .format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal('kitten','fluffy','rawr')
    a1 = Animal('duck','donald','quak')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor','veronica','hello'))

if __name__ == '__main__' : main()
