#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(' ')
        res = []
        for sub_s in ls:
            res.append(sub_s[::-1])
        return ' '.join(res)
        
# @lc code=end

