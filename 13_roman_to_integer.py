class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to their integer values
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # Initialize the total to 0
        total = 0

        # Iterate through the string
        for i in range(len(s)):
            # If the current value is less than the next value, subtract it
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                # Otherwise, add the current value
                total += roman_to_int[s[i]]

        return total
