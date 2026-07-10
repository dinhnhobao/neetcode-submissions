# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        0 <- 1  2
            s  f
        '''
        if not head:
            return None

        slow, fast = None, head # note the initialisation (head node usually have edge cases)
        while fast:
            fast.next, fast, slow = slow, fast.next, fast
        return slow