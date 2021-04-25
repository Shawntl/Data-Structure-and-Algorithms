#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(' ')
        old_ls = [sub_s for sub_s in ls if sub_s]
        left, right = 0, len(old_ls) - 1
        while left < right:
            old_ls[left], old_ls[right] = old_ls[right], old_ls[left]
            left += 1
            right -= 1
        return ' '.join(old_ls)
        
# @lc code=end

