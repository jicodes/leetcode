from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add the current subset to the result
            result.append(path[:])

            # Explore all possible subsets that can be formed by adding elements from 'start' onwards
            for i in range(start, len(nums)):
                # Add nums[i] to the current subset
                path.append(nums[i])

                # Explore further by recursively calling backtrack with the next index and the updated path
                backtrack(i + 1, path)

                # Backtrack: Remove nums[i] from the current subset to explore other possibilities
                path.pop()

        # Initialize an empty list to store the result
        result = []

        # Start backtracking from index 0 with an empty path
        backtrack(0, [])

        return result
