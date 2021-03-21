|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | stack&queue |  2021-03-15 | Shawn_Song  | leetcode
-------

# 栈和队列


## Content
* 20.valid parentheses
* 641.Design Circular deque
* 155.Min stack
* 239.Sliding Window Maximum
* 1021.Remove Outermost Parentheses

## 20. valid parentheses(Easy)

[https://leetcode-cn.com/problems/valid-parentheses/](https://leetcode-cn.com/problems/valid-parentheses/)


### Solution
```python
class Solution:
    def isValid(self, s: str) -> bool:
        left_brackets = '({['
        right_brackets = ')}]'
        if s[0] in right_brackets or len(s) % 2 != 0:
            return False
        stack = []
        for bracket in s:
            if bracket in left_brackets:
                stack.append(bracket)
            elif bracket in right_brackets:
                if len(stack) == 0:
                    return False
                pair = stack[-1]
                if left_brackets.index(pair) == right_brackets.index(bracket):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
```

**思路**：使用list实现栈的功能，将左边类型的括号压栈，右边类型的括号与栈顶元素比较，配对则弹出尾部元素。

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


## 155. Min Stack(Easy)

[https://leetcode-cn.com/problems/min-stack/](https://leetcode-cn.com/problems/min-stack/)

### Description
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

### Solution
```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return  self.stack[-1][1]
```
思路：重点在于如何在常数时间内获得最小数。需要每次push操作都把当前栈内最小元素存在当前节点。原本栈里每个元素储存一个值，现在使用一个tuple储存当前值和当前栈中最小元素。

## 239. Sliding Window Maximum(Hard)

[https://leetcode-cn.com/problems/sliding-window-maximum/](https://leetcode-cn.com/problems/sliding-window-maximum/)

### Description
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

### Solution
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque, res = [], []
        for i in range(len(nums)):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            if i - deque[0] > k-1:
                deque.pop(0)
            if i >= k-1:
                res.append(nums[deque[0]])
        return res
```
思路：遍历数组过程，依次将数值索引放入队列。保证队列中从头到尾存放的索引对应的值是从大到小，保证deque[0]是当前窗口内的最大值的索引。当队列内最大值的索引与当前值索引的距离大于窗口距离，说明已经超出了该最大值的作用范围，此时推出deque[0]。


##  1021. Remove Outermost Parentheses(Easy)

[https://leetcode-cn.com/problems/remove-outermost-parentheses/](https://leetcode-cn.com/problems/remove-outermost-parentheses/)

### Solution
```python
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, stack = '', []
        for bracket in S:
            if bracket == '(':
                if stack: res += bracket
                stack.append(bracket)
            elif bracket == ')':
                stack.pop()
                if stack: res += bracket
        return res
```
思路：题意是将字符串拆成几个能用()包起来的子字符串，然后把外面的（）去掉返回。创建一个栈，两两配对，两个if stack,判断就是考虑最外层的（）不加入返回值。



