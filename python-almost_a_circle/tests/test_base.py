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

    def test_id_auto_assign(self):
        """
        Test that ID is assigned automatically.
        """
        Base._Base__nb_objects = 0  # Reset for testing
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_passed(self):
        """
        Test that the passed ID is correctly set.
        """
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """
        Test Base.to_json_string with None.
        """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """
        Test Base.to_json_string with an empty list.
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """
        Test Base.to_json_string with a valid list.
        """
        data = [{"id": 12}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"id": 12}]')
        self.assertIsInstance(json_str, str)

    def test_from_json_string_none(self):
        """
        Test Base.from_json_string with None.
        """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """
        Test Base.from_json_string with an empty JSON string.
        """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """
        Test Base.from_json_string with a valid JSON string.
        """
        data = '[{"id": 89}]'
        result = Base.from_json_string(data)
        self.assertEqual(result, [{"id": 89}])
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()

