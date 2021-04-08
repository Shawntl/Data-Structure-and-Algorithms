|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | dynamic programming |  2021-03-28 | Shawn_Song  | leetcode
-------
 
# 动态规划  
1. 分治+最优子结构。
2. 动规和递归、分治没有本质区别，主要看是否有最优子结构。共性是是否有重复子问题。差异：最优子结构，中途可淘汰次优解。  

**最重要的三点**  
1. 最优子结构。
2. 储存中间状态。
3. 递推公式，一维二维   

**解题思路**  
1. 读题
2. 定义状态，找递推公式
3. 初始化，边界条件
4. 实现递推公式

## content
### 斐波那契数列(一维)
* 70.Climbing Stairs
* 91.Decode Ways
* 53.Maximum Subarray
* 152.Maximum Product Subarray
* 300.Longest Increasing Subsequence
* 322.Coin Change

### 二维转一维
* 2021.Maximum Submatrix
* 363.Max Sum of Rectangle No larger Than K


### 矩阵路径
* 64.Minimum Path Sum
* 62.Unique Paths
* 63.Unique Paths II
* 120.Triangle

### 最长公共子序列
* 1143.Longest Common Subsequence
* 221.Maximal Square
* 72.Edit Distance

### 字符串
* 647.Palindormic Substrings

## 70. Climbing Stairs(Easy)

[https://leetcode-cn.com/problems/climbing-stairs/](https://leetcode-cn.com/problems/climbing-stairs/)  

### Solution
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        fst = 1
        sec = 2
        res = fst + sec
        for i in range(4, n+1):
            fst = sec
            sec = res
            res = fst + sec
        return res
```
思路：自底向上的动态规划，由递推树可以看出n<4时，res就是n自己。n>4时，res=f(n-1)+f(n-2),我们只要每一次存下下一个n的前两个res即可，前两个res我们用fst和sec来存，每一次循环更新这两个变量即可。

## 91. Decode Ways(Meidum)

[https://leetcode-cn.com/problems/decode-ways/](https://leetcode-cn.com/problems/decode-ways/)

### Solution
```python
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
```
思路：可以按爬楼梯的思路去理解这道题，当前字符前所有字符组成的字符串解码方法=到前一个字符的解码方法+到前两个字符的解码方法。区别是这里加了限制条件：  
只有当当前字符不为零（即可解码）时才可以加前一个字符的所有解码方法数。  
当当前字符和上一个字符可以组成10～26的解码时，才可以加上倒数第二个字符的解码方法数。


## 53. Maximum Subarray(Medium)

[https://leetcode-cn.com/problems/maximum-subarray/](https://leetcode-cn.com/problems/maximum-subarray/)

### Description
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

### Solution
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
        return max(nums)
```
思路：dp状态可以在一维空间解决，也就是说，数组所有子序列一定是以数组某个元素结尾的，我们状态空间dp[i]定义的就是以nums[i]结尾的所有子序列中和最大的和。这些最大的和里再求最大值就是我们要的答案。这个dp[i]要么是自己要么是一个正数（dp[i-1])加上自己。  


## 152. Maximum Product Subarray(Medium)

