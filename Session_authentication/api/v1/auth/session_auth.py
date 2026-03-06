#!/usr/bin/env python3
"""
Module api.v1.auth.session_auth

This module defines the SessionAuth class that extends the Auth class.
"""

from api.v1.auth.auth import Auth
import uuid
from typing import TypeVar
# import base64
from models.user import User


class SessionAuth(Auth):
    """
    SessionAuth class that implements Basic HTTP authentication.
    """
    user_id_by_session_id = {}

    # Méthode create_session
    def create_session(self, user_id: str = None) -> str:
        """
        Create a new session for a given user_id

        Parameters:
            user_id (str): The user identifier

        Returns:
            str: The generated session ID
            None: If user_id is None or not a string
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())  # Création d'un session_id random
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    # Méthode user_id_for_session_id
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the User ID associated with a given Session ID.

        Parameters:
            session_id (str): The session ID.

        Returns:
            str: The corresponding User ID if found, otherwise None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)  # récup user_id
        return user_id

    # Méthode current_user
    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return the User instance based on the session cookie.

        Retrieves the session ID from the request cookie using session_cookie(),
        then finds the corresponding user ID using user_id_for_session_id().
        Finally returns the User instance associated with that user ID.

        Parameters:
            request: Flask request object.

        Returns:
            User instance if a valid session exists, otherwise None.
        """
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return None
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return None
        user = User.get(user_id)
        return user
