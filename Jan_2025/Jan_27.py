from collections import OrderedDict
class LRUCache:
    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.capacity = cap
        self.cache = OrderedDict()
    # Function to return value corresponding to the key.
    def get(self, key):
        if key in self.cache:
            # Move the accessed item to the end to indicate recent use
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    # Function for storing key-value pair.
    def put(self, key, value):
        if key in self.cache:
            # Remove the existing key to update its value
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove the least recently used item (first item)
            self.cache.popitem(last=False)
