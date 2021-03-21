|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | week02HW |  2021-03-21 | Shawn_Song  | leetcode
-------
  
* 77.Combinations
* 46.Permutations
* 47.Permutations II
* 236.Lowest Common Ancestor of a Binary Tree
* 74.Search a 2D Matrix


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


## 236. Lowest Common Ancestor of a Binary Tree

[https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

### Description
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

### Solution
```python
# 终止条件
        if not root: return None
        # 每一层递归执行的操作
        if root.val == p.val or root.val == q.val:
            return root
        # dfs+后序遍历，向下一层进行递归，分为两个子问题
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 合并两个子问题的结果：
        # 若两个子树都匹配，返回根节点。
        # 若左子树匹配则返回左子树，若只有右子树匹配返回右子树
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
```
思路：只有两种可能：  
1. p,q在当前节点两侧子节点。
2. p, q在当前节点单侧子树。  
向下递归的过程左右子树谁先匹配到p,q, 就优先递归地向上返回哪个节点。同时在一层匹配到则返回父节点。

## 74. Search a 2D Matrix(Medium)

[https://leetcode-cn.com/problems/search-a-2d-matrix/](https://leetcode-cn.com/problems/search-a-2d-matrix/)

### Description
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
* 每行的元素从左到右升序排列。
* 每列的元素从上到下升序排列。

### Solution one(Brute Force)
```python
class Solution:
    def searchMatrix(self, matrix, target):
        # 把二维矩阵重构为一维数组，直接判断数组里是否有目标元素
        res = [i for j in matrix for i in j]
        if target in res:
            return True
        else:
            return False
```
**思路**：暴力解法，忽略矩阵的元素排列特殊性，当作一般乱序矩阵，直接在矩阵中搜索目标元素。时间复杂度为$O(2N)$, 空间复杂度为$O(N)$

### Solution two(从两个对角开始搜索)
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 当矩阵为空时
        if len(matrix) == 0:
            return False
        # 从矩阵右上角开始搜索，也可以从左下角
        i = 0
        j = len(matrix[0]) - 1
        # 设置终止条件
        while i < len(matrix) and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False
```

**思路**：首先要注意到该矩阵的特殊结构，行依次递增，列依次递增。在一维数组中若数组有序，我们考虑二分法去查找。而在二维数组中我们也可以使用类似的思想，我们注意到矩阵的右上角和左下角的元素皆处在一个一维数组中间的位置，例如右上角的元素，下方的元素均大于它，左边的元素皆小于它。此时通过当前元素和目标元素的对比我们就可以筛去一个方向的元素，一行或一列，向左或者向下移动一个位置，当前元素便处于新的行和列的中间位置，再和目标元素进行比较，直到找到目标元素或运动到矩阵对角位置。时间复杂度对应$O(R+C)$, 空间复杂度为$O(1)$
