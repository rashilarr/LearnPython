# you can also create dictionary using the dictionary constructor and keyword arguments 

def main():
    animals = dict( kitten='meow', puppy='ruff!', lion='grrr', giraffe='i am a giraffe!', dragon='rawr')
    print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x} : {o[x]}')

if __name__ == '__main__' : main()

# keys and values may be any type 
# keys must be immutable, strings and numbers can always be keys
# this keyword argument method of creating the dictionary is obviously most convinient when you are using the strings for your keys

