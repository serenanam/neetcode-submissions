class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
        
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.header = self.Node(0, 0)
        self.trailer = self.Node(0, 0)
        self.header.next, self.trailer.prev = self.trailer, self.header

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
        else:
            node = self.Node(key, value)
            if len(self.cache) == self.cap:
                oldNode = self.trailer.prev
                self.remove(oldNode)
                del self.cache[oldNode.key]
        self.insert(node)
        self.cache[key] = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        nxt = self.header.next
        node.prev, node.next = self.header, nxt
        self.header.next, nxt.prev = node, node
    
