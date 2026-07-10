import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <= 1:
            return int(tokens[0])
        stack = []
        for token in tokens:
            if token in "+-*/": # this is an operator
                first, second = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(second + first)
                elif token == '-':
                    stack.append(second - first) # note the reverse order
                elif token == "*":
                    stack.append(second * first)
                elif token == '/':
                    # division truncates (rounds down) towards 0 -> use int
                    stack.append(int(second / first))
            else: # this is an operand
                stack.append(int(token))
        # there is one value left in the stack which is the result
        return stack.pop()