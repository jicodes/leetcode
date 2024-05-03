# Dutch National Flag Algorithm, also known as the three-way partitioning algorithm

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize pointers for the three colors
        red, white, blue = 0, 0, len(nums) - 1
        
        while white <= blue:
            if nums[white] == 0:
                # If current element is red, swap with red pointer and move both pointers to the right
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                # If current element is white, just move white pointer to the right
                white += 1
            else:
                # If current element is blue, swap with blue pointer and move blue pointer to the left
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

# Test cases
nums = [2, 0, 2, 1, 1, 0]
solution = Solution()
solution.sortColors(nums)
print(nums)  

# Output should be [0, 0, 1, 1, 2, 2]
