import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Clarify k, is k 0-based or 1-based
        Use a heap to get the top k largest elements

        kth largest -> (n-k+1) minimum element
        '''
        if not nums or k > len(nums):
            return 0

        n = len(nums)
        heap = []
        heapq.heapify(heap) # Python has min heap only

        for num in nums:
            heapq.heappush(heap, num)

        element = -1
        for _ in range(n-k+1):
            element = heapq.heappop(heap)
        return element