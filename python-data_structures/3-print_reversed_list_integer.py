#!/usr/bin/python3


def print_reversed_list_integer(my_list=None):
    """Print all integers of a list in reverse order."""
    if my_list is None:
        return  # Exit if my_list is None

    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
