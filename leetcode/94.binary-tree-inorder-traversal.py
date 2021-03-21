#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
        
# @lc code=end

