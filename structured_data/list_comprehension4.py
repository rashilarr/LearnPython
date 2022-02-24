

# I can call the functions
# i have rounded the pi to the no of places for each element in the sequence
# so pi rounded to zero, pi rounded to one, pi rounded to two, three, four, five, etc

def main():
    seq = range(11)
    from math import pi
    seq2 = [round(pi,i) for i in seq]
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o : print(x, end = ' ')
    print()

if __name__ == '__main__' : main()
