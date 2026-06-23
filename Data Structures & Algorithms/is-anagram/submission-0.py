from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int) 
        # defaultdict takes a callable function
        # int means the default value is integer 0
        # string -> default value is '', list -> default value is []
        for char in s:
            freq[char] += 1
    
        for char in t:
            freq[char] -= 1
        
        # freq of all characters in freq should be 0
        for char in freq:
            if freq[char] != 0:
                return False # not anagram
        # all freqs are 0:
        return True
