
# I can also create a list of tuple

def main():
    seq = range(11)
    seq2 = [(x, x**2) for x in seq] # creating tuple with elements in seq and square of each element of seq as                                      # new sequence seq 2
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o : print(x, end = ' ')
    print()

if __name__ == '__main__' : main()

