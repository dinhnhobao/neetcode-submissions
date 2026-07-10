class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = [1] + nums + [1]
        dp = {}
        def dfs(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            maximum = 0
            for k in range(i, j+1):
                coins = nums[k] * nums[i-1] * nums[j+1] # pop at balloon k last
                coins += dfs(i, k-1) + dfs(k+1, j)
                maximum = max(maximum, coins)
            dp[(i, j)] = maximum
            return maximum

        return dfs(1, len(nums) - 1 - 1) # between the original numbers
