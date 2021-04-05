#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(0, n+1):
            for j in range(0, m+1):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1]+1
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j]+1
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
        return dp[i][j]
        
# @lc code=end

