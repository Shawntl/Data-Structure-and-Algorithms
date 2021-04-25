#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for sub_s in s:
            if sub_s in m.keys():
                m[sub_s] += 1
            else:
                m[sub_s] = 1

        for i, sub_s in enumerate(s):
            if m[sub_s] == 1:
                return i
        return -1
        
# @lc code=end

