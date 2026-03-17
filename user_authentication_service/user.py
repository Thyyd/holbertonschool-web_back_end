#!/usr/bin/env python3
"""
Module that creates a SQLAlchemy model named User for a database
table named users
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the users table.

    Represents a user stored in the database and contains
    authentication-related fields.

    Attributes:
        id (int): Primary key of the user.
        email (str): User email address (not nullable).
        hashed_password (str): Hashed password of the user (not nullable).
        session_id (str): Session identifier for the user.
        reset_token (str): Token used for password reset.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
