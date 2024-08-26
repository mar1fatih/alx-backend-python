#!/usr/bin/env python3
"""unittests file"""
import unittest
import utils
from unittest.mock import patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test cases for a nested map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_nested_map(self, nested_map, path, result):
        """test cases for a nested map"""
        self.assertEqual(utils.access_nested_map(nested_map, path), result)
