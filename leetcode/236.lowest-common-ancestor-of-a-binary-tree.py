#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 终止条件
        if not root: return None
        # 每一层递归执行的操作
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
        
# @lc code=end

