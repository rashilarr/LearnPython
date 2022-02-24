# Formating Strings
# Different ways : 1. old style with % operator, 2. .format() method and 2. f-strings

print('---old style with % operator---')
var1 = 'Tom'
var2 = 3
var3 = 3.1234567
str1 = 'the variable is %s' % var1
str2 = 'the variable is %d' % var2
str3 = 'the variable is %f' % var3
str4 = 'the variable is %.2f' % var3
print(str1)
print(str2)
print(str3)
print(str4)

''' % is place holder
    %s is for string var
    %d for integer decimal value
    %f for floating point value - default 6 digits after the decimal value
    %.2f - you can specify the digits after decimal value, here 2 digits
'''
print('----new style with format method----')

v1 = 'Tom'
v2 = 3
v3 = 3.1234567
newstr1 = 'the variable is {}'.format(v1)
newstr2 = 'the variable is {}'.format(v2)
newstr3 = 'the variable is {}'.format(v3)
newstr4 = 'the variable is {:.2f}'.format(v3)
print(newstr1)
print(newstr2)
print(newstr3)
print(newstr4)
# if there are more variables you can use like this
newstr = 'the variable is: {} {} {} and {:.2f}'.format(v1,v2,v3,v3)
print(newstr)
''' {} is place holder
    .format(arg) - arg is variable name
    {:.2f} - to show 2 digits after decimal point
'''
print('--- new style with f-string---')

a1 = 'Tom'
a2 = 3
a3 = 3.1234567
new_str1 = f'the variable is {a1}'
new_str2 = f'the variable is {a2}'
new_str3 = f'the variable is {a3}'
new_str4 = f'the variable is {a3:.2f}'
print(new_str1)
print(new_str2)
print(new_str3)
print(new_str4)
# if there are more variables you can use like this
new_str = f'the variable is: {a1} {a2} {a3 * 2} and {a3:.2f}'
print(new_str)

''' f string is used infront of strings
    {} is place holders
    var names are given inside the place holders directly like {a1}
    this method is convinient and faster
    this method is highly recommended
    {a3 * 2} - this is evaluated at run time, you can do mathematical operation here
'''

