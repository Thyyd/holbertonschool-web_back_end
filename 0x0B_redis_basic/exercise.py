#!/usr/bin/env python3
"""
Basic Redis Module
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Class Cache for the DB
    """
    def __init__(self):
        """
        Constructor of the class.
        It initialize a Redis client before flushing it.
        """
        # Initialisation du client Redis
        self._redis = redis.Redis()
        # Vide la DB
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store a value in Redis using a random key.

        Parameters:
            data: Data to store in Redis. Can be str, bytes, int or float.

        Returns:
            str: The generated key used to store the data.
        """
        # génération d'une key random
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
