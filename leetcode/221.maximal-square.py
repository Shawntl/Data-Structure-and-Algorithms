#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != 0 and j != 0 and matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i-1][j]),
                                       int(matrix[i][j-1]),
                                       int(matrix[i-1][j-1]))+1
                res = max(int(matrix[i][j]), res)
        return res**2
        
# @lc code=end

