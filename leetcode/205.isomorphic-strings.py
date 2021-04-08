#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))
        
# @lc code=end

