
# Slicing
# slicing is very nice way to access the sub parts of your list
mylist = [1,2,3,4,5,6,7,8,9]

a = mylist[1:5]   # [start index : stop index: step index]
# if we dont specify the start index, by default takes from the begining
# if we dont specify the stop index, it goes all the way to the end

print(a) # print from index 1 to (stop index -1) i.e it will print index 1 to 4

b = mylist[::2] # step index to 2
print(b)

# i can also specify an negative index
# -1 is nice trick to reverse your list
c = mylist[::-1]
print(c)

d = mylist[::-2]
print(d)


