#!/usr/bin/env python3
"""
This module defines the BasicCache class that inherits from
BaseCaching and implements a simple dictionary-based cache.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and
    implements a simple caching system without eviction policy.
    """
    def __init__(self):
        super().__init__()

    # Redéfinition de la méthode put
    def put(self, key, item):
        """
        Add an item to the cache.

        If key or item is None, the method does nothing.
        Otherwise, it stores the item in the cache dictionary.
        """
        if key is None or item is None:
            return  # Arrête la fonction en ne faisant rien
        else:
            self.cache_data[key] = item

    # Redéfinition de la méthode get
    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Returns None if the key is None or does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
