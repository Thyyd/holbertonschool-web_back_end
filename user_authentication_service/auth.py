#!/usr/bin/env python3
""" Auth module
"""
import bcrypt


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
