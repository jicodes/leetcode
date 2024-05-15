from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # If the total sum is odd, we cannot partition the array into two equal subsets
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        # Initialize a DP array to store whether a sum can be achieved using a subset of nums
        dp = [False] * (target_sum + 1)
        dp[0] = True

        # Iterate through each number in nums
        for num in nums:
            # Iterate backward from target_sum to num
            for j in range(target_sum, num - 1, -1):
                """
				Case 1: The current sum(j) has been seen before. 
				Then, if we don't select the current element, the sum will not change.
				So, this total sum will still exist, and its dp value remains True.
				
				Case 2: The current sum(j) has not been seen before,
				but it can be obtained by selecting the current element.
				This means that dp[j-num] = True, and thus dp[curr] now becomes True.
				
				Case 3: The current sum(j) has not been seen before,
				and it cannot be obtained by selecting the current element.
				So, this total sum will still not exist, and its dp value remains False.
                """
                dp[j] = dp[j] or dp[j - num]

        # If dp[target_sum] is True, it means we can partition nums into two subsets with equal sum
        return dp[target_sum]
