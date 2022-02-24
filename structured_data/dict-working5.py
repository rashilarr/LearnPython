# Keys method
# The keys method returns a view of dictionary keys

# Values method 
# The values method returns a view of dictionary values

def main():
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe='i am a giraffe!', dragon='rawr')
    for k in animals.keys(): print(k)
    print()
    for v in animals.values(): print(v)
    #print_dict(animals)

def print_dict(o):
    for k,v in o.items(): print(f'{k} : {v}')

if __name__ == '__main__' : main()
