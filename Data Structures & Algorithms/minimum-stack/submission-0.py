class MinStack:

    def __init__(self):
        '''
        Maintains another stack that stores the current minimum element
        '''
        self.values = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.minimum: # empty
            self.minimum.append(val)
        else: # compare and insert the current minimum
            self.minimum.append(min(val, self.minimum[-1]))

    def pop(self) -> None:
        # pop, top and getMin will always be called on non-empty stacks.
        self.values.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
