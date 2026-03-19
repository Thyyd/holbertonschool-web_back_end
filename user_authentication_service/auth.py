#!/usr/bin/env python3
""" Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hash a password with a salt using bcrypt.

    Parameters:
        password (str): The plain-text password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    # Hashage du MdP en convertissant password en bytes et en générant un salt
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the provided email and password.

        Parameters:
            email (str): email of the user to register
            password (str): plain text password to hash and store

        Raises:
            ValueError: If a user with the given email already exists

        Returns:
            User: the created user object
        """
        try:
            # Vérification si l'user existe
            user = self._db.find_user_by(email=email)

            # S'il existe, on raise ValueError
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # L'User n'existe pas, on le créé.
            user_pwd = _hash_password(password)  # Hashage password
            user = self._db.add_user(email, user_pwd)  # Ajout user à DB

            return user
