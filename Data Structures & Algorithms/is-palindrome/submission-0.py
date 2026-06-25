class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: # empty string
            return True
        filtered = list(filter(lambda char: char.isalnum(), s)) # remove non-alphanumeric characters

        left, right = 0, len(filtered) - 1
        while (left < right):
            if filtered[left].lower() != filtered[right].lower(): # different, case-insensitive
                return False
            left += 1
            right -= 1
        return True