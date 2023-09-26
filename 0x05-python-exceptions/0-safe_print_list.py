#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # Initialize a counter for the elements printed
    
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")  # Print the element without a newline
            count += 1
    except IndexError:  # Handle the exception when the index is out of range
        pass
    
    print()  # Print a newline to separate the printed elements from the next output
    return count  # Return the number of elements printed

# Test cases
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
