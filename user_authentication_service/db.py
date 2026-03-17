#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import Any

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    # Méthode add_user
    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a new user to the database

        Parameters:
            email (str): The email linked to the user
            hashed_password (str): The hashed_password linked to the user

        Returns:
            User
        """
        # Création de l'objet User
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()  # Sauvegarde l'user dans la DB
        return user

    # Méthode find_user_by
    def find_user_by(self, **kwargs: dict[str, Any]) -> User:
        """
        Finds a user in the `users` table based on dynamic criteria.

        This method accepts one or more keyword arguments corresponding to
        columns in the `User` model and returns the **first user** that
        matches all provided criteria.

        Parameters:
            - **kwargs: dict of column_name=value pairs, where the key is a
            valid column in the `User` model and the value is what is being
            searched for.

        Raises:
            - InvalidRequestError: if a key in kwargs does not correspond
            to a valid column.
            - NoResultFound: if no user matches the provided criteria.

        Returns:
            User: the first user found that matches the criteria.
        """
        # Parcours des noms de champs passés en paramètres
        for key in kwargs:
            # Si un nom de champ n'est pas dans la DB, raise l'erreur
            if key not in User.__table__.columns:
                raise InvalidRequestError
        # Récupère les valeurs associées au champ
        query = self._session.query(User).filter_by(**kwargs)
        user = query.first()
        # S'il n'y a pas de valeur dans user, raise l'erreur
        if user is None:
            raise NoResultFound

        return user
