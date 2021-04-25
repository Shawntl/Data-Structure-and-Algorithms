#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for s in str:
            if s.isupper():
                res.append(s.lower())
            else:
                res.append(s)
        return ''.join(res)
        
# @lc code=end

