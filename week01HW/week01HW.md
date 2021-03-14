|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | week01HW |  2021-03-14 | Shawn_Song  | leetcode
-------
  
* 66.Plus One
* 189.Rotate array
* 242.Valid Anagram
* 641.Design circular deque
* 49.Group Anagram



## 66. Plus One(Easy)

[https://leetcode-cn.com/problems/plus-one/](https://leetcode-cn.com/problems/plus-one/)

### Solution
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] + 1 == 10:
                digits[i] = 0
                i -= 1
            else:
                digits[i] = digits[i] + 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits
```
思路：注意考虑满十进位就行。时间复杂度O(N), 遍历一次即可，空间复杂度O(1)。


## 189. Rotate array(Medium)

[https://leetcode-cn.com/problems/rotate-array/](https://leetcode-cn.com/problems/rotate-array/)

### Description
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

### Solution
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def swap(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        nums.reverse()
        swap(0, k-1)
        swap(k, n-1)
```

思路：三次反转：  
1. 第一次整个数组反转，此时原数组后k个元素顺序和前 n-k个元素顺序与正确旋转数组的结果不一致，需要分别进行反转。
2. 反转前k个元素。
3. 反转后n-k个元素。

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


## 641. Design Circular deque(Medium)

[https://leetcode-cn.com/problems/design-circular-deque/](https://leetcode-cn.com/problems/design-circular-deque/)

### Description
设计实现双端队列。

### Solution
```python
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max_len = k
        self.cur_len = 0
        self.front, self.last = 0, 0
        self.queue = [0]*k
        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.max_len == self.cur_len:
            return False
        self.front = (self.front - 1) % self.max_len
        self.queue[self.front] = value
        self.cur_len += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.max_len == self.cur_len:
            return False
        self.queue[self.last] = value
        self.last = (self.last + 1) % self.max_len
        self.cur_len += 1
        return True
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.cur_len == 0:
            return False
        self.front = (self.front + 1) % self.max_len
        self.cur_len -= 1
        return True
        
    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.cur_len == 0:
            return False
        self.last = (self.last - 1) % self.max_len
        self.cur_len -= 1
        return True
        
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.cur_len == 0:
            return -1
        return self.queue[self.front]
        
    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.cur_len == 0:
            return -1
        return self.queue[self.last-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cur_len == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cur_len == self.max_len
```

思路：初始化两个指针，一个指针是要指向队列头部当前元素索引，一个指针要指向队列尾部下一个加入元素索引。尾部加入元素是与数组索引增加顺序一致的，头部增加元素是从数组尾部依次向头部方向添加。删除对应各自反方向的顺序。  
本题不需要考虑数组加满后再添加元素的操作，如队列已满，则返回false。



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





















