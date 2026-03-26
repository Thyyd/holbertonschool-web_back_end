#!/usr/bin/env python3
"""Test module"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


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

    def test_public_repos_url(self):
        """
        Unit Test for the method _public_repos_url
        """
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        # Création du mock pour qu'il fonctionne pour des property
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            # Définition de ce que mock doit retourner
            mock_org.return_value = payload
            # Création du client et appel de la property
            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Unit Test for the method public_repos
        """
        payload = {"name": "repo1"}, {"name": "repo2"}
        # Définition de ce que mock_get_json doit retourner
        mock_get_json.return_value = payload

        # Création du mock pour qu'il fonctionne pour des property
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_url:
            # Définition de ce que mock_url doit retourner
            mock_url.return_value = "https://api.github.com/orgs/test/repos"
            # Création du client et appel de la property
            client = GithubOrgClient("test")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])

            # Vérification que les mocks aient bien été appelés
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Unit Test for the method has_license
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
