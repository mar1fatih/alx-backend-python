#!/usr/bin/env python3
"""unittests file"""
import unittest
import utils
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


class TestGetJson(unittest.TestCase):
    """ TestGetJson class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch('utils.get_json')
    def test_get_json(self, url, payload, patch):
        """ test get_json method """
        patch.return_value = payload
        self.assertEqual(utils.get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """ class TestMemoize """
    def test_memoize(self):
        """ test memoize method """
        class TestClass:
            """ Testclass class"""
            def a_method(self):
                """ a_method method"""
                return 42

            @memoize
            def a_property(self):
                """a_property method"""
                return self.a_method()
        
        with patch.object(TestClass, "a_method") as pM:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            pM.assert_called_once
