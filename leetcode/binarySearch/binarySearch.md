|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | binarySearch |  2020-11-12 | Shawn_Song  | leetcode
-------
 **二分查找最原始的用途**是对于一个**排好序**的列表，在其中查找指定的元素，采用二分查找，时间复杂度为O(logN),N是列表的长度。

 最基本的二分查找代码实现思路： 
 ```python
 def binarySearch(nums: List[int], target: int):
     if not nums: return
     left, right = 0, len(nums) - 1
     # 设置终止条件
     while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return
 ```

 ## Recap:
 回顾数组矩阵部分的
 * 378 Kth Smallest Element in a Sorted Matrix
 * 287 Find the duplicate number
- [Array&Matrix](leetcode/array%26matrix/array%26matrix.md)  
这两道题也用到了二分查找的思想，首先1他们都是查找问题，那我们就应该想到二分查找。但是两道题都不是有序的数组，首先说第378题： 
给了一个特殊矩阵，我们无法像一维数组一样找到一种索引方式去将矩阵分成两份，所以我们定义left, right时只能找到矩阵的两个对角的元素。这时我们假设我们的一维数组是在left和right之间的所有数字。注意和上面最原始的二分查找不一样的地方是我们用的是元素实际值而不是下标。这就导致我们的mid可能并不在矩阵中，不能直接返回mid值，只有迭代到left==right时，才能返回此时的left或者right。
287题：  
这道题完全是乱序的一维数组，每一次二分后都要去找小于mid的元素个数，因为题目要求不改变原数组，所以时间复杂度有点高。因为是乱序，和上一题一样，我们不能通过不断二分下标去索引到查找元素,只有迭代到left==right时，才能返回此时的left或者right。
**特别注意**这两道题在我们判断right和left的移动时在我看来是个难点，因为题目特殊情况，往往判断规则的临界条件，并不像原始二分法一样简单（等于就找到了元素，大于中值找中值左边，小于中值找中值右边）。378题中当小于等于中值的数大于等于k时，意味着我们要找的数一定在中值左边且中值是闭区间,所以right = mid。而如果当小于等于中值的数小于k时，那么我们要找的数一定在中值右边且不包含中值，所以left = mid + 1。  
同理，我们再来看287题的边界条件，只有当小于等于中值的元素数量严格大于中值时，才表示重复的元素一定在中值左边且中值是闭区间。而如果小于等于中值的元素数量小于等于中值，等于的情况证明中值左边1包括中值没有多元素，重复的元素一定在中值右边，left=mid + 1, 小于的情况是中值右边的元素重复不止一次，中值左边包括中值的元素有缺失。  




* 69 Sqrt(x)
* 744 Find Smallest Letter Greater Than Target
* 540 Single Element in a Sorted Array
* 278 First Bad Version
* 153 Find Minimum in Rotated Sorted Array
* 34 Find First and Last Position of Element in Sorted Array

## 69. Sqrt(x)(Easy)

