#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for stone in stones:
            if stone in jewels:
                res += 1
        return res
        
# @lc code=end

