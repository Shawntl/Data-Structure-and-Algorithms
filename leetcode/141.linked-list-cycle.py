#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slower, faster = head, head
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return True
        return False
        
# @lc code=end

