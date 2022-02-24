# we have list called points2D
points2D = [(1,2),(15,1),(5,-1),(10,4)]

points2D_sorted = sorted(points2D)   # sorted is built in fn, no need to import

print(points2D)
print(points2D_sorted)

'''
[(1, 2), (15, 1), (5, -1), (10, 4)]
[(1, 2), (5, -1), (10, 4), (15, 1)]
sorted the values based on zeroth index or x values
1,5,10,15

If you want to sort based on y values, use lambda func
'''

points2D_lambda = sorted(points2D, key = lambda x: x[1])
print(points2D_lambda)

'''' like this
[(5, -1), (15, 1), (1, 2), (10, 4)]
'''
# If you wanted to sort according to sums of each tuples
points2D_sum = sorted(points2D, key = lambda x: x[0] + x[1])
print(points2D_sum)

'''
[(1, 2), (5, -1), (10, 4), (15, 1)]
'''


