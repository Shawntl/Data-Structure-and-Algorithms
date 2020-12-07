#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return
        slower, faster = head, head.next
        while faster:
            while faster and faster.val == slower.val:
                faster = faster.next
            slower.next = faster
            if not faster: break

            slower = slower.next
            faster = faster.next
        return head
      
# @lc code=end

