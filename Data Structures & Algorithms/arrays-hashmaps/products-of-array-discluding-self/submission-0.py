class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix = [1, 2, 8, 48]
        postfix = [48, 48, 24, 6]
        output = [48, 24, 12, 8]
        '''
        if not nums:
            return None
        # product of array except self = left product * right product
        prefix = [0 for i in range(len(nums))]
        for i in range(len(prefix)):
            prefix[i] = nums[i] * (prefix[i-1] if i >= 1 else 1)
        
        postfix = [0 for i in range(len(nums))]
        for i in range(len(postfix) - 1, -1, -1):
            postfix[i] = nums[i] * (postfix[i+1] if i+1 < len(postfix) else 1)

        output = [0 for i in range(len(nums))]
        for i in range(len(output)):
            prefix_product = prefix[i-1] if i >= 1 else 1
            postfix_product = postfix[i+1] if i+1 < len(postfix) else 1
            output[i] = prefix_product * postfix_product
        
        return output