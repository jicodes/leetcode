from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize the result list with all 0's
        stack = []  # This stack will store indices of the temperatures list

        for i in range(n):
            # While there is an index on the stack and the current temperature is higher
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()  # Get the index of the previous day
                answer[prev_index] = i - prev_index  # Calculate the difference in days
            stack.append(i)  # Push the current day's index onto the stack

        return answer


# Example usage:
sol = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(sol.dailyTemperatures(temperatures))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
