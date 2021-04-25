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

### 深度优先搜索和广度优先搜索
1. 搜索不带任何智能因素，就是把所有节点遍历一遍且只遍历一次。
2. DFS代码模版：  

```python  
#Python
visited = set() 
def dfs(node, visited):    
    if node in visited: # terminator    
        # already visited     	     return 	
    visited.add(node) 	
    # process current node here.
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited) 
    
```   
3. BFS代码模版：  
 
```python
# Python
def BFS(graph, start, end):    
    visited = set()	
    queue = [] 	
    queue.append([start]) 	
    while queue: 		
        node = queue.pop() 	
        visited.add(node)		
        process(node) 		
        nodes = generate_related_nodes(node) 
        queue.push(nodes)	
        # other processing work 	...
```  

### 贪心算法
适用贪心算法的场景： 简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。  
贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。   
### 二分查找
1. 前提： 

* 目标函数单调性。
* 存在上下界
* 能够通过索引访问

###  第三周：动态规划  
1. 分治+最优子结构。
2. 动规和递归、分治没有本质区别，主要看是否有最优子结构。共性是是否有重复子问题。差异：最优子结构，中途可淘汰次优解。    

### 第四周：位运算  
1. 指定位置的位运算：

* 和1做与运算，和0做或运算，位值不会改变。  
* 将x最右边的第n位清零： x & (~0 << n)  
* 获取x的第n位值（0或1）：（x>>n）&1
* 获取x的第n位的幂值： x&(1<<n)


1. 算数移位与逻辑移位
2. 位运算的应用

### GBDT和xgboost区别
1. GBDT损失函数做了一阶泰勒展开，Xgboost做了二阶泰勒展开。
2. xgboost在损失函数中加入了正则项，树的节点数以及L2正则。
3. GBDT对每个特征的每一个值都做分割尝试，Xgboost排好序后一个quantile一个quantile分割，即xgboost提出以二阶梯度$h_i$为权重进行分位数切割算法。不需要把所有数据读入内存。
4. xgboost对缺失值可以自动放在某一边，尝试对它们的分裂方向。
5. xgboost对特征进行预排序储存在block上，每次不需要重新排序。
6. column block按特征大小顺序存储，相应的样本的梯度信息是分散的，造成内存的不连续访问，降低CPU cache命中率。这时xgboost采用的缓存优化方法是预取数据到buffer中（非连续->连续），再统计梯度信息。调节块的大小。
7. xgboost数据按列存储，可以多线程并行执行。

### lightGBM、GBDT、Xgboost
1. lightGBM相对xgboost使用分位数算法进行特征分割选择，它选用直方图算法，将特征值分桶装进箱子里。
2. lightGBM可以通过父节点的直方图和一个子节点的直方图作差计算出另外一个节点的直方图。
3. 对于树的分裂方法，lightGBM使用leaf-wise, xgboost使用level-wise.意思xgboost每一次对树的一层节点不加区分地进行分裂，最后进行剪枝。而lightGBM只对loss下降最大的节点进行分裂。这样lightgbm可以生成更精确更复杂的树，但是更容易过拟合。
4. lightGBM有goss采样算法，即每次迭代只采样一部分样本，采样原则是，当前梯度大的样本全部保留，梯度较小的样本因为对降低目标函数贡献不大，只采样一部分。从而降低计算成本。
5. lightGBM的EFB算法可以对互斥的类别特征进行捆绑成一个新的特征，而不至于one hot后过于稀疏。并且他会对类别特征自动分bins，不需要人工one-hot。
6. Xgboost模型复杂度 = 树的数量*每棵树叶子数量*生成每个叶子复杂度。  
   生成每个叶子复杂度 = 特征数量*特征分裂点*样本数量。  
   lightGBM的三个优化算法就是在优化xgboost上述复杂度。
   
   


