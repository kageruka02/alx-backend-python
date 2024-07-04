#!/usr/bin/env python3

"testing utils.py"
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class for Testing Access Nested Map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, result):
        """Test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([({}, ("a",), "a"), ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, nested_map, path, error):
        """Test that a KeyError is raised for the respective inputs"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{error}')", repr(cm.exception))
