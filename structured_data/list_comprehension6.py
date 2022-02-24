

# you may also create a set 
# so when i run this code there is just four letters there that are not p or d in superduper
# so list comprehension is powerful technique for creating lists and other collections

def main():
    seq = range(11)
    from math import pi
    seq2 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o : print(x, end = ' ')
    print()

if __name__ == '__main__' : main()
