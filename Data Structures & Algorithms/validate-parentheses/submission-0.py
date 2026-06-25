class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        matching = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or char != matching[stack[-1]]: # empty stack or no matching open bracket
                    return False
                # for matching brackets, pop from the stack
                stack.pop() 
        return not stack # a valid string should have empty stack by now