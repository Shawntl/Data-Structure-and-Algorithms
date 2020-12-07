#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None

        def length(head: ListNode):
            n = 0
            while head:
                head = head.next
                n += 1
            return n

        len1, len2 = length(headA), length(headB)
        if len2 > len1:
            headA, headB = headB, headA
        for _ in range(abs(len1 - len2)):
            headA = headA.next
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA

        
        
# @lc code=end

