#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list, one integer per line."""
    for integer in my_list:
        # Using str.format() to print the integer
        print("{}".format(integer))

# Example usage
if __name__ == "__main__":
    print_list_integer([1, 2, 3, 4])  # This will print each integer on a new line