[https://leetcode-cn.com/problems/sqrtx/](https://leetcode-cn.com/problems/sqrtx/)

### Description
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

### Solution(二分法)
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
```
**思路**： 这道题重点关注左右指针移动的边界条件，在$mid^2$严格大于x时，target值一定在mid左边，且不包括mid,所以right = mid - 1. 而mid的计算是向left取整的，所以left必须改变，不然当left和right相差1时并且mid**2 < x，会陷入死循环。所以left = mid + 1。最后一次循环是left == right时，如果$mid^2$ < x, 说明相等时的值就是target. 如果$mid^2$ > x, mid - 1 = right才是target值，所以返回right。  

这一道题还有一个点，就是终止条件 left > right, 朴素的二分法这样做是因为在while循环内一定可以找到mid == target的情况。而本题当left == right时，$mid^2$可能大于x也可能小于x，还要进行一步判断和操作，不能直接像378题和287题一样返回left，所以退出条件不是left == right. 而在378和287题中，只有left一个指针在移动，并且left是左边是开区间，所以退出条件是left == right。  

时间复杂度：$O(logx)$


## 744. Find Smallest Letter Greater Than Target(Easy)

[https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/)

### Description
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。在比较时，字母是依序循环出现的。举个例子：
* 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'


### Solution

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        if ord(target) < ord(letters[left]) or ord(target) >= ord(letters[right]):
            return letters[left]
        while left <= right:
            mid = (left + right) // 2
            if ord(letters[mid]) > ord(target):
                right = mid - 1
            else:
                left = mid + 1
        return letters[left]
```

**思路**：将字母转成对应的数字，这个问题就是在一个有序数组上查找第一个比目标元素大的元素。因为是有序数组所以想到用二分查找。因为比目标元素大的元素会有重复，我们取得是重复元素里左边第一个元素值，所以right = mid - 1, right指针要移动，而当mid值小于等于target时，要找的元素一定在mid右侧，所以left = mid + 1.当right和left指针都移动时，说明right == left仍然要分情况讨论，终止条件一定要包含‘等于’。即当right == left时如果mid>target正好返回当前值，如果mid <= target, mid + 1返回。 时间复杂度：$O(logn)$


## 540. Single Element in a Sorted Array(Medium)

[https://leetcode-cn.com/problems/single-element-in-a-sorted-array/](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/)

### Description
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

### Solution
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            condition1 = (nums[mid] == nums[mid - 1] and mid%2 == 0)
            condition2 = (nums[mid] == nums[mid + 1] and mid%2 != 0)

            condition3 = (nums[mid] == nums[mid - 1] and mid%2 != 0)
            condition4 = (nums[mid] == nums[mid + 1] and mid%2 == 0)
            if nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            elif condition1 or condition2:
                right = mid - 1
            elif condition3 or condition4:
                left = mid + 1
        return  nums[left]
```

**思路**：首先是有序数组查找问题，想到二分法。数组长度只可能是奇数，长度为1时是特殊情况。我们每次计算mid时有三种情况，  
1.当mid前后值不一样时，找到target元素。  
2. target元素在mid左侧，不包括mid。（right指针移动到mid左侧）  
3. target元素在mid右侧，不包括mid。（left指针移动到mid右侧）  
第二步就是要确认后两种情况的判断条件，当mid不是target元素时，mid一定是一对儿pair元素中的前一个或者后一个。  
* 当mid是pair元素对儿中的前一个时，如果它是第偶数个元素，说明target元素在mid左侧；  
* 当mid是pair元素对儿中的后一个时，如果它是第奇数个元素，说明target元素在mid左侧； 

上述两种情况的反面说明target元素在mid右侧。  

当right == left时，当前元素一定是target元素，所以终止条件就是right == left。当边界收缩到只有三个元素时只有三种情况AAB,ABB, BAB。  
 

## 278. First Bad Version(Easy)

[https://leetcode-cn.com/problems/first-bad-version/](https://leetcode-cn.com/problems/first-bad-version/)

### Description
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

### Solution
```python
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid - 1
            elif not isBadVersion(mid):
                left = mid + 1
        return left
```

**思路**：错误版本list是一个1-n的顺序列表，查找其中的第一个错误版本号。所以是一个二分查找左边界问题。这道题中left, right指针移动的判断条件函数已经给出接口，isBadVersion().我们只需要考虑左右指针的移动。因为是左边界问题，所以右指针必须移动，当mid值不是坏版本时，坏版本一定在mid右侧，左指针要向右移动。该问题下因为两个指针都在移动，left == right时的元素不一定是第一个坏版本，所以相等应该写在终止循环内，以便我们分析相等后指针移动的两种情况，确认返回值。  

## 153. Find Minimum in Rotated Sorted Array(Medium)

[https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

### Description
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。
请找出其中最小的元素

### Solution
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # target元素在列表两端的特殊情况
        if (nums[0] < nums[1]) and (nums[0] < nums[-1]):
            return nums[0]
        if (nums[-1] < nums[-2]) and (nums[-1] < nums[0]):
            return nums[-1]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 找到了target元素
            if (nums[mid] < nums[mid-1]) and (nums[mid] < nums[mid+1]):
                return nums[mid]
            # 找到了target元素前一个元素
            elif (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
                return nums[mid + 1]
            elif nums[mid] < nums[right]:
                right = mid - 1
            elif nums[mid] > nums[left]:
                left = mid + 1
        return
```

**思路**：列表部分有序，查找元素，可以尝试二分思路。因为列表具有旋转前后连环性质，所以我们将target元素在列表两端的情况作为特殊情况考虑。 下面的主要因素就是，计算出mid值后如何判断target元素在mid左边还是右边？ 经过观察如果mid同时小于两端的值，mid是target元素，如果mid同时大于两边的元素，mid+ 1是target元素。  
刚才说列表部分有序，我们观察除了上述两种情形，在mid不是target值时，mid应该是右大左小。保持一种顺序的一侧一定不存在target值，即mid应该小于right大于left，对应的一侧可以被收缩掉。因为while循环里，包含了mid为target的情况和mid为target前一个元素的情况，所以在left==right之前就会找到target值，故找到后自动终止函数。   


## 34. Find First and Last Position of Element in Sorted Array(Medium)

[https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)


### Description
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。如果数组中不存在目标值，返回 [-1, -1]。

### Solution
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # 寻找左边界
        left1, right1 = 0, len(nums) - 1
        while left1 <= right1:
            mid = (left1 + right1) // 2
            if nums[mid] >= target:
                right1 = mid - 1
            else:
                left1 = mid + 1
        start = left1
        # 寻找右边界
        left2, right2 = 0, len(nums) - 1
        while left2 <= right2:
            mid = (left2 + right2) // 2
            if nums[mid] <= target:
                left2 = mid + 1
            else:
                right2 = mid - 1
        end = right2
        # target大于列表中最大值，或者小于列表中最小值时
        if start > (len(nums)-1) or end < 0:
            return [-1, -1]
        elif nums[start] == nums[end] == target:
            return [start, end]
        else:
            return [-1, -1]
```

**思路**： 分别寻找target元素在数组中的上边界和下边界，注意target元素不在列表中的几种特殊情况。


































