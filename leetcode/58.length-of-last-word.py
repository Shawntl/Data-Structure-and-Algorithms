#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        length = 0
        flag = True
        for i, sub_str in enumerate(s):
            if sub_str == ' ':
                flag = False
                continue
            else:
                if flag:
                    length += 1
                else:
                    length = 1
                    flag = True
        return length

        
# @lc code=end

