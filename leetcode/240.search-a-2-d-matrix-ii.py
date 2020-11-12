#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    # Brute Force
    # def searchMatrix(self, matrix, target):
        
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     res = [i for j in matrix for i in  j]
    #     if target in res:
    #         return True
    #     else:
    #         return False

    def searchMatrix(self, matrix, target):
        
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] == target:
                return True
        return False    
# @lc code=end

