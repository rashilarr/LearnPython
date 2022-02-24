# you can also create tuple from a built-in tuple function
# syntax is tuple(iterable)
mytuple = tuple(['Max',28,'Boston'])
print(mytuple)

# if you want to access the elements, 
item1 = mytuple[0]
item2 = mytuple[1]
item3 = mytuple[2]
print(item1,item2,item3)
# negative index
item4 = mytuple[-2]
print(item4)

# what happens when we try to change the values in tuples, show you error
#mytuple[0] = 'Tim' 

# easily iterated using for in loop
for i in mytuple:
    print(i)

# easily check the element was inside a tuple
if 'Boston' in mytuple:
    print('yes')
else:
    print('No')


