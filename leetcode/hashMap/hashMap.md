|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | LinkedList |  2021-03-13 | Shawn_Song  | leetcode
-------

# Hash表


## Content
* 299.bulls and cows
* 242.Valid Anagram
* 49.Group Anagram
* 438.Find All  Anagrams in a String

## 299. bulls and cows(Easy)

[https://leetcode-cn.com/problems/bulls-and-cows/](https://leetcode-cn.com/problems/bulls-and-cows/)


### Solution(Brute force)
```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 1. 将secret存入字典，键为字符，值为1
        # 2. 遍历第一遍字符，计算bull数
        # 3. 遍历第二遍字符，计算cow数
        secret_dict = {x:secret.count(x) for x in secret}
        n = len(secret)
        bull, cow = 0, 0
        for i in range(n):
            if guess[i] == secret[i]:
                bull += 1
                secret_dict[guess[i]] -= 1
                
        for j in range(n):
            if guess[j] not in secret_dict.keys():
                continue
            
            if guess[j] != secret[j] and secret_dict[guess[j]] > 0:
                secret_dict[guess[j]] -= 1
                cow += 1
    
        return str(bull)+'A'+str(cow)+'B'
```

**思路**：暴力法，两次遍历。利用字典先将频数存起来。


## 242. Valid Anagram(Easy)

[https://leetcode-cn.com/problems/valid-anagram/](https://leetcode-cn.com/problems/valid-anagram/)

### Description
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

### Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
```
思路：使用字典记录字符串内元素频数，比较字典是否相同。


## 49.Group Anagram(Medium)

[https://leetcode-cn.com/problems/group-anagrams/](https://leetcode-cn.com/problems/group-anagrams/)

### Description
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

### Solution
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for gram in strs:
            key = ''.join(sorted(gram))
            if key in anagram_dict.keys():
                anagram_dict[key].append(gram)
            else:
                anagram_dict[key] = [gram]
        return [group for group in anagram_dict.values()]

```
思路：首先想到创建一个字典，一个key映射一个anagram组，那么怎么表示key呢？key的特点是唯一的确定一个anagram组，所有的anagram字符频数一样只是顺序不同，但是key不能是一个可迭代的数据类型，例如字典。所以想到所有anagram按字母排序后是一样的，就以排序后的字符串作为字典的键值。

## 438. Fina All Anagrams in a String(Medium)

[https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

### Description
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

### Solution
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        res = []
        p_dict = collections.Counter(p)
        sub_s_dict = collections.Counter(s[0:m])
        if p_dict == sub_s_dict:
            res.append(0)
        for i in range(1, n-m+1):
            if sub_s_dict[s[i-1]] > 1:
                sub_s_dict[s[i-1]] -= 1
            else:
                del sub_s_dict[s[i-1]]
            if s[i+m-1] in sub_s_dict.keys():
                sub_s_dict[s[i+m-1]] += 1
            else:
                sub_s_dict[s[i+m-1]] = 1
            if sub_s_dict == p_dict:
                res.append(i)

        return res
```
思路：滑动窗口，每滑动一次做一次相同异位词比对。异位词比对方法和上一题一样。每一次滑动不需要重新创建字典，只需要统计出窗口的字符和进窗口的字符计数即可。








