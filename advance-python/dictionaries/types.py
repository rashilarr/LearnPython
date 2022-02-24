
# you can use numbers in dictionary
my_dict = {3:9,6:36,9:81}
print(my_dict)

# how to access the value
value = my_dict[3]   # 3 is not index here, it is key 
print(value)

# we can use tuple as key
mytuple = (8,7)
mydict = {mytuple : 15}
print(mydict)

# we cannot use list as key, list is mutable and unhasable.
# it will through type error: unhasable type
mylist = [8,7]
mydict2 = {mylist :15}
print(mydict2)


