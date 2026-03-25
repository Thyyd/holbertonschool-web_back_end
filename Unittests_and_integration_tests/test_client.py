#!/usr/bin/env python3
"""Test module"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for the tests of the methods of the GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    # Remplace requests.get par un Mock pour éviter un appel HTTP réel
    @patch("client.get_json")
    def test_org(self, org, mock_payload, mock_get_json):
        """
        Unit Test to check if GithubOrgClient.org returns correct value
        """
        # Définition de ce que mock doit retourner
        mock_get_json.return_value = mock_payload

        client = GithubOrgClient(org)
        self.assertEqual(client.org, mock_payload)
        # Vérification que requests.get a été appelé avec les bons paramètres
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )
