#!/usr/bin/env python3
""" Auth module
"""
import bcrypt


def _hash_password(pwd: str) -> bytes:
    """
    Hash a password with a salt using bcrypt.

    Parameters:
        pwd (str): The plain-text password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    # Hashage du MdP en convertissant pwd en bytes et en générant un salt
    return bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt())
