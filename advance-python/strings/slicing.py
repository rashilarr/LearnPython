# slicing
# i can access substing with slicing

mystr = "Hello World"
print('my string :',mystr)

substr = mystr[1:5] # start index - 1, stop index - 5 (stop index is excluded)
print(substr)

''' start index:stopindex:step index(optional)
    * if i dont give start index, its starts from beginning
    * if i dont give stop index, it will go all the way to end
    * [:] gives all from begining to end
    * optional step index, eg [::], default is 1 i.e [::1]
                           *[::2] takes every second char
                           *[::-1] it will reverse our string
                           *[::-2] takes every second char from last
'''

s1 = mystr[:5]
s2 = mystr[1:]
s3 = mystr[::2]
s4 = mystr[::-1]
s5 = mystr[::-2]

print(':5', s1)
print('1:', s2)
print('::2', s3)
print('::-1', s4)
print('::-2', s5)


