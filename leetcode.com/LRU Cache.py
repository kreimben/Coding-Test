"""
https://leetcode.com/problems/lru-cache/
LRU Cache
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.keys = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.keys.remove(key)
        elif len(self.keys) == self.capacity:
            del self.cache[self.keys.pop(0)]
        self.cache[key] = value
        self.keys.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


i = ["LRUCache", "put", "put", "put", "put", "get", "get", "get", "get", "put", "get", "get", "get", "get", "get"]
v = [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]]
s = None
expected = [None, None, None, None, None, 4, 3, 2, -1, None, -1, 2, 3, -1, 5]
actualll = [None, None, None, None, None, 4, 3, -1, -1, None, -1, -1, 3, -1, 5]

for command, value, result in list(zip(i, v, expected)):
    if command == 'LRUCache':
        s = LRUCache(value[0])
    elif command == 'put':
        s.put(*value)
    elif command == 'get':
        actual = s.get(value[0])
        assert actual == result
