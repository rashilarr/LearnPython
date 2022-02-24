# we can get a list of all elements of our first list that are not divided by 3


def main():
    seq = range(11)
    seq2 = [x for x in seq if x%3 !=0]   # if clause is used only after the for clause
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o : print(x, end =' ')
    print()

if __name__ == '__main__' : main()
