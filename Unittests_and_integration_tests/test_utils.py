#!/usr/bin/env python3
"""Test module"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for the tests of the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        # Context manager pour inspecter l'erreur levée.
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Class for the tests of the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    # Remplace requests.get par un Mock pour éviter un appel HTTP réel
    @patch("utils.requests.get")
    def test_get_json(self, test_url, expected, mock_get):
        # Définition de ce que mock doit retourner
        mock_get.return_value.json.return_value = expected
        response = get_json(test_url)
        # Vérification que requests.get a été appelé avec les bons paramètres
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, expected)
