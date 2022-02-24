# while loops 
# while loops uses a conditional expression to control the loop

# Three Aditional controls : continue, break and else

password = "secret"
pw = ''

auth = False
count =0
max_attempt = 5

while pw != "secret":
    count +=1
    if count > max_attempt: break   # the loop will break,if condition is true
     
    if count == 3: continue

    pw = input(f'{count}:what is the password?')
else:              
    auth = True      # else is executed only when while condition is true

print('Authorise' if auth else 'Calling the FBI..')  #Ternary operator


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
