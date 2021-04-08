|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | week05HW |  2021-04-08 | Shawn_Song  | leetcode
-------
  
* 242.Valid Anagram
* 1122.Relative Sort Array
* 300.Longest Increasing Subsequence
* 56.Merge Intervals
* 205.Isomorphic Strings


## 242. Valid Anagram(Medium)

[https://leetcode-cn.com/problems/valid-anagram/](https://leetcode-cn.com/problems/valid-anagram/)

### Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        l_l = list(s)
        l_l.sort()
        s_l = "".join(l_l)
        l_r = list(t)
        l_r.sort()
        s_r = "".join(l_r)
        
        return s_l == s_r
```
思路：两个字符串转list排序，转回字符串，判断是否相等。


## 1122. Relative sort array(Easy)

[https://leetcode-cn.com/problems/relative-sort-array/submissions/](https://leetcode-cn.com/problems/relative-sort-array/submissions/)

### Solution
```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = [0]*1001
        res = []
        for num1 in arr1:
            cnt[num1] += 1
        
        for num2 in arr2:
            res.extend([num2]*cnt[num2])
            cnt[num2] = 0
        
        for i in range(1001):
            if cnt[i] != 0:
                res.extend([i]*cnt[i])
        return res
```
思路：使用计数排序，因为两个数组的数值范围在0～1000以内。

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

## 56. Merge Intervals(Medium)

[https://leetcode-cn.com/problems/merge-intervals/](https://leetcode-cn.com/problems/merge-intervals/)

### Description
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

### Solution
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])
        return res
```
思路：首先想到要对数组中的元素按第一个start位排序，然后从头开始遍历，如果end小于下一个元素start则不合并，否则，将下一个元素和当前元素大的那个end赋给当前元素的end。

## 205. Isomorphic Strings

[https://leetcode-cn.com/problems/isomorphic-strings/](https://leetcode-cn.com/problems/isomorphic-strings/)

### Description
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

### Solution
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))
```
思路：同构字符串中对应位字符的索引（该字符在字符串中第一次出现的下标）一定相等。如果没有重复出现的字符，那么索引一一对应。


