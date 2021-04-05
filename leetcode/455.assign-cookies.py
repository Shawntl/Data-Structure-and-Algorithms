#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = len(g) - 1, len(s) - 1
        count = 0
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                count += 1
                j -= 1
            i -= 1
        return count
      
# @lc code=end

