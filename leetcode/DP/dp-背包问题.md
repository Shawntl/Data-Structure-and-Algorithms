|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | dp-背包问题 |  2021-05-27 | Shawn_Song  | leetcode
-------
 
# 动态规划-背包问题
## 背包问题具备的特征  
是否可以根据一个**target（直接给出或间接求出)**，target可以是数字也可以是字符串，再给定一个数组arrs,问：能否使用arrs中的各元素做各种排列组合得到target.  再就是要思考一下递推公式
常见背包问题可分为：
## content
### 完全背包问题
如果是完全背包，即数组中的元素可重复使用，target循环正序。如果不考虑arrs中顺序，arrs放在外循环，target在内循环。
```python
for ele in arrs:
    for i in range(ele, target+1):
```
* 322.Coin Change
* 279.Perfect Squares
* 518.Coin Change II  

考虑arrs中的顺序（一旦顺序改变就不能得到target了），arrs放在内循环，target在外循环。
```python
for i in range(1, target+1):
    for ele in arrs:
```
* 139.Word Break
* 377.Combination Sum IV  

### 01背包问题
如果是01背包问题，即数组中的元素不可以重复使用，target循环逆序。如果不考虑arrs中顺序，arrs放在外循环，target在内循环。
```python
for ele in arrs:
    for i in range(target, ele-1, -1):
```
* 416.Partition Equal Subset Sum
* 494.Target Sum  
### 二维01背包
两个变量组成target
* 474.Ones and Zeros

## 322. Coin Change(Medium)

[https://leetcode-cn.com/problems/coin-change/](https://leetcode-cn.com/problems/coin-change/)

### Description
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

### Solution
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')]*amount
        for coin in coins:
            # 当背包最后一个硬币为固定面值时，需要的最少个数。然后改变硬币面值迭代dp里的值
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != float('inf') else -1
```
思路：当前填满容量j最少需要的硬币 = min( 之前填满容量j最少需要的硬币, 填满容量 j - coin 需要的硬币 + 1个当前硬币）

## 279.Perfect Squares(Medium)

[https://leetcode-cn.com/problems/perfect-squares/](https://leetcode-cn.com/problems/perfect-squares/)

### Solution
```python
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')]*n
        for num in range(1, round(n**0.5)+1):
            for i in range(num*num, n+1):
                dp[i] = min(dp[i], dp[i-num*num]+1)
        return dp[-1]
```
思路： 完全背包问题，元素可重复且不考虑顺序。和322零钱兑换类似。

## 518. Coin Change II(Medium)

[https://leetcode-cn.com/problems/coin-change-2/](https://leetcode-cn.com/problems/coin-change-2/)

### Solution
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]
```
思路：当前凑成总金额的组合数 = 原来凑成总金额的组合数 + 最后一个硬币为当前面值时凑成总金额的组合数。

## 139.Word Break(Medium)

[https://leetcode-cn.com/problems/word-break/](https://leetcode-cn.com/problems/word-break/)

### Solution
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False]*len(s)
        for i in range(1, len(s)+1):
            for word in wordDict:
                if (i >= len(word)) and (s[i-len(word):i] == word):
                    dp[i] = dp[i] or dp[i-len(word)]
        return dp[-1]
```
思路：转化为是否可以用 wordDict 中的词组合成 s，完全背包问题，并且为“考虑排列顺序的完全背包问题”，外层循环为 target ，内层循环为选择池 wordDict


## 377.Combination Sum IV(Medium)

[https://leetcode-cn.com/problems/combination-sum-iv/](https://leetcode-cn.com/problems/combination-sum-iv/)

### Solution
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0]*target
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]

        return dp[-1]
```
思路：完全背包问题考虑顺序的组合问题，和518题零钱兑换2唯一不同的一点是考虑顺序，不同顺序的组合视为不同。

## 416.Partition Equal Subset Sum(Medium)

[https://leetcode-cn.com/problems/partition-equal-subset-sum/](https://leetcode-cn.com/problems/partition-equal-subset-sum/)

## Description
能不能装满容量为target的背包

### Solution
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumAll = sum(nums)
        if sumAll % 2:
            return False
        target = sumAll // 2
        dp = [True] + [False]*target
        for num in nums:
            # 倒序
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[-1]
```
思路：当前target是否能装满 = 之前就能装满 or 最后加入当前num后能装满，倒序因为状态是由前往后转移的，而数组中的元素不能重复使用。

## 494.Target Sum(Medium)

[https://leetcode-cn.com/problems/target-sum/](https://leetcode-cn.com/problems/target-sum/)

### Solution
```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumAll = sum(nums)
        if (target+sumAll) % 2:
            return 0
        S = (target+sumAll) // 2
        dp = [1]+[0]*S
        for num in nums:
            for i in range(S, num-1, -1):
                dp[i] += dp[i-num]
        return dp[-1]
```
思路：先将本问题转换为01背包问题。
假设所有符号为+的元素和为x，符号为-的元素和的绝对值是y。
我们想要的 target = 正数和 - 负数和 = x - y
而已知x与y的和是数组总和：x + y = sum
可以求出 x = (target + sum) / 2 = S
也就是我们要从nums数组里选出几个数，令其和为S
于是就转化成了求容量为target的01背包问题 =>要装满容量为target的背包，有多少种组合，数组元素不能重复，和上一题一样倒序，状态转移方程和518题类似：  
当前凑成S的组合数 = 原来凑成S的组合数 + 最后一个元素为当前元素时凑成S的组合数。

## 474.Ones aand Zeros(Medium)

[https://leetcode-cn.com/problems/ones-and-zeroes/](https://leetcode-cn.com/problems/ones-and-zeroes/)

### Solution
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 背包最多能装m个0和n个1时的最大子集个数
        dp = [[0]*(n+1) for _ in range(m+1)]
        for ele in strs:
            zeros = ele.count('0')
            ones = ele.count('1')
            # 01背包问题，元素不能重复，倒序
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    # 当前元素放入背包或不放入背包
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[-1][-1]
```

