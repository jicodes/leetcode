class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D array to store the number of paths
        dp = [[0] * n for _ in range(m)]

        # Initialize the number of paths for the first row and column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill in the DP table using the recurrence relation
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The bottom-right cell stores the total number of unique paths
        return dp[m - 1][n - 1]
