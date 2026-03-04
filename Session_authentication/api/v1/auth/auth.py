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
            - bool: True si le chemin donné nécessite une authentification,
            sinon False
        """
        # path vaut None
        if path is None:
            retour = True
        # excluded_paths vaut None OU est une liste vide
        elif excluded_paths is None or excluded_paths == []:
            retour = True
        else:
            # Si path ne finit pas par un "/", on le rajoute. (slash tolerant)
            if path and path[-1] != '/':
                path += '/'
            # Si path est dans excluded_path, return False, sinon True
            if path in excluded_paths:
                retour = False
            else:
                retour = True
        return retour

    # Méthode authorization_header
    def authorization_header(self, request=None) -> str:
        """
        Récupère le header d'autorisation d'une requête Flask.

        Parameters:
            - request (flask.Request, optional): Objet Flask request. Par
            défaut None.

        Returns:
            - str: None si request vaut None et si request.headers ne contient
            pas la clé "Authorization".
            Sinon, retourne le contenu du header Authorization.
        """
        # Si request vaut None ou qu'il n'y a pas de clé "Authorization"
        if request is None or request.headers.get("Authorization") is None:
            retour = None
        else:
            retour = request.headers.get("Authorization")
        return retour

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
