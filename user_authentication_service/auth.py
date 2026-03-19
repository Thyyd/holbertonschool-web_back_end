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
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            user_pwd = _hash_password(password)
            user = self._db.add_user(email, user_pwd)

            return user
