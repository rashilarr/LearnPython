# sets : unordered, mutable, no duplicates
myset = {1,2,3,1,2}  # set doesnot allows duplicates it will print {1,2,3}
print(myset)

# we can also use set function
# syntax set(iterable)
myset2 = set([1,2,3])
print(myset2)

# we can use string here
myset3 = set("Hello")
print(myset3)

# if you want a empty set,
myset4 = set()
print(type(myset4))

# a set is mutable
# adding items using .add() method
myset4.add(1)
myset4.add(2)
myset4.add(3)
myset4.add(4)
myset4.add(5)
print(myset4)

# we can also remove elements with the remove() method
myset4.remove(3)
print(myset4)

# we can also use discard() method
myset4.discard(4)
myset4.discard(6) # if it does not find the element, it will not show error here
print(myset4)

# pop() method - removes arbitrary value of a set and returns it
print(myset4.pop())  # arbitrary value is any value


# clear() method - empty our set
myset4.clear()
print(myset4)

