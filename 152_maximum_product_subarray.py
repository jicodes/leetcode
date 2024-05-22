from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for num in nums[1:]:
            temp_max = max(num, max_prod * num, min_prod * num)
            min_prod = min(num, max_prod * num, min_prod * num)
            max_prod = temp_max
            result = max(result, max_prod)

        return result
