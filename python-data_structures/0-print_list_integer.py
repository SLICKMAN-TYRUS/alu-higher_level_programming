#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list, one integer per line."""
    for integer in my_list:
        if type(integer) is not int:  # Check for non-integer types
            raise TypeError("list must contain only integers")
        print("{}".format(integer))


if __name__ == "__main__":
    # Test cases to demonstrate functionality
    print_list_integer([1, 2, 3])  # Expected output: 1\n2\n3
    print_list_integer([1])         # Expected output: 1
    print_list_integer([])          # Expected output: (nothing printed)
    try:
        print_list_integer([1, 2, "H", 9])  # Should raise an exception
    except TypeError as e:
        print(e)  # Expected output: list must contain only integers

