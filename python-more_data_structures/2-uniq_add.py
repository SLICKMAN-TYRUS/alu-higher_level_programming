#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_numbers = set(my_list)  # Create a set to keep only unique numbers
    return sum(unique_numbers)      # Return the sum of the unique numbers
