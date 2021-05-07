|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | backtrack |  2021-03-18 | Shawn_Song  | leetcode
-------

# 树与递归


## Content
### 回溯
* 22.Generate Parentheses
* 77.Combinations
* 46.Permutations
* 47.Permutations II
* 78.Subsets
* 17.Letter Combinations of a Phone Number
* 51.N-Queens
* 79.Word Search
* 113.Path Sum II


## 22.Generate Parenthese(Medium)

[https://jmq.h5.xeknow.com/s/3nk3lb](https://jmq.h5.xeknow.com/s/3nk3lb)

### Description
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

### Solution
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = 0, 0
        res = []

        def recurGenBracket(l, r, n, s):

            if l == n and r == n:
                res.append(s)
                return
            s1 = s + '('
            s2 = s + ')'
            if l < n:
                recurGenBracket(l+1, r, n, s1)
            if r < l:
                recurGenBracket(l, r+1, n, s2)
        recurGenBracket(left, right, n, '')
        return res
```
思路： 
第一步是想用递归的思路生成所有可能的括号组合，一共是$2^2n$种组合。  
第二步是想如何筛选出合法的括号组合，在生成括号时：  
* 如果左边的括号没有到n个就可以一直加
* 只有已经加入的左边括号数量小于已经加入的右边括号数量时，才可以加入右边括号。



## 77.Combinations(Medium)

[https://leetcode-cn.com/problems/combinations/](https://leetcode-cn.com/problems/combinations/)

### Description
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

### Solution
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, k, cbs):
            if k == 0:
                res.append(cbs)
                return
            for j in range(i, n+1):
                backtrack(j+1, k-1, cbs+[j])
        backtrack(1, k, [])
        return res
```
思路： 可以看成是一共有k个格子，第一个格子可以放1-n个数，第二个格子只能放比第一个格子大的数。如此递归k层，就找到了放满格子的所有组合情况。时间复杂度为O(nk),空间复杂度为O(k).


## 46.Permutations(Medium)

[https://leetcode-cn.com/problems/permutations/](https://leetcode-cn.com/problems/permutations/)

### Description
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

### Solution
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def bracktrack(nums, permutes):
            if len(permutes) == n:
                res.append(permutes)
                return
            for j in range(len(nums)):
                cur_nums = nums[:j]+nums[j+1:]
                bracktrack(cur_nums, permutes+[nums[j]])
        bracktrack(nums, [])
        return res
```
思路：可以看成n个格子，第一个格子可以放n个数，后面的格子能放的数依次减去之前已经被放过的数。如此递归n层，时间复杂度为$O(N^2)$, 空间复杂度为O(N).

## 47.Permutations II(Medium)

[https://leetcode-cn.com/problems/permutations-ii/](https://leetcode-cn.com/problems/permutations-ii/)

### Description
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

### Solution
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def bracktrack(nums, permutes):
            if len(permutes) == n:
                res.append(permutes)
                return
            check = []
            for j in range(len(nums)):
                if nums[j] not in check:
                    cur_nums = nums[:j]+nums[j+1:]
                    bracktrack(cur_nums, permutes+[nums[j]])
                    check.append(nums[j])
        bracktrack(nums, [])
        return res
```
思路：在上一题的基础上加入减支判断条件，画递归树可以看出，当每一层递归时加入permute中的额元素重复时，应该把当前重复元素对应的分支剪除。

## 78.Subsets(Medium)

[https://leetcode-cn.com/problems/subsets/](https://leetcode-cn.com/problems/subsets/)

### Description
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

### Solution
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(j, k, subsets):
            if k == 0:
                res.append(subsets)
                return
           
            backtrack(j+1, k-1, subsets+[nums[j]])
            backtrack(j+1, k-1, subsets+[])
        backtrack(0, n, [])
        return res
```
思路：回溯法，看成n个格子，每个格子内的元素可以选或不选。一共n层递归，每层递归执行选当前元素或者不选当前元素。

## 17.Letter Combinations of a Phone Number(Meidum)

[https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

### Description
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

### Solution
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_dic = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}
        res = []
        n = len(digits)
        if n == 0:
            return []
        def backtrack(dig_idx, s):
            if dig_idx == n:
                res.append(s)
                return
            key = digits[dig_idx]
            for j in range(len(dig_dic[key])):
                backtrack(dig_idx+1, s+dig_dic[key][j])
        backtrack(0, '')
        return res
```
思路：可以看成n个格子，n是digits长度，每层往格子中可以放k种可能的字母，k是当前数字对应的字母串的长度。下一层递归考虑往第二个格子里放第二个digits对应的字母串中的一个。


## 51. N-Queens

[https://leetcode-cn.com/problems/n-queens/](https://leetcode-cn.com/problems/n-queens/)

### Description
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

### Solution
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()

        def backtrack(n, row, cur_trail):
            if row == n:
                self.result.append(cur_trail)
                return

            for col in range(n):
                if (col in self.cols) or (row + col in self.pie) or (row - col in self.na):
                    continue 

                self.cols.add(col)
                self.pie.add(row + col)
                self.na.add(row - col)

                backtrack(n, row+1, cur_trail+[col])

                self.cols.remove(col)
                self.pie.remove(row+col)
                self.na.remove(row-col)
        backtrack(n, 0, [])

        return self._generate_result(n)
    
    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append('.' * i + 'Q' + '.' * (n- i-1))

        return [board[i:i+n] for i in range(0, len(board), n)]
```
思路：本题有三个关键点：   
第一： 题目需要用回溯法来解，一共n层递归，每一层选择将皇后放在当前行的某一列（for 循环遍历当前行的所有列），进入下一层时行数加一。  
第二： 在当前递归层决定是否放皇后时，需要判断在皇后的上一行（上一层递归）的当前列以及对角线上是否有被放过皇后。这就需要每一层递归落子时记录列和两个对角坐标，对角坐标计算方式为row+col、row-col，记住就好。  
第三：每一层递归调用结束后都需要清除还原环境储存的变量（self.col, self.pie, self.na），以便下一轮从顶层的递归重新使用。


## 79.Word Search(Medium)

[https://leetcode-cn.com/problems/word-search/](https://leetcode-cn.com/problems/word-search/)

### Description
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


### Solution
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        # 回溯法判断当前位置字母是否为单词对应位置的字母
        def backtrack(i, j, k):
            # 当前位置字母不是单词对应位置的字母
            if not 0<=i<n or not 0<=j<m or board[i][j] != word[k]:
                return False
            # 当前位置字母是单词对应位置的字母

            # 当前字母已经遍历到单词的最后一个字母
            if k == len(word) - 1:
                return True
            # 将当前位置的字母置为空，意为已经标记为遍历过
            board[i][j] = ''
            # 向周围相邻的位置做探索递归
            res = backtrack(i-1, j, k+1) or backtrack(i, j-1, k+1) or backtrack(i+1, j, k+1) or backtrack(i, j+1, k+1)  
            # 回溯过后恢复数组中原本的元素值
            board[i][j] = word[k]
            return res
        # 在矩阵中搜索单词的第一个字母
        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True
        return False
```

## 113. Path Sum II(Medium)

[https://leetcode-cn.com/problems/path-sum-ii/](https://leetcode-cn.com/problems/path-sum-ii/)

### Solution
```python
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        def backtrack(root,node_lst,target):
            if not root: return
            if not root.left and not root.right and (target-root.val) == 0:
                node_lst.append(root.val)
                res.append(node_lst)
            
            backtrack(root.left,node_lst + [root.val], target - root.val)
            backtrack(root.right,node_lst + [root.val], target - root.val)
            
        backtrack(root, [], targetSum)
        return res
```
思路：回溯遍历所有路径，检查是否符合要求。