#!/usr/bin/python3
"""
Module Base: contains the Base class for our project.
"""


class Base:
    """
    Base class that will be the foundation for other classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base object.
        Args:
            id (int): The id of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

