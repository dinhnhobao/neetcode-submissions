from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
'''
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
        (n1, 1)

         (n1, 1)

        (n6, 11)


        


        
        '''
        if not root:
            return 0
        
        queue = deque()
        total = 0
        queue.append((root, 0)) # current value so far, not counting this node
        while queue:
            node, value = queue.popleft()
            next_value = value * 10 + node.val
            if node.left:
                queue.append((node.left, next_value))
            if node.right:
                queue.append((node.right, next_value))
            if (not node.left) and (not node.right): # leaf
                total += next_value
        return total