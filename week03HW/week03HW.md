|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | week03HW |  2021-04-05 | Shawn_Song  | leetcode
-------
  
* 64.Minimum Path Sum
* 91.Decode Ways
* 221.Maximal Square
* 363.Max Sum of Rectangle No larger Than K
* 647.Palindormic Substrings


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