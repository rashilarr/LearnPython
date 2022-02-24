

# I can also create a dictionary
# we have the key, which is the original element for our sequence and its square.

def main():
    seq = range(11)
    seq2 = { x:x**2 for x in seq}
    print_list(seq)
    print(seq2)

def print_list(o):
    for x in o : print(x, end = ' ')
    print()

if __name__ == '__main__' : main()
