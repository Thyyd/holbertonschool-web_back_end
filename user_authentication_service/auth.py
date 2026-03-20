#!/usr/bin/env python3
""" Auth module
"""
import bcrypt
import uuid
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


# Méthode _generate_uuid
def _generate_uuid() -> str:
    """
    Generate a new UUID.

    Returns:
        str: String representation of a newly generated UUID.
    """
    return str(uuid.uuid4())


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

    # Méthode create_session
    def create_session(self, email: str) -> str:
        """
        Create a new session for the user corresponding to the given email.

        This method finds the user associated with the provided email,
        generates a new UUID as a session ID, stores it in the database,
        and returns the session ID.

        Args:
            email (str): The email address of the user.

        Returns:
            str: The generated session ID. Returns None if no user is found.
        """
        try:
            # Vérification de l'existence de l'user
            user = self._db.find_user_by(email=email)
            # Génération de la session ID
            session_id = _generate_uuid()

            # Sauvegarde dans la DB
            self._db.update_user(user.id, session_id=session_id)

            return session_id
        except NoResultFound:
            return None

    # Méthode get_user_from_session_id
    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Retrieve a User instance based on the session ID.

        Parameters:
            session_id (str): The session ID associated with the user.

        Returns:
            User: The corresponding user if found.
            None: If the session ID is None or no user is found.
        """
        if session_id is None:
            return None
        try:
            # Vérification de l'existance de l'user
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    # Méthode destroy_session
    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a user's session.

        Finds the user corresponding to the given user_id and updates
        their session_id to None in the database. If the user does not
        exist, the method silently returns None.

        Parameters:
            user_id (int): The ID of the user whose session will be destroyed.

        Returns:
            None
        """
        try:
            # Vérification de l'existance de l'user
            user = self._db.find_user_by(id=user_id)

            # Modifie sa session_id à None dans la DB
            self._db.update_user(user.id, session_id=None)

            return None
        except NoResultFound:
            return None

    # Méthode get_reset_password_token
    def get_reset_password_token(self, email: str) -> str:
        """
        Generate and store a reset token for a user.

        Parameters:
            email (str): The email of the user requesting a password reset.

        Raises:
            ValueError: If no user is found with the provided email.

        Returns:
            str: The generated reset token.
        """
        try:
            # Vérification de l'existance de l'user
            user = self._db.find_user_by(email=email)
            # Génération d'un nouveau UUID pour réinitialiser le MdP
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)

            return reset_token
        except NoResultFound:
            raise ValueError

    # Méthode update_password
    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update a user's password using a reset token.

        Parameters:
            reset_token (str): The reset token identifying the user.
            password (str): The new password to hash and store.

        Raises:
            ValueError: If no user is found with the provided reset token.

        Returns:
            None
        """
        try:
            # Vérification de l'existance de l'user
            user = self._db.find_user_by(reset_token=reset_token)
            # Hachage du password
            user_pwd = _hash_password(password)
            self._db.update_user(user.id,
                                 hashed_password=user_pwd,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
