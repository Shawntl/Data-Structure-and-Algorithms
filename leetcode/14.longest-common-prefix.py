#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0: return ''
        res = ''
        for j, prefix in enumerate(strs[0]):
            i = 1
            while i < len(strs) and j < len(strs[i]):
                if strs[i][j] == prefix:
                    i += 1
                else:
                    break
            if i == len(strs):
                res += prefix
            else:
                break
        return res
        
# @lc code=end

