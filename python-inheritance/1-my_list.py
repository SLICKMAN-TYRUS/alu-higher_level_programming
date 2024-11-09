#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """A custom list class that inherits from the built-in list.

    Methods:
        print_sorted: Prints the list in ascending order.
    """

    def print_sorted(self):
        """Prints the list in ascending order.

        The elements are sorted without modifying the original list.
        """
        print(sorted(self))
