#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <= 1: return 0
        stack = [s[0]]
        dp = 0
        for i in range(1, n):
            if not stack: stack.append(s[i])
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
                dp += 2
            else:
                stack.append(s[i])
        return dp

        
# @lc code=end

