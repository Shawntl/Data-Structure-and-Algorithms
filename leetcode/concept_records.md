## 第一周：数组、链表、跳表
1. 数组和链表在增删改查上的主要区别是：数组的增加和删除较慢，会引起整个数组上其他元素的移动，而链表不会，只会发生$O(1)$的复杂度。但是查找速度链表相对于数组较慢，尤其是当在有序元素列上查找时，数组可以使用二分查找。链表在有序序列上的查找为了进一步优化时间复杂度，提出了跳表。
2. 给一维数据结构进行优化，往往是将它扩展到二维，因为二维数据结构增加了信息。
3. 解题一般的思路，先是看暴力枚举是否可以，如果不可以，就去找最小重复子问题，因为程序只能执行简单的if else loop, 根本上是机械的重复工作，不涉及人工智能。

### 队列、栈、hash表

1. python高性能库collections支持很多container，要了解。
2. 优先队列heapq要掌握，优先队列的实现一般是二叉搜索树。
3. 一般具有最近相关性的问题可能就可以用栈来解决。  

### 堆、树、二叉树
1. heap 是一种可以迅速找到一堆数中最大数和最小数的数据结构。
2. 堆的优点是O(1)查找最值，O(logn)删除最值，插入值。但是堆不一定是二叉堆，还有其他形式的堆可以实现更好的效率。
3. 二叉堆是通过完全二叉树来实现的，不是二叉搜索树。  
    * 性质一：是一颗完全树
    * 性质二：树中任意节点的值总是 >=  它的子节点  
4. 因为是完全二叉树，所以可以用数组的形式储存，不需要之前的链表形式。因为左右子节点的索引可以由父节点的索引推算出来。

## 第二周：递归
1. 递归本质也是一种循环，只不过是通过函数体循环调用自己。
递归代码模版：   

```python
def recursion(level, param1, param2...):
    # recursion terminator
    if level > max_level:
        process result
        return
    # process logic in current level
    process(level, data)
    
    # drill down
    self.recursion(level+1, p1..)
```  

2. 分治代码模版  
比范型递归主要多的一点是，最后要把各个子问题的结果合并。   

```python  
def divide_conquer(problem, param1, param2, ...):   
    # recursion terminator   
    if problem is None: 	
        print_result 	
        return   
    # prepare data   
    data = prepare_data(problem)   
    subproblems = split_problem(problem, data)   
    # conquer subproblems   
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)   
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)   
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)   …  
    # process and generate the final result   
    result = process_result(subresult1, subresult2, subresult3, …)	  
    # revert the current level states  
    
```   

3. 回溯本质是一种递归，意思就是让你在每一层去尝试不同的方法。很多时候我们需要在每层执行不同的方法时做判断进行剪枝。
