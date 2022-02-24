# --------- Inheritance ---------
# Class inheritance is a fundamental part of object-oriented programming
# This alows you to extend your classes by driving, properties and methods from parent classes

class Animal:
    def __init__(self, **kwargs):                             # in init method
        if 'type' in kwargs : self._type = kwargs['type']     # no longer to provide any default values
        if 'name' in kwargs : self._name = kwargs['name']     # because now it is just a base class
        if 'sound' in kwargs : self._sound = kwargs['sound']  # it's going to be inherited in order to be used.

        # because of that we need to do a little bit of extra checking in our setter getters.
        # we cant just return a value, we need to check and see if the value's actually there.
        # and so using exceptions for this, a normal way to do this.
        # It attemps to returns the value if not it will return none instead.

    def type(self, t=None):
        if t : self._type = t
        try: return self._type
        except AttributeError: return None

    def name(self, n=None):
        if n : self._name = n
        try : return self._name
        except AttributeError : return None

    def sound(self, s=None):
        if s : self._sound = s
        try : return self._sound
        except AttributeError : return None

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

# To use this class we are now inheriting it to create other classes. we got a Duck class and Kitten class 
# and each of these cases, we set the type to duck and kitten

class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'                      # we set the type duck 
        if 'type' in kwargs: del kwargs['type']  # we check and see if there is a type in the keyword args and if so we delete that
        super().__init__(**kwargs)               # Through the super function, we call the parent class initializer with our kwargs. 
                                                 # so super always calls the parent class
class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs : del kwargs['type']
        super().__init__(**kwargs)

        # This allows me to do things like a special case
        # we can define a method that does not exist in any of the other subclasses of animal, and so in this case we'll call this one kill.
        # kittens are always predators always trying to kill something
        
    def kill(self, s):
        print(f'{self.name()} will now kill all {s}!')

def main():
    a0 = Kitten(name = 'fluffy', sound = 'rawr')  # we initialize a0 with kitten and a1 with duck 
    a1 = Duck(name = 'donald', sound = 'quack')
    print(a0)
    print(a1)
    a0.kill('humans')

if __name__ == '__main__' : main()

