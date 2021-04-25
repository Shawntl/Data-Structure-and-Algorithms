#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        ls = list(s)
        for i in range(0, n, 2*k):
            if n - i < k:
                self.reverse(ls, i, n-1)
            else:
                self.reverse(ls, i, i+k-1)
        return ''.join(ls)

    def reverse(self, ls, start, end):
        while start < end:
            ls[start], ls[end] = ls[end], ls[start]
            start += 1
            end -= 1

        
# @lc code=end

