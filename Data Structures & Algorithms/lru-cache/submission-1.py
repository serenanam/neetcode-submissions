class LRUCache:
    class Node:
        def __init__(self, val, key):
            self.prev = None
            self.next = None
            self.val = val
            self.key = key

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.cache = {}
        self.header = self.Node(0, 0)
        self.trailer = self.Node(0, 0)

        self.header.next = self.trailer
        self.trailer.prev = self.header
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
                
            prev = node.prev
            nxt = node.next

            prev.next = nxt
            nxt.prev = prev

            prev = self.trailer.prev
            prev.next = node
            node.prev = prev

            self.trailer.prev = node
            node.next = self.trailer

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            
            prev = node.prev
            nxt = node.next

            prev.next = nxt
            nxt.prev = prev

            prev = self.trailer.prev
            prev.next = node
            node.prev = prev

            self.trailer.prev = node
            node.next = self.trailer
            
        else:
            if self.size == self.cap:
                node = self.header.next
                nxt = node.next
                self.header.next = nxt
                nxt.prev = self.header
                del self.cache[node.key]
                self.size -= 1

            
            node = self.Node(value, key)
            self.trailer.prev.next = node
            node.prev = self.trailer.prev
            node.next = self.trailer
            self.trailer.prev = node
            self.cache[key] = node
            self.size+= 1

        
            

