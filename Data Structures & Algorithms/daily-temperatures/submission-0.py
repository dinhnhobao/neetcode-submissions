class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        stack = [(5, 40), (6, 28)
        result = [1,4,1,2,1,0,0]
        '''
        if len(temperatures) <= 1:
            return [0]
        result = [0 for i in range(len(temperatures))]
        stack = [] # decreasing values
        for i, num in enumerate(temperatures):
            # if not stack or num <= stack[-1][1]:
            #     stack.push((i, num)) # decreasing value
            # elif num > stack[-1][1]: # find the warmer day for all temperatures in the stack
            while (stack and num > stack[-1][1]):  # found the warmer day for all temperatures in the stack
                index, _ = stack.pop() # find the next warmer temperature for index
                result[index] = i - index
            stack.append((i, num))
        return result
                    

