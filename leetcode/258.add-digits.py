#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 9:
            return num
        elif num % 9:
            return num % 9
        else:
            return 9
        
# @lc code=end

