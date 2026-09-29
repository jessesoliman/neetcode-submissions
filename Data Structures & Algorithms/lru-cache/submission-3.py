class Node:

    def __init__(self, key=None, val=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.last_access = Node(0, 0) # basically head of the list -> dummy?
        self.recent_access = Node(0, 0, self.last_access) # end of the list

    def get(self, key: int) -> int:
        # print(self.cache.keys(), self.recent_access.prev.key, key)
        if key in self.cache:
            r_node = self.remove_node(self.cache[key])
            self.insert_node(r_node)
            # print(self.cache.keys(), self.recent_access.prev.key, key, 'ok')
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            r_node = self.remove_node(self.cache[key])
            self.insert_node(r_node)
            return
        l_node = Node(key, value)
        # print(l_node.key, l_node.val, l_node.prev, l_node.next)
        if len(self.cache) == self.capacity:
            del self.cache[self.last_access.next.key]
            self.remove_node(self.last_access.next)
        self.cache[key] = l_node
        self.insert_node(l_node)

    def insert_node(self, node):
        node.prev = self.recent_access.prev
        node.next = self.recent_access
        node.prev.next = node
        node.next.prev = node

    def remove_node(self, node):
        r_node = node # hold node in case we want to do something with it
        node.prev.next = node.next # point prev and next to each other 
        node.next.prev = node.prev # point next and prev to each other
        r_node.prev, r_node.next = None, None # remove pointers
        return r_node