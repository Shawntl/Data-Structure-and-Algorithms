|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | TwoPointers（快慢指针） |  2020-11-27 | Shawn_Song  | leetcode
-------

# 双指针（快慢指针）

* 141 Linked List Cycle
* 142 Linked List Cycle II
* 283 Move Zeros
* 27 Remove Element
* 26 Remove Duplicates from Sorted Array
* 80 Remove Duplicates from Sorted Array II


## 141. Linked List Cycle(Easy)

[https://leetcode-cn.com/problems/linked-list-cycle/](https://leetcode-cn.com/problems/linked-list-cycle/)


### Description
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。
进阶：
你能用 O(1)（即，常量）内存解决此问题吗？

### Solution
```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slower, faster = head, head
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return True
        return False
```

**思路**：一个指针快一个指针慢，如果存在环，一定会有一个指针把另外一个指针“套圈”。另外如果不存在环，快指针一定先到达终点，一旦快指针到达终点，就可以停止循环，返回False。

## 142. Linked List Cycle II(Medium)

[https://leetcode-cn.com/problems/linked-list-cycle-ii/](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

### Description
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

### Solution
```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return 
        slower, faster = head, head
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                break
        # 无环
        if not faster or not faster.next:
            return
        # 有环
        faster = head
        while faster != slower:
            faster, slower = faster.next, slower.next
        return faster
```
思路：首先判断是否有环，使用上一题的代码。判断有环之后如何算出环的入口呢？设快指针步数f, 满指针步数为s,则有第一次相遇时：  
f = 2s  
f = s + nb  
b为环上节点数，两式相减，得到第一次相遇慢指针已经走了nb步，那么他再走a步一定可以到环的入口，a为环外节点数。此时如果让一个指针从头开始和慢指针一起走a步，他们相遇时一定是在环的入口处。

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
        slower, faster = 0, 0
        while faster < len(nums):
            if nums[slower] != 0:
                slower += 1
            elif nums[faster] != 0:
                nums[slower], nums[faster] = nums[faster], nums[slower]
                slower += 1
            faster += 1
```

**思路**： 这道题我在[Array&Matrix](leetcode/array%26matrix/array%26matrix.md)数组矩阵的部分遇到过，当时的解法是慢指针并不指向零元素，只是快指针找到一个非零元素，就挨着放在数组前面，最后剩下几个元素，全部填零。那个方法其实对整个数组执行了两次遍历，第一次快指针找到所有非零元素，第二次再将零元素挨个放到数组最后，时间复杂度是$O(N+M)$, N是数组长度，M是零元素个数。  

这次我们就想能不能使用一次遍历，在将快指针指向的非零元素放到正确位置的同时，也可以把一个零元素放到正确位置。所以这次慢指针不仅仅用来给非零元素计数，而是只指向零元素等待快指针将找到的非零元素和它进行交换，这样当快指针遍历完一次数组，对应的零元素也放到了正确位置。这样时间复杂度在测试数据集中零元素多的时候比较低，在非零元素多的时候，第一种方法时间复杂度较优。  

现在我们来看快慢指针怎么保证一前一后移动，首先是慢指针和快指针在遇到非零元素一起保持前进，一旦遇到零元素，慢指针不动，快指针继续向前移动，直到快指针遇到了和慢指针分开后的第一个非零元素，然后和慢指针交换后，同时向前移动一位。自慢指针第一次遇到零元素停下来后，它就再也不可能指向非零元素了，因为非零元素都被快指针提前找到进行了交换。所以慢指针遇到零元素就停下等待快指针的交换，快指针则遇到零元素向前移动，遇到非零元素交换后向前移动，每一步都在移动。


## 27 Remove Element(Easy)

[https://leetcode-cn.com/problems/remove-element/](https://leetcode-cn.com/problems/remove-element/)

### Description
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素.

### Solution
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        slower, faster = 0, 0
        while faster < len(nums):
            if nums[slower] != val:
                slower += 1
            elif nums[faster] != val:
                nums[faster], nums[slower] = nums[slower], nums[faster]
                slower += 1
            faster += 1
        return slower
```

**思路**：和上一题相似，只是上一题的零元素换成了val，本质是将所有val移到数组末尾。

## 26 Remove Duplicates from Sorted Array(Easy)

[https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

### Description
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

### Solution
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        slower, faster = 0, 1
        while faster < len(nums):
            if nums[faster] > nums[slower]:
                nums[faster], nums[slower+1] = nums[slower+1], nums[faster]
                slower += 1
            faster += 1
        return slower+1
```
**思路**：该题的解法与前几题思路类似，快指针去寻找比慢指针大的元素，因为是有序数组，慢指针只需要等着和快指针交换一次进行递增，而快指针一直向前移动不断去寻找下一个大于当前遍历过所有元素的元素，指导快指针遍历完所有元素，也就将所有独立的递增元素交换给了慢指针。

## 80 Remove Duplicates from Sorted Array II(Medium)

[https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/)

### Description
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。  

### Solution
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        flag = True
        slower, faster = 0, 1
        while faster < len(nums):
            if nums[faster] == nums[slower] and flag:
                nums[faster], nums[slower+1] = nums[slower+1], nums[faster]
                slower += 1
                flag = False
            elif nums[faster] > nums[slower]:
                nums[faster], nums[slower+1] = nums[slower+1], nums[faster]
                flag = True
                slower += 1
            faster += 1
        return slower+1
```

**思路**：本题只是在上一题的基础上改变了一点，增加了一个限制条件，可以允许两个以内的相同元素存在。所以我们只要在快指针**第一次**遇到和当前慢指针所指元素相同的元素时，也进行交换即可。怎么控制这个“第一次”而不让第二次、第三次...遇到的相同元素也被交换到前面呢，我想到设置一个开关flag，当快慢指针出现相同时，交换完即关闭开关flag= False,不在考虑相等情况。当慢指针更新后（nums[faster] > nums[slower]），再将开关打开，flag = True.






































