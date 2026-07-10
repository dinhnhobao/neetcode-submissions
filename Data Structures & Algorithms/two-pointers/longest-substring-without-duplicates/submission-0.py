class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        left = 0
        longest = 0
        for right in range(len(s)):
            # loop invariant: window consisting only of unique characters
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, len(seen))
        return longest       