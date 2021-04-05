#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[i][j] = 1
                elif i == 0 and j != 0:
                    grid[i][j] = grid[i][j-1]
                elif i != 0 and j == 0:
                    grid[i][j] = grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j-1] + grid[i-1][j]
        return grid[i][j]
        
# @lc code=end

