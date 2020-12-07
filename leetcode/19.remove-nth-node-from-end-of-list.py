#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Solution two(Two pointer)
        if not head: return
        dummy = ListNode()
        dummy.next = head
        p1, p2 = dummy, dummy
        for i in range(n):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next

        return dummy.next
        # Solution one hash table
        # if not head or not head.next: return
        # pointer_dict = {}
        # idx = 1
        # cur = head
        # while cur:
        #     pointer_dict[idx] = cur
        #     cur = cur.next
        #     idx += 1
        # pointer_dict[idx] = cur
        # length = idx
        # if length == n+1:
        #     return head.next
        # pointer_dict[length-n-1].next = pointer_dict[length-n+1]
        # return head
        
# @lc code=end

