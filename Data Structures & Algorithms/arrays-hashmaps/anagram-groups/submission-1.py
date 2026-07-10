from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_freq(string):
            freq = [0 for i in range(ord('z') - ord('a') + 1)]
            for char in string:
                freq[ord(char) - ord('a')] += 1
            return tuple(freq) # tuple so that it's immutable
        groups = defaultdict(list) # (freq tuple) -> list of strings
        for string in strs:
            groups[get_freq(string)].append(string)
        return list(groups.values())