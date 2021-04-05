#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

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
    
# @lc code=end

