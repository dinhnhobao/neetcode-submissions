class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: # no solution
            return []
        # based on TwoSum -> needs to sort the array first
        nums = sorted(nums)
        result = set()
        for i in range(0, len(nums) - 2, 1):
            j, k = i+1, len(nums) - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if current > 0: # nums[k] is too big
                    k -= 1
                elif current < 0: # nums[j] is too small
                    j += 1
                elif current == 0: # found! -> store the values
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
        
        return list(result)
