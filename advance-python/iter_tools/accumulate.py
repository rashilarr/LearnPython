''' itertools : accumulate - accumulate function makes an iterator that returns accumulated sums or any other binary function
'''

from itertools import accumulate
import operator

a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))

'''
[1, 2, 3, 4]
[1, 3, 6, 10]
first element is 1, second is 1+2=3, third is 3+3=6, forth is 6+4=10
it gives us sum

'''
# we can also multiply the elements, lets import operator and then we can give second arg func=operator.mul

acc2 = accumulate(a, func=operator.mul)
print(a)
print(list(acc2))
'''[1, 2, 3, 4]
   [1, 2, 6, 24] it multiples 1*2=2, 2*3=6,6*4=24
'''
# third example, we will use the max
b = [1,2,5,3,4]
acc3 = accumulate(b, func=max)
print(b)
print(list(acc3))

'''
[1, 2, 5, 3, 4]
[1, 2, 5, 5, 5] it gives the max value 
[1, 2 >1 = 2, 5>2 =5, 5>3=5, 5>4=5]
'''

