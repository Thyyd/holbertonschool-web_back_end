#!/usr/bin/env python3
"""
This module defines the hash_password function that will crypt
a string so that passwords don't get stored in plain text
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password with a salt using bcrypt.

    Parameters:
        password (str): The plain-text password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    # Conversion de password en octets
    password_in_bytes = password.encode("utf-8")

    # Génération d'un salt unique aléatoire
    salt = bcrypt.gensalt()

    # Hashage du mot de passe combiné au salt
    hashed = bcrypt.hashpw(password_in_bytes, salt)

    return hashed
