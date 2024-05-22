from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        if not heights or not heights[0]:
            return res

        rows, cols = len(heights), len(heights[0])

        pacific_reachable = [[False] * cols for _ in range(rows)]
        atlantic_reachable = [[False] * cols for _ in range(rows)]

        # Iterate over leftmost and rightmost columns
        for row in range(rows):
            self.dfs(heights, pacific_reachable, float("-inf"), row, 0)
            self.dfs(heights, atlantic_reachable, float("-inf"), row, cols - 1)

        # Iterate over topmost and bottommost rows
        for col in range(cols):
            self.dfs(heights, pacific_reachable, float("-inf"), 0, col)
            self.dfs(heights, atlantic_reachable, float("-inf"), rows - 1, col)

        # Check for cells reachable from both oceans
        for row in range(rows):
            for col in range(cols):
                if pacific_reachable[row][col] and atlantic_reachable[row][col]:
                    res.append([row, col])

        return res

    def dfs(self, heights, reachable, prev_height, row, col):
        if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]):
            return
        if reachable[row][col]:
            return
        if heights[row][col] < prev_height:
            return

        reachable[row][col] = True
        self.dfs(heights, reachable, heights[row][col], row + 1, col)
        self.dfs(heights, reachable, heights[row][col], row - 1, col)
        self.dfs(heights, reachable, heights[row][col], row, col - 1)
        self.dfs(heights, reachable, heights[row][col], row, col + 1)
