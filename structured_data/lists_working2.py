# List working
# List is mutable that means i can change it


def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    
    #game.append('Computer')
    #game.insert(0, 'Computer')
    #game.remove('Paper')
    #game.pop()

    #x = game.pop()
    #print(x)

    #game.pop(3)

    #del game[3]
    #del game[1:3]
    #del game[1:5:2]

    #print(', ' .join(game))

    print(len(game))

    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__' : main()


# i can append an item using this game.append('Computer')
# i can insert an item with index game.insert(0, 'Computer')
# i can remove an item by value game.remove('Paper')
# i can use pop to remove an item at the end of the list  game.pop()
          # pop also returns the value 
          # x = game.pop()
          # print(x)  will print the value 'Spock'

          # i can also use pop to remove an item at a particular index
          # game.pop(3)
# i can use the del statement to remove an item by index --> del game[3]
          # i can remove by slice
          # del game[1:3]
          # del game[1:5:2] will delete game[1] and game[1+2] till game[end<5]
          # removes game[1] game[3] i.e paper and lizard
# i can joint the list using the join method on the string type
# print(', ' .join(game))
# i can get a raw count of the items in the list using the len function and this is a function 
# it is not an object method
# print(len(game))
