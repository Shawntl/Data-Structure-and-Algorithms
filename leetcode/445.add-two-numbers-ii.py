#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first, second = '', ''
        while l1:
            first += str(l1.val)
            l1 = l1.next
        while l2:
            second += str(l2.val)
            l2 = l2.next
        first_num, second_num = int(first), int(second)
        sum_num = first_num + second_num
        dummy = ListNode()
        p = dummy
        for num in str(sum_num):
            p.next = ListNode(int(num))
            p = p.next
        return dummy.next

# @lc code=end

