|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | TwoPointers（对撞指针） |  2020-11-23 | Shawn_Song  | leetcode
-------

# 双指针（对撞指针）

* 167 Two Sum II - Input arraay is sorted
* 633 Sum of Square Numbers
* 345 Reverse Vowels of a String
* 125 Valid Palindrome
* 680 Valid Palindrome II
* 344 Reverse String
* 541 Reverse String II
* 917 Reverse Only Letters
* 151 Reverse Words in a String
* 11.Container With Most Water


## 167. Two Sum II - Input arraay is sorted(Easy)
[https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

### Description
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

### Solution One(hash map)
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(numbers)):
            first = target - numbers[i]
            if first in num_dict.keys():
                return [num_dict[first], i+1]
            else:
                num_dict[numbers[i]] = i + 1
```
**思路**：同题1.Two Sum, 一次遍历，利用target值减去当前值，求出另外一个元素值，同时用字典保存遍历过的元素下标。该方法时间复杂度为$O(n)$. 没有利用数组本身的有序性。  

### Solution Two(Two pointers)
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return
```
**思路**：利用有序数组的这一特性，因为是查找两个元素并且有相关性，不好用二分法。首先我们分析一下这道题如何一步步想到用双指针求解： 看到题第一反应是暴力求解，从第一个元素挨个双重遍历计算是否等于target，但因为是有序数组，当选定第一个元素后，挨个比较n次和后面的元素之和才能扔掉一个元素。如果利用两个指针从两端遍历，因为数组有序，如果大于target值只需要右端移动一位，这是当前操作能执行的最小的缩小值，如果小于target值，只需要左端移动一位。这样每比较一次就可以扔掉一个元素，很好的利用了有序数组这个特性。这种方法的时间复杂度也是$O(N)$.   
那么本题中两种方法的时间复杂度在一个数量级上，怎么比较呢。个人认为应该分情况讨论，当target值偏大时，方法二比较能快速的找到target，当target值偏小时，方法一比较能快速的找到target.实际应用时要分析数据的总体情况计算平均时间复杂度。


## 633. Sum of Square Numbers(Medium)

