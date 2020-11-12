#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num, res = 0, 0
        for i in nums:
            if i == 1:
                res += 1
                if res > max_num:
                    max_num = res
            else:
                res = 0

        return max_num
        
# @lc code=end

