|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | tree&recursion |  2021-03-16 | Shawn_Song  | leetcode
-------

# 树与递归


## Content
### 深度优先遍历
* 144.binary tree preorder traversal
* 94.binary tree inorder traversal
* [235. 二叉搜索树的最近公共祖先](#235-二叉搜索树的最近公共祖先easy)
* 236.Lowest Common Ancestor of a Binary Tree
* 589.N-ary Tree Preorder Traversal

### 泛型递归、树的递归
* 98.Validate Binary Search Tree
* 104.Maximum Depth of Binary Tree
* 111.Minimum Depth of Binary Tree
* 226.Invert Binary Tree
* 101.Symmetric Tree
* 110.Balanced Binary Tree



## 144. binary tree preorder traversal(Medium)

[https://leetcode-cn.com/problems/binary-tree-preorder-traversal/](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)


### Solution
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recursivePreorder(root):
            if not root: return
            res.append(root.val)
            recursivePreorder(root.left)
            recursivePreorder(root.right)
        recursivePreorder(root)
        return res
```

## 94. binary tree inorder traversal(Medium)

[https://leetcode-cn.com/problems/binary-tree-inorder-traversal/](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)


### Solution
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recursiveInorder(root):
            if not root: return
            recursiveInorder(root.left)
            res.append(root.val)
            recursiveInorder(root.right)
        recursiveInorder(root)
        return res
```


## 98. Validate Binary Search Tree(Medium)

[https://leetcode-cn.com/problems/validate-binary-search-tree/](https://leetcode-cn.com/problems/validate-binary-search-tree/)


### Description
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

### Solution(Medium)
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def isBST(node, lower, upper):
            if not node: return True

            if node.val > lower and node.val < upper:
                return isBST(node.left, lower, node.val) and isBST(node.right, node.val, upper)
            else:
                return False
        return isBST(root, float('-inf'), float('inf'))
```
思路：递归验证 ，大致思路如下：
1. 如果当前节点可用，则将当前节点值与其上、下限进行比较。  
2. 然后对于左、右子树重复该步骤。  

需要注意以下几点：  
1. 程序初始化时，上、下限分别为对应语言中正无穷和负无穷，python中使用float('-inf')和float('inf')表示。  
2. 递归过程中需不断更新上、下限，左子节点上限为当前节点值，右子节点下限为当前节点值。


## 104. Maximum Depth of Binary Tree(Easy)

[https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

### Description
给定一个二叉树，找出其最大深度。

### Solution
```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
```
思路：二叉树的最大深度等于左子树和右子树深度的最大值加一。


## 111. Minimum Depth of Binary Tree(Easy)

[https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

### Description
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

### Solution
```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root: return 0
        if not root.left: return self.minDepth(root.right)+1
        if not root.right: return self.minDepth(root.left)+1

        return min(self.minDepth(root.left), self.minDepth(root.right))+1
```
思路：  
当 root 节点为空时，返回0
当 root 节点左右孩子至少有一个为空时，返回不为空的孩子节点的深度  
当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值。  


## 226. Invert Binary Tree(Easy)

[https://leetcode-cn.com/problems/invert-binary-tree/](https://leetcode-cn.com/problems/invert-binary-tree/)

### Description
翻转一棵二叉树。

### Solution
```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```
思路：递归地交换父节点的两个子节点。

## 235. 二叉搜索树的最近公共祖先(Easy)

[https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

### Description
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

### Solution
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
```

## 236. Lowest Common Ancestor of a Binary Tree(Meidum)

[https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

### Description
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

### Solution(分治)
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 终止条件
        if not root: return None
        if root.val == p.val or root.val == q.val:
            return root
        # dfs+后序遍历，向下一层进行递归，分为两个子问题
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 合并两个子问题的结果：
        # 若两个子树都匹配，返回根节点。
        # 若左子树匹配则返回左子树，若只有右子树匹配返回右子树
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
```
思路：只有两种可能：  
1. p,q在当前节点两侧子节点。
2. p, q在当前节点单侧子树。  
向下递归的过程左右子树谁先匹配到p,q, 就优先递归地向上返回哪个节点。同时在一层匹配到则返回父节点。  


## 589.N-ary Tree Preorder Traversal(Easy)

[https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)

### Description
给定一个 N 叉树，返回其节点值的 前序遍历 。
N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

### Solution
```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def recursivePreorder(root):
            if not root: return
            res.append(root.val)
            for child in root.children:
                recursivePreorder(child)
        recursivePreorder(root)
        return res
```
思路：和二叉树的前序遍历类似。

## 101.Symmetric Tree(Easy)

[https://leetcode-cn.com/problems/symmetric-tree/](https://leetcode-cn.com/problems/symmetric-tree/)

### Description
给定一个二叉树，检查它是否是镜像对称的。

### Solution
```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def helper(left, right):
            if not left and not right: return True
            if not left or not right: return False
            return left.val == right.val and helper(left.right, right.left) and helper(left.left, right.right)

        return helper(root.left, root.right)
```
思路：镜像对称的条件是，对称子树（left, right）的根节点值相等。(注意这里left和right不是一个根节点的左右子树）。left子树的右节点和right子树的左节点判断相等，left子树的左节点和right子树的右节点判断相等。

## 110.Balanced Binary Tree(Easy)

[https://leetcode-cn.com/problems/balanced-binary-tree/](https://leetcode-cn.com/problems/balanced-binary-tree/)

### Description
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

### Solution
```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        def depth(root):
            if not root: return 0
            return max(depth(root.right), depth(root.left)) + 1
        if abs(depth(root.right) - depth(root.left)) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)
```
思路：递归的判断左右子树是否为深度相差一，求左右子树的深度又是一次递归的求解。两层递归。