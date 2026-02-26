#!/usr/bin/env python3
"""
Module api.v1.auth.auth

This module contains the class Auth that will manage the authentification to
the API
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Classe de gestion de l'authentification pour l'API.

    Cette classe fournit des méthodes pour :
        - déterminer si un chemin nécessite une authentification,
        - récupérer le header d'autorisation,
        - récupérer l'utilisateur courant à partir d'une requête Flask.
    """

    # Méthode __init__
    def __init__(self):
        """
        Méthode d'initialisation de l'objet Auth
        """
        pass

    # Méthode require_path
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Détermine si un chemin donné nécessite une authentification.

        Parameters:
            - path (str): Le chemin de la requête HTTP à vérifier.
            - excluded_paths (List[str]): Liste des chemins exclus de
            l'authentification.

        Returns:
            - bool: False pour l'instant. Dans le futur, True si le chemin
            nécessite une auth.
        """
        return False

    # Méthode authorization_header
    def authorization_header(self, request=None) -> str:
        """
        Récupère le header d'autorisation d'une requête Flask.

        Parameters:
            - request (flask.Request, optional): Objet Flask request. Par
            défaut None.

        Returns:
            - str: None pour l'instant. Devrait retourner le contenu du header
            Authorization.
        """
        pass

    # Méthode current_user
    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retourne l'utilisateur courant basé sur la requête.

        Parameters:
            - request (flask.Request, optional): Objet Flask request. Par
            défaut None.

        Returns:
            - User: None pour l'instant. Devrait retourner un objet
            représentant l'utilisateur connecté.
        """
        pass
