# reduce function
# reduce(func, seq)
# reduce functions, it repeatedly applies to the elements and returns a single value

from functools import reduce

a = [1,2,3,4]

# compute the product of all the elements
product_a = reduce(lambda x,y: x*y, a)  # reduce function has two arg x,y
print(product_a)


