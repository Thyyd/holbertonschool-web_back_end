#!/usr/bin/env python3
""" Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


# Méthode _hash_password
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

    # Constructeur
    def __init__(self):
        self._db = DB()

    # Méthode register_user
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
            # Vérification de l'existance de l'user
            user = self._db.find_user_by(email=email)

            # S'il existe, on raise ValueError
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # L'User n'existe pas, on le créé.
            user_pwd = _hash_password(password)  # Hashage password
            user = self._db.add_user(email, user_pwd)  # Ajout user à DB

            return user

    # Méthode valid_login
    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate a user's login credentials.

        Search for a user by email and verify that the provided password
        matches the stored hashed password using bcrypt.

        Parameters:
            email (str): The email of the user attempting to log in.
            password (str): The plaintext password provided by the user.

        Returns:
            bool: True if the email exists and the password is correct,
            False otherwise.
        """
        try:
            # Vérification de l'existence de l'user
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode("utf-8"),
                                  user.hashed_password)
        # S'il n'existe pas, return False
        except NoResultFound:
            return False
