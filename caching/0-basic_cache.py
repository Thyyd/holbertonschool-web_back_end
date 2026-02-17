#!/usr/bin/python3
"""
BasicCache Module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Docstring for BasicCache
    """
    def __init__(self):
        super().__init__()

    # Redéfinition de la méthode put
    def put(self, key, item):
        if key is None or item is None:
            return  # Arrête la fonction en ne faisant rien
        else:
            self.cache_data[key] = item

    # Redéfinition de la méthode get
    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
