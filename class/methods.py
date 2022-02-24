#----------- Class methods -----------
# A function that is associated with a class is called a method.
# This provides the interface to the class and its objects

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type']
        self._name = kwargs['name']
        self._sound = kwargs['sound']

    def type(self, t = None):
        if t : self._type = t
        return self._type
    
    def name(self, n = None):
        if n : self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound
    
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type='kitten',name='fluffy',sound='rawr')
    a1 = Animal(type='duck',name='donald',sound='quak')
    print(a0)
    print(a1)

if __name__ == '__main__':main()
