# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        result = [0]

        1 2 3
        9 9 9 1
              l1

        r=1
        [0] -> [2] -> [3] ->

        The start and end of linked list have tricky edge cases
        '''
        result = ListNode(0)
        curr, prev = result, None
        remainder = 0
        while l1 or l2:
            l1_val, l2_val = l1.val if l1 else 0, l2.val if l2 else 0
            total = l1_val + l2_val + remainder
            curr.val, remainder = total % 10, total // 10
            curr.next = ListNode(0)
            curr, prev = curr.next, curr
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        # l1 or l2 might have remainder
        if remainder > 0:
            curr.val = remainder
        else: # remove the extra node
            prev.next = None
        return result