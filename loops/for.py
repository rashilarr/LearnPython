# for loops
# for loops uses a sequence like an iterator list,tuple or other sequence obj  # to control the loop

stu = ('akshara','venba','saathvik','pratheik','ishaan')

for students in stu:
    print(students)

for i in range(5):   #you can use other sequence in for loop
    print(i)         # for loop is widely used more than while loop

# Additional controls : continue, break and else
# continue : 
    # The continue clause is used to shortcut a loop 
    # and start it again as if it had reached the end of its body of the code

# break :
    # The break clause is used to break out of a loop prematurely
    # execution will continue after the entire loop structure and the else control is not common in other language

# else :
    # The else block executes only if the loop ends normally
    # it will not execute if a break is used to end the loop
# These controls are available for both while and for loop
    

print('additional controls: using continue,break,else')
for students in stu:
    if students == 'saathvik': continue
#    if students == 'ishaan': break      # uncomment this line for break execution
    print(students)
else:                                   
    print('that is all of the students')  
