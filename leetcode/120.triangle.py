#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0:
                    continue
                elif j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
        
# @lc code=end

