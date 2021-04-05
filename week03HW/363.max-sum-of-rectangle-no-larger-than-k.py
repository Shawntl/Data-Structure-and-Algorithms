#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#

# @lc code=start
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = float('-inf')
        for i in range(n):
            dp = [0]*m
            for j in range(i, n):
                cur_sum = 0
                # 创建一个数组储存cur_sum(0, i-1)
                lst = [0]
                for p in range(m):
                    dp[p] += matrix[j][p]
                    cur_sum += dp[p]
                    # 求使得cur_sum(i,j)=k时cur_sum(0, i-1)在保存数组中的位置
                    loc = bisect.bisect_left(lst, cur_sum-k)
                    # 如果储存的cur_sum(0, i-1)的值中有大于cur_sum(0, j) - k的，
                    # 我们就取刚刚比它大的那个值作为当前不大于k的cur_sum(i, j)
                    if loc < len(lst):
                        res = max(cur_sum - lst[loc], res)

                    # 储存当前cur_sum(0, j)的值
                    bisect.insort(lst, cur_sum)
        return res
        
# @lc code=end

