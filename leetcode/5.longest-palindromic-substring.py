#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        max_len = 0
        for i in range(n):
            for j in range(i+1):
                length = i - j + 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2 and s[i] == s[j]:
                    dp[i][j] = True
                elif length > 2 and s[i] == s[j] and dp[i-1][j+1] == True:
                    dp[i][j] = True
                
                if dp[i][j] == True and length > max_len:
                    left, right = j, i
                    print(left, right)
                    max_len = length
        return s[left:right+1]
# @lc code=end

