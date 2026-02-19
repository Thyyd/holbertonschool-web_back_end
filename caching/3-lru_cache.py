#!/usr/bin/env python3
"""
This module defines the LRUCache class that inherits from
BaseCaching and implements a dictionary-based LRU cache.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and implements
    a LRU caching system with eviction when the cache is full.
    """
    def __init__(self):
        super().__init__()
        self.order = []

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
            if key in self.cache_data:
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                oldest = self.order.pop(0)
                del self.cache_data[oldest]
                print(f"DISCARD: {oldest}")

    # Redéfinition de la méthode get
    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Returns None if the key is None or does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
