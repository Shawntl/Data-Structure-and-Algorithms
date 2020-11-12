#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     res = sorted(sum(matrix, []))

    #     return res[k-1]
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(mid):
            i, j = n-1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k


        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

        
# @lc code=end

