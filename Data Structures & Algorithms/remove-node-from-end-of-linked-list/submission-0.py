# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Fast and slow pointers
        1 2 3 4
              f
          s

        Edge case for head and tail:
        0 -> 5
             f
        
        s

        0 -> 1   2
                 f
        s
        '''
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for i in range(n):
            fast = fast.next
        while (fast.next):
            fast = fast.next
            slow = slow.next
        # remove the node after slow
        slow.next = slow.next.next
        return dummy.next # <-- note the edge case for head