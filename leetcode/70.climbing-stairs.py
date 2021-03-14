#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        fst = 1
        sec = 2
        res = 0
        if n < 3:
            return n
        else:
            for i in range(2, n):
                res = fst + sec

                fst = sec
                sec = res
        return res

# @lc code=end

