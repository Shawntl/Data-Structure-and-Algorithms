#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(0, i+1):
                length = i - j + 1
                if length == 1:
                    dp[j][i] = True
                    count += 1
                if length == 2 and s[j] == s[i]:
                    dp[j][i] = True
                    count += 1
                if length > 2 and s[i] == s[j] and dp[j+1][i-1] is True:
                    dp[j][i] = True
                    count += 1
        return count

        
# @lc code=end