[https://leetcode-cn.com/problems/sum-of-square-numbers/](https://leetcode-cn.com/problems/sum-of-square-numbers/)

### Description
给定一个非负整数c ，你要判断是否存在两个整数a和b，使得 a2 + b2 = c.

### Solution(Two Pointers)
```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)
        while left <= right:
            if (left**2 + right**2) == c:
                return True
            elif (left**2 + right**2) > c:
                right -= 1
            else:
                left += 1
        return False
```

**思路**：思路同上一题，确定a和b的范围，一定属于0-sqrt(c)。平方和大了区间就向左收缩，小了就向右收缩。不同的是本题考虑a=b的情况，所以a=b写在while循环中。


## 345. Reverse Vowels of a String(Easy)

[https://leetcode-cn.com/problems/reverse-vowels-of-a-string/](https://leetcode-cn.com/problems/reverse-vowels-of-a-string/)

### Description
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

### Solution
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left],  s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in vowels:
                right -= 1
            elif s[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(s)
```

**思路**：反转的主要思想是对应位置交换，两端交换，所以想到使用前后两个指针。只要注意两两交换一定要是从两端开始数的同一位置元音字母。先找到一端的元音字母，另外一端不断移动去找和它匹配的元音字母，交换后两端要同时向中间收缩。


## 125. Valid Palindrome(Easy)

[https://leetcode-cn.com/problems/valid-palindrome/](https://leetcode-cn.com/problems/valid-palindrome/)

### Description
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

### Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            elif s[left].isalnum():
                right -= 1
            elif s[right].isalnum():
                left += 1
            else:
                right -= 1
                left += 1
        return True
```

**思路**： 和上题思想类似，从两端开始比较，两个指针慢慢往中间收缩，相等时终止。


## 680. Valid Palindrome II(Easy)

[https://leetcode-cn.com/problems/valid-palindrome-ii/](https://leetcode-cn.com/problems/valid-palindrome-ii/)


### Description
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

### Solution
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 2: return True

        def isPalindrome(l):
            start, end = 0, len(l) - 1
            while start < end:
                if l[start] == l[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
        return True
```

**思路**：这道题和上一道题不一样的是当前左指针value和右指针value不相等时，因为字符串没有非字符数字元素，所以此时一定有一个指针的value是多余的元素。那么如果仅有这一个多余的元素，除去这个元素后剩下的字符串(左指针往右或右指针往左)一定符合回文规则，如果不符合则多余元素不止一个，返回False。


## 344.Reverse String(Easy)

[https://leetcode-cn.com/problems/reverse-string/](https://leetcode-cn.com/problems/reverse-string/)

### Description
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

### Solution
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return
```
**思路**：与前面几道题一样，两个指针从两端开始交换value便可实现列表的反转。

## 541. Reverse String II(Easy)

[https://leetcode-cn.com/problems/reverse-string-ii/](https://leetcode-cn.com/problems/reverse-string-ii/)

### Description
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

### Solution
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        ls = list(s)
        for i in range(0, n, 2*k):
            if n - i < k:
                self.reverse(ls, i, n-1)
            else:
                self.reverse(ls, i, i+k-1)
        return ''.join(ls)

    def reverse(self, ls, start, end):
        while start < end:
            ls[start], ls[end] = ls[end], ls[start]
            start+= 1
            end -= 1
```
思路：利用python切片进行每隔2k一次的循环。

## 917. Reverse Only Letters(Easy)

[https://leetcode-cn.com/problems/reverse-only-letters/](https://leetcode-cn.com/problems/reverse-only-letters/)

### Description
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

### Solution
```python
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S: return S
        left, right = 0, len(S) - 1
        S_l = list(S)
        while left <= right:
            if S_l[left].isalpha() and S_l[right].isalpha():
                S_l[left], S_l[right] = S_l[right], S_l[left]
                left += 1
                right -= 1
            elif S_l[left].isalpha():
                right -= 1
            elif S_l[right].isalpha():
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(S_l)
```
思路：头尾对撞指针，遇到字母交换，遇到非字母向前/向后移动。

## 151. Reverse Words in a String(Medium)

[https://leetcode-cn.com/problems/reverse-words-in-a-string/](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

### Description
给定一个字符串，逐个翻转字符串中的每个单词。

### Solution
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(' ')
        old_ls = [sub_s for sub_s in ls if sub_s]
        left, right = 0, len(old_ls) - 1
        while left < right:
            old_ls[left], old_ls[right] = old_ls[right], old_ls[left]
            left += 1
            right -= 1
        return ' '.join(old_ls)
```
思路：去除空格转为列表反转后再转回字符串。

## 11. Container With Most Water(Medium)

[https://leetcode-cn.com/problems/container-with-most-water/](https://leetcode-cn.com/problems/container-with-most-water/)


### Description
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器

### Solution
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            length = right - left
            width = min(height[left], height[right])
            max_area = max(length*width, max_area)
            if width == height[left]:
                while height[left] <= width and left < right:
                    left += 1
            else:
                while height[right] <= width and left < right:
                    right -= 1
        return max_area
```

**思路**：计算面积是长（横坐标）乘宽（纵坐标），首先我们可以先从长最大时开始搜索，所以想到list两端开始遍历。我们再考虑宽是两个数中较小的那一个，所以下一次遍历两端的指针一定会往中间收缩，长一定会变小，要想面积大于当前值，只有较小的那个数变的比当前大才有可能更新最大值，否则可以一直往前（后）移动指针，知道较小值大于当前值，在进行面积计算。注意指针移动过程中left == right或者 left > right的退出条件，不然会陷入死循环。






































