#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            #  print(left, right)
            mid = (left + right) // 2
            if mid**2 <= x:
                left = mid + 1
            else:
                right = mid - 1
        return right
        
# @lc code=end

