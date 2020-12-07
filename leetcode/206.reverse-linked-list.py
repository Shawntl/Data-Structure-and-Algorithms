#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return
        pre = None
        cur = head
        while cur:
            ori_next = cur.next
            cur.next = pre 
            pre = cur 
            cur = ori_next
        return pre
        
# @lc code=end

