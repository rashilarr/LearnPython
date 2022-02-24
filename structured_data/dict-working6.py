# A dictionary is indexed by its keys, so you can easily pick a particular value



def main():
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe='i am a giraffe!', dragon='rawr')
    print(animals['lion'])  # prints the value i.e grrr

    animals['lion'] = 'I am a lion'  # you may use this to assign new value to lion
    animals['monkey'] = 'haha'       # you may use this to add a new item
    
    print('lion' in animals)   # you can search for a key by using the in operator
    print('found' if 'lion' in animals else 'nope!') # you can use that in any conditional expression

    #print(animals['godzilla'])   # if you try to access the key that does not exist then it shows key error
    
    # you can use the get method if you dont know if the key exists
    print(animals.get('godzilla'))   # it will print None value

    print_dict(animals)

def print_dict(o):
    for k,v in o.items(): print(f'{k} : {v}')

if __name__ == '__main__' : main()
