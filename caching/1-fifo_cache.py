#!/usr/bin/env python3
"""
This module defines the FIFOCache class that inherits from
BaseCaching and implements a dictionary-based FIFO cache.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and implements
    a FIFO caching system with eviction when the cache is full.
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
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                first_key = next(iter(self.cache_data))  # Récupère la clé n°1
                del self.cache_data[first_key]  # Supprime l'item
                print("DISCARD: " + first_key)

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
