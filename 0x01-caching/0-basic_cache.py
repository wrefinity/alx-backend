#!/usr/bin/env python3
'''Basic dictionary'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''The BasicCache class inherits from BaseCaching
    '''

    def put(self, key, item):
        '''attach cahes to dictionary
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''return the cache data for the input key
        '''

        return self.cache_data.get(key, None)
