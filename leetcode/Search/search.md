|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | Search |  2021-03-26 | Shawn_Song  | leetcode
-------
 
 ## BFS
 BFS使用队列，把每个还没有搜索到的点依次放入队列，然后再弹出队列的头部元素当作当前遍历点。BFS总共有两个模版：  
 1. 如果不需要确定当前遍历到了哪一层，BFS模版如下。
 ```python
 while queue:
    cur = queue.pop()
    for 节点 in cur的所有相邻节点:
        if 该节点有效且未访问过:
            queue.push(该节点)
 ```  
 2.如果要确定当前遍历到了哪一层，BFS模版如下。这里增加了level表示当前遍历到二叉树中的哪一层了，也可以理解为在一个图中，现在已经走了多少步了。size表示在当前遍历层有多少个元素，也就是队列中的元素，我们把这些元素一次性遍历完，即把当前层的所有元素都向外走了一步。  
 ```python
 level = 0
 while queue:
     size = queue.size()
     while size:
         cur = queue.pop()
         for 节点 in cur所有相邻节点:
             if  该节点有效且为被访问过:
                 queue.push(该节点)
        size -= 1
    level += 1
 ```

* 102.Binary Tree Level order traversal

## DFS  
* 200.Number of Island


## 102.Binary Tree Level order traversal(Medium)

[https://leetcode-cn.com/problems/binary-tree-level-order-traversal/](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

### Description
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点).

### Solution one(DFS)
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def DFS(root, level):
            if not root: return
            # 当前层执行的操作
            if level == len(res):
                res.append([])
            res[level].append(root.val)
            # 向下递归
            if root.left:
                DFS(root.left, level+1)
            if root.right:
                DFS(root.right, level+1)
        DFS(root, 0)
        return res
```
思路：也算是回溯法，注意点是第一次递归到每一层都要新建一个list,把当前遍历的元素存入，后面再进入这一层时可以直接将元素存入已经建好的list。  

### Solution two(BFS)
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            while size:
                cur = queue.popleft()
                size -= 1
                # 有的父节点缺少左或右子节点，queue中有可能有空值
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res
```

## 200. Number of Island(Medium)

[https://leetcode-cn.com/problems/number-of-islands/](https://leetcode-cn.com/problems/number-of-islands/)

### Description
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。   

### Solution  
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0]) 
        count = 0
        def DFSMasking(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != '1':
                return
            # 当前层执行操作
            grid[i][j] = '0'
            # drill down
            DFSMasking(i + 1, j)
            DFSMasking(i - 1, j)
            DFSMasking(i, j + 1)
            DFSMasking(i, j - 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    DFSMasking(i, j)
                    count += 1
        return count
```
思路：遍历矩阵，遇到'1', count+1。 然后开始对当前'1'附近上下左右进行dfs搜索，如果遇到'1'就把他们改成'0'.因为这代表他们在一个岛屿。直到将所有在一个岛屿上的'1'都变成'0'。等到下次再遇到'1'，count+1.




