#!/usr/bin/env python3
"""unittests file"""
import unittest
from utils import *
from unittest.mock import patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test cases for a nested map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, result):
        """test cases for a nested map"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test raise exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
