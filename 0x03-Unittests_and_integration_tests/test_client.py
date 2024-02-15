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

    def test_public_repos_url(self) -> None:
        '''Test public repos url'''
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
