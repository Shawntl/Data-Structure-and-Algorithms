#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        dp[0] = 1 if s[0] != '0' else 0
        if n < 2:
            return dp[0]
        if s[1] != '0':
            dp[1] = dp[0]
        if int(s[0]+s[1]) >= 10 and int(s[0]+s[1]) <= 26:
            dp[1] = dp[1] + 1
        for i in range(2, n):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if int(s[i-1]+s[i]) >= 10 and int(s[i-1]+s[i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

        
# @lc code=end

