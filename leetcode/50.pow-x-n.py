#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        def div_con(x, n):
            if n < 2:
                return x
            if n % 2 == 0:
                return div_con(x, n // 2)**2
            elif n % 2 == 1:
                return div_con(x, n//2)*div_con(x, (n//2)+1)
        res = div_con(x, n)
        return res
        
# @lc code=end

