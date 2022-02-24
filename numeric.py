# Numeric types

x = 7               # integer
print(f'x is {x}')
print(type(x))

y = 7 * 3           # int
print(f'y is {y}')
print(type(y))

z = 7.0              # float
print(f'z is {z}')
print(type(z))

a = 7 * 3.14159      #float
print(f'a is {a}')
print(type(a))

b = 7 / 3            # output shows floating type but in python 2 it will do integer division
print(f'b is {b}')
print(type(b))


c = 7 // 3           # if you use double division symbol it will do integer division and show int
print(f'c is {c}')
print(type(c))

d = 7 % 3           # modulo operator gives you remainder so int      
print(f'd is {d}')
print(type(d))

e = .1+.1+.1-.3           # output will not be 0 and not int; it will be floating number       
print(f'e is {e}')        # it is precision but not acurate
print(type(e))            # dont use this for money calculation it will end up with wrong ans 

from decimal import *     # to get accurate ans use this
f = Decimal('.10')        # you will get 0.00 as ans and balance your account when using in billing system
g = Decimal('.30')        # proper arithmetic decimal model
h = f + f + f - g
print(f'h is {h}')
print(type(h))
