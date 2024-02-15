#!/usr/bin/env python3
'''Test client file'''
import unittest
from parameterized import parameterized, parameterized_class
from typing import Dict
from requests import HTTPError
from fixtures import TEST_PAYLOAD
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from client import (
    GithubOrgClient
)


class TestGithubOrgClient(unittest.TestCase):
    '''Test Github client methods'''
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, res: Dict, mockedFun: MagicMock) -> None:
        '''Test org method'''
        mockedFun.return_value = MagicMock(return_value=res)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), res)
        mockedFun.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
