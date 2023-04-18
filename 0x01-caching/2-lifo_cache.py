#!/usr/bin/env python3
"""LIFO Caching"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO way of retrieving append cache"""
    def __init__(self):
        """Initialize a class instance"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ add cache dictionary items"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ return cahce based on the key"""
        return self.cache_data.get(key, None)
