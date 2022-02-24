# ---------------- Lists and tuples -------------

def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    i = game.index('Paper')
    print(game[i])
    print(game[1])   
    print(game[1:3])
    print(game[1:5:2])
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__' : main()


# i can access individual item in the list using an index
# print(game[1])
# list are zero based, item no 0 will be rock and item 1 will be paper

# print(game[1:3]) first number is begining of the slice and second no is end of the slice non-inclusive

# just like range, i can use the begining, the end and the step
# [begining:end:step]#
# print(game[1:5:2])

# i can search a list using the index method
# i = game.index('Paper') 
# It will search the paper and return the index to i
# print(game[i]) will print paper

