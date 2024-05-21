from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        # Step 1: Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, reverse the list.
        k = n - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1

        if k == -1:
            nums.reverse()
            return

        # Step 2: Find the largest index l greater than k such that nums[k] < nums[l].
        l = n - 1
        while l > k and nums[l] <= nums[k]:
            l -= 1

        # Step 3: Swap the value of nums[k] with that of nums[l].
        nums[k], nums[l] = nums[l], nums[k]

        # Step 4: Reverse the sequence from nums[k + 1] to the end.
        nums[k + 1 :] = reversed(nums[k + 1 :])
