class LRUCache:
    class Node:
        def __init__(self, val, key):
            self.prev = None
            self.next = None
            self.val = val
            self.key = key

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.header = self.Node(0, 0)
        self.trailer = self.Node(0, 0)

        self.header.next = self.trailer
        self.trailer.prev = self.header
        

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
            node.val = value
            
            self.remove(node)
            self.insert(node)
            
        else:
            if len(self.cache) == self.cap:
                node = self.header.next
                self.remove(node)
                del self.cache[node.key]
            
            node = self.Node(value, key)
            self.insert(node)
            self.cache[key] = node
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev = self.trailer.prev
        prev.next = node
        node.prev = prev

        node.next = self.trailer
        self.trailer.prev = node
    


