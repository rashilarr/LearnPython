# list : ordered,mutable, alows duplicate elements

mylist = ['Banana','cherry','apple']
print(mylist)

mylist2 = list()   # creates empty list you can append with elements
print(mylist2)     

# list allows different datatypes
mylist3 = [5,True,'apple','apple']
print(mylist3)

#you can access elements through index
item1 = mylist[0]
item2 = mylist[1]
item3 = mylist[2]
print(item1,item2,item3)

# you can also specify a negative index: -1 is last element
x = mylist[-1]
y = mylist[-2]
z = mylist[-3]
print(x,y,z)

# you can iterate over your list using for in loop 
for i in mylist:
    print(i)

# you can check an item is inside your list you can use if 
if 'Banana' in mylist:
    print('yes')
else:
    print('no')

if 'lemon' in mylist:
    print('yes')
else:
    print('No')

# To check how many elements inside your list using len() method
print(len(mylist))

# To add elements to the list using append: it will insert an item at the end of the list
mylist.append('lemon')
print(mylist)

# if you want to insert the items at the specific position, we can use the insert method
mylist.insert(1, 'blueberry')  # listname.insert(index, item)
print(mylist) # blueberry is inserted in the postion 1

# To remove item in the list
# pop() method - remove last item in the list and returns the item
a = mylist.pop()
print(a)
print(mylist)

# To remove a specific element in the list using remove() method
b = mylist.remove('cherry')
print(mylist)

# we can reverse the list with reverse() method
mylist.reverse()
print(mylist)

# we can sort the list using sort() method
numlist = [4,3,-1,-5,10]
print(numlist)
numlist.sort() # sorts in accending order
print(numlist) # this will change your list

# if you dont want to change the list rather you want to create new list, use built in sorted method
list1 = [9,5,-6,7,1,0,-5,-7,3]
print(list1)
list2 = sorted(list1)
print(list1) # it does not change the list1
print(list2) # new sorted list


# we can also remove all the elements using the clear() method
mylist.clear()
print(mylist)
