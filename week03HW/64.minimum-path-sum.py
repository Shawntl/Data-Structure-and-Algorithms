#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    grid[i][j] == grid[i][j]
                elif i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1] 
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = min(grid[i][j-1]+grid[i][j], 
                                     grid[i-1][j]+grid[i][j])
        return grid[i][j]
    
# @lc code=end

