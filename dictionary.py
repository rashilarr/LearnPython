# -------- Dictionary-------

# A Dictionary is a searchable sequence of key-value pairs and you construct it like this:

x = { 'one':1, 'two':2, 'three':3, 'four':4, 'five':5}

for i in x:
    print('i is {}'.format(i))  # displays only the keys not values

print('')

# to display both keys and values

for k,v in x.items():
    print(f'k is {k}, v is {v}')  # displays both keys and values

print('')
# Dictionary is mutable 

x['three'] = 42

for k,v in x.items():
    print(f'k is {k}, v is {v}')  
