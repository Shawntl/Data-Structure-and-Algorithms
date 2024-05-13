|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | divide&conquer |  2021-03-21 | Shawn_Song  | leetcode
-------

# 树与递归


## Content
### 分治法
50.Pow(x,n)


## 50. Pow(x,n)(Meidum)

[https://leetcode-cn.com/problems/powx-n/](https://leetcode-cn.com/problems/powx-n/)

### Description
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。


### Solution
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        def div_con(x, n):
            if n < 2:
                return x
            if n % 2 == 0:
                return div_con(x, n // 2)**2
            elif n % 2 == 1:
                return div_con(x, n//2)*div_con(x, (n//2)+1)
        res = div_con(x, n)
        return res
```
思路：用二分法将幂乘分解为两个相同的子问题，时间复杂度为O(logn)。空间复杂度也为O(logN)

