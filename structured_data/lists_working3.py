
# Tuple is exactly like the list except that its immutable and it's indicated by paranthese ( )

def main():
    game = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
       
    print(game[1])
    
    #game.append('Computer')

    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__' : main()

# if i try to append, i will get an error that says tuple object has no attribute append 
# because tuples are immutable and they cannot be changed 
# game.append('Computer')
# Attribute error

# List and tuples are the fundamental sequence type in Python
# The List type is mutable and the Tuple is not.
