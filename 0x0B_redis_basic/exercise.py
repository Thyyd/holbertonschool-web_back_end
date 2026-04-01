#!/usr/bin/env python3
"""
Basic Redis Module
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


# Count_calls declarator
def count_calls(method: Callable) -> Callable:
    """
    Decorator that increments a Redis counter each time the method is called.

    Parameters:
        method: The method to be decorated

    Returns:
        Callable: The wrapped method that increments a counter
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Increment the call count in Redis and execute the original method.

        Parameters:
            self: The instance of the class
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            The return value of the original method
        """
        # Création de la clé Redis qui agira comme un compteur
        key = method.__qualname__
        # Incrémente la valeur d'une clé de 1
        self._redis.incr(key)
        # Exécution de la méthode.
        return method(self, *args, **kwargs)
    return wrapper


# Fonction call_history
def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs
    for a method in Redis lists.

    Parameters:
        method: The method to be decorated

    Returns:
        Callable: The wrapped method that increments a counter
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Store the method's input arguments and output in Redis.

        Parameters:
            self: The instance of the class
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            The return value of the original method
        """
        # Création des clés inputs et outputs
        inputs_key = method.__qualname__ + ":inputs"
        outputs_key = method.__qualname__ + ":outputs"

        # Ajout des arguments de la fonction dans inputs_key
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        # Ajout du résultat de la fonction dans outputs_key
        self._redis.rpush(outputs_key, result)

        return result
    return wrapper


class Cache:
    """
    Class Cache for the DB
    """
    # Constructeur
    def __init__(self):
        """
        Constructor of the class.
        It initialize a Redis client before flushing it.
        """
        # Initialisation du client Redis
        self._redis = redis.Redis()
        # Vide la DB
        self._redis.flushdb()

    # Méthode store
    @count_calls
    @call_history
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

    # Getter
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
        """
        Retrieve a value from Redis by key.
        Optionally apply a conversion function `fn` to the result.
        Returns None if key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        else:
            return data

    # Méthode get_int
    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve a value from Redis and convert it to int.
        Returns None if key does not exist.
        """
        return self.get(key, int)

    # Méthode get_str
    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a value from Redis and convert it to UTF-8 string.
        Returns None if key does not exist.
        """
        return self.get(key, lambda d: d.decode("utf-8"))
