#!/usr/bin/python3
"""
Unit tests for the Base class.
"""
import unittest
from python_almost_a_circle.Base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_assignment(self):
        """
        Test that the id is correctly assigned.
        """
        b1 = Base()
        b2 = Base(100)
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 2)

    def test_auto_increment(self):
        """
        Test that ids are auto-incremented correctly.
        """
        Base._Base__nb_objects = 0  # Reset counter for testing
        b1 = Base()
        b2 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)


if __name__ == "__main__":
    unittest.main()

