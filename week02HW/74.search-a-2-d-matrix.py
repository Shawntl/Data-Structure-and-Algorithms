#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            if target < matrix[i][j]:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
            else:
                return True
        return False
        
# @lc code=end

