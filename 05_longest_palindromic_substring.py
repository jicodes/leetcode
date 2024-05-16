class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        start = 0
        max_length = 0
        
        for i in range(len(s)):
            # Check for odd length palindromes
            len1 = self.expand_around_center(s, i, i)
            # Check for even length palindromes
            len2 = self.expand_around_center(s, i, i + 1)
            # Choose the longer palindrome length
            length = max(len1, len2)
            if length > max_length:
                max_length = length
                start = i - (length - 1) // 2
        
        return s[start:start + max_length]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        # Expand around the center defined by left and right indices
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of the palindrome
        return right - left - 1
