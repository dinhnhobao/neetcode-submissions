class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        loop invariant: nums[:read] is all non-zeros

        [1,2,0,0,0,5]
        
        [0,3,4,0,0]

        [3, 0, 4, 0, 0]
        [3,0,0,0,0]
        r  
         w
        """
        if not nums:
            return []
        # right is used to find the non-zero element to move to the front
        # left is used as a write pointer to write the non-zero element. write should always point to 0
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0: # found, should replace
               nums[left], nums[right] = nums[right], nums[left] # it's okay that nums[left] 
               left += 1
                
        