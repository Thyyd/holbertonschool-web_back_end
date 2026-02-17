#!/usr/bin/env python3
"""
This module defines the LIFOCache class that inherits from
BaseCaching and implements a dictionary-based LIFO cache.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements
    a LIFO caching system with eviction when the cache is full.
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
            if (len(self.cache_data) < BaseCaching.MAX_ITEMS):
                self.cache_data[key] = item  # Ajout de l'item
            else:
                # Récupération de la dernière clé
                last_key = next(reversed(self.cache_data))
                self.cache_data[key] = item  # Ajout de l'item
                if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                    del self.cache_data[last_key]  # Supprime l'item
                    print("DISCARD: " + last_key)

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
