# union and intersection
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

print('odds' , odds)
print('evens' , evens)
print('primes', primes)

print('union')
# find out the union : union combines the elements in the sets without duplication
u = odds.union(evens)
print(u)

u2 = evens.union(primes)
print(u2)

print('intersection')
# find out the intersection: the intersection takes the elements only that are found in both sets
i = odds.intersection(evens)
print(i)

i2 = evens.intersection(primes)
print(i2)
