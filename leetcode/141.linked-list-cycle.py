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
        if not head or head.next == None:
            return False
        slower, faster = head, head.next
        while slower and faster:
            if slower == faster:
                return True
            slower = slower.next
            if faster.next:
                faster = faster.next.next
            else:
                return False

        return False
        
# @lc code=end

