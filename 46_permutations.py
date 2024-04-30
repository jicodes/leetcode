from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Result list to store permutations
        result = []
        
        # Backtracking function to generate permutations
        def backtrack(path, remaining):
            # Base case: If there are no remaining elements, add the current permutation to result
            if not remaining:
                result.append(path)
                return
            # Iterate through remaining elements
            for i in range(len(remaining)):
                # Choose the i-th element from the remaining list
                chosen = remaining[i]
                # Generate new remaining list by excluding the chosen element
                new_remaining = remaining[:i] + remaining[i+1:]
                # Recursively call backtrack with updated path and remaining list
                backtrack(path + [chosen], new_remaining)
        
        # Start backtracking with an empty path and initial list of numbers
        backtrack([], nums)
        
        return result


# Create an instance of the solution
sol = Solution()

# Test with example cases
print(sol.permute([1,2,3])) 

# Output:
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]