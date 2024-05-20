class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map key to node

        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # remove node from double linked lisk
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    # insert the node right after head, mark it as most recent
    def _insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # update node to the most recent
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


# Example usage:
# lru = LRUCache(2)
# lru.put(1, 1)
# lru.put(2, 2)
# print(lru.get(1))  # returns 1
# lru.put(3, 3)      # evicts key 2
# print(lru.get(2))  # returns -1 (not found)
# lru.put(4, 4)      # evicts key 1
# print(lru.get(1))  # returns -1 (not found)
# print(lru.get(3))  # returns 3
# print(lru.get(4))  # returns 4
