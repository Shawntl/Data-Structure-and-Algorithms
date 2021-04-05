|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | Greedy |  2021-03-27 | Shawn_Song  | leetcode
-------
 
# 贪心算法  
## content
* 874.Walking Robot Simulation  
* 455.Assign Cookies
* 122.Best Time to Buy and Sell Stock II
* 55.Jump Game

## 874. Walking Robot Simulation(Easy)

[https://leetcode-cn.com/problems/walking-robot-simulation/](https://leetcode-cn.com/problems/walking-robot-simulation/)  

### Solution
```python
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = {'up': [0, 1, 'left', 'right'],
                     'down': [0, -1, 'right', 'left'],
                     'left': [-1, 0, 'down', 'up'],
                     'right': [1, 0, 'up', 'down']}
        x, y = 0, 0
        ort = 'up'
        res = 0
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command > 0:
                for step in range(command):
                    if (x + direction[ort][0], y + direction[ort][1]) not in obstacles:
                        x += direction[ort][0]
                        y += direction[ort][1]
                        res = max(res, x**2+y**2)
                    else:
                        break
            else:
                if command == -1:
                    ort = direction[ort][3]
                else:
                    ort = direction[ort][2]
        return res
```  
思路：主要是direction这个字典的构造，key是当前方向，value前两个值是在当前方向移动时x, y坐标的变化。后两个值是在当前方向左转和右转后的方向。  

## 455. Assign Cookies(Easy)

[https://leetcode-cn.com/problems/assign-cookies/](https://leetcode-cn.com/problems/assign-cookies/)

### Solution  
```python
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
```
思路：直观地想法是将最大尺寸的饼干优先分给胃口值最大的孩子，因为每个孩子只能分一块饼干。所以count最大值也只能是饼干数，为了尽可能地将饼干用上，一定是按饼干尺寸从大到小开始分。

## 122.Best Time to Buy and sell Stock(Easy)

[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

### Description
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

### Solution
```python
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
```
思路：因为可以多次交易，所以可以使用贪心，只要下一天价格比当前天低就持续观望不买入，直到看到下一天价格比当前天低就在当前买入，下一天卖出。卖出后再在卖出当前买入，重复上一过程。这种办法把周期内所有的涨幅都计算在内了。

## 55. Jump Game(Medium)

[https://leetcode-cn.com/problems/jump-game/](https://leetcode-cn.com/problems/jump-game/)

### Description
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标.数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个下标。

### Solution
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endReachable = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= endReachable:
                endReachable = i
        return endReachable == 0
```
思路：从后往前贪心，如果上一个节点能走到当前节点，那么只要进一步判断是否能走到上一个节点即可。如果最后推到第一个节点，说明第一个节点一定能够走到最后一个节点。