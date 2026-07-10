class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left, count, maximum = 0, 0, 0 # count of 1s
        for right in range(len(nums)):
            if nums[right] == 0: # can flip
                count += 1
            if (count > k):
                while (nums[left] == 1):
                    left += 1
                # nums[left] = 0 here, skip over it
                left += 1
                count -= 1
            maximum = max(maximum, right-left+1)
        return maximum