[https://leetcode-cn.com/problems/maximum-product-subarray/](https://leetcode-cn.com/problems/maximum-product-subarray/)

### Description
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

### Solution
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxdp = [nums[0]]+[float('-inf')]*(len(nums)-1)
        mindp = [nums[0]]+[float('inf')]*(len(nums)-1)
        for i in range(1, len(nums)):
            maxdp[i] = max(nums[i]*maxdp[i-1], 
                           nums[i]*mindp[i-1],
                           nums[i])
            mindp[i] = min(nums[i]*maxdp[i-1], 
                           nums[i]*mindp[i-1],
                           nums[i])
        return max(maxdp)
```
思路：和上一题最大子序和的思路类似，唯一不同的是当前值如果为负数时有可能乘以上一个状态值的最小值达到最优。还需要维护一个储存最小值的dp数组。  

## 300. Longest Increasing Subsequence(Medium)

[https://leetcode-cn.com/problems/longest-increasing-subsequence/](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

### Description
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

### Solution
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
```
思路：这道题和最大子序和不同的地方在于子结构不能单由上一个dp[i-1]计算，而是需要遍历0~i-1的dp储存值，找到最优解。dp[i]的含义依然是以i结尾的序列中最长上升子序列。


## 322. Coin Change(Medium)

[https://leetcode-cn.com/problems/coin-change/](https://leetcode-cn.com/problems/coin-change/)

### Description
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

### Solution
```python
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
```
思路：状态dp[i]是兑换当前amount最少硬币数，和爬楼梯问题不一样的是：爬楼梯是将几种最优子结构解相加，而这里是求最优子结构中的最小值，每一个状态保证最小，就一定可以保证最后的dp[amount]也一定是最小的。

## 2021. Max submatirx LCCI(hard)

[https://leetcode-cn.com/problems/max-submatrix-lcci/](https://leetcode-cn.com/problems/max-submatrix-lcci/)

### Description
给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。
返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。

### Solution
```python
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        max_val = float('-inf')
        res = [0]*4
        for i in range(n):
            # 二维转一维，dp中每个值代表以当前位结尾的最大子序和
            dp = [0]*m
            r1, c1 = i, 0
            for j in range(i, n):
                cur_sum = 0
                for k in range(m):
                    dp[k] += matrix[j][k]
                    if cur_sum > 0:
                        cur_sum += dp[k]
                    else:
                        cur_sum = dp[k]
                        r1 = i
                        c1 = k

                    if cur_sum > max_val:
                        max_val = cur_sum
                        res[0] = r1
                        res[1] = c1
                        res[2] = j
                        res[3] = k

        return res
```
思路：二维问题转换成一维问题，在矩阵行上设置上边和下边，遍历矩阵高的所有组合。求和变成一维问题后，使用标记法不断更新最大值，并且记录坐标。


## 363. Max Sum of  Rectangle No Larger Than K(hard)

[https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/)

### Descritption
给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。

### Solution
```python
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = float('-inf')
        for i in range(n):
            dp = [0]*m
            for j in range(i, n):
                cur_sum = 0
                # 创建一个数组储存cur_sum(0, i-1)
                lst = [0]
                for p in range(m):
                    dp[p] += matrix[j][p]
                    cur_sum += dp[p]
                    # 求使得cur_sum(i,j)=k时cur_sum(0, i-1)在保存数组中的位置
                    loc = bisect.bisect_left(lst, cur_sum-k)
                    # 如果储存的cur_sum(0, i-1)的值中有大于cur_sum(0, j) - k的，
                    # 我们就取刚刚比它大的那个值作为当前不大于k的cur_sum(i, j)
                    if loc < len(lst):
                        res = max(cur_sum - lst[loc], res)

                    # 储存当前cur_sum(0, j)的值
                    bisect.insort(lst, cur_sum)
        return res
```
思路：前面部分和2021题最大子矩阵的求法一样，都是二维转一维。不同的是限制条件加了不大于k，标记法部分的内容需要调整。我们有cur_sum(0, j) = cur_sum(0, i-1) + cur_sum(i, j)。cur_sum(i, j)就是我们要求的子序列的和，要让他不大于k，cur_sum(0, i-1)就要大于等于cur_sum(0, j)-k. 每一步将cur_sum存起来方便未来bisect去查询是否有cur_sum(0, i-1)大于等于cur_sum(0, j)-k。



## 64. Minimum Path Sum(Meidum)

[https://leetcode-cn.com/problems/minimum-path-sum/](https://leetcode-cn.com/problems/minimum-path-sum/)

### Description
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。  

### Solution
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    grid[i][j] == grid[i][j]
                elif i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1] 
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = min(grid[i][j-1]+grid[i][j], 
                                     grid[i-1][j]+grid[i][j])
        return grid[i][j]
```
思路：自底向上的动态规划，从底开始更新矩阵中的最小路径和，等于上面格子的最小路径和加上左边格子的最小路径和。这样只要保证每个格子最优的子结构，就可以保证最后end格子的全局最优解。

## 62.Unique Paths(Medium)

[https://leetcode-cn.com/problems/unique-paths/](https://leetcode-cn.com/problems/unique-paths/)

### Description
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。问总共有多少条不同的路径？

### Solution
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[i][j] = 1
                elif i == 0 and j != 0:
                    grid[i][j] = grid[i][j-1]
                elif i != 0 and j == 0:
                    grid[i][j] = grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j-1] + grid[i-1][j]
        return grid[i][j]
```
思路：自底向上的动态规划，先创建一个二维数组用来初始化所有格子路径数的初始值为0，然后在机器人从start开始走到end过程中更新每个格子中的路径数，每个格子的路径数只有可能等于它上方格子的路径加上左方格子的路径，所以只要保证这两个格子的值计算正确，就可以计算出end中的路径数。  

## 63. Unique Paths II(Meidum)

[https://leetcode-cn.com/problems/unique-paths-ii/](https://leetcode-cn.com/problems/unique-paths-ii/)

### Description
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

### Solution
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                    continue
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                elif i == 0 and j != 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif i != 0 and j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[i][j]
```
思路：和上一题类似，但是注意这里障碍物格子是1需要变成0，start位置要变成1，再继续更新格子里的值。


## 120. Triangle(Medium)

[https://leetcode-cn.com/problems/triangle/](https://leetcode-cn.com/problems/triangle/)

### Solution
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0:
                    continue
                elif j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
```
思路：和在矩阵中搜索最小路径和类似。


## 1143. Longest Common Subsequence(Medium)

[https://leetcode-cn.com/problems/longest-common-subsequence/](https://leetcode-cn.com/problems/longest-common-subsequence/)

### Solution
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        strMat = [[0]*m for _ in range(n)]
        if text1[0] == text2[0]:
            strMat[0][0] = 1
        else:
            strMat[0][0] = 0
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    strMat[i][j] = max(strMat[i][j-1], 
                                       int(text1[i] == text2[j]))
                elif i != 0 and j == 0:
                    strMat[i][j] = max(strMat[i-1][j], 
                                       int(text1[i] == text2[j]))
                else:
                    if text1[i] == text2[j]:
                        strMat[i][j] = strMat[i-1][j-1] + 1
                    else:
                        strMat[i][j] = max(strMat[i-1][j], strMat[i][j-1]) 

        return strMat[i][j]
```
思路：将两个字符串比对转化为矩阵路径问题，横轴纵轴分别代表一个字符串，格子内的值代表两个字符串从头对齐到当前位置的最长公共子序列长度。如果当前格子两个对应字符相同，则当前值=左上角格子值加一，否则当前值为上面格子或者右边格子的值。

## 221. Maximal Sqaure(Medium)

[https://leetcode-cn.com/problems/maximal-square/](https://leetcode-cn.com/problems/maximal-square/)

### Description
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

### Solution
```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != 0 and j != 0 and matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i-1][j]),
                                       int(matrix[i][j-1]),
                                       int(matrix[i-1][j-1]))+1
                res = max(int(matrix[i][j]), res)
        return res**2
```
思路：本题的状态空间和最优子结构有点类似上一题最长公共子序列。状态空间还是matrix[i][j]代表以当前格子为正方形右下角顶点的最大正方形边长。而当它不为0时的大小就等于上方、左方、左上角格子中值的最小值加上1。当它为0时肯定组不成正方形，所以继续填0。  
和最长子序列那道题的相似点就在于，状态空间都由当前格子以上、以左的区间来定义。值的大小由上、左、左上三个格子的最优解来递推。  


## 72. Edit Distance(Hard)

[https://leetcode-cn.com/problems/edit-distance/](https://leetcode-cn.com/problems/edit-distance/)

### Description
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。你可以对一个单词进行如下三种操作：  
* 插入一个字符
* 删除一个字符
* 替换一个字符  

### Solution
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(0, n+1):
            for j in range(0, m+1):
                if i == 0 and j == 0:
                    continue
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j]+1
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1]+1
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp[i][j]
```
思路：将两个字符串比对转化为矩阵路径问题，横轴纵轴分别代表一个字符串，格子内的值代表两个字符串从头对齐到当前位置需要的最小操作数。下面来它的子问题是从上一个最小操作数状态转换到当前状态，因为有三种操作，所以当最后一步操作是：   
插入：考虑dp[i][j-1]  
删除：考虑dp[i-1][j]   
替换：考虑dp[i-1][j-1]  



## 647. Palindromic Substrings(Meidum)

[https://leetcode-cn.com/problems/palindromic-substrings/](https://leetcode-cn.com/problems/palindromic-substrings/)

### Description
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。  

### Solution
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = 0
        # 枚举所有子串（状态）
        for i in range(n):
            for j in range(0, i+1):
                length = i - j + 1
                # 子串长度等于1，一定是回文
                if length == 1:
                    dp[j][i] = True
                    count += 1
                # 子串长度等于且两个字符一样，一定是回文
                if length == 2 and s[j] == s[i]:
                    dp[j][i] = True
                    count += 1
                # 字串长度大于二，如果外层两个字符相等，里面的
                # 字符串是回文，则当前的子串一定是回文
                if length > 2 and s[i] == s[j] and dp[j+1][i-1] is True:
                    dp[j][i] = True
                    count += 1
        return count
```
思路：用一个头指针i和尾指针j定义所有子串的状态空间，每次i加一，所以注意在第三个条件判断中，length>2时，除去外层两个字符，dp[j+1][i-1]一定在之前的遍历中判断过是否为回文。
