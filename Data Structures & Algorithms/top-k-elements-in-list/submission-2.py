from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int) # number -> count occured
        for num in nums:
            seen[num] += 1
        
        buckets = [[] for i in range(len(nums)+1)] # number of occurences -> value with that occurences
        # number of occurences is between 0 and len(nums)
        for num, count in seen.items():
            buckets[count].append(num) # freq -> values with that frequency

        # iterate and find the top k unique elements
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            result.extend(buckets[i])
            if len(result) >= k: # unique test cases are guaranteed
                return result[:k]
        return None
            