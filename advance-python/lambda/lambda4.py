# map function
# syntax is map(function, seq)

a = [1,2,3,4,5]

# if you want list b with the elements of a multiplied by 2
b = map(lambda x:x*2, a)
print(list(b))  # b is map object, convert it to list to view elements

# you can do this with list comprehension

c = [x*2 for x in a]
print(c)
