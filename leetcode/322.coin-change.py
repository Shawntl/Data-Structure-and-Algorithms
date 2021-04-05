#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[float('inf')]*amount
        for i in range(1, amount+1):
            for k in coins:
                if k <= i:
                    dp[i] = min(dp[i], dp[i-k]+1)
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
        
# @lc code=end
