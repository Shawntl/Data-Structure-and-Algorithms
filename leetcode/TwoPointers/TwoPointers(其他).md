|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | TwoPointers（其他） |  2020-11-30 | Shawn_Song  | leetcode
-------

# 双指针（其他类型）

* 88 Merge Sorted Array
* 524 Longest Word in Dictionary through Deleting
* 350 Intersection of two arrays II


## 88. Merge Sorted Array(Easy)

[https://leetcode-cn.com/problems/merge-sorted-array/](https://leetcode-cn.com/problems/merge-sorted-array/)


### Description
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

### Solution
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s1, s2, end = m-1, n-1, m+n-1
        while s1 >= 0 and s2 >= 0:
            if nums1[s1] >=  nums2[s2]:
                nums1[end] = nums1[s1]
                s1 -= 1
            else:
                nums1[end] = nums2[s2]
                s2 -= 1
            end -= 1
        if  s2 >= 0:
            nums1[:s2+1] = nums2[:s2+1]
```

**思路**：这道题最重要的思想是从大到小(从后往前)遍历两个数组。在merge过程中要有效利用nums1中n大小的空间。这n的大小对应nums2的数组长度，nums2中的元素需要插入到nums1中才能完成合并，如果从两个数组开头开始遍历，就会发生，nums1数组元素被覆盖的情况，如果进行频繁交换，会把问题变得复杂。而如果设置三个指针，从后往前填元素，现将大的元素从后往前放入数组，则nums2中元素插入nums1中的位置会及时被挪到后面，不会被覆盖。


## 524. Longest Word in Dictionary through Deleting(Medium)

[https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/)

### Description
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        max_length = 0
        max_idx = -1
        for i, string in enumerate(d):
            m, n, cur_length = 0, 0, 0
            while m < len(s) and n < len(string):
                if s[m] == string[n]:
                    cur_length += 1
                    m += 1
                    n += 1
                else:
                    m += 1
            # 子字符串不在母字符串中
            if n < len(string):
                continue
            # 更新最大值
            if cur_length > max_length:
                max_length = cur_length
                max_idx = i
            # 当与当前最大值相等时，进一步比较字符串的字典序
            elif cur_length == max_length:
                if string < d[max_idx]:
                    max_idx = i
                else:
                    continue

        if max_idx == -1:
            return ''
        return d[max_idx]
```

**思路**：本题思路比较简单，两个指针一个遍历字符串，一个挨个遍历list里的字符串。记录下每个子字符串在母字符串中的长度，更新最大值，并记录当前最大值下标。注意题目要求返回字典序最小的字符串元素，所以当两个字符串对应在母字符串的最长子序列长度相等时，再进行一步字典序的比较。


## 350.Intersection Of Two Arrays II(Easy)

[https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

### Description
给定两个数组，编写一个函数来计算它们的交集。

### Solution
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
```
思路：
第一步要将两个list排序。  
第二步初始化两个指针从两个list头部遍历，相等则添加元素，不相等时，小的元素向前移一位。   
时间复杂度为O(max(nlogn, mlogm, m+n)),空间复杂度为O(1)。如使用hash表时间复杂度较低，空间复杂度为O(n).




































