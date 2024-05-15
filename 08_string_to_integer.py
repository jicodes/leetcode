class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespace
        
        if not s:  # Empty string after stripping
            return 0
        
        sign = 1  # Initialize sign to positive
        i = 0
        
        # Check for sign
        if s[i] in ['+', '-']:
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Build the integer
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        # Apply sign and handle overflow
        num *= sign
        num = max(-2**31, min(2**31 - 1, num))
        
        return num
