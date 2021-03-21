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