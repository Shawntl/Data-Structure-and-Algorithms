#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length = 0
        res = []
        head = root
        while head:
            head = head.next
            length += 1
        quotient = length // k
        remainder = length % k
        p1 = root
        i = 0
        while k:
            if i < remainder:
                sublength = quotient + 1
            else:
                sublength = quotient
            if sublength:
                p2 = p1
                while sublength - 1:
                    p1 = p1.next
                    sublength -= 1
                temp = p1.next
                p1.next = None
                p1 = temp
                res.append(p2)
            else:
                res.append(None)
            k -= 1
            i += 1
        return res
        
# @lc code=end

