#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
# @lc code=end

