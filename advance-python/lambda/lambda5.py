# filter function
# filter(func, seq)
# this func - will returns true or false
# and filter function will returns all the elements for which this func evaluates to true

a = [1,2,3,4,5,6]

# to filter this and to get only even number
b = filter(lambda x:x%2==0, a)
print(list(b))

# we can achieve this with list comprehension
c = [x for x in a if x%2==0]
print(c)

