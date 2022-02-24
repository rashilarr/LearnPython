# ------------ Dictionaries --------------
# Python's Dictionary type is a hashed key value structure
# this is comparable to associative arrays in other languages

def main():
    animals = { 'kitten':'meow', 'puppy':'ruff!', 'lion':'grrr', 'giraffe':'i am a giraffe!', 'dragon':'rawr'}
    print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x} : {o[x]}')

if __name__ == '__main__' : main()
