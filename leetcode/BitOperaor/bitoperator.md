|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | Bit Operator |  2021-04-06 | Shawn_Song  | leetcode
-------
 
# 位运算
## content
* 190.Reverse Bits
* 191.Number of 1 Bits
* 231.Power of Two
* 338.Counting Bits
* 547.Number of Provinces


## 190. Reverse Bits(Easy)

[https://leetcode-cn.com/problems/reverse-bits/](https://leetcode-cn.com/problems/reverse-bits/)

### Description
颠倒给定的 32 位无符号整数的二进制位。

### Solution
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
```  
思路：先用n & 1计算n的右边第一位，res左移一位后n的右边第一位放到自己的右边第一位。最后n右移一位。  


## 191. Number of 1 Bits(Easy)

[https://leetcode-cn.com/problems/number-of-1-bits/](https://leetcode-cn.com/problems/number-of-1-bits/)

### Description
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

### Solution
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n & (n-1)
            res += 1
        return res
```
思路：不断清零最低位（从右往左第一个为1的位）的1，一旦数值为零说明清除了所有1，返回count。


## 231. Power of Two(Easy

[https://leetcode-cn.com/problems/power-of-two/](https://leetcode-cn.com/problems/power-of-two/)

### Description
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

### Solution
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while n & 1 == 0 and i < 32:
            n >>= 1
            i += 1
        if i < 32:
            if n & (~1) != 0:
                return False
            else:
                return True
        else:
            return False
```
思路： 二进制中有且只有一位为1的数才是2的幂，我们从低位开始遍历，一旦碰到1，退出循环，判断剩下高位是否为0即可。


## 338. Counting Bits(Medium)

[https://leetcode-cn.com/problems/counting-bits/](https://leetcode-cn.com/problems/counting-bits/)

### Description
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

### Solution
```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        if num == 0: return res
        cur_count = 0
        for i in range(1, num+1):
            if ((i-1) & 1) == 0:
                res.append(res[i-1] + 1)
            else:
                pre_1_cnt = 0
                pre_val = i-1
                while (pre_val & 1) == 1:
                    pre_val >>= 1
                    pre_1_cnt += 1
                res.append(res[i-1] - pre_1_cnt + 1)
        return res
```
思路： 位运算+动态规划，每一个数中1的个数都可以由上一个数中1的个数计算得到，如果上一个数，最后一位为0，则res[i] = res[i-1]+1.如果上一个数最后一位为1，则计算出上一个数最低位连续为1的个数pre_1_cnt,res[i] = res[i-1] - pre_1_cnt + 1  

## 547. Number of Provinces(Medium)

[https://leetcode-cn.com/problems/number-of-provinces/](https://leetcode-cn.com/problems/number-of-provinces/)

### Solution
```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self._union(p, i, j)
        return len(set([self._parent(p, i) for i in range(n)]))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p1] = p2

    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i; i = p[i]; p[x] = root
        return root
```
思路： 使用并查集模版，将相连的两个集合进行union，最后遍历p中独立不相交（头元素不同）的集合。
