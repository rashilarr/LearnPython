# Items method

def main():
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe='i am a giraffe!', dragon='rawr')
    print_dict(animals)

def print_dict(o):
    for k,v in o.items(): print(f'{k} : {v}')

if __name__ == '__main__' : main()
