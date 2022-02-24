# slicing with tuples
# slicing is a very nice way to access the subparts of your tuple with the use of the colon

a = (1,2,3,4,5,6,7,8,9,10)

b = a[2:5]  # start index : stop index
print(b)

c = a[:5] # if we dont specify the start index, it begins with index 0
print(c)

d = a[2:] # if we dont specify the stop index, it goes all the way to the end
print(d)

# optional step argument
e = a[::2]
print(e)

# reverse the tuple
f = a[::-1]
print(f)

