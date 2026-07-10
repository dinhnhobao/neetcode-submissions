# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use a dummy to link to a sorted linked list
            1 -> 2  -> 7 
                c      c   l1
        d ->1 
                        
          -> 5 ->.  -> l2 
            c.   l2, null
        ''' 
        if not list1 or not list2:
            return (list1 or list2)
        dummy = ListNode(0)
        curr = dummy
        while (list1 and list2):
            if list1.val <= list2.val:
                curr.next = list1 
                curr = curr.next
                list1 = list1.next
            elif list1.val > list2.val:
                curr.next = list2 
                curr = curr.next
                list2 = list2.next
        # last link
        curr.next = (list1 or list2)
        return dummy.next

            