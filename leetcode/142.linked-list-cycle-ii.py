#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return 
        slower, faster = head, head
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                break
        if not faster or not faster.next:
            return
        faster = head
        while faster != slower:
            faster, slower = faster.next, slower.next
        return faster

        
# @lc code=end

