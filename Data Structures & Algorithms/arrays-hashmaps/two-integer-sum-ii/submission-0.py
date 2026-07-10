class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return None
        left, right = 0, len(nums) - 1 # guaranteed to be different
        while left < right:
            current = nums[left] + nums[right]
            if current > target: # the right value is too big
                right -= 1
            elif current < target: # the left value is too small
                left += 1
            elif current == target: # found
                return [left+1, right+1]
        
        return None # not found
