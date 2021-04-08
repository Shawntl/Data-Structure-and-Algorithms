#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while n & 1 == 0 and i < 32:
            n >>= 1
            i += 1
        if i < 32:
            if n & (~1) != 0:
                return False
            else:
                return True
        else:
            return False
        
# @lc code=end

