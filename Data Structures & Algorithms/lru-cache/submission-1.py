class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # maps key to nodes 

        # left - least recently used, right - most recently used
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right # connect to each other
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            # move to most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
    # node to remove node from linked list
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert new node at the rightmost end
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev



    
