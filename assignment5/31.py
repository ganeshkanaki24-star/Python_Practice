# 31. Implement an LRU Cache with O(1) time complexity for get() and put().

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):

        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print("Get 1:", cache.get(1))

cache.put(3, 30)

print("Get 2:", cache.get(2))
print("Get 3:", cache.get(3))