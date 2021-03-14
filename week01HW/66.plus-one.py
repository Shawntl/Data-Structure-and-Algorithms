#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while digits[i] + 1 == 10:
            digits[i] = 0
            i -= 1
            if i == -1:
                digits.insert(0, 1)
                return digits
        digits[i] = digits[i] + 1

        return digits
        
# @lc code=end

