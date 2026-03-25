#!/usr/bin/env python3
"""Test module"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
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
        """
        Unit Test for the function access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Unit Test to check if the Error is raised correctly
        in the function access_nested_map
        """
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
        """Unit Test for the function get_json"""
        # Définition de ce que mock doit retourner
        mock_get.return_value.json.return_value = expected
        response = get_json(test_url)
        # Vérification que requests.get a été appelé avec les bons paramètres
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, expected)


class TestMemoize(unittest.TestCase):
    """
    Class for the tests of the memoize function
    """
    def test_memoize(self):
        """
        Unit Test for the function memoize
        """
        class TestClass:
            """
            Class TestClass
            """
            def a_method(self):
                """
                Method that returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                Method that calls a_method
                """
                return self.a_method()

        # Objet à tester avec unittest.mock.patch
        obj = TestClass()
        # Création du Mock pour la méthode a_method
        with patch.object(TestClass, "a_method") as mock_method:
            self.assertEqual(obj.a_property(), 42)
            self.assertEqual(obj.a_property(), 42)
            mock_method.assert_called_once()
