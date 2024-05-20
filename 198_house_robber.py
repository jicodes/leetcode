from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Initialize DP table
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Fill DP table
        for i in range(2, n):
            # Rob the current house i and the money from the previous non-adjacent house (i-2).
            # or Skip the current house i and take the maximum money robbed from the previous adjacent house (i-1).
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        # Return the maximum amount of money robbed without alerting the police
        return dp[n - 1]
