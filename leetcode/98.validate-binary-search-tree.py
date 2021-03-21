#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def isBST(node, lower, upper):
            if not node: return True

            if node.val > lower and node.val < upper:
                return isBST(node.left, lower, node.val) and isBST(node.right, node.val, upper)
            else:
                return False
        return isBST(root, float('-inf'), float('inf'))
        
# @lc code=end

