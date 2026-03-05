#!/usr/bin/env python3
"""
Module api.v1.auth.session_auth

This module defines the SessionAuth class that extends the Auth class.
"""

from api.v1.auth.auth import Auth
import uuid
# from typing import TypeVar
# import base64
# from models.user import User


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
