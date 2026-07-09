from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Sliding window works? --> NO! since there are negative numbers, there is no loop invariant to expand or collapse the window

        Prefix sum works:

        {0: 1, 2: 2, 1:1, 4:1} 

        total 2
        count = 4

        '''
        if not nums:
            return 0
        prefix = defaultdict(int)
        prefix[0] = 1

        total = 0 # running sum
        count = 0
        for num in nums:
            total += num
            count += prefix[total-k]
            prefix[total] += 1
        return count




