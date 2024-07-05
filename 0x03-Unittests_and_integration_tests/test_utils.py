#!/usr/bin/env python3

"testing utils.py"
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize
import requests
import unittest


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


class TestGetJson(unittest.TestCase):
    """Class for Testing Get Json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """Test that utils.get_json returns the expected result."""
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Class for Testing Memoize"""

    def test_memoize(self):
        """Test that when calling a_property twice, the correct result
        is returned but a_method is only called once using
        assert_called_once
        """

        class TestClass:
            """Test Class for wrapping with memoize"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
