# The items method returns a view of key value pairs. This can be used to simplify the loop


def main():
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe='i am a giraffe!', dragon='rawr')
    for k,v in animals.items():
        print(f'{k}:{v}') 

    #print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x} : {o[x]}')

if __name__ == '__main__' : main()
