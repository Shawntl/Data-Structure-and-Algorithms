|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | String |  2021-04-15 | Shawn_Song  | leetcode
-------

# 字符串


## Content  
* 709.To Lower Case
* 58.Length of Last Word
* 771.Jewels and Stones
* 387.First Unique Character in a String
* 8.String to Integer
* 14.Longest Common Prefix
* 557.Reverse Words in a String III


## 709. To Lower Case(Easy)

[https://leetcode-cn.com/problems/to-lower-case/](https://leetcode-cn.com/problems/to-lower-case/)

### Description
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。


### Solution
```python
class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for s in str:
            if s.isupper():
                res.append(s.lower())
            else:
                res.append(s)
        return ''.join(res)
```

## 58. Length of Last Word(Easy)

[https://leetcode-cn.com/problems/length-of-last-word/](https://leetcode-cn.com/problems/length-of-last-word/)

### Description
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

### Solution
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        length = 0
        flag = True
        for i, sub_str in enumerate(s):
            if sub_str == ' ':
                flag = False
                continue
            else:
                if flag:
                    length += 1
                else:
                    length = 1
                    flag = True
        return length
```
思路： 遍历字符串，设置一个flag当遍历到空格时置为False, 直到遍历到单词第一个字母置为True.

## 771. Jewels and Stones(Easy)

[https://leetcode-cn.com/problems/jewels-and-stones/submissions/](https://leetcode-cn.com/problems/jewels-and-stones/submissions/)

### Solution
```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for stone in stones:
            if stone in jewels:
                res += 1
        return res
```
思路：遍历石头字符串看每个字符是否在宝石字符串中。

## First Unique Character in a String(Easy)

[https://leetcode-cn.com/problems/first-unique-character-in-a-string/](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)

### Description
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


### Solution
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for sub_s in s:
            if sub_s in m.keys():
                m[sub_s] += 1
            else:
                m[sub_s] = 1

        for i, sub_s in enumerate(s):
            if m[sub_s] == 1:
                return i
        return -1
```
思路：创建一个字典计数，然后遍历字符找到第一个计数为一的字符。


## String to Integer(atoi)(Medium)

[https://leetcode-cn.com/problems/string-to-integer-atoi/](https://leetcode-cn.com/problems/string-to-integer-atoi/)

### Solution
```python
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0 or len(s.strip()) == 0: return 0
        s = s.strip()

        sign = -1 if s[0] == '-' else 1
        if s[0] in '-+': s = s[1:]

        res, i = 0, 0
        while i < len(s) and s[i].isdigit():
            res = res*10 + (ord(s[i]) - ord('0'))
            i += 1
        return max(-2**31, min(sign*res, 2**31 - 1))
```
思路：首先去除前后空格，其次判断符号，最后转换开头的数字字符串。

## 14. Longest Common Prefix(Easy)

[https://leetcode-cn.com/problems/longest-common-prefix/](https://leetcode-cn.com/problems/longest-common-prefix/)

### Description
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。


### Solution
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0: return ''
        res = ''
        for j, prefix in enumerate(strs[0]):
            i = 1
            while i < len(strs) and j < len(strs[i]):
                if strs[i][j] == prefix:
                    i += 1
                else:
                    break
            if i == len(strs):
                res += prefix
            else:
                break
        return res
```
思路：外层循环首先看每个字符串的第几位（从第一位开始循环），里层循环比较每个字符串的当前位是否相同。时间复杂度为$O(n^2)$。


## 557. Reverse Words in a String III

[https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)

### Description
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

### Solution
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(' ')
        res = []
        for sub_s in ls:
            res.append(sub_s[::-1])
        return ' '.join(res)
```
思路：split -> reverse(用切片) -> join






