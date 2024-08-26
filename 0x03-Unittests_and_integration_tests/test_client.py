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

    def test_public_repos_url(self):
        """ testing GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mk:
            mk.return_value = {"repos_url": "known payload"}
            known_p = "known payload"
            _client = GithubOrgClient(known_p)
            _return = _client._public_repos_url
            self.assertEqual(_return, known_p)
            mk.assert_called_once
