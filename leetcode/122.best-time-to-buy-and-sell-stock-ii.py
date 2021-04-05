#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0
        while buy < len(prices) and sell < len(prices):
            if prices[buy] < prices[sell]:
                profit += prices[sell] - prices[buy]
                buy = sell
                sell = sell + 1
            else:
                buy += 1
                sell += 1
        return profit
                        
# @lc code=end

