|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | Sorting&select |  2021-01-03 | Shawn_Song  | leetcode
-------

* Brute Force Sort
* Bubble Sort
* Select Sort
* Insert Sort
* Merge Sort
* Quick Sort
* Heap Sort
* Count Sort
* Bucket Sort
* Radix Sort


## Brute Force Sort(Easy)

### Solution
```python
def Brute_Force(nums):
    for i in range(len(nums)):
        j = i+1
        while j < len(nums):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums
```
思路：遍历n次长度为n的数组，每一次遍历找到当前遍历的最小值放在第一位，第一位向前移动遍历下一次。时间复杂度为$O(N^2)$, 空间复杂度为O(1). 不稳定排序。

## Bubble Sort(Easy)

### Solution
```python
def Bubble_Sort(nums):
    for i in range(len(nums)):
        j = len(nums) - 1
        while i < j:
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums
```
思路：将最小的元素从数组最后端通过不断的比较交换移动至第一位，然后第一位向前移动，重复上述操作。该方法的时间复杂度是$O(N^2)$,空间复杂度是O(1). 稳定排序

## Select Sort(Easy)

### Solution
```python
def Select_Sort(nums):
    for i in range(len(nums)):
        j = i+1
        minIndex = i
        while j < len(nums):
            if nums[j] < nums[minIndex]:
                minIndex = j
            j += 1
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums
```
思路：和brute force唯一的区别在于每一轮找最小元素时不是不断的和第一位交换，而是通过记录更新最小元素的位置索引，每一轮只做一次交换，然后第一位向前移动。时间复杂度为$O(N^2)$,空间复杂度为$O(1)$. 稳定排序。

## Insert Sort

### Solution
```python
def Insert_Sort(nums):
    for i in range(1, len(nums)-1):
        # 如果最后一个待插入元素比尾部元素小
        if nums[i] < nums[i-1]:
            # 将最后一个元素记录为最小值
            mini = nums[i]
            j = i-1
            # 直到在被插入数组中找到小于等于目标元素的时候停止向后遍历
            while nums[j] > mini:
                # 每个大于目标元素的元素依次往前移动
                nums[j+1] = nums[j]
                j -= 1
            # 将目标元素插入正确的位置
            nums[j+1] = mini
    return nums         
```
思路：从数组前两个元素开始算起，将目前选出来的n-1个元素作为被插入目标，因为这n-1个元素已经是有序的，最后一个元素作为即将插入的元素。依次和前面n-1个元素进行比较，插入合适的位置。平均时间复杂度为$O(n^2)$,最坏时间复杂度为$O(N)$. 稳定排序。

## Merge Sort

### Solution
```python
def Merge_Sort(nums):
    n = len(nums)
    mid = n // 2
    left = nums[:mid]
    right = nums[mid:]
    if n < 2:
        return
    Merge_Sort(left)
    Merge_Sort(right)
    Merge(left, right, nums)

def Merge(left, right, nums):
    i = j= 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[i+j] = left[i]
            i += 1
        else:
            nums[i+j] = right[j]
            j += 1
    if i == len(left):
        nums[i+j:] = right[j:]
    else:
        nums[i+j:] = left[i:]
```
思路：先递归从中间切分序列成两个子序列，直到切分为两个长度为一的数组后（注意递归的终止条件），在自底向上进行合并。注意合并时每次比较出的较小的元素所放位置的索引是此时两个子序列遍历到的索引相加，即上面的i+j。

## Heap Sort

### Solution
```python
LEFT = lambda i: 2*i + 1
RIGHT = lambda i: 2*i + 2
 def HeapSort(nums):
     BuildMaxHeap(nums)
     for i in range(len(nums)-1, -1, -1):
         nums[0], nums[i] = nums[i], nums[0]
         # heap_size = i
         KeepHeap(nums, 0, i)

def BuildMaxHeap(nums):
    '''
    对现在的数组构建完全二叉树
    '''
    n = len(nums)
    for i in range(len(nums)//2-1, -1, -1):
        KeapHeap(nums, i, n)

def KeepHeap(nums, i, heap_size):
    '''
    以当前节点i为根结点，维持一颗完全二叉树，即每个子树都是一个大顶堆
    '''
    l, r = LEFT(i), RIGHT(i)
    largest = l if l < heap_size and nums[i] < nums[l] else: i
    largest = r if r < heap_size and largest < nums[r] else: largest

    if i != largest:
        nums[i], nums[largest] = nums[largest], nums[i]
        KeapHeap(nums, largest, heap_size)
    return
```
思路：  
第一步：创建一个完全二叉树（大顶堆）。 O(NlogN)  
第二步：把堆顶元素放到队尾。  
第三步：对剩下的元素再维护一个完全二叉树（大顶堆）    O(logN)   
第四步：循环进行第2、3步






