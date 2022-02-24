# ------------------------ List Comprehension ----------------

# A list comprehension is a list created based on another list or iterator
# List comprehension is very common in python, so it is good to understand it.
# lets create a list comprehension

def main():
    seq = range(11)
    seq2 = [x*2 for x in seq]  # It will be a list of each of the elements of our first list is multiplied by 2
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o : print(x, end =' ')
    print()

if __name__ == '__main__' : main()
