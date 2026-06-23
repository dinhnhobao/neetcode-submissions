class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {} # number -> index
        for i, num in enumerate(nums):
            if (target - num) in indexes: # seen
                # Return the answer with the smaller index first.
                return [indexes[target-num], i]
            # You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
            # with this assumption, we can insert the num into indexes directly without checking if it already exists in indexes
            indexes[num] = i
        return None
