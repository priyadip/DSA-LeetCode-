# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Remove from current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # Move to MRU position
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            # Remove old node
            node.prev.next = node.next
            node.next.prev = node.prev

        node = Node(key, value)
        self.cache[key] = node

        # Insert at MRU position
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        # Remove LRU if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.left.next = lru.next
            lru.next.prev = self.left

            del self.cache[lru.key]