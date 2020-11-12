#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     res = True
    #     m = len(matrix)
    #     n = len(matrix[0])
    #     if m == 1 or n == 1:
    #         return True
    #     for i in range(0, m-1):
    #         r = i
    #         c = 0
    #         while c < min(n-1, m-i-1):
    #             if matrix[r][c] == matrix[r+1][c+1]:
    #                 r += 1
    #                 c += 1
    #             else:
    #                 res = False
    #                 return res
    #     for j in range(1, n-1):
    #         c = j
    #         r = 0
    #         while r < min(m-1, n - j - 1):
    #             if matrix[r][c] == matrix[r+1][c+1]:
    #                 r += 1
    #                 c += 1
    #             else:
    #                 res = False
    #                 return res
        
    #     return res
    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
      
# @lc code=end

