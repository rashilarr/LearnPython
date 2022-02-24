''' collections : namedtuple
    * easy to create
    * light weight object type similar to struct
'''
from collections import namedtuple
# lets create a 2D point
point = namedtuple('point', 'x,y') 
''' first arg is class name, second arg is string --> has all fields you want to have
    This will create a class called point with the fields x and y
'''
pt = point(1,-4)
print(pt)           # point with x =1 and y=-4
print(pt.x,pt.y)    # you can also access the points


