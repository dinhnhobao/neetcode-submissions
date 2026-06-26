# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next # note the starting point
        while fast and fast.next: # fast can still traverse
            slow = slow.next
            fast = fast.next.next
            if fast == slow: # found
                return True
        return False # fast has traversed to the end of the linked list -> no cycles