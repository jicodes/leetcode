from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on their start values
        # This is a key function that specifies the criterion for sorting. Here, `lambda x: x[0]` is a lambda function that takes an interval `x` and returns its first element, which is the start value of the interval. This lambda function acts as a sorting key, indicating that the intervals should be sorted based on their start values.
        intervals.sort(key=lambda x: x[0])

        # Initialize a list to store the merged intervals
        merged = []

        # Iterate through the sorted intervals
        for interval in intervals:
            # If the merged list is empty or if the current interval does not overlap with the last interval in the merged list
            if not merged or interval[0] > merged[-1][1]:
                # Append the current interval to the merged list
                merged.append(interval)
            else:
                # Merge the current interval with the last interval in the merged list
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# Create an instance of the solution
sol = Solution()

# Test with example cases
print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

# Output: [[1,6],[8,10],[15,18]]
