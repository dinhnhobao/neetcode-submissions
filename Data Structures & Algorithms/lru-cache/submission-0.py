class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        '''
        HashMap for key->value pairs with double linked list for LRU logic
        '''
        self.capacity = capacity
        self.mapping = {} # key -> node, **important

        # left: LRU, right: MRU
        self.left, self.right = ListNode(-1, -1), ListNode(-1, -1)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node): # insert at the end
        prev, nxt = self.right.prev, self.right
        prev.next = self.right.prev = node
        node.prev, node.next = prev, nxt

    def remove(self, node): # remove at anywhere in the linked list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.mapping:
            node = self.mapping[key]
            self.remove(node) # remove at the middle
            self.insert(node) # insert at the end
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
        self.mapping[key] = ListNode(key, value)
        self.insert(self.mapping[key])
        if len(self.mapping) > self.capacity: # need to remove
            node = self.left.next
            self.remove(node)
            del self.mapping[node.key]
        
