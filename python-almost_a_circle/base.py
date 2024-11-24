#!/usr/bin/python3
"""
Base class module for managing ID and JSON serialization.
"""

import json


class Base:
    """
    Base class for all other classes in the project.
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string back to a list of dictionaries.
        Args:
            json_string (str): JSON string to convert.
        Returns:
            list: A list of dictionaries.
        """
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

