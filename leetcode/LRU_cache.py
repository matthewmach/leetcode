"""
Solution:
- Idea: keep dict of key value pairs
    - list of keys and last use time
- double linked list
    - can remove elements in O(1) time by dereferencing it
    - can change elements in O(1) time and move to the back with a hash map
        - get node from hash, dereference, move to front
    
    - get = delete, add, get value from hashmap
    - put = delete if exists, add, delete head if length too big
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.hashmap = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        self.delete(self.hashmap[key])
        self.add(self.hashmap[key])
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            old = self.hashmap[key]
            self.delete(old)
        
        node = Node(key,value)
        self.hashmap[key] = node
        self.add(node)

        if len(self.hashmap) > self.size:
            to_delete = self.head.next
            self.delete(to_delete)
            del self.hashmap[to_delete.key]

    def delete(self, to_delete):
        to_delete.prev.next = to_delete.next
        to_delete.next.prev = to_delete.prev

    def add(self, to_add):
        cur_tail = self.tail.prev
        cur_tail.next = to_add
        to_add.prev = cur_tail
        to_add.next = self.tail
        self.tail.prev = to_add

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)