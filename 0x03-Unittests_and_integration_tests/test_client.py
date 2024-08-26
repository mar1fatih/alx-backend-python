#!/usr/bin/env python3
""" module to test client """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient class"""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, return_v, patch):
        """ test that GithubOrgClient.org returns the correct value."""
        patch.return_value = return_v
        org_client = GithubOrgClient(org_name)
        _return = org_client.org
        self.assertEqual(_return, patch.return_value)
        patch.assert_called_once
