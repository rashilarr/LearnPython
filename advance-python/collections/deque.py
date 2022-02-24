# collections : deque
'''
* The deque is a double ended queue
* It can be used to add or remove elements from both ends
* both are implemented in a way that this will be very efficiently

'''
from collections import deque

# create a deque
d = deque()

# can append items like list
d.append(1)
d.append(2)

# To add elements in left
d.appendleft(3)
print(d)

print('---extend---')
# we can extend our elements will all elements inside list 
d.extend([4,5,6])
print(d)

# To extend elements in left
d.extendleft([-1,-2,-3]) # note that it will add elements from left [-3,-2,-1]
print(d)                 # -3 is most left element in our deque

print('---Rotate---')
# we can rotate our deque; orig deque is [-3,-2.-1,3,1,2,4,5,6]
d.rotate(1)              # this will rotate our deck by 1 element in right side
print(d)                 # [6,-3,-2,-1,3,1,2,4,5]
d.rotate(2)              # this will rotate by 2 in right side
print(d)                 # [4,5,6,-3,-2,-1,3,1,2]
# to rotate left side, use negative sign
d.rotate(-1)             # this will rotate our deck by 1 element in left side
print(d)                 # [5,6,-3,-2,-1,3,1,2,4]

print('---Remove---')
# we can remove elements from both sides
d.pop()                  # will return and remove the element
print(d)

d.popleft()              # will return and remove the element from left 
print(d)

# To remove all the elements 
d.clear()
print(d)


