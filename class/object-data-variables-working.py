# --------------- Object Data ----------
# Data may be associated with a class or an object and it's important to understand the distinction.

class Animal:
    x = [1,2,3]      # class variables
    def __init__(self, **kwargs):   # init method 
        self._type = kwargs['type'] if 'type'in kwargs else 'kitten'    # object variables
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'   # object variables
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'  # object variables

    def type(self, t = None):    # this method is getter and setter
        if t : self._type = t
        return self._type

    def name(self, n = None):
        if n : self._name = n
        return self._name 

    def sound(self, s = None):
        if s : self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rawr')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1) 

    # accessing object variables
    #a0._name= 'joe'  # bad idea to access directly from here
    #print(a0.name)
    
    # accessing class variables
    print(a0.x)  # prints [1,2,3]
    a1.x[0] = 7  # changing a1 not a0
    print(a0.x)  # changes seen in a0 prints [7,2,3]

if __name__ == '__main__': main()
