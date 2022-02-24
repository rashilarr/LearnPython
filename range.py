
# range() - you can also create a sequence using range
# It has 3 parameters
# range(start,end,step by) 
      #range starts from start number or default by zero
      #range ends by end-1  
      #range step = incremebt default by 1

# if you give one paremeter it will take as end

z = range(5)   # range(5) will be (0,1,2,3,4)
for i in z:
    print('{}'.format(i))

print('')

# if you give two parameters it will take as start and end
x = range(5,10)
for i in x:
    print('{}'.format(i))

print('')

# using 3 parameters
y = range(5,50,5) # range of values starts from 5 ends 49 and increment by 5
for i in y:
    print(f'{i}')

print('')

# Like Tuple, range is immutable or not mutable i.e you cannot change the value after assignment
# To resolve this by using list constructor

a = list(range(5))
a[2]=42
for i in a:
    print('{}'.format(i))

# without using list

a = range(5)   #Type error: range does not support item assignment 
a[2]=42
for i in a:
    print('{}'.format(i))
