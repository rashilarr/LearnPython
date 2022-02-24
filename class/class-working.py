
# ------------ Class ---------------
# A class is the basis of all data in python, everything is object in python
# and a class is how an object is defined

class Duck:
    sound = 'Quack quack'
    movement = 'walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()
    #print(donald.sound)  # will get the same result but this is not recommended
    donald.move()

if __name__ == '__main__' : main()
