#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0]) 
        count = 0
        def DFSMasking(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != '1':
                return
            # 当前层执行操作
            grid[i][j] = '0'
            # drill down
            DFSMasking(i + 1, j)
            DFSMasking(i - 1, j)
            DFSMasking(i, j + 1)
            DFSMasking(i, j - 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    DFSMasking(i, j)
                    count += 1
        return count
     
# @lc code=end

