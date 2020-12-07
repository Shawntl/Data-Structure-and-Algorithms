#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head

        p = dummy
        while head and head.next:
            first = head
            second = head.next
            p.next = second
            first.next = second.next
            second.next = first
            p = first
            head = p.next
        return dummy.next

# @lc code=end

