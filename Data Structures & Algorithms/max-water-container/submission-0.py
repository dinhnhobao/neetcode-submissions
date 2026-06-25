class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return None

        left, right = 0, len(heights) - 1
        maximum = 0
        while (left < right):
            amount = (right-left) * min(heights[left], heights[right])
            maximum = max(maximum, amount)
            if heights[left] < heights[right]:
                # move the lower bar since the current amount
                # is the highest amount of water possible with this lower bar
                left += 1
            elif heights[left] >= heights[right]: 
                # for the '=' case, we can mathematically prove that either is fine to move 
                right -= 1
        return maximum