|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | array |  2020-11-03 | Shawn_Song  | leetcode
-------

* 1 Two Sum
* 283 Move Zeroes
* 566 Reshape the Matrix
* 485 Max Consecutive Ones
* 240 Search a 2D Matrix II
* 378 Kth Smallest Element in a Sorted Matrix
* 645 Set Mismatch
* 287 Find the duplicate number
* 667 Beautiful Arrangement II
* 697 Degree of an Array
* 766 Toeplitz Matrix
* 565 Array Nesting
* 769 Max Chunks To Make Sorted
* 66 Plus One
* 189 Rotate array
* 15 3Sum


## 1. Two Sum(Easy)

[https://leetcode-cn.com/problems/two-sum/](https://leetcode-cn.com/problems/two-sum/)

### Description
给定一个整数数组nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。并且和为目标值的两个整数不能是数组中的同一个元素。

### Solution one(Brute Force)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```
思路：暴力解法，两层遍历数组直到找到求和等于目标值的整数对，时间复杂度为$O(n^2)$,空间复杂度为$O(1)$

### Solution two(use hash table)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个字典用于记录扫描过的数值下标
        h = {}
        # 遍历一遍数组
        for i, num in enumerate(nums):
            # 通过目标值和当前数值的差计算另一个数值大小
            n = target - num
            # 判断字典中是否保存过该数值
            if n not in h:
                # 如果记录中没有该数值出现，将当前数值的下标保存在字典中
                h[num] = i
            # 否则便找到了结果数值对儿
            else:
                return [h[n], i]
```
**思路**： 主要是利用了hash table将遍历过的数值下标保存起来，便于快速查找，致使只需遍历一遍数组就找到解。时间复杂度优化到$O(n)$,空间复杂度增加为$O(n)$.

## 283. Move Zeros(Easy)

[https://leetcode-cn.com/problems/move-zeroes/](https://leetcode-cn.com/problems/move-zeroes/)

### Description
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
并且要求在数组内操作，不得创建新的内存，即空间复杂度要求$O(1)$

### Solution(Two pointers)
```python
class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 慢指针，用于指向非零元素
        idx = 0
        # 进行第一次遍历，目的是按顺序找到所有非零元素的值
        for num in nums:
            if num != 0:
                nums[idx]= num
                idx += 1
        # 第二次遍历
        while idx < len(nums):
            #找到所有非零元素后，idx指针后的位置全部赋值0
            nums[idx] = 0
            idx += 1

```
**思路**： 一个快指针第一次对整个数组进行遍历，依次找到所有非零元素。慢指针用于标记非零元素应该放置的位置，只有找到一个非零元素，慢指针才会递增。第一次遍历将所有非零元素依次排列在数组前n-m位，n为数组长度, m 为0的个数。然后进行第二次遍历，将剩下的m位置零。 时间复杂度为O(N+M),空间复杂度为O(1).

## 566. Reshape the Matrix(Easy)

[https://leetcode-cn.com/problems/reshape-the-matrix/](https://leetcode-cn.com/problems/reshape-the-matrix/)

### Description
给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

### Solution(Naive)
```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        current_r = len(nums)
        current_c = len(nums[0])
        # 如果要求重建的矩阵元素总数不等于原矩阵元素总数，则返回原矩阵
        if (current_c * current_r) != c * r:
            return nums
        # 将原矩阵所有元素取出放入一个一维数组
        for i in range(1, len(nums)):
            nums[0].extend(nums[i])
        
        # 利用python切片，重建要求的新数组
        result = [nums[0][j:j+c] for j in range(0, len(nums[0]), c)]
        return result
```

**思路**： 第一步将二维矩阵化为一维数组，第二步利用切片重构新的二维矩阵。时间复杂度为$O(current_r+r)$, 空间复杂度为$O(2(r*c))$

## 485. Max Consecutive Ones(Easy)

[https://leetcode-cn.com/problems/max-consecutive-ones/](https://leetcode-cn.com/problems/max-consecutive-ones/)

### Description
给定一个二进制数组， 计算其中最大连续1的个数。

### Solution(一次遍历)

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
         res, max_num = 0, 0
         for i in nums:
             if i == 1:
                 res += 1
                 if res > max_num:
                     max_num = res
            else:
                res = 0
        return max_num
```

**思路**： 遍历过程中遇到0，res置零，遇到1累加。重点在于最大值变量max_num的更新，第一次自己写的时候容易陷入在算完每一段连续1的子序列遇到0时再比较当前长度与之前最大值的大小。更简洁的方式是把max_num的更新写在当前连续1的子序列遍历下，同步更新max_num。**整个过程类似于res在数组上指向1时累加，指向0时置零，并实时更新当前res的最大值。**


## 240. Search a 2D Matrix II(Medium)

[https://leetcode-cn.com/problems/search-a-2d-matrix-ii/](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)

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


## 378. Kth Smallest Element in a Sorted Matrix（Medium）

[https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)

### Description
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

### Solution One(Brute Force)
```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = sorted(sum(matrix, []))
        return res[k-1]
```

**思路**： 直接将二维矩阵化为一维数组并排序，直接找到第k个元素，完全不考虑矩阵的排列规则。时间复杂度$O(n^2logn^2)$, 空间复杂度$O(n^2)$, n为矩阵的行数。

### Solution Two(二分法 + 规则矩阵的对角搜索思想)
```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(mid):
            '''
            利用矩阵的性质，从矩阵左下角开始搜索，计算小于等于mid
            的元素有多少个
            '''
            i, j = n - 1, 0
            num = 0
            # 设置终止条件是搜索到右上角为止
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j + = 1
                else:
                    i -= 1
            return num >= k
            
        # 从矩阵左上角和右下角分别取得所有元素中的最小值和最大值
        left, right = matrix[0][0], matrix[-1][-1]
        # 设定终止条件，当left == right时便找到了目标值
        while left < right:
            # 取中值时向左边界靠近
            mid = (left + right) // 2
            # 比较中值和kth smallest value, 方法是计算小于等于中值的元素个数
            if check(mid):
                # 若小于等于中值的元素个数大于等于k，继续在[left, mid]中二分
                right = mid
            else:
                # 否则在[mid+1, right]中二分
                left = mid + 1
        return left
```

**思路**： 第一个主要思想是利用二分法找到数组中值，因为矩阵的性质，我们可以定位到最大值和最小值在两个对角。找到中值后如何将中值和第k小个元素做比较进行下一步迭代？这又利用了矩阵的性质，和上一题的思想相似，从左下角开始搜索既可以找到特定目标值（上一题），也可以计算出小于目标值的元素个数，这里的目标值就是中值。然后再将元素个数与k做比较，进行二分收缩。
这道题思路清晰后，在代码实现上的注意点在于，二分法的边界条件，如何收缩，最终找到kth smallest element。  
由于利用了矩阵性质，时间复杂度为$O(nlog(right - left))$,  空间复杂度为O(1).

## 645. Set Mismatch(Easy)

[https://leetcode-cn.com/problems/set-mismatch/](https://leetcode-cn.com/problems/set-mismatch/)

### Description
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

### Solution One(排序后进行一次遍历)
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = sorted(nums)
        # 考虑缺失元素在第一位的情况
        miss = 1
        # 考虑缺失元素在最后一位的情况
        if res[-1] != len(res):
            miss = res[-1]
        for i in range(1, len(res)):
            if res[i] - res[i-1] == 1:
                continue
            elif res[i] == res[i-1]:
                repeti = res[i]
            elif res[i] - res[i-1] == 2:
                miss = res[i] - 1
        return [repeti, miss]
```
**思路**： 第一步对无序数组排序, 第二步遍历有序数组，当前位与上一位元素一样则找到重复元素，当前位与上一位差值为2则找到缺失数组。边界情况是缺失元素在有序数组第一位和最后一位的时候。时间复杂度为排序时间复杂度$O(nlogn)$, 空间复杂度为$O(logn)$

### Solution Two(利用字典保存元素出现次数)
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        res_dict = Counter(nums)
        for i in range(1, len(nums)+1):
            if i not in res_dict:
                miss = i
            elif res_dict[i] == 2:
                repeti = i
        return [repeti, miss]
```

时间复杂度：O(n), 空间复杂度：O(n)

### Solution Three(利用数学思想)
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = (n*(n+1)) / 2
        lack = total - sum(set(nums))
        repeti = sum(nums) + lack - total
        return [int(repeti), int(lack)]
```

**思路**：首先通过set方法去除数组中的重复元素，利用等差数列求和减去去除重复元素的数组就可以得到缺失元素。进一步计算可得重复元素。主要利用了顺序数组的性质和set函数。时间复杂度O(N),  空间复杂度O(N)。


## 287. Find the duplicate number(Medium)

[https://leetcode-cn.com/problems/find-the-duplicate-number/](https://leetcode-cn.com/problems/find-the-duplicate-number/)

### Description
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
* 不能更改原数组
* 只能使用额外的O(1)的空间

### Solution(二分查找)
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 二分查找问题首先找到最大值和最小值
        n = len(nums)
        left, right = 1, n-1
        # 确定终止条件
        while left < right:
            count = 0
            # 计算小于等于中值的元素个数
            for num in nums:
                if num <= mid:
                    count += 1
            mid = （left + right） // 2
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left
```

**思路**：首先要思考如何找到这个重复的元素，这里可以联系上上题378题：我们通过二分法的中间值去计算**小于等于**中间值的元素个数是否**大于等于**k，然后向左收缩查找空间。本题的思路类似，我们通过二分法的中间值去计算数组中**小于等于**中间值的元素个数是否**严格大于**中间值，因为这里只有**严格大于**中间值才能说mid左侧数组中一定有一个重复的元素。这里和387题还有一点不同是，387题在搜索小于等于mid的元素个数时借助了矩阵的性质，每次循环只用遍历矩阵的行数次，而本题由于是利用时间换空间，不能改变数组，所以每一次计算都要遍历整个数组。所以时间复杂度为$O(nlog(right-left))$, 空间复杂度为 O(1). 


## 667.Beautiful Arrangement II(Medium)

[https://leetcode-cn.com/problems/beautiful-arrangement-ii/](https://leetcode-cn.com/problems/beautiful-arrangement-ii/)

### Description
给定两个整数 n 和 k，你需要实现一个数组，这个数组包含从 1 到 n 的 n 个不同整数，同时满足以下条件：
* 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数；.
* 如果存在多种答案，你只需实现并返回其中任意一种.

### Solution(找规律构造数列)
```python
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # 表示k个不同的差值，只需要【1, k+1]个数即可，数组中初始化的1就是k+1中的1 
        result = [1]
        # 用于构造符号间隔变换的数列
        flag = True
        # 循环找到构成[1,k]个差值的数列([1,k+1]中的【1,k])
        for i in range(k, 0, -1):
            if flag:
                result.append(result[-1] + i)
                flag = False
            else:
                result.append(result[-1] - i)
                flag = True
        # 将剩下的元素依次放到k+1个元素后，因为是依次，差值均为1.
        for i in range(1+k+1, n+1):
            result.append(i)
        return result
```

**思路**： 数组是一个以1为间隔的等差数列，我们要构造一个有规律的数列，使得它的差在[1, k]中。我们发现用【1，k+1]内个数就能找到这样的数列。即：  
a1 = 1, a2 = a1 + k, a3 = a2 - (k-1), a4 = a3 + (k -2),....  
注意上面这个递推数列的前后项依赖关系代表了k个差值，以及运算符号的变换保证了数列最大值不超过k+1。
剩下的n-(k+1)个数则依次填入数组，因为差值均为一，不影响结果。时间复杂度：$ O(N)$,  空间复杂度为$O(N)$


## Degree of an Array(Easy)

[https://leetcode-cn.com/problems/degree-of-an-array/](https://leetcode-cn.com/problems/degree-of-an-array/)

### Description
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

### Solution(利用hash map, 空间换时间)
```python
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 创建三个hash map用来储存每个元素的频数，元素在数组中出现的起始下标，终止下标。
        left, right, count = {}, {}, {}
        for i, k in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        # 计算数组的度
        degree = max(count.values())
        ans = len(nums)
        # 找到满足数组度的元素中的最小间隔
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans
```

**思路**： 得到该题的解首先要找到每个元素出现的频数，然后找到频数最高的元素。在这些频数出现最高的元素中进一步计算数组中该元素第一次出现的位置和最后一次出现的位置之间的间隔就是输出。所以构造了三个hash map分别通过一次遍历数组，储存每个元素的频数、第一次在数组中出现的位置和最后一次出现的位置。第二次遍历频数字典。


## 766. Toeplitz Matrix(Easy)

[https://leetcode-cn.com/problems/toeplitz-matrix/](https://leetcode-cn.com/problems/toeplitz-matrix/)

### Description
如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵。
给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。

### Solution(特殊矩阵遍历)
```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # 按行一个个遍历矩阵中的元素
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                # 边界条件是只有一行或一列时返回True
                if r == 0 or c == 0 or matrix[r-1][c-1] == val:
                    continue
                else:
                    return False
        return True
```

**思路**：我们发现只要每个元素都满足当前元素与它左上角的元素相等，该矩阵就是Toeplitz矩阵。即val == matrix[r-1][c-1]。但是考虑到遍历时的边界条件即第一行和第一列的元素没有左上角的元素，也就是当遍历到第一行和第一列元素时自动向下一个元素遍历，不进行判断，这也巧妙的考虑了矩阵1只有一行或1一列时的情况。剩下的元素只要全部满足和左上角元素相等就可以返回True. 这样也不需要用特殊的方法遍历矩阵，只要从第一行开始挨个遍历元素就好了。


## 565. Array Nesting(Medium)

[https://leetcode-cn.com/problems/array-nesting/](https://leetcode-cn.com/problems/array-nesting/)

### Description
索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。
假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。


### Solution One(Brute Force)
```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 1
        for i in range(len(nums)):
            # 构建一个s数列
            s = []
            index = i
            while nums[index] not in s:
                s.append(nums[index])
                # 当前元素在数组中的下标是s数列中的上一个元素值
                index = s[-1]
            max_length = max(max_length, len(s))
        
        return max_length
```

**思路**： 暴力求解就是依次以数组中的元素为起始索引构造数列，找到最长的可能数列长度。时间复杂度为$O(N^2)$, 空间复杂度为O(N).该方法是超时的。

### Solution Two(标记每个访问过的元素)
```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 1
        for i in range(len(nums)):
            s = []
            index = i
            # 如果未曾访问过该元素，则继续填充数列
            while nums[index] != -1:
                s.append(nums[index])
                # 将当前访问的元素在数组中标记为-1
                nums[index] = -1
                index = s[-1]
            max_length = max(max_length, len(s))
        return max_length
```

**思路**：该解法比暴力解法只有两行代码不同，确将时间复杂度优化提升了一个数量级。**主要是我们发现以一个其实索引构建的数列s如果发生元素重复实际上形成了一个闭环，因为一共是0~n-1的索引，而数组里的元素也是0~n-1,所以必然会出现数组中某个元素值是他的一个下标，即在这个闭环中的所有元素不管以谁为其实索引，最终形成的数列都包含这个闭环中经过的所有元素**。因此当我们找到一个这样的数列后将它经过的所有元素标记为-1，下一次构建数列直接绕过为-1的元素，这样就避免了重复找到相同闭环的情况。时间复杂度为O(N),空间复杂度为O(N)。
PS. 可对数组[5,4,0,3,1,6,2]手动画图进行可视化闭环。

## 769. Max Chunks To Make Sorted(Medium)

[https://leetcode-cn.com/problems/max-chunks-to-make-sorted/](https://leetcode-cn.com/problems/max-chunks-to-make-sorted/)

### Description
数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
我们最多能将数组分成多少块？

### Solution(一次遍历，满足条件进行cut)
```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # 数组被切割次数计数
        count = 0
        current_max = 0
        # 因为计算的是切割次数，所以循环边界条件是倒数第二个元素
        while i < len(arr) - 1:
            # 当前元素之前包括当前元素的总个数
            chunk_len = i+1
            # 计算当前位置之前元素的最大值
            current_max = max(current_max, arr[i])
            # 是否进行切割的条件判断： 1. 后一个元素大于之前所有元素，2. 之前所有元素是从
            # 0开始连续不间断的
            if current_max < arr[i+1] and chunk_len == (current_max + 1):
                count += 1
            i += 1
        # chunk数 == 切割次数 + 1
        return count + 1
```

**思路**： 本题基本思路就是从头开始遍历数组，因为最后是一次拼接，所以只需要找到数组中的N-1个切割点,假设N是要求的chunk数。最重要的是遍历是判断当前位置是否进行切割，主要需要满足两个条件：  
* 当前元素是之前遍历过的所有元素中最大的元素，并且当前元素小于下一个元素。
* 作为最大元素的当前元素与之前的元素数量 = 当前元素值 - 1， 因为数组arr是[0, 1, ..., arr.length - 1]的一种排列。例如当前元素是5，那么他之前的元素一定要包括1-4.


## 66. Plus One(Easy)

[https://leetcode-cn.com/problems/plus-one/](https://leetcode-cn.com/problems/plus-one/)

### Solution
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        # 满十进位，直到不需进位为止
        while digits[i] + 1 == 10:
            digits[i] = 0
            i -= 1
            if i == -1:
                digits.insert(0, 1)
                return digits
        # 在第一个不需要满十进位的位加一
        digits[i] = digits[i] + 1

        return digits
```
思路：注意考虑满十进位就行。


## 189. Rotate array(Medium)

[https://leetcode-cn.com/problems/rotate-array/](https://leetcode-cn.com/problems/rotate-array/)

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


## 15. 3Sum(Medium)

[https://leetcode-cn.com/problems/3sum/](https://leetcode-cn.com/problems/3sum/)

### Solution
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        k, res = 0, []
        for k in range(len(nums)-2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue
            i, j = k+1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return res
```
思路：**双指针法思路**： 固定 3 个指针中最左（最小）数字的指针 k，双指针 i，j 分设在数组索引 (k, len(nums))两端，通过双指针交替向中间移动，记录对于每个固定指针 k 的所有满足 nums[k] + nums[i] + nums[j] == 0 的 i,j 组合：
1. 当 nums[k] > 0 时直接break跳出：因为 nums[j] >= nums[i] >= nums[k] > 0，即3个数字都大于0 ，在此固定指针 k 之后不可能再找到结果了。
2. 当 k > 0且nums[k] == nums[k - 1]时即跳过此元素nums[k]：因为已经将 nums[k - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。
3. i，j 分设在数组索引 (k, len(nums))两端，当i < j时循环计算s = nums[k] + nums[i] + nums[j]，并按照以下规则执行双指针移动：
当s < 0时，i += 1并跳过所有重复的nums[i]；
当s > 0时，j -= 1并跳过所有重复的nums[j]；
当s == 0时，记录组合[k, i, j]至res，执行i += 1和j -= 1并跳过所有重复的nums[i]和nums[j]，防止记录到重复组合。

复杂度分析：
时间复杂度 $O(N^2)$：其中固定指针k循环复杂度O(N)，双指针 i，j 复杂度 O(N)。
空间复杂度 O(1)：指针使用常数大小的额外空间。









