class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        {2: 4, 20: 1, 4: 2, 10: 1, 3:3, 5:1}
        '''
        if not nums:
            return 0

        result = {}
        for num in nums:
            result[num] = 1 # edge case
        
        def find_consecutive(val): # i: index
            if result[val] > 1: # have checked
                return result[val]
            if (val + 1 in result):
                result[val] = 1 + find_consecutive(val+1)
                return result[val]
            else:
                return 1 # base case

        for num in result:
            result[num] = find_consecutive(num)
        return max(result.values